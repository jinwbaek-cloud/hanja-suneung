import os
import sys
import json
import re
import hashlib
from collections import Counter

def run_verification():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_js_path = os.path.join(base_dir, 'js', 'data.js')
    backup_data_js_path = os.path.join(base_dir, 'js', 'data.js.pre_stage9c.bak')
    review_json_path = os.path.join(base_dir, 'review_import_20261004 2', 'hanalgukshwi_2017_2021_metadata_stage9C_editorial_review_v1.11.json')
    payload_json_path = os.path.join(base_dir, 'review_import_20261004 2', 'hanalgukshwi_2017_2021_editorial_payload_v2.3_display_candidate.json')

    results = {}

    print("=== 1. Reading current js/data.js ===")
    with open(data_js_path, 'r', encoding='utf-8') as f:
        text = f.read()

    prefix = 'window.MOCK_WORDS = '
    m_words = re.search(r'window\.MOCK_WORDS\s*=\s*(\{.+?\});\s*(?:window\.STAGE9_READING_NOTES\s*=\s*(\{.+?\});)?', text, re.DOTALL)
    if not m_words:
        print("FAILED: Could not parse window.MOCK_WORDS in js/data.js")
        sys.exit(1)

    words = json.loads(m_words.group(1))
    notes = json.loads(m_words.group(2)) if m_words.group(2) else {}

    results['total_words'] = len(words)
    total_contexts = sum(len(w.get('contexts', [])) for w in words.values())
    results['total_contexts'] = total_contexts

    print(f"Total Words: {results['total_words']} (Expected: 1084)")
    print(f"Total Contexts: {results['total_contexts']} (Expected: 1516)")
    assert results['total_words'] == 1084, f"Word count mismatch: {results['total_words']}"
    assert results['total_contexts'] == 1516, f"Context count mismatch: {results['total_contexts']}"

    print("\n=== 2. Baseline 700 Words & 878 Contexts Preservation ===")
    with open(backup_data_js_path, 'r', encoding='utf-8') as f:
        b_text = f.read()
    base_data = json.loads(b_text[len(prefix):].rstrip().rstrip(';'))

    rekeys = {
        '경향': '경향-京鄕', '부정': '부정-不正', '사단': '사단-事端', '사서': '사서-史書',
        '산정': '산정-算定', '소실': '소실-小室', '시가': '시가-市價', '시비': '시비-是非',
        '실정': '실정-失政', '전사': '전사-戰死', '조명': '조명-造命', '중화': '중화-中和'
    }

    base_words_preserved = 0
    base_contexts_preserved = 0
    for old_k, old_w in base_data.items():
        new_k = rekeys.get(old_k, old_k)
        if new_k in words:
            base_words_preserved += 1
            curr_w = words[new_k]
            curr_sigs = [(c.get('source'), c.get('section'), c.get('content')) for c in curr_w.get('contexts', [])]
            for bc in old_w.get('contexts', []):
                bsig = (bc.get('source'), bc.get('section'), bc.get('content'))
                if bsig in curr_sigs:
                    base_contexts_preserved += 1
                else:
                    print(f"FAILED: Missing baseline context in {new_k}: {bsig}")

    print(f"Baseline Words Preserved: {base_words_preserved} / 700")
    print(f"Baseline Contexts Preserved: {base_contexts_preserved} / 878")
    assert base_words_preserved == 700, f"Only {base_words_preserved}/700 baseline words preserved"
    assert base_contexts_preserved == 878, f"Only {base_contexts_preserved}/878 baseline contexts preserved"

    print("\n=== 3. Excluded 27 Words Absence Check ===")
    with open(review_json_path, 'r', encoding='utf-8') as f:
        review_data = json.load(f)
    excluded_ids = [r['id'] for r in review_data['records'] if r.get('review_status') == 'EXCLUDED']
    print(f"Approved Excluded Records in Review: {len(excluded_ids)} (Expected: 27)")
    assert len(excluded_ids) == 27, f"Expected 27 excluded, found {len(excluded_ids)}"

    revived = []
    all_word_ids = {w['id'] for w in words.values()}
    for eid in excluded_ids:
        if eid in words or eid in all_word_ids:
            revived.append(eid)
    print(f"Revived Excluded Words: {len(revived)}")
    assert len(revived) == 0, f"Revived words detected: {revived}"

    print("\n=== 4. Duplicate Contexts Check ===")
    duplicate_contexts = []
    for k, w in words.items():
        seen_ctxs = set()
        for idx, c in enumerate(w.get('contexts', [])):
            sig = (c.get('source'), c.get('section'), c.get('content'))
            if sig in seen_ctxs:
                duplicate_contexts.append((k, idx, sig))
            seen_ctxs.add(sig)
    print(f"Duplicate Contexts: {len(duplicate_contexts)}")
    assert len(duplicate_contexts) == 0, f"Duplicates found: {duplicate_contexts}"

    print("\n=== 5. Invalid Relation References & Homonyms Check ===")
    broken_relations = []
    homonym_edges = 0
    for k, w in words.items():
        for rel in w.get('relations', []):
            tid = rel.get('targetId')
            if tid not in all_word_ids and tid not in words:
                broken_relations.append((k, tid))
            if rel.get('type') == 'homonym':
                homonym_edges += 1
    print(f"Broken Relations: {len(broken_relations)}")
    assert len(broken_relations) == 0, f"Broken relations: {broken_relations}"
    print(f"Total Homonym Directed Edges: {homonym_edges} (Expected: 50, which is 10 baseline + 40 from 20 pairs)")
    assert homonym_edges == 50, f"Expected 50 homonym edges, got {homonym_edges}"

    print("\n=== 6. Reading Notes Check ===")
    print(f"Notes in window.STAGE9_READING_NOTES: {notes}")
    expected_notes = {
        "상쇄-相殺": "※ 殺은 여기서 ‘쇄’로 읽습니다.",
        "감쇄-減殺": "※ 殺은 여기서 ‘쇄’로 읽습니다."
    }
    for wid, exp_note in expected_notes.items():
        assert notes.get(wid) == exp_note, f"Missing window note for {wid}"
        rec = words.get(wid)
        assert rec is not None, f"Missing record {wid}"
        assert rec.get('stage9C_reading_note') == exp_note, f"Missing stage9C_reading_note on record {wid}"
    print("Reading notes verified for 상쇄-相殺 and 감쇄-減殺!")

    print("\n=== 7. 복선화음 Verification ===")
    assert '복선화음-福善禍淫' in words, "Missing 복선화음-福善禍淫"
    bok = words['복선화음-福善禍淫']
    assert bok['word'] == '복선화음', f"Wrong word: {bok['word']}"
    assert bok['hanja'] == '福善禍淫', f"Wrong hanja: {bok['hanja']}"
    assert bok['id'] == '복선화음-福善禍淫', f"Wrong id: {bok['id']}"
    print("복선화음 福善禍淫 verified!")

    print("\n=== 8. Quarantined Contexts Check ===")
    quarantined = []
    for k, w in words.items():
        for c in w.get('contexts', []):
            content = c.get('content', '')
            if '朝廷' in content and '천거' in content:
                quarantined.append(('朝廷 천거', k))
            if '간장' in content and ('된장' in content or '식품' in content or '종자간장' in content):
                quarantined.append(('식품 간장', k))
    print(f"Quarantined Contexts in Active Study: {len(quarantined)}")
    assert len(quarantined) == 0, f"Quarantined items found: {quarantined}"

    print("\n=== 9. Active New Word Contexts Meaning Coverage ===")
    verified_new_ids = {r['id'] for r in review_data['records'] if r.get('review_status') == 'VERIFIED'}
    assert len(verified_new_ids) == 384, f"Expected 384 verified new words, got {len(verified_new_ids)}"
    active_new_contexts = 0
    active_new_contexts_with_meaning = 0
    for k, w in words.items():
        if w['id'] in verified_new_ids:
            for c in w.get('contexts', []):
                active_new_contexts += 1
                if c.get('meaning'):
                    active_new_contexts_with_meaning += 1
    print(f"Active New Contexts: {active_new_contexts} (Expected: 476)")
    print(f"Active New Contexts with Meaning: {active_new_contexts_with_meaning} (Expected: 476)")
    assert active_new_contexts == 476, f"Expected 476 active new contexts, got {active_new_contexts}"
    assert active_new_contexts_with_meaning == 476, f"Expected 476 with meaning, got {active_new_contexts_with_meaning}"

    print("\n=== 10. Display Policy Metadata Null Values Check ===")
    for field in ['brief', 'hanjaExplanation', 'category', 'difficulty']:
        non_nulls = [w['id'] for w in words.values() if w['id'] in verified_new_ids and w.get(field) is not None]
        assert len(non_nulls) == 0, f"Non-null {field} found in new words: {non_nulls}"
    print("All 384 new words have null brief, hanjaExplanation, category, difficulty!")

    print("\n=== 11. Source Hanja Readings and 不·率 Policy ===")
    words_with_readings = 0
    for wid in verified_new_ids:
        w = words[wid]
        assert 'hanjaSourceReadings' in w, f"Missing hanjaSourceReadings in {wid}"
        words_with_readings += 1
        for r in w['hanjaSourceReadings']:
            if r.get('character') in ['不', '率']:
                assert len(r.get('pairs', [])) == 0, f"Unverified reading not hidden for {r.get('character')} in {wid}"
    print(f"All {words_with_readings} new words have hanjaSourceReadings; 不 and 率 unverified readings hidden!")

    print("\n=== 12. Active Original Image Fallbacks (13 contexts) ===")
    image_contexts = []
    for k, w in words.items():
        for c in w.get('contexts', []):
            if 'source_display' in c:
                sd = c['source_display']
                image_contexts.append((k, c.get('source'), sd.get('page_label'), sd.get('image')[:30]))
    print(f"Active Image Fallback Contexts: {len(image_contexts)} (Expected: 13)")
    assert len(image_contexts) == 13, f"Expected 13 image fallbacks, got {len(image_contexts)}"

    print("\n=== 13. Consolidated Specialist Authority & POS Bindings ===")
    specialists = []
    pos_consolidated = []
    for k, w in words.items():
        for c in w.get('contexts', []):
            m = c.get('meaning', {})
            if m and m.get('specialist_authority'):
                specialists.append((k, c.get('source')))
            if m and m.get('dictionary_definitions'):
                for d in m['dictionary_definitions']:
                    if 'entry_pos_raw' in d:
                        pos_consolidated.append((k, c.get('source')))
    print(f"Specialist Authority Bindings: {len(specialists)} (Expect 33 total including 9 added)")
    print(f"Selected Definition POS Consolidated: {len(pos_consolidated)} (Expected: 19)")
    assert len(pos_consolidated) == 19, f"Expected 19 POS consolidated, got {len(pos_consolidated)}"

    print("\n=======================================================")
    print("ALL 13 DATA INTEGRITY VERIFICATION SUITES PASSED (100%)")
    print("=======================================================")

if __name__ == '__main__':
    run_verification()
