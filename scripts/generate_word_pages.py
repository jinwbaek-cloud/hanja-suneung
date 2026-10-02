#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/generate_word_pages.py

Deterministic generator for:
1. 700 Suneung static SEO word pages (word/[slug].html) with percent-encoded canonical/OG/links
2. Full vocabulary index page (word/index.html) with 700 static links grouped by initial consonant
3. Common stylesheet (word/word.css)
4. Expanded sitemap.xml with 704 URLs (3 base + 1 word index + 700 percent-encoded word URLs)
"""

import json
import os
import re
import html
import xml.etree.ElementTree as ET
from urllib.parse import quote

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "js", "data.js")
WORD_DIR = os.path.join(BASE_DIR, "word")
CSS_FILE = os.path.join(WORD_DIR, "word.css")
INDEX_FILE = os.path.join(WORD_DIR, "index.html")
SITEMAP_FILE = os.path.join(BASE_DIR, "sitemap.xml")

CHOSUNG = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]


def encode_url_path(path):
    """Single centralized URL helper for percent encoding.
    Preserves safe URI characters: /-._~
    """
    return quote(path, safe="/-._~")


def get_chosung(char):
    if "가" <= char <= "힣":
        code = ord(char) - ord("가")
        cho_idx = code // (21 * 28)
        cho = CHOSUNG[cho_idx]
        if cho == "ㄲ": return "ㄱ"
        if cho == "ㄸ": return "ㄷ"
        if cho == "ㅃ": return "ㅂ"
        if cho == "ㅆ": return "ㅅ"
        if cho == "ㅉ": return "ㅈ"
        return cho
    return "기타"


COMMON_CSS = """/* word/word.css - Common stylesheet for Hanal Gukshi Suneung word SEO pages */
:root {
  --classicBg: #F9F6F0;
  --classicText: #2C2520;
  --classicRed: #8B263E;
  --classicTeal: #3A606E;
  --classicCard: #FDFCF7;
  --classicBorder: #E6DFD3;
  --classicMuted: #7A7267;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background-color: var(--classicBg);
  color: var(--classicText);
  font-family: 'Outfit', 'Noto Sans KR', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  padding: 0 16px;
  -webkit-font-smoothing: antialiased;
}
.container {
  max-width: 720px;
  margin: 0 auto;
  padding: 24px 0 64px;
}
header.site-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 20px;
  margin-bottom: 24px;
  border-bottom: 1px solid var(--classicBorder);
}
.back-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--classicRed);
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
}
.back-link:hover {
  text-decoration: underline;
}
.service-tag {
  font-size: 12px;
  font-weight: 500;
  color: var(--classicMuted);
  background: rgba(122, 114, 103, 0.1);
  padding: 4px 10px;
  border-radius: 9999px;
}
.hero-card {
  background: var(--classicCard);
  border: 1px solid var(--classicBorder);
  border-radius: 16px;
  padding: 28px 24px;
  margin-bottom: 20px;
  box-shadow: 0 4px 20px -2px rgba(139, 38, 62, 0.04);
}
.category-pill {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  color: var(--classicTeal);
  background: rgba(58, 96, 110, 0.1);
  padding: 3px 10px;
  border-radius: 6px;
  margin-bottom: 12px;
}
h1.word-title {
  font-size: 32px;
  font-weight: 800;
  line-height: 1.25;
  color: var(--classicText);
  margin-bottom: 8px;
  letter-spacing: -0.02em;
  word-break: keep-all;
  overflow-wrap: break-word;
}
.word-hanja {
  font-family: 'Noto Serif KR', Georgia, serif;
  color: var(--classicRed);
  font-weight: 700;
  margin-left: 6px;
}
.sound-info {
  font-size: 14px;
  color: var(--classicMuted);
}
.section-card {
  background: var(--classicCard);
  border: 1px solid var(--classicBorder);
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 20px;
  box-shadow: 0 4px 20px -2px rgba(139, 38, 62, 0.03);
}
h2.section-heading {
  font-size: 18px;
  font-weight: 700;
  color: var(--classicText);
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1px solid rgba(230, 223, 211, 0.7);
  padding-bottom: 10px;
}
.brief-box {
  background: #FFF9F3;
  border: 1px solid #F0DCCE;
  border-left: 4px solid var(--classicRed);
  border-radius: 8px;
  padding: 16px;
  font-size: 16px;
  font-weight: 600;
  color: #4A2E18;
  line-height: 1.5;
}
.definition-text {
  font-size: 15px;
  color: var(--classicText);
  line-height: 1.7;
  margin-bottom: 8px;
}
.source-meta {
  font-size: 12px;
  color: var(--classicMuted);
}
.hanja-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 12px;
  margin-bottom: 16px;
}
.hanja-char-card {
  background: #F8F5EE;
  border: 1px solid #E8E1D5;
  border-radius: 10px;
  padding: 14px 12px;
  text-align: center;
}
.hanja-char {
  font-family: 'Noto Serif KR', Georgia, serif;
  font-size: 32px;
  font-weight: 700;
  color: var(--classicRed);
  line-height: 1.1;
  margin-bottom: 6px;
}
.hanja-hun-sound {
  font-size: 13px;
  font-weight: 600;
  color: var(--classicText);
  margin-bottom: 4px;
}
.hanja-meaning {
  font-size: 11px;
  color: var(--classicMuted);
  line-height: 1.4;
}
.hanja-explanation {
  font-size: 14px;
  color: #3D3833;
  line-height: 1.7;
  background: rgba(58, 96, 110, 0.04);
  border-left: 3px solid var(--classicTeal);
  padding: 12px 14px;
  border-radius: 0 8px 8px 0;
}
.homonym-notice {
  margin-top: 14px;
  background: #F0F4F6;
  border: 1px solid #D0DEE5;
  border-radius: 8px;
  padding: 12px 14px;
  font-size: 13px;
  color: #234351;
}
.homonym-link {
  color: var(--classicRed);
  font-weight: 600;
  text-decoration: underline;
}
.context-item {
  padding: 16px 0;
  border-bottom: 1px dashed var(--classicBorder);
}
.context-item:first-child {
  padding-top: 0;
}
.context-item:last-child {
  padding-bottom: 0;
  border-bottom: none;
}
.context-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}
.context-source-badge {
  font-size: 12px;
  font-weight: 700;
  color: var(--classicRed);
  background: rgba(139, 38, 62, 0.08);
  padding: 2px 8px;
  border-radius: 4px;
}
.context-domain-badge {
  font-size: 12px;
  color: var(--classicMuted);
  background: rgba(122, 114, 103, 0.08);
  padding: 2px 8px;
  border-radius: 4px;
}
.context-passage {
  font-size: 15px;
  color: var(--classicText);
  line-height: 1.7;
  background: #FAF7F2;
  border: 1px solid #ECE4D8;
  border-radius: 8px;
  padding: 14px 16px;
  margin-bottom: 10px;
  font-style: normal;
}
.tip-box {
  background: #EDF4F2;
  border: 1px solid #CCE0D9;
  border-radius: 8px;
  padding: 12px 14px;
  font-size: 13px;
  color: #1F453B;
  line-height: 1.6;
}
.cta-card {
  text-align: center;
  background: linear-gradient(135deg, #FDFCF7 0%, #F5F0E6 100%);
  border: 1px solid var(--classicBorder);
  border-radius: 16px;
  padding: 32px 20px;
  margin-top: 32px;
}
.cta-title {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 8px;
}
.cta-desc {
  font-size: 13px;
  color: var(--classicMuted);
  margin-bottom: 18px;
}
.btn-primary {
  display: inline-block;
  background: var(--classicRed);
  color: #fff;
  text-decoration: none;
  font-size: 14px;
  font-weight: 700;
  padding: 12px 24px;
  border-radius: 9999px;
  box-shadow: 0 4px 12px rgba(139, 38, 62, 0.25);
  transition: transform 0.2s, background-color 0.2s;
}
.btn-primary:hover {
  background: #731F33;
  transform: translateY(-1px);
}
.footer-links {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 20px;
  font-size: 13px;
}
.footer-links a {
  color: var(--classicMuted);
  text-decoration: none;
}
.footer-links a:hover {
  color: var(--classicRed);
  text-decoration: underline;
}
.site-footer {
  text-align: center;
  margin-top: 32px;
  font-size: 12px;
  color: var(--classicMuted);
}

/* Styles for word/index.html */
.index-jump-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  background: var(--classicCard);
  border: 1px solid var(--classicBorder);
  border-radius: 12px;
  padding: 12px 14px;
  margin-bottom: 24px;
  justify-content: center;
}
.jump-chip {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: #F4EFE6;
  color: var(--classicText);
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  transition: all 0.15s ease;
}
.jump-chip:hover {
  background: var(--classicRed);
  color: #fff;
}
.index-section {
  margin-bottom: 32px;
}
.index-chosung-header {
  font-size: 20px;
  font-weight: 800;
  color: var(--classicRed);
  border-bottom: 2px solid var(--classicBorder);
  padding-bottom: 8px;
  margin-bottom: 14px;
  display: flex;
  align-items: baseline;
  gap: 8px;
}
.index-chosung-count {
  font-size: 12px;
  color: var(--classicMuted);
  font-weight: 500;
}
.index-word-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 10px;
}
.index-word-card {
  display: block;
  background: var(--classicCard);
  border: 1px solid var(--classicBorder);
  border-radius: 10px;
  padding: 12px 14px;
  text-decoration: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px rgba(0,0,0,0.02);
}
.index-word-card:hover {
  border-color: var(--classicRed);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(139, 38, 62, 0.08);
}
.iwc-word {
  font-size: 15px;
  font-weight: 700;
  color: var(--classicText);
}
.iwc-hanja {
  font-family: 'Noto Serif KR', Georgia, serif;
  font-size: 13px;
  color: var(--classicRed);
  margin-left: 4px;
}
.iwc-brief {
  display: block;
  font-size: 11px;
  color: var(--classicMuted);
  margin-top: 4px;
  line-height: 1.4;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
"""


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        text = f.read()
    idx = text.find("{")
    last_idx = text.rfind("}")
    return json.loads(text[idx : last_idx + 1])


def analyze_homonyms_and_slugs(db):
    word_groups = {}
    for key, item in db.items():
        w = (item.get("word") or key).strip()
        if w not in word_groups:
            word_groups[w] = []
        word_groups[w].append((key, item))

    duplicate_groups = {w: lst for w, lst in word_groups.items() if len(lst) > 1}

    slug_map = {}  # key -> slug info
    used_slugs = {}  # raw_slug -> key

    for key, item in db.items():
        w = (item.get("word") or key).strip()
        hanja = (item.get("hanja") or "").strip()
        is_dup = len(word_groups[w]) > 1

        if is_dup:
            raw_slug = f"{w}-{hanja}".replace(" ", "-")
        else:
            raw_slug = w.replace(" ", "-")

        assert raw_slug.strip() != "", f"Empty slug for {key}"
        assert " " not in raw_slug, f"Whitespace in slug: {raw_slug}"

        if raw_slug in used_slugs:
            raise ValueError(f"Slug collision: '{raw_slug}' used by '{used_slugs[raw_slug]}' and '{key}'")

        used_slugs[raw_slug] = key

        # Centralized percent-encoded URL and paths
        encoded_slug = encode_url_path(raw_slug)
        filename = f"{raw_slug}.html"
        href_path = f"/word/{encoded_slug}.html"
        canonical_url = f"https://suneung.easyhanja.org/word/{encoded_slug}.html"

        slug_map[key] = {
            "raw_slug": raw_slug,
            "encoded_slug": encoded_slug,
            "filename": filename,
            "href": href_path,
            "canonical_url": canonical_url,
            "is_duplicate": is_dup,
            "word_group": word_groups[w],
        }

    return word_groups, duplicate_groups, slug_map


def build_page_html(item, meta_info, all_slug_map):
    word = (item.get("word") or "").strip()
    hanja = (item.get("hanja") or "").strip()
    sound = (item.get("sound") or word).strip()
    category = (item.get("category") or "").strip()
    tags = item.get("tags") or []
    brief = (item.get("brief") or "").strip()
    definition = (item.get("definition") or "").strip()
    definitionSource = (item.get("definitionSource") or "").strip()
    hanjaBreakdown = item.get("hanjaBreakdown") or []
    hanjaExplanation = (item.get("hanjaExplanation") or "").strip()
    contexts = item.get("contexts") or []
    is_dup = meta_info["is_duplicate"]
    word_group = meta_info["word_group"]
    canonical_url = meta_info["canonical_url"]

    # SEO Title & Description (Neutral, truthful, ungrounded words removed)
    title = f"{word}({hanja}) 뜻·한자·수능 기출 문맥 | 한알국쉬 수능"
    desc = f"{word}({hanja})의 한자 풀이와 사전 뜻풀이, 수능 기출 문맥을 확인해 보세요. {brief}"

    # Category badge text
    cat_badges = [category] if category else []
    if tags:
        cat_badges.extend(tags)
    cat_display = " · ".join(cat_badges)

    # Hanja breakdown HTML
    breakdown_html = ""
    if hanjaBreakdown:
        cards = []
        for hb in hanjaBreakdown:
            c = html.escape(hb.get("character") or "")
            hun = html.escape(hb.get("hun") or "")
            snd = html.escape(hb.get("sound") or "")
            hun_snd = f"{hun} {snd}" if hun else snd
            m = html.escape(hb.get("meaning") or "")
            cards.append(f"""          <div class="hanja-char-card">
            <div class="hanja-char">{c}</div>
            <div class="hanja-hun-sound">{hun_snd}</div>
            <div class="hanja-meaning">{m}</div>
          </div>""")
        breakdown_html = f"""        <div class="hanja-grid">
{chr(10).join(cards)}
        </div>"""

    # Hanja explanation HTML
    explanation_html = ""
    if hanjaExplanation:
        explanation_html = f"""        <div class="hanja-explanation">
          {html.escape(hanjaExplanation)}
        </div>"""

    # Homonym cross-links (automatic linking with encoded href)
    homonym_html = ""
    if is_dup:
        other_links = []
        for o_key, o_item in word_group:
            o_hanja = (o_item.get("hanja") or "").strip()
            if o_key != item.get("id", "") and (o_hanja != hanja or o_key != item.get("word")):
                o_href = all_slug_map[o_key]["href"]
                other_links.append(f'<a class="homonym-link" href="{o_href}">\'{word}({o_hanja})\'</a>')
        if other_links:
            links_str = ", ".join(other_links)
            homonym_html = f"""        <div class="homonym-notice">
          💡 <strong>동음이의어 안내:</strong> 소리는 같으나 한자와 뜻이 다른 {links_str} 표제어 페이지가 있습니다.
        </div>"""

    # Contexts HTML (Neutral heading: 수능 기출 문맥)
    contexts_html = []
    for ctx in contexts:
        c_src = html.escape(ctx.get("source") or "")
        c_sec = html.escape(ctx.get("section") or "")
        c_dom = html.escape(ctx.get("domain") or "")
        c_content = html.escape(ctx.get("content") or "")
        c_tip = ctx.get("tip") or ""

        badges = [f'<span class="context-source-badge">{c_src}</span>'] if c_src else []
        meta_sub = []
        if c_sec: meta_sub.append(c_sec)
        if c_dom: meta_sub.append(c_dom)
        if meta_sub:
            badges.append(f'<span class="context-domain-badge">{" · ".join(meta_sub)}</span>')

        header_str = f'<div class="context-header">{"".join(badges)}</div>' if badges else ""
        passage_str = f'<blockquote class="context-passage">"{c_content}"</blockquote>'
        tip_str = f'<div class="tip-box">{html.escape(c_tip)}</div>' if c_tip else ""

        contexts_html.append(f"""        <div class="context-item">
          {header_str}
          {passage_str}
          {tip_str}
        </div>""")

    all_contexts_str = "\n".join(contexts_html)

    # Standard JSON-LD Schema: WebPage -> mainEntity (DefinedTerm) -> inDefinedTermSet (DefinedTermSet)
    json_ld = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canonical_url,
        "mainEntity": {
            "@type": "DefinedTerm",
            "name": word,
            "alternateName": hanja,
            "description": definition,
            "inDefinedTermSet": {
                "@type": "DefinedTermSet",
                "name": "한알국쉬 수능 국어 한자 어휘",
                "url": "https://suneung.easyhanja.org/"
            }
        }
    }
    json_ld_str = json.dumps(json_ld, ensure_ascii=False, indent=2)

    def_source_str = f'<div class="source-meta">출처: {html.escape(definitionSource)}</div>' if definitionSource else ""

    page_html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="한알국쉬 수능">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{canonical_url}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(desc)}">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&family=Noto+Serif+KR:wght@600;700&family=Outfit:wght@500;700;800&display=swap" rel="stylesheet">

  <!-- Common Stylesheet -->
  <link rel="stylesheet" href="/word/word.css">

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
{json_ld_str}
  </script>
</head>
<body>
  <div class="container">
    <header class="site-header">
      <a href="/" class="back-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
        한알국쉬 수능으로
      </a>
      <span class="service-tag">수능 국어 한자 어휘</span>
    </header>

    <main>
      <article>
        <!-- 표제어 Hero -->
        <div class="hero-card">
          <span class="category-pill">{html.escape(cat_display)}</span>
          <h1 class="word-title">{html.escape(word)}<span class="word-hanja">({html.escape(hanja)})</span></h1>
          <div class="sound-info">[독음: {html.escape(sound)}]</div>
        </div>

        <!-- 핵심 뜻 -->
        <section class="section-card">
          <h2 class="section-heading">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--classicRed)">
              <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
            </svg>
            핵심 의미
          </h2>
          <div class="brief-box">
            {html.escape(brief)}
          </div>
        </section>

        <!-- 사전 뜻풀이 -->
        <section class="section-card">
          <h2 class="section-heading">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--classicTeal)">
              <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
              <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
            </svg>
            사전 뜻풀이
          </h2>
          <p class="definition-text">{html.escape(definition)}</p>
          {def_source_str}
        </section>

        <!-- 한자 풀이 -->
        <section class="section-card">
          <h2 class="section-heading">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--classicRed)">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="16" x2="12" y2="12"></line>
              <line x1="12" y1="8" x2="12.01" y2="8"></line>
            </svg>
            한자 낱자 분해 및 결합 원리
          </h2>
{breakdown_html}
{explanation_html}
{homonym_html}
        </section>

        <!-- 수능 기출 문맥 -->
        <section class="section-card">
          <h2 class="section-heading">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--classicTeal)">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              <polyline points="14 2 14 8 20 8"></polyline>
              <line x1="16" y1="13" x2="8" y2="13"></line>
              <line x1="16" y1="17" x2="8" y2="17"></line>
              <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
            수능 기출 문맥
          </h2>
{all_contexts_str}
        </section>

        <!-- 하단 CTA: Includes link to /word/ 전체 어휘 목록 -->
        <div class="cta-card">
          <div class="cta-title">한알국쉬 수능 국어 한자 어휘</div>
          <div class="cta-desc">한알국쉬 수능의 700개 어휘와 미니 퀴즈를 학습해 보세요.</div>
          <a href="/" class="btn-primary">한알국쉬 수능에서 더 많은 어휘 학습하기 →</a>
          <div class="footer-links">
            <a href="/word/">전체 어휘 목록</a>
            <a href="/about.html">서비스 소개</a>
            <a href="/guide.html">학습 가이드</a>
          </div>
        </div>
      </article>
    </main>

    <footer class="site-footer">
      <p>© 2026 한알국쉬 수능 (Hanal Gukshi). All rights reserved.</p>
    </footer>
  </div>
</body>
</html>'''
    return page_html


def build_index_html(db, slug_map):
    # Group and sort by initial consonant and then (word, hanja)
    consonants = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    grouped = {c: [] for c in consonants}

    # Sort all keys alphabetically by (word, hanja)
    sorted_keys = sorted(db.keys(), key=lambda k: ((db[k].get("word") or k).strip(), (db[k].get("hanja") or "").strip()))

    for k in sorted_keys:
        item = db[k]
        w = (item.get("word") or k).strip()
        cho = get_chosung(w[0])
        if cho not in grouped:
            grouped[cho] = []
        grouped[cho].append((k, item))

    # Jump bar HTML
    jump_chips = []
    for c in consonants:
        if grouped[c]:
            jump_chips.append(f'<a href="#{c}" class="jump-chip">{c}</a>')
    jump_bar_html = f"""    <nav class="index-jump-nav" aria-label="초성 바로가기">
      {"\n      ".join(jump_chips)}
    </nav>"""

    # Sections HTML
    sections_html = []
    for c in consonants:
        items = grouped[c]
        if not items:
            continue
        cards = []
        for k, item in items:
            w = html.escape((item.get("word") or k).strip())
            h = html.escape((item.get("hanja") or "").strip())
            b = html.escape((item.get("brief") or "").strip())
            href = slug_map[k]["href"]
            cards.append(f"""        <a class="index-word-card" href="{href}">
          <span class="iwc-word">{w}</span><span class="iwc-hanja">({h})</span>
          <span class="iwc-brief">{b}</span>
        </a>""")

        cards_str = "\n".join(cards)
        sections_html.append(f"""    <section class="index-section" id="{c}">
      <h2 class="index-chosung-header">{c} <span class="index-chosung-count">({len(items)}개)</span></h2>
      <div class="index-word-grid">
{cards_str}
      </div>
    </section>""")

    all_sections_str = "\n".join(sections_html)

    title = "수능 국어 한자 어휘 700개 전체 목록 | 한알국쉬 수능"
    desc = "한알국쉬 수능에 수록된 700개 한자 어휘를 가나다순으로 확인하고 각 표제어의 뜻풀이, 한자 풀이, 수능 기출 문맥을 살펴볼 수 있습니다."
    canonical_url = "https://suneung.easyhanja.org/word/"

    json_ld = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": title,
        "description": desc,
        "url": canonical_url,
        "inDefinedTermSet": {
            "@type": "DefinedTermSet",
            "name": "한알국쉬 수능 국어 한자 어휘",
            "url": "https://suneung.easyhanja.org/"
        }
    }
    json_ld_str = json.dumps(json_ld, ensure_ascii=False, indent=2)

    index_html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="한알국쉬 수능">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{canonical_url}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(desc)}">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&family=Noto+Serif+KR:wght@600;700&family=Outfit:wght@500;700;800&display=swap" rel="stylesheet">

  <!-- Common Stylesheet -->
  <link rel="stylesheet" href="/word/word.css">

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
{json_ld_str}
  </script>
</head>
<body>
  <div class="container">
    <header class="site-header">
      <a href="/" class="back-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
        한알국쉬 수능으로
      </a>
      <span class="service-tag">수능 국어 한자 어휘</span>
    </header>

    <main>
      <div class="hero-card">
        <span class="category-pill">700 어휘 색인</span>
        <h1 class="word-title">수능 국어 한자 어휘 전체 목록</h1>
        <p class="definition-text" style="margin-top: 8px;">
          한알국쉬 수능에 수록된 700개 한자 어휘를 가나다순으로 확인하고 각 표제어의 뜻풀이, 한자 풀이, 수능 기출 문맥을 살펴볼 수 있습니다.
        </p>
      </div>

{jump_bar_html}

{all_sections_str}

      <div class="cta-card">
        <div class="cta-title">한알국쉬 수능 국어 한자 어휘</div>
        <div class="cta-desc">한알국쉬 수능에서 700개 어휘와 미니 퀴즈를 학습해 보세요.</div>
        <a href="/" class="btn-primary">한알국쉬 수능 홈으로 →</a>
        <div class="footer-links">
          <a href="/about.html">서비스 소개</a>
          <a href="/guide.html">학습 가이드</a>
        </div>
      </div>
    </main>

    <footer class="site-footer">
      <p>© 2026 한알국쉬 수능 (Hanal Gukshi). All rights reserved.</p>
    </footer>
  </div>
</body>
</html>'''
    return index_html


def update_sitemap(slug_map):
    # Preserving the original 3 base URLs with historical lastmod
    base_urls = [
        {"loc": "https://suneung.easyhanja.org/", "lastmod": "2026-09-08"},
        {"loc": "https://suneung.easyhanja.org/about.html", "lastmod": "2026-09-08"},
        {"loc": "https://suneung.easyhanja.org/guide.html", "lastmod": "2026-09-08"},
    ]

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]

    for bu in base_urls:
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{bu['loc']}</loc>")
        xml_lines.append(f"    <lastmod>{bu['lastmod']}</lastmod>")
        xml_lines.append("  </url>")

    # 1 Word index URL
    xml_lines.append("  <url>")
    xml_lines.append("    <loc>https://suneung.easyhanja.org/word/</loc>")
    xml_lines.append("  </url>")

    # 700 word URLs sorted deterministically by raw slug, using encoded URLs
    for key, info in sorted(slug_map.items(), key=lambda x: x[1]["raw_slug"]):
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{info['canonical_url']}</loc>")
        xml_lines.append("  </url>")

    xml_lines.append("</urlset>\n")
    sitemap_content = "\n".join(xml_lines)

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap_content)


def main():
    print("=== 1. Loading js/data.js ===")
    db = load_data()
    print(f"Loaded {len(db)} records from js/data.js")
    assert len(db) == 700, f"Expected 700 records, got {len(db)}"

    print("\n=== 2. Analyzing Homonyms and Generating Slugs ===")
    word_groups, duplicate_groups, slug_map = analyze_homonyms_and_slugs(db)
    print(f"Total Unique Words: {len(word_groups)}")
    print(f"Duplicate Word Groups: {len(duplicate_groups)} ({sum(len(v) for v in duplicate_groups.values())} entries)")
    print(f"Total Slugs Generated: {len(slug_map)}")

    os.makedirs(WORD_DIR, exist_ok=True)

    print("\n=== 3. Writing Common CSS: word/word.css ===")
    with open(CSS_FILE, "w", encoding="utf-8") as f:
        f.write(COMMON_CSS.strip() + "\n")
    print(f"Written: {CSS_FILE} ({os.path.getsize(CSS_FILE)} bytes)")

    print("\n=== 4. Generating 700 Word HTML Pages ===")
    for key, item in db.items():
        info = slug_map[key]
        filepath = os.path.join(WORD_DIR, info["filename"])
        content = build_page_html(item, info, slug_map)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    print(f"Generated 700 HTML files in {WORD_DIR}")

    print("\n=== 5. Generating Full Vocabulary Index: word/index.html ===")
    index_content = build_index_html(db, slug_map)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"Generated: {INDEX_FILE} ({os.path.getsize(INDEX_FILE)} bytes)")

    print("\n=== 6. Updating sitemap.xml with 704 URLs ===")
    update_sitemap(slug_map)
    print(f"Updated: {SITEMAP_FILE} with 704 URLs")


if __name__ == "__main__":
    main()
