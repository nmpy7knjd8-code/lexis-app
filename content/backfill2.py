# Quote backfill round 2 (Oct 2026). BF2 entries override any earlier quote. Same Q tuple:
# (verbatim original, translation, work, citation, verify_file). SRC2 maps verify_file -> source label for the note.
# Files prefixed "fair_" are short fair-use quotations from copyrighted 20th-c. works, checked against the
# scholarly page named in SRC2 (URL recorded there); build.py labels them accordingly.
BF2={}
SRC2={
"sth1003.html":"Corpus Thomisticum (corpusthomisticum.org, Leonine text)","sth1077.html":"Corpus Thomisticum (corpusthomisticum.org, Leonine text)",
"qdv01.html":"Corpus Thomisticum (corpusthomisticum.org)","oee.html":"Corpus Thomisticum (corpusthomisticum.org)",
"gorg.xml":"Perseus Digital Library (PerseusDL canonical-greekLit)","lunyu12.txt":"Chinese Wikisource",
"gita.txt":"GRETIL (Göttingen Register of Electronic Texts in Indian Languages)","mmk.txt":"GRETIL","sveta.txt":"GRETIL","chand.txt":"GRETIL",
"sn56.pali":"SuttaCentral (Mahāsaṅgīti Pali text)","sn22_59.pali":"SuttaCentral (Mahāsaṅgīti Pali text)","sn38_1.pali":"SuttaCentral (Mahāsaṅgīti Pali text)",
"pi.html":"The Wittgenstein Project (German text of the 1953 edition)",
"sks_ba.txt":"Søren Kierkegaards Skrifter, via Det Kgl. Biblioteks tekstportal","sks_sd.txt":"Søren Kierkegaards Skrifter, via Det Kgl. Biblioteks tekstportal",
"rnotes.html":"French Wikisource (1823 edition)","bergson2.html":"French Wikisource (1908 edition)",
}
def q(id,*t): BF2[id]=t
q("t-quidditas","nomen essentiae a philosophis in nomen quiditatis mutatur","the philosophers change the name 'essence' into the name 'quiddity'.","De ente et essentia","ch. 1","oee.html")
q("t-actus-purus","Deus est purus actus, non habens aliquid de potentialitate","God is pure act, having nothing of potentiality.","Summa theologiae","I, q. 3, a. 2","sth1003.html")
q("t-esse","Aliquid enim est, sicut Deus, cuius essentia est ipsummet suum esse","For there is something, namely God, whose essence is his very act of being itself.","De ente et essentia","ch. 4","oee.html")
q("t-analogia-entis","Et iste modus communitatis medius est inter puram aequivocationem et simplicem univocationem.","And this mode of community lies midway between pure equivocation and simple univocity.","Summa theologiae","I, q. 13, a. 5","sth1003.html")
q("t-synderesis","synderesis dicitur instigare ad bonum, et murmurare de malo","synderesis is said to urge us toward good and to murmur against evil.","Summa theologiae","I, q. 79, a. 12","sth1077.html")
q("t-adaequatio","veritas est adaequatio rei et intellectus","truth is the correspondence of thing and intellect.","De veritate","q. 1, a. 1","qdv01.html")
q("t-nomos","ὡς τὰ πολλὰ δὲ ταῦτα ἐναντί' ἀλλήλοις ἐστίν, ἥ τε φύσις καὶ ὁ νόμος","For the most part these two are opposed to each other: nature and convention.","Plato, Gorgias (Callicles)","482e","gorg.xml")
q("t-li","克己復禮爲仁","To master oneself and return to ritual propriety is humaneness.","Analects (Confucius)","12.1","lunyu12.txt")
q("t-dharma","śreyān sva-dharmo viguṇaḥ para-dharmāt svanuṣṭhitāt","Better one's own dharma done imperfectly than another's dharma done well.","Bhagavad Gītā","3.35","gita.txt")
q("t-karma","karmaṇy evādhikāras te mā phaleṣu kadācana","Your right is to the action alone, never to its fruits.","Bhagavad Gītā","2.47","gita.txt")
q("t-sunyata","yaḥ pratītyasamutpādaḥ śūnyatāṃ tāṃ pracakṣmahe","Whatever is dependent arising, that we call emptiness.","Mūlamadhyamakakārikā","24.18","mmk.txt")
q("t-maya","māyāṃ tu prakṛtiṃ vidyān māyinaṃ tu maheśvaraṃ","Know that nature is māyā, and the great Lord the wielder of māyā.","Śvetāśvatara Upaniṣad (a text Śaṅkara relies on)","4.10","sveta.txt")
q("t-atman","tat satyam | sa ātmā | tat tvam asi śvetaketo","That is the real. That is the self. You are that, Śvetaketu.","Chāndogya Upaniṣad","6.8.7","chand.txt")
q("t-dukkha","jātipi dukkhā, jarāpi dukkhā, byādhipi dukkho, maraṇampi dukkhaṁ","Birth is suffering, old age is suffering, illness is suffering, death is suffering.","Saṁyutta Nikāya 56.11 (Pali), first sermon","SN 56.11","sn56.pali")
q("t-nirvana","Yo kho, āvuso, rāgakkhayo dosakkhayo mohakkhayo—idaṁ vuccati nibbānan","The ending of greed, the ending of hatred, the ending of delusion: this, friend, is called nibbāna (Sanskrit nirvāṇa).","Saṁyutta Nikāya 38.1 (Pali, Sāriputta)","SN 38.1","sn38_1.pali")
q("t-anatman","Rūpaṁ, bhikkhave, anattā.","Form, monks, is not-self (Pali anattā).","Saṁyutta Nikāya 22.59 (Pali), Anattalakkhaṇa Sutta","SN 22.59","sn22_59.pali")
q("t-sprachspiel","Ich werde auch das Ganze: der Sprache und der Tätigkeiten, mit denen sie verwoben ist, das »Sprachspiel« nennen.","I shall also call the whole, consisting of language and the activities into which it is woven, the 'language-game'.","Philosophische Untersuchungen","§ 7","pi.html")
q("t-familienahnlichkeit","Ich kann diese Ähnlichkeiten nicht besser charakterisieren als durch das Wort »Familienähnlichkeiten«","I can think of no better expression to characterise these similarities than 'family resemblances'.","Philosophische Untersuchungen","§ 67","pi.html")
q("t-lebensform","Und eine Sprache vorstellen heißt, sich eine Lebensform vorstellen.","And to imagine a language means to imagine a form of life.","Philosophische Untersuchungen","§ 19","pi.html")
q("t-privatsprache","Die Wörter dieser Sprache sollen sich auf das beziehen, wovon nur der Sprechende wissen kann; auf seine unmittelbaren, privaten, Empfindungen.","The words of this language are to refer to what only the speaker can know: to his immediate, private sensations.","Philosophische Untersuchungen","§ 243","pi.html")
q("t-angst","Saaledes er Angest den Frihedens Svimlen, der opkommer, idet Aanden vil sætte Synthesen","Thus anxiety is the dizziness of freedom, which arises when spirit wants to posit the synthesis.","Begrebet Angest","ch. I, § 5","sks_ba.txt")
q("t-springet","Imellem disse tvende Øieblikke ligger Springet, som ingen Videnskab har forklaret eller kan forklare.","Between these two moments lies the leap, which no science has explained or can explain.","Begrebet Angest","ch. I, § 5","sks_ba.txt")
q("t-oieblikket","Øieblikket er hiint Tvetydige, hvori Tiden og Evigheden berøre hinanden","The moment is that ambiguity in which time and eternity touch each other.","Begrebet Angest","ch. III","sks_ba.txt")
q("t-fortvivlelse","Fortvivlelse er en Sygdom i Aanden, i Selvet, og kan saaledes være et Tredobbelt","Despair is a sickness of the spirit, of the self, and so can take three forms.","Sygdommen til Døden","Part I, A.A","sks_sd.txt")
q("t-amour-propre","L'amour-propre n'est qu'un sentiment relatif, factice et né dans la société, qui porte chaque individu à faire plus cas de soi que de tout autre","Amour-propre is only a relative, artificial feeling born in society, which leads each individual to value himself above everyone else.","Discours sur l'origine de l'inégalité","Note XV","rnotes.html")
q("t-duree","La durée toute pure est la forme que prend la succession de nos états de conscience quand notre moi se laisse vivre","Pure duration is the form taken by the succession of our states of consciousness when our self lets itself live.","Essai sur les données immédiates de la conscience","ch. II","bergson2.html")
SRC2.update({"hfam_all.txt":"Projekt Gutenberg-DE","evolIII.txt":"French Wikisource (1908 edition)","wwv4.txt":"Projekt Gutenberg-DE",
"pasc_all.txt":"French Wikisource (Port-Royal text, 2nd Desprez ed.)",
"ia_grundlinienderph00hege.txt":"archive.org scan of the 1911 Lasson edition (OCR, fuzzy-matched)",
"ia_grundlagedergesa00fich.txt":"archive.org scan of the 1794 first edition (OCR, fuzzy-matched)",
"ia_psychologievome00kraugoog.txt":"archive.org scan of the 1874 first edition (OCR, fuzzy-matched)",
"ia_logischeuntersuc00hussuoft.txt":"archive.org scan of the 1901 first edition, vol. II (OCR, fuzzy-matched)",
"ia_erkenntnisundirr00machuoft.txt":"archive.org scan of the 1906 edition (OCR, fuzzy-matched)",
"ia_extraitsdelath00leibuoft.txt":"archive.org scan of the 1912 Hachette text (OCR, fuzzy-matched)",
"ia_bub_gb_qNBx4o0oisAC.txt":"archive.org scan of the 1742 edition (OCR, fuzzy-matched)"})
q("t-entfremdung","Die besitzende Klasse und die Klasse des Proletariats stellen dieselbe menschliche Selbstentfremdung dar.","The propertied class and the class of the proletariat present the same human self-alienation.","Die heilige Familie (with Engels)","ch. IV.4","hfam_all.txt")
q("t-elan-vital","l'élan vital n'est ni unité ni multiplicité pures","the vital impetus is neither pure unity nor pure multiplicity.","L'Évolution créatrice","ch. III","evolIII.txt")
q("t-mitleid","alle wahre und reine Liebe ist Mitleid, und jede Liebe, die nicht Mitleid ist, ist Selbstsucht.","all true and pure love is compassion, and every love that is not compassion is selfishness.","Die Welt als Wille und Vorstellung I","§ 66","wwv4.txt")
q("t-roseau-pensant","L'homme n'est qu'un roseau le plus faible de la nature ; mais c'est un roseau pensant.","Man is only a reed, the weakest in nature; but he is a thinking reed.","Pensées","Br. 347 (Port-Royal art. XXIII)","pasc_all.txt")
q("t-esprit-de-finesse","Il y a beaucoup de différence entre l'esprit de Géométrie et l'esprit de finesse.","There is a great difference between the mathematical mind and the intuitive mind.","Pensées","Br. 1 (Port-Royal art. XXXI)","pasc_all.txt")
q("t-sittlichkeit","Die Sittlichkeit ist die Idee der Freiheit, als das lebendige Gute","Ethical life is the Idea of freedom as the living good.","Grundlinien der Philosophie des Rechts","§ 142","ia_grundlinienderph00hege.txt")
q("t-tathandlung","Er soll diejenige Thathandlung ausdrücken, die … allem Bewußtseyn zum Grunde liegt","It is to express that Act which … underlies all consciousness.","Grundlage der gesammten Wissenschaftslehre","§ 1","ia_grundlagedergesa00fich.txt")
q("t-intentionalitat","Jedes psychische Phänomen ist durch das charakterisirt, was die Scholastiker des Mittelalters die intentionale (auch wohl mentale) Inexistenz eines Gegenstandes genannt haben","Every mental phenomenon is characterised by what the Scholastics of the Middle Ages called the intentional (or mental) inexistence of an object.","Brentano, Psychologie vom empirischen Standpunkte","Book II, ch. 1, § 5","ia_psychologievome00kraugoog.txt")
q("t-zu-den-sachen","Wir wollen auf die „Sachen selbst\" zurückgehen.","We want to go back to the 'things themselves'.","Logische Untersuchungen II","Introduction, § 2","ia_logischeuntersuc00hussuoft.txt")
q("t-gedankenexperiment","Außer dem physischen Experiment gibt es noch ein anderes, welches auf höherer intellektueller Stufe in ausgedehntem Maße geübt wird — das Gedankenexperiment.","Besides the physical experiment there is another, practised extensively at a higher intellectual level: the thought experiment.","Erkenntnis und Irrtum","'Über Gedankenexperimente', § 3","ia_erkenntnisundirr00machuoft.txt")
q("t-meilleur-monde","s'il n'y avait pas le meilleur (optimum) parmi tous les mondes possibles, Dieu n'en aurait produit aucun.","if there were not a best (optimum) among all possible worlds, God would not have produced any.","Essais de Théodicée","§ 8","ia_extraitsdelath00leibuoft.txt")
q("t-bellum","conditionem hominum extra societatem civilem (quam conditionem appellare liceat statum naturae) aliam non esse quam bellum omnium contra omnes","the condition of men outside civil society (which we may call the state of nature) is nothing other than a war of all against all.","De Cive","Preface","ia_bub_gb_qNBx4o0oisAC.txt")
