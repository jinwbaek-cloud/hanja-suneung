import os
import sys
import json
import re
import copy
import hashlib

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_js_path = os.path.join(base_dir, 'js', 'data.js')
    index_html_path = os.path.join(base_dir, 'index.html')
    candidate_html_path = os.path.join(base_dir, 'review_import_20261004 2', 'stage9C_actual_ui_candidate_v1.1.html')
    review_json_path = os.path.join(base_dir, 'review_import_20261004 2', 'hanalgukshwi_2017_2021_metadata_stage9C_editorial_review_v1.11.json')
    payload_json_path = os.path.join(base_dir, 'review_import_20261004 2', 'hanalgukshwi_2017_2021_editorial_payload_v2.3_display_candidate.json')

    print("=== Step 1: Pre-condition Baseline Verification ===")
    with open(data_js_path, 'rb') as f:
        data_js_bytes = f.read()
    current_sha256 = hashlib.sha256(data_js_bytes).hexdigest()
    expected_sha256 = 'f0a202c989bc3bbac87e9115975e71690c0a0b9caa24fbb8cc4837bf5b4cbc98'
    print(f"data.js SHA256: {current_sha256}")
    if current_sha256 != expected_sha256:
        print(f"FATAL: data.js SHA256 mismatch! Expected {expected_sha256}, got {current_sha256}")
        sys.exit(1)

    with open(data_js_path, 'r', encoding='utf-8') as f:
        data_js_text = f.read()
    prefix = 'window.MOCK_WORDS = '
    if not data_js_text.startswith(prefix):
        print("FATAL: data.js does not start with 'window.MOCK_WORDS = '")
        sys.exit(1)
    base_mock_words = json.loads(data_js_text[len(prefix):].rstrip().rstrip(';'))
    base_word_count = len(base_mock_words)
    base_context_count = sum(len(w.get('contexts', [])) for w in base_mock_words.values())
    print(f"Baseline Words: {base_word_count} (expected 700)")
    print(f"Baseline Contexts: {base_context_count} (expected 878)")
    if base_word_count != 700 or base_context_count != 878:
        print(f"FATAL: Baseline counts mismatch! Words: {base_word_count}/700, Contexts: {base_context_count}/878")
        sys.exit(1)

    print("Baseline verified 100% OK!")

    print("\n=== Step 2: Extract Verified Candidate Words from Tested Candidate ===")
    with open(candidate_html_path, 'r', encoding='utf-8') as f:
        cand_text = f.read()

    m = re.search(r'window\.MOCK_WORDS\s*=\s*(\{.+?\});window\.STAGE9_READING_NOTES', cand_text)
    if not m:
        print("FATAL: Could not extract window.MOCK_WORDS from candidate HTML!")
        sys.exit(1)

    candidate_words = json.loads(m.group(1))
    print(f"Candidate words extracted: {len(candidate_words)} keys")
    total_cand_contexts = sum(len(w.get('contexts', [])) for w in candidate_words.values())
    print(f"Candidate total contexts: {total_cand_contexts}")

    if len(candidate_words) != 1084 or total_cand_contexts != 1516:
        print(f"FATAL: Candidate counts mismatch! Expected 1084 words / 1516 contexts, got {len(candidate_words)} / {total_cand_contexts}")
        sys.exit(1)

    # Attach stage9C_reading_note explicitly on word objects as well
    notes = {
        "상쇄-相殺": "※ 殺은 여기서 ‘쇄’로 읽습니다.",
        "감쇄-減殺": "※ 殺은 여기서 ‘쇄’로 읽습니다."
    }
    for wid, note_text in notes.items():
        if wid in candidate_words:
            candidate_words[wid]["stage9C_reading_note"] = note_text

    print("\n=== Step 3: Write Updated js/data.js ===")
    # Format with clean 4-space indentation
    formatted_json = json.dumps(candidate_words, ensure_ascii=False, indent=4)
    notes_json = json.dumps(notes, ensure_ascii=False, indent=4)
    new_data_js_content = f"window.MOCK_WORDS = {formatted_json};\n\nwindow.STAGE9_READING_NOTES = {notes_json};\n"

    # Backup original data.js
    with open(data_js_path + '.pre_stage9c.bak', 'wb') as f:
        f.write(data_js_bytes)

    with open(data_js_path, 'w', encoding='utf-8') as f:
        f.write(new_data_js_content)
    print("Successfully wrote updated js/data.js!")

    print("\n=== Step 4: Apply Display Policy & Adapter to index.html ===")
    with open(index_html_path, 'r', encoding='utf-8') as f:
        index_html_content = f.read()

    # Backup original index.html
    with open(index_html_path + '.pre_stage9c.bak', 'w', encoding='utf-8') as f:
        f.write(index_html_content)

    s = index_html_content

    # 1. CSS
    css_target = '.print-area {\n      display: none;\n    }\n  </style>'
    css_replacement = '''.print-area {
      display: none;
    }
    .review-extra{border-top:1px solid #ded8ce;padding-top:12px;margin-top:12px}
    .review-extra a{color:#8B263E;text-decoration:underline}
    .review-extra img{max-width:100%;height:auto}
    .review-extra button{padding:8px 12px;border:1px solid #aaa;border-radius:8px}
    .review-extra dialog{width:96vw;height:94vh;max-width:none;overflow:auto}
    .review-extra dialog img{width:1200px;max-width:none}
    .review-extra p{overflow-wrap:anywhere}
  </style>'''
    assert css_target in s, 'css_target not found in index.html'
    s = s.replace(css_target, css_replacement)

    # 2. Stage9ContextDisplay component before App()
    comp_target = '    // --- Main React App ---\n    function App() {'
    comp_replacement = '''    // --- Main React App ---
    function Stage9ContextDisplay({ctx, word}) {
      const m=ctx.meaning||{}, scope=ctx.learning_choice_scope, sd=ctx.source_display;
      const dictionary=m.dictionary_definitions||[], specialist=m.specialist_authority;
      const openImage=()=>{const d=document.createElement('dialog');d.className='review-image-dialog';d.style.cssText='width:96vw;height:94vh;max-width:none;overflow:auto';const b=document.createElement('button');b.textContent='닫기';b.style.font='inherit';b.onclick=()=>d.close();const im=document.createElement('img');im.src=sd.image;im.alt=sd.page_label;im.style.cssText='display:block;width:1200px;max-width:none';d.append(b,im);document.body.append(d);d.addEventListener('close',()=>d.remove());d.showModal();};
      return <div className="review-extra" data-review-context="true">
        {sd && <section data-source-image="true"><p>{ctx.source} · {sd.page_label} · 평가원 원문 페이지</p><img src={sd.image} alt={sd.page_label}/><button onClick={openImage}>원문 확대</button></section>}
        {scope && <section data-choice-scope="true"><h4>확인된 선택지 범위</h4><p>{scope.display_text||ctx.content||ctx.desc}</p><p>{scope.question}번 · {scope.choice}번 선택지</p></section>}
        {dictionary.map((d,i)=><section key={i} data-dictionary="true"><h4>문맥별 사전 원문</h4><p>{d.raw_headword} {d.hanja} · {d.sense_label} · {Array.isArray(d.pos)?d.pos.join(', '):d.pos}</p><p>{d.definition}</p><a href={d.url} target="_blank" rel="noreferrer">{d.source}</a></section>)}
        {specialist && <section data-editorial="true"><h4>문맥 편집 설명</h4><p>{specialist.editorial_summary}</p><p>사전 원문과 구별한 설명 · {specialist.pos||''}</p><a href={specialist.url} target="_blank" rel="noreferrer">{specialist.source}</a><p>{specialist.source_locator}</p></section>}
        {(window.STAGE9_READING_NOTES?.[word.id]||word.stage9C_reading_note) && <p data-reading-note="true">{(window.STAGE9_READING_NOTES?.[word.id]||word.stage9C_reading_note)}</p>}
      </div>;
    }

    function App() {'''
    assert comp_target in s, 'comp_target not found in index.html'
    s = s.replace(comp_target, comp_replacement)

    # 3. window.__stage9Select helper
    helper_target = 'const [activeDetailContext, setActiveDetailContext] = useState(0);'
    helper_replacement = '''const [activeDetailContext, setActiveDetailContext] = useState(0);
      window.__stage9Select=(id,idx=0)=>{setSelectedWord(Object.values(MOCK_WORDS).find(x=>x.id===id));setActiveDetailContext(idx);setShowHanjaInContext(false);};'''
    assert helper_target in s, 'helper_target not found in index.html'
    s = s.replace(helper_target, helper_replacement)

    # 4. todayWord guards
    tw_cat_target = '''<span className="text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded bg-classicRed/10 border border-classicRed/20 text-classicRed">
                      {todayWord.category}
                    </span>'''
    tw_cat_replacement = '''{todayWord.category && (<span className="text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded bg-classicRed/10 border border-classicRed/20 text-classicRed">
                      {todayWord.category}
                    </span>)}'''
    assert tw_cat_target in s, 'tw_cat_target not found in index.html'
    s = s.replace(tw_cat_target, tw_cat_replacement)

    tw_brief_target = '''<p className="text-sm font-medium text-classicText leading-relaxed italic">
                    “{todayWord.brief}”
                  </p>'''
    tw_brief_replacement = '''{todayWord.brief && (<p className="text-sm font-medium text-classicText leading-relaxed italic">
                    “{todayWord.brief}”
                  </p>)}'''
    assert tw_brief_target in s, 'tw_brief_target not found in index.html'
    s = s.replace(tw_brief_target, tw_brief_replacement)

    # 5. selectedWord category and brief guards
    sw_cat_target = '''<span className={"text-xs font-bold uppercase px-2.5 py-0.5 rounded border " + (wordColorInfo ? wordColorInfo.badge : "")}>
                        {selectedWord.category}
                      </span>'''
    sw_cat_replacement = '''{selectedWord.category && (<span className={"text-xs font-bold uppercase px-2.5 py-0.5 rounded border " + (wordColorInfo ? wordColorInfo.badge : "")}>
                        {selectedWord.category}
                      </span>)}'''
    assert sw_cat_target in s, 'sw_cat_target not found in index.html'
    s = s.replace(sw_cat_target, sw_cat_replacement)

    sw_brief_target = '''<p className="text-lg text-classicText font-serif italic">
                      “{selectedWord.brief}”
                    </p>'''
    sw_brief_replacement = '''{selectedWord.brief && (<p data-policy-section="brief" className="text-lg text-classicText font-serif italic">{`“${selectedWord.brief}”`}</p>)}'''
    assert sw_brief_target in s, 'sw_brief_target not found in index.html'
    s = s.replace(sw_brief_target, sw_brief_replacement)

    # 6. Central Contents columns & cards
    cent_target = '''              {/* Central Contents (2 Columns) */}
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">

                {/* Central Left Column: Dictionary & Hanja Analysis */}
                <div className="flex flex-col gap-8">

                  {/* Dictionary Definition Card */}'''
    cent_replacement = '''              {/* Central Contents (2 Columns) */}
              <div className={(selectedWord.definition || selectedWord.hanjaBreakdown?.length || selectedWord.hanjaExplanation || selectedWord.hanjaSourceReadings?.some(x=>x.pairs.length)) ? "grid grid-cols-1 lg:grid-cols-2 gap-8" : "grid grid-cols-1 gap-8"}>

{(selectedWord.definition || selectedWord.hanjaBreakdown?.length || selectedWord.hanjaExplanation || selectedWord.hanjaSourceReadings?.some(x=>x.pairs.length)) && (<div data-policy-section="left-column">
                {/* Central Left Column: Dictionary & Hanja Analysis */}
                <div className="flex flex-col gap-8">

{selectedWord.definition && (<div data-policy-section="word-definition">
                  {/* Dictionary Definition Card */}'''
    assert cent_target in s, 'cent_target not found in index.html'
    s = s.replace(cent_target, cent_replacement)

    # End of Dictionary Definition Card & Hanja Source readings & Hanja Breakdown Card
    hanja_wrap_target = '''                    </div>
                  </div>

                  {/* Hanja Breakdown Card */}
                  <div className={"classic-card rounded-3xl p-6 md:p-8 flex flex-col gap-6 shadow-md relative overflow-hidden group transition-all duration-300 " + (wordColorInfo ? wordColorInfo.border : "")}>'''
    hanja_wrap_replacement = '''                    </div>
                  </div>

</div>)}
{selectedWord.hanjaSourceReadings?.some(x=>x.pairs.length) && <section data-source-readings className="bg-white rounded-3xl border border-classicBorder p-6"><h3 className="font-bold mb-4">출처 자료의 훈·음</h3><div className="space-y-3">{selectedWord.hanjaSourceReadings.filter(x=>x.pairs.length).map(x=><div key={x.character}><b className="text-xl mr-3">{x.character}</b>{x.pairs.map((p,i)=><span key={i} className="mr-3">{p[0].join('·')} / {p[1].join('·')}</span>)}<a className="text-xs text-classicMuted underline block" href={x.source_url} target="_blank" rel="noopener noreferrer">{x.source}</a></div>)}</div></section>}{(selectedWord.hanjaBreakdown?.length || selectedWord.hanjaExplanation) && (<div data-policy-section="hanja-card">
                  {/* Hanja Breakdown Card */}
                  <div className={"classic-card rounded-3xl p-6 md:p-8 flex flex-col gap-6 shadow-md relative overflow-hidden group transition-all duration-300 " + (wordColorInfo ? wordColorInfo.border : "")}>'''
    assert hanja_wrap_target in s, 'hanja_wrap_target not found in index.html'
    s = s.replace(hanja_wrap_target, hanja_wrap_replacement)

    # item.meaning in Hanja breakdown
    item_meaning_target = '<p className="text-[10px] text-classicMuted font-medium mt-1 leading-snug">{item.meaning}</p>'
    item_meaning_replacement = '{item.meaning && <p className="text-[10px] text-classicMuted font-medium mt-1 leading-snug">{item.meaning}</p>}'
    assert item_meaning_target in s, 'item_meaning_target not found in index.html'
    s = s.replace(item_meaning_target, item_meaning_replacement)

    # hanjaExplanation guard & close left column
    exp_close_target = '''                    <div className="bg-classicBg/40 border border-classicBorder rounded-2xl p-5 mt-2">
                      <p className="text-sm font-serif font-bold text-classicText mb-2 flex items-center gap-1.5">
                        <span className={wordColorInfo ? wordColorInfo.text : "text-classicRed"}>✒️</span> 자구 속뜻 풀이
                      </p>
                      <p className="text-sm text-classicText leading-relaxed font-medium">
                        {selectedWord.hanjaExplanation}
                      </p>
                    </div>
                  </div>

                </div>

                {/* Central Right Column: Suneung Usage Cases */}'''
    exp_close_replacement = '''{selectedWord.hanjaExplanation && (<div data-policy-section="hanja-explanation">
                    <div className="bg-classicBg/40 border border-classicBorder rounded-2xl p-5 mt-2">
                      <p className="text-sm font-serif font-bold text-classicText mb-2 flex items-center gap-1.5">
                        <span className={wordColorInfo ? wordColorInfo.text : "text-classicRed"}>✒️</span> 자구 속뜻 풀이
                      </p>
                      <p className="text-sm text-classicText leading-relaxed font-medium">
                        {selectedWord.hanjaExplanation}
                      </p>
                    </div></div>)}

                  </div>
</div>)}

                </div>

</div>)}
                {/* Central Right Column: Suneung Usage Cases */}'''
    assert exp_close_target in s, 'exp_close_target not found in index.html'
    s = s.replace(exp_close_target, exp_close_replacement)

    # 7. Suneung usage cases: render bold and Stage9ContextDisplay
    detail_ctx_target = '''                              <p id="detailContextContent" className="text-sm text-classicText leading-relaxed font-medium">
                                {renderContentWithBold(ctx.content || ctx.desc, selectedWord)}
                              </p>'''
    detail_ctx_replacement = '''                              <p id="detailContextContent" className="text-sm text-classicText leading-relaxed font-medium">
                                {ctx.source_display ? null : renderContentWithBold(ctx.learning_choice_scope?.display_text || ctx.content || ctx.desc, selectedWord)}
                              </p>

                              <Stage9ContextDisplay ctx={ctx} word={selectedWord} />'''
    assert detail_ctx_target in s, 'detail_ctx_target not found in index.html'
    s = s.replace(detail_ctx_target, detail_ctx_replacement)

    # 8. Card list category badge guard
    card_cat_target = '''<span className={"text-[10px] font-bold uppercase px-2 py-0.5 rounded border flex items-center gap-1 " + color.badge}>
                                  {getCategoryIcon(wordData.category, "w-3 h-3")}
                                  {wordData.category}
                                </span>'''
    card_cat_replacement = '''{wordData.category && (<span className={"text-[10px] font-bold uppercase px-2 py-0.5 rounded border flex items-center gap-1 " + color.badge}>
                                  {getCategoryIcon(wordData.category, "w-3 h-3")}
                                  {wordData.category}
                                </span>)}'''
    assert card_cat_target in s, 'card_cat_target not found in index.html'
    s = s.replace(card_cat_target, card_cat_replacement)

    # 9. Card list brief guard
    card_brief_target = '''<p className="text-xs text-classicMuted leading-relaxed font-medium">
                              {wordData.brief}
                            </p>'''
    card_brief_replacement = '''{wordData.brief && (<p className="text-xs text-classicMuted leading-relaxed font-medium">
                              {wordData.brief}
                            </p>)}'''
    assert card_brief_target in s, 'card_brief_target not found in index.html'
    s = s.replace(card_brief_target, card_brief_replacement)

    # 10. Card list context text with source_display fallback
    card_ctx_target = '''<p className="text-[11px] text-classicText leading-relaxed font-medium bg-classicBg/60 p-2 rounded border border-classicBorder/30 italic">
                                        🔍 {renderContentWithBold(currentCtx.desc || currentCtx.content, wordData)}
                                      </p>'''
    card_ctx_replacement = '''<p className="text-[11px] text-classicText leading-relaxed font-medium bg-classicBg/60 p-2 rounded border border-classicBorder/30 italic">
                                        🔍 {renderContentWithBold(currentCtx.source_display ? '원문 페이지를 상세 화면에서 확인하세요.' : currentCtx.learning_choice_scope?.display_text || currentCtx.desc || currentCtx.content, wordData)}
                                      </p>'''
    assert card_ctx_target in s, 'card_ctx_target not found in index.html'
    s = s.replace(card_ctx_target, card_ctx_replacement)

    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(s)
    print("Successfully wrote updated index.html with all approved display policy adapters!")

if __name__ == '__main__':
    main()
