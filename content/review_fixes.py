"""Independent-review corrections, applied after build.py assembles each batch (idempotent).
Each quote here was checked against the source named in its note (see content/review-independent.md)."""
def Q(text,tr,work,cit,note): return dict(quote=dict(text=text,translation=tr),source=dict(work=work,citation=cit),attribution_confidence="verified",attribution_note=note)
FIX={
 "t-ren":Q("樊遲問仁。子曰：「愛人。」","Fan Chi asked about humaneness. The Master said: 'Love people.'","Analects","12.22","Quote checked verbatim against Chinese Wikisource (Lunyu 12)"),
 "t-harmonie":Q("L'âme suit ses propres loix, et le corps aussi les siennes; et ils se rencontrent en vertu de l'harmonie préétablie entre toutes les substances","The soul follows its own laws and the body its own; and they agree by virtue of the harmony pre-established among all substances.","Monadologie","§ 78","Quote checked verbatim against Project Gutenberg ebook 17641 (1909 ed.)"),
 "t-contrat-social":Q("L'homme est né libre, & par-tout il est dans les fers.","Man is born free, and everywhere he is in chains.","Du contrat social","I.1","Quote checked verbatim against French Wikisource (1762 edition)"),
 "t-substanz-subjekt":Q("das Wahre nicht als Substanz, sondern ebensosehr als Subjekt aufzufassen und auszudrücken","to grasp and express the true not as substance, but equally as subject.","Phenomenology of Spirit","Preface","Quote checked verbatim against Projekt Gutenberg-DE"),
 "t-ressentiment":Q("Der Sklavenaufstand in der Moral beginnt damit, dass das Ressentiment selbst schöpferisch wird und Werthe gebiert","The slave revolt in morals begins when ressentiment itself becomes creative and gives birth to values.","Zur Genealogie der Moral","I § 10 (KSA 5, 270)","Quote checked verbatim against the KSA text as quoted in Vogt, 'Starke Gefühle' (zfkm.org) and the Wuppertal seminar text"),
 "t-gott-ist-tot":Q("Gott ist todt! Gott bleibt todt! Und wir haben ihn getödtet!","God is dead! God remains dead! And we have killed him!","Die fröhliche Wissenschaft","§ 125, 'Der tolle Mensch'","Quote checked verbatim against the 1882 text (The Nietzsche Channel) and Zeno.org"),
 "t-deuxieme-sexe":Q("Il est le Sujet, il est l'Absolu : elle est l'Autre.","He is the Subject, he is the Absolute: she is the Other.","Le Deuxième Sexe I","Introduction","Short quotation (fair use) from a copyrighted work; wording checked against the archive.org scan of vol. I"),
 "t-visage":Q("Le visage est ce qu'on ne peut tuer, ou du moins dont le sens consiste à dire : « tu ne tueras point ».","The face is what one cannot kill, or at least it is that whose meaning consists in saying: 'thou shalt not kill'.","Éthique et Infini","Livre de poche 1982, p. 81","Short quotation (fair use) from a copyrighted work; wording checked against two independent French transcriptions (coin-philo.net)"),
 "t-potentia-absoluta":Q("quaedam potest Deus facere de potentia ordinata et aliqua de potentia absoluta","God can do some things by his ordained power and others by his absolute power.","Quodlibeta","VI, q. 1, a. 1 (OTh IX, 585)","Quote checked verbatim against the Opera Theologica text as quoted in two scholarly articles (philarchive AMEGDO; Revista Ambiente 2017)"),
}
CTX={
 "t-elenchus":("Socrates claimed his only wisdom was knowing that he did not know.","Socrates said his only wisdom was that he did not think he knew what he did not know."),
 "t-apeiron":("It is the first abstract concept in Western philosophy.","It is often called the first abstract principle in Greek thought."),
 "t-haecceitas":("The term has been revived","In the Ordinatio he calls it simply 'this entity'; the word haecceitas itself appears in his Questions on the Metaphysics and the Reportatio. The term has been revived"),
 "t-springet":("Abraham's readiness to sacrifice Isaac, in Fear and Trembling, is his great example.","Abraham's readiness to sacrifice Isaac, in Fear and Trembling, is his great example. In The Concept of Anxiety, quoted here, sin too enters by a qualitative leap that no science can explain."),
}
PERSON={"t-ataraxia":"Epicurus · the Sceptics"}
def apply(out):
    for d in out:
        i=d["id"]
        if i in FIX:
            f=dict(FIX[i]); f["source"]={**d.get("source",{}),**f["source"]}; d.update(f)
        if i in CTX and CTX[i][1] not in d["context"]: d["context"]=d["context"].replace(*CTX[i])
        if i in PERSON: d["person"]=PERSON[i]
    return out
