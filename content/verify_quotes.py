"""Check every card quote appears verbatim (whitespace/markup-normalised) in its downloaded source text."""
import re,sys,unicodedata as U,html,importlib
SRC="/tmp/norm/"
def clean(t):
    t=re.sub(r"\{\{\*\|[^}]*\}\}","",t); t=re.sub(r"(?m)^:","",t); t=re.sub(r"\{\{SperrSchrift\|([^}]*)\}\}",r"\1",t); t=t.replace("'''","").replace("''","")
    t=t.replace("_","");t=re.sub(r"\[\d+\]","",t); t=U.normalize("NFC",t).replace("\u2019","'").replace("\u1fbd","'")
    t=re.sub(r"\s+"," ",t)
    t=re.sub(r"(?<=[\u3000-\u9fff\uff00-\uffef])\s+|\s+(?=[\u3000-\u9fff\uff00-\uffef])","",t)
    return re.sub(r"(?<=[\u3000-\u303f\uff00-\uffef]):","",t)  # wiki indent markup after CJK punctuation
def _fold(t):
    t=U.normalize("NFKD",clean(t).lower()); t="".join(c for c in t if not U.combining(c))
    t=t.replace("ſ","s").replace("f","s").replace("rn","m").replace("æ","ae")  # OCR / long-s folding
    return re.sub(r"[^a-z0-9]","",t)
def fuzzy_in(q,hay,thr=0.9):
    """For archive.org OCR scans (files named ia_*): accept when a window of the folded scan text matches the folded quote at >= thr."""
    import difflib
    n,h=_fold(q),_fold(hay)
    if n in h: return True
    k=12; best=0
    for a in range(0,len(n)-k+1,max(1,k//2)):
        i=h.find(n[a:a+k])
        while i!=-1:
            st=max(0,i-a); w=h[st:st+len(n)]
            best=max(best,difflib.SequenceMatcher(None,n,w).ratio())
            if best>=thr: return True
            i=h.find(n[a:a+k],i+1)
    return False
def check(cards):
    bad=[]
    for c in cards:
        q=c.get("q")
        if not q: continue
        hay=clean(open(SRC+q[4]+".n").read())
        parts=q[0].split(" … ")  # an elided quote: every part must be found, in order
        if "ia_" in q[4]: ok=all(_fold(p) and fuzzy_in(p,hay) for p in parts)  # OCR scans (ia_*, fair_ia_*); a part that folds to nothing (non-Latin script) fails
        else:
            pos=0; ok=True
            for p in parts:
                i=hay.find(clean(p),pos); ok=ok and i>=0; pos=max(i,0)
        if not ok: bad.append(c["id"])
    return bad
if __name__=="__main__":
    m=importlib.import_module(sys.argv[1]); b=check(m.C); print(len(m.C),"cards;",sum(1 for c in m.C if c["q"]),"quotes; NOT FOUND:",b)
