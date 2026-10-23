"""Build content/<batch>-cards.json from <batch>_cards.py; quotes that fail verification are dropped."""
import json,sys,importlib,os
from verify_quotes import check
b=sys.argv[1]; m=importlib.import_module(b+"_cards"); I=json.load(open("img_info.json"))
bad=set(check(m.C)); out=[]
LANG={"grc":"Ancient Greek","la":"Latin","de":"German","fr":"French","da":"Danish","zh":"Chinese","sa":"Sanskrit","ar":"Arabic"}
for c in m.C:
    i=I[c["who"]]; lic=i["lic"].replace("Public domain","Public domain")
    credit=(i["artist"].replace("Unknown authorUnknown author","Unknown author").replace("Unknown artistUnknown artist","Unknown artist") or ("Eric Gaba" if "Epicurus" in i["file"] else "Unknown author"))
    q=c["q"] if c["q"] and c["id"] not in bad else None
    d=dict(id=c["id"],type="term",era=c["era"],unit=c["unit"],greek=c["term"],lang=c["lang"],language=LANG[c["lang"]],translit=c["translit"],
      translation=c["gloss"],context=c["meaning"],person=c["person"],
      source=dict(work=q[2],citation=q[3],date="") if q else dict(work="",citation="",date=""),
      attribution_confidence="verified" if q else "",
      attribution_note=("Quote checked verbatim against "+{"g6343.txt":"Project Gutenberg ebook 6343 (modernised spelling)","zara.txt":"Project Gutenberg ebook 7205","g7204.txt":"Project Gutenberg ebook 7204","g7203.txt":"Project Gutenberg ebook 7203","g7202.txt":"Project Gutenberg ebook 7202","aufkl.txt":"German Wikisource","g17641.txt":"Project Gutenberg ebook 17641 (1909 ed.)","g13846.txt":"Project Gutenberg ebook 13846","spin3.html":"The Latin Library","spin4.html":"The Latin Library"}.get(q[4],"Perseus Digital Library (PerseusDL canonical-greekLit)")) if q else "",
      quote=dict(text=q[0],translation=q[1]) if q else None,
      respelling=c["respelling"],
      image=dict(src="img/p/"+c["who"].lower().replace(" ","-").replace("é","e")+".webp",alt="Portrait of "+c["who"],kind="painting",aspect="3:4",transparent=False,
        license=lic,credit=f"{credit} · {lic} · via Wikimedia Commons",source_url=i["page"],license_url=i["licurl"],modified="cropped to 3:4, resized"),
      learn_more=dict(label=c["lm"][0],url=c["lm"][1]))
    out.append(d)
json.dump(out,open(b+"-cards.json","w"),ensure_ascii=False,indent=1)
print(b,len(out),"cards,",sum(1 for d in out if d["quote"]),"quotes, dropped:",sorted(bad))
