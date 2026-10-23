"""Check every card quote appears verbatim (whitespace/markup-normalised) in its downloaded source text."""
import re,sys,unicodedata as U,html,importlib
SRC="/tmp/norm/"
def clean(t):
    t=re.sub(r"\{\{\*\|[^}]*\}\}","",t); t=re.sub(r"(?m)^:","",t); t=re.sub(r"\{\{SperrSchrift\|([^}]*)\}\}",r"\1",t); t=t.replace("'''","").replace("''","")
    t=t.replace("_","");t=re.sub(r"\[\d+\]","",t); t=U.normalize("NFC",t).replace("\u2019","'").replace("\u1fbd","'")
    t=re.sub(r"\s+"," ",t)
    t=re.sub(r"(?<=[\u3000-\u9fff\uff00-\uffef])\s+|\s+(?=[\u3000-\u9fff\uff00-\uffef])","",t)
    return re.sub(r"(?<=[\u3000-\u303f\uff00-\uffef]):","",t)  # wiki indent markup after CJK punctuation
def check(cards):
    bad=[]
    for c in cards:
        q=c.get("q")
        if not q: continue
        hay=clean(open(SRC+q[4]+".n").read())
        if clean(q[0]) not in hay: bad.append(c["id"])
    return bad
if __name__=="__main__":
    m=importlib.import_module(sys.argv[1]); b=check(m.C); print(len(m.C),"cards;",sum(1 for c in m.C if c["q"]),"quotes; NOT FOUND:",b)
