# -*- coding: utf-8 -*-
import os, glob, re, json

base_dir = r"D:\winch-hegazy"
html_files = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if f.endswith('.html')]
html_files += [os.path.join(base_dir, 'blog', f) for f in os.listdir(os.path.join(base_dir, 'blog')) if f.endswith('.html')]

print(f"Total HTML files analyzed: {len(html_files)}")

report = {
    "technical_seo": {
        "status": "PASS",
        "total_files": len(html_files),
        "valid_json_ld_schemas": 0,
        "schema_errors": [],
        "missing_canonicals": [],
        "broken_images": [],
        "missing_alts": [],
        "mobile_viewport_ok": 0
    },
    "content_seo": {
        "status": "PASS",
        "h1_counts": {},
        "missing_h1": [],
        "titles": {},
        "meta_descriptions": {},
        "short_descriptions": [],
        "keyword_coverage": {}
    },
    "aeo_geo": {
        "status": "PASS",
        "has_llms_txt": os.path.exists(os.path.join(base_dir, "llms.txt")),
        "has_llms_full_txt": os.path.exists(os.path.join(base_dir, "llms-full.txt")),
        "faq_schema_count": 0,
        "video_schema_count": 0,
        "local_business_schema_count": 0
    },
    "local_seo": {
        "status": "PASS",
        "has_maps_embed": 0,
        "has_nap": 0,
        "coordinates_ok": 0
    },
    "backlinks_readiness": {
        "status": "PASS",
        "guest_posts_ready": os.path.exists(os.path.join(base_dir, "backlinks", "READY_GUEST_POSTS.md")),
        "local_citations_ready": os.path.exists(os.path.join(base_dir, "backlinks", "LOCAL_CITATIONS_DIRECTORY.md")),
        "parasite_seo_ready": os.path.exists(os.path.join(base_dir, "backlinks", "PARASITE_SEO_AND_OUTREACH.md")),
        "press_release_ready": os.path.exists(os.path.join(base_dir, "backlinks", "PRESS_RELEASE_AR.md")),
        "instant_indexing_key": os.path.exists(os.path.join(base_dir, "3f8a92b104dc4a8e99b2e7fa811c7694.txt"))
    }
}

target_keywords = ["ونش إنقاذ", "أولاد حجازي", "01032194206", "600", "كارفور العبور"]

for fp in html_files:
    rel = os.path.relpath(fp, base_dir).replace("\\", "/")
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()

    # Viewport
    if 'name="viewport"' in c:
        report["technical_seo"]["mobile_viewport_ok"] += 1

    # Title
    m_title = re.search(r'<title>(.*?)</title>', c, re.I | re.S)
    if m_title:
        report["content_seo"]["titles"][rel] = m_title.group(1).strip()
    else:
        report["content_seo"]["titles"][rel] = None

    # Meta Description
    m_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', c, re.I)
    if m_desc:
        desc_text = m_desc.group(1).strip()
        report["content_seo"]["meta_descriptions"][rel] = len(desc_text)
        if len(desc_text) < 50:
            report["content_seo"]["short_descriptions"].append(rel)
    else:
        report["content_seo"]["meta_descriptions"][rel] = 0
        report["content_seo"]["short_descriptions"].append(rel)

    # Canonical
    m_canon = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', c, re.I)
    if not m_canon:
        report["technical_seo"]["missing_canonicals"].append(rel)

    # H1
    h1s = re.findall(r'<h1.*?>(.*?)</h1>', c, re.I | re.S)
    report["content_seo"]["h1_counts"][rel] = len(h1s)
    if len(h1s) == 0:
        report["content_seo"]["missing_h1"].append(rel)

    # Schemas
    schemas = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', c, re.I | re.S)
    for s_raw in schemas:
        try:
            s_obj = json.loads(s_raw.strip())
            report["technical_seo"]["valid_json_ld_schemas"] += 1
            # Check type
            s_str = json.dumps(s_obj)
            if "FAQPage" in s_str:
                report["aeo_geo"]["faq_schema_count"] += 1
            if "VideoObject" in s_str:
                report["aeo_geo"]["video_schema_count"] += 1
            if "LocalBusiness" in s_str or "EmergencyService" in s_str:
                report["aeo_geo"]["local_business_schema_count"] += 1
        except Exception as err:
            report["technical_seo"]["schema_errors"].append((rel, str(err)))

    # Images
    imgs = re.findall(r'<img\s+([^>]*?)>', c, re.I)
    for it in imgs:
        src_m = re.search(r'src=["\'](.*?)["\']', it, re.I)
        alt_m = re.search(r'alt=["\'](.*?)["\']', it, re.I)
        if not alt_m or not alt_m.group(1).strip():
            report["technical_seo"]["missing_alts"].append((rel, src_m.group(1) if src_m else "unknown"))
        if src_m:
            src = src_m.group(1)
            # Resolve relative
            if src.startswith("http"):
                continue
            base_img = os.path.dirname(fp)
            img_real_path = os.path.normpath(os.path.join(base_img, src.replace("/", os.sep)))
            if not os.path.exists(img_real_path):
                report["technical_seo"]["broken_images"].append((rel, src))

    # Local SEO signals
    if "maps.google.com" in c or "maps.app.goo.gl" in c:
        report["local_seo"]["has_maps_embed"] += 1
    if "01032194206" in c and "كارفور العبور" in c:
        report["local_seo"]["has_nap"] += 1
    if "30.1741147" in c and "31.4761952" in c:
        report["local_seo"]["coordinates_ok"] += 1

print("\n--- COUNCIL AUDIT SUMMARY ---")
print(f"Total Pages Checked: {len(html_files)}")
print(f"Mobile Viewport Configured: {report['technical_seo']['mobile_viewport_ok']}/{len(html_files)}")
print(f"Valid JSON-LD Schemas: {report['technical_seo']['valid_json_ld_schemas']}")
print(f"Schema Errors: {len(report['technical_seo']['schema_errors'])}")
print(f"Missing Canonicals: {len(report['technical_seo']['missing_canonicals'])}")
print(f"Broken Images: {len(report['technical_seo']['broken_images'])}")
print(f"Missing Image Alts: {len(report['technical_seo']['missing_alts'])}")
print(f"Pages with H1: {len(html_files) - len(report['content_seo']['missing_h1'])}/{len(html_files)}")
print(f"FAQ Schemas: {report['aeo_geo']['faq_schema_count']}")
print(f"Video Schemas: {report['aeo_geo']['video_schema_count']}")
print(f"LocalBusiness Schemas: {report['aeo_geo']['local_business_schema_count']}")
print(f"Pages with NAP (Phone + Address): {report['local_seo']['has_nap']}/{len(html_files)}")
print(f"Pages with GPS Coordinates: {report['local_seo']['coordinates_ok']}/{len(html_files)}")
print(f"llms.txt Present: {report['aeo_geo']['has_llms_txt']}")
print(f"llms-full.txt Present: {report['aeo_geo']['has_llms_full_txt']}")
print(f"Instant IndexNow Key Present: {report['backlinks_readiness']['instant_indexing_key']}")
print(f"Guest Posts Arsenal Ready: {report['backlinks_readiness']['guest_posts_ready']}")
print(f"Local Citations Directory Ready: {report['backlinks_readiness']['local_citations_ready']}")
print(f"Parasite SEO Ready: {report['backlinks_readiness']['parasite_seo_ready']}")
print(f"Press Release Ready: {report['backlinks_readiness']['press_release_ready']}")

# Write json report
with open(os.path.join(base_dir, "scripts", "audit_report.json"), "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print("Saved full report to scripts/audit_report.json")
