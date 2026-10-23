"""Build content/<batch>-cards.json from <batch>_cards.py; quotes that fail verification are dropped."""
import json,sys,importlib,os
from verify_quotes import check
from backfill import BF
from backfill2 import BF2,SRC2
b=sys.argv[1]; m=importlib.import_module(b+"_cards")
for c in m.C:
    if not c["q"] and c["id"] in BF: c["q"]=BF[c["id"]]
    if c["id"] in BF2: c["q"]=BF2[c["id"]]
I=json.load(open("img_info.json"))
bad=set(check(m.C)); out=[]
def note(q):
    # allowlisted verification paths for round-2 quotes: fair_* = short fair-use quotation from a copyrighted work,
    # checked against the scholarly source/URL in SRC2; ia_* = fuzzy OCR match against an archive.org scan
    f=q[4]
    if f.startswith("fair_"): return "Short quotation (fair use) from a copyrighted work; wording checked against "+SRC2[f]
    if "ia_" in f: return "Quote checked against "+SRC2[f]
    return "Quote checked verbatim against "+SRC2[f]
LANG={"grc":"Ancient Greek","la":"Latin","de":"German","fr":"French","da":"Danish","zh":"Chinese","sa":"Sanskrit","ar":"Arabic"}
for c in m.C:
    i=I[c["who"]]; lic=i["lic"].replace("Public domain","Public domain")
    credit=(i["artist"].replace("Unknown authorUnknown author","Unknown author").replace("Unknown artistUnknown artist","Unknown artist") or ("Eric Gaba" if "Epicurus" in i["file"] else "Unknown author"))
    q=c["q"] if c["q"] and c["id"] not in bad else None
    d=dict(id=c["id"],type="term",era=c["era"],unit=c["unit"],greek=c["term"],lang=c["lang"],language=LANG[c["lang"]],translit=c["translit"],
      translation=c["gloss"],context=c["meaning"],person=c["person"],
      source=dict(work=q[2],citation=q[3],date="") if q else dict(work="",citation="",date=""),
      attribution_confidence="verified" if q else "",
      attribution_note=(note(q) if q and q[4] in SRC2 else "Quote checked verbatim against "+{"g6343.txt":"Project Gutenberg ebook 6343 (modernised spelling)","zara.txt":"Project Gutenberg ebook 7205","g7204.txt":"Project Gutenberg ebook 7204","g7203.txt":"Project Gutenberg ebook 7203","g7202.txt":"Project Gutenberg ebook 7202","aufkl.txt":"German Wikisource","g17641.txt":"Project Gutenberg ebook 17641 (1909 ed.)","g13846.txt":"Project Gutenberg ebook 13846","spin3.html":"The Latin Library","spin4.html":"The Latin Library","proslog.html":"The Latin Library","lunyu1.txt":"Chinese Wikisource","ddjw.txt":"Chinese Wikisource","ddj.txt":"Chinese Wikisource","spin.html":"The Latin Library","spin1.html":"The Latin Library","spin2.html":"The Latin Library","spin5.html":"The Latin Library","g6342.txt":"Project Gutenberg ebook 6342","g39441.txt":"Project Gutenberg ebook 39441","conf1.html":"The Latin Library","tlp.txt":"Project Gutenberg ebook 5740 (German text)","g6729.txt":"Project Gutenberg ebook 6729","hph.html":"Projekt Gutenberg-DE","hgesch.html":"Projekt Gutenberg-DE","wwv.html":"Projekt Gutenberg-DE","g7206.txt":"Project Gutenberg ebook 7206","ee1.html":"Danish Wikisource","contrat.html":"French Wikisource (1762 edition)","feuer.txt":"German Wikisource","manif.html":"German Wikisource (1848 edition)","g13846.txt":"Project Gutenberg ebook 13846","g39441.txt":"Project Gutenberg ebook 39441","ee21.html":"Danish Wikisource","g4723.txt":"Project Gutenberg ebook 4723","g10615.txt":"Project Gutenberg ebook 10615","g3207.txt":"Project Gutenberg ebook 3207","kk_aa04_421.txt":"korpora.org (Akademie-Ausgabe)","kk_aa04_433.txt":"korpora.org (Akademie-Ausgabe)","kk_aa05_179.txt":"korpora.org (Akademie-Ausgabe)","kk_aa05_221.txt":"korpora.org (Akademie-Ausgabe)","kk_aa05_248.txt":"korpora.org (Akademie-Ausgabe)","desmed2.html":"The Latin Library (1642 ed.)","civ14.html":"The Latin Library"}.get(q[4],"Perseus Digital Library (PerseusDL canonical-greekLit)")) if q else "",
      quote=dict(text=q[0],translation=q[1]) if q else None,
      respelling=c["respelling"],
      image=dict(src="img/p/"+c["who"].lower().replace(" ","-").replace("é","e")+".webp",alt=("Krishna and Arjuna on the chariot (Indian painting, 18th–19th c.)" if c["who"]=="Krishna and Arjuna" else "Portrait of "+c["who"]),kind="painting",aspect="3:4",transparent=False,
        license=lic,credit=f"{credit} · {lic} · via Wikimedia Commons",source_url=i["page"],license_url=i["licurl"],modified="cropped to 3:4, resized"),
      learn_more=dict(label=c["lm"][0],url=c["lm"][1]))
    out.append(d)
json.dump(out,open(b+"-cards.json","w"),ensure_ascii=False,indent=1)
print(b,len(out),"cards,",sum(1 for d in out if d["quote"]),"quotes, dropped:",sorted(bad))
