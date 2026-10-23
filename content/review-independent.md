# LEXIS — independent review (2026-10-23)

Scope: all 206 cards (b1–b4). I checked each card's term, script, transliteration, gloss, meaning, thinker and era, quote wording, relevance and citation, translation, fair-use length, learn_more link and image licence. Quotes were checked against the normalized source texts in /tmp/norm. New quotes were checked against public editions or scholarly transcriptions; the source is named in each card's attribution_note.

## Fixes (content/review_fixes.py, hooked into build.py so rebuilds reproduce them)
| Card | Problem | Fix |
|---|---|---|
| t-ren | Same Analects 1.2 quote as t-xiao | Analects 12.22 樊遲問仁。子曰：「愛人。」 |
| t-harmonie | Same Monadology §7 'windows' quote as t-sans-fenetres | Monadologie §78 (pre-established harmony) |
| t-contrat-social | Quote didn't define the term well | I.1 « L'homme est né libre… » |
| t-substanz-subjekt | Quote was cut off mid-sentence | Full Preface clause |
| t-ressentiment | Quote didn't define the term | GM I §10, KSA 5, 270 |
| t-gott-ist-tot | Quote wasn't the defining passage | FW §125 'Der tolle Mensch' |
| t-deuxieme-sexe (l'Autre) | « On ne naît pas femme » is about becoming a woman, not the Other | Introduction « Il est le Sujet, il est l'Absolu : elle est l'Autre. » |
| t-visage (flagged) | Weak quote | Éthique et Infini p. 81 « Le visage est ce qu'on ne peut tuer… » |
| t-potentia-absoluta (flagged) | Weak quote | Ockham Quodl. VI q.1 a.1 (OTh IX 585) |
| t-haecceitas (flagged) | Quote is genuine (Ord. II d.3 p.1 q.6) but lacks the word | Context now explains 'ista entitas'; the word itself is in QQ Metaph. VII q.13 and the Reportatio |
| t-ataraxia | Person given as Diogenes Laërtius (a doxographer, not the thinker) | 'Epicurus · the Sceptics' |
| t-elenchus | Repeated the 'knew that he knew nothing' cliché | Now follows Apology 21d |
| t-apeiron | Overclaimed 'first abstract concept' | 'often called the first abstract principle in Greek thought' |
| t-springet | Context is about faith but the quote is from Concept of Anxiety (sin's leap) | Context sentence added |
| cards/index.html | og:image pointed to greek-app/og.png | Removed; twitter:card set to summary |

## Flagged sources kept, verified
- lebenswelt (Krisis §9h), dike (Anaximander B1 via Simplicius), existence-precede (Sartre 1946), il-y-a (De l'existence à l'existant p. 38): all genuine and relevant.

## Weaker fits noted, not changed
engagement (the quote lacks the word), weltgeist, epoche, elenchus, objet-a and an-und-für-sich are on topic but not defining. physis pairs a Heraclitus image with an Aristotle quote.

## 'Greek font not loaded': not a real problem
In Chromium all Gentium Book Plus Greek and Greek-Extended faces load (U+0370 and U+1F00 ranges), and CDP reports Greek terms rendering in GentiumBookPlus. The old shot_mobile check used document.fonts.check() and returned a false negative; it now loads the faces and checks them.

## Validation
- build b1–b4: 206/206 quotes, none dropped. `tools_validate.py --strict`: 206/206 valid.
- Overflow at 390×844, 430×932, 375×667 and 390×664: no vertical or horizontal overflow. Long contexts clamp, with a 'more' button, at the two short heights.

**Result: PASS** (after fixes).
