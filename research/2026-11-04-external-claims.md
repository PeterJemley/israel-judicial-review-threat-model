# External claims from the round-1 review: verification pass, 31 October and 4 November 2026

**Question.** The round-1 review (research/review-2026-10-28-round1.md, "External claims to verify") lists eleven claims the project's own files cannot settle. This pass checks them. Its method is the layered order of the israel-law-dossier skill: English texts of decisions, then scholarship, institutes, the Israeli English-language press, and machine translation for triage only.

**History of the pass.**
- On 31 October and the morning of 4 November the session's network policy blocked every source host, and only Scite and web-search summaries were available.
- The author allowed the hosts on 4 November. After that, Versa, the Jerusalem Post, Open Knesset, Hebrew Wikisource and Crossref were read directly.
- Four hosts were still unusable:
  - `supreme.court.gov.il` and `web.archive.org` did not answer;
  - `www.timesofisrael.com` refuses automated requests (403);
  - `is.muni.cz` serves the Meatrael translation behind an anti-bot check, which was not circumvented.
- Three hosts are not on the allowed list: `production.oknesset.org` (Open Knesset's vote data), `www.adalah.org` (an English translation of the Interpretation Law) and `academic.oup.com`.

**Short answer.**
- **Settled:**
  - item 1 (Resler);
  - item 5 (Meatrael), from a translation the author supplied;
  - item 4 (Peretz);
  - item 7 (Bar-On);
  - item 8 (the article's dates);
  - item 11 (reference metadata);
  - the Shin Bet part of item 9, which reverses part of change log (aq) and (at).
- **Item 10** is settled on abstracts for ten of eleven works.
- **Not settled:** items 2, 3 and 6.
- **Applied to the note:** change log (av), (aw) and (ax).

**Tags used.**
- `[attested: ...]`: an English text read, named.
- `[abstract: Scite]`: an abstract only.
- `[MT-triage]`: a Hebrew text read only to locate a provision. Never a characterization.
- `[search-lead]`: a web-search summary, not read.
- `[conjectural]`: this project's inference, with what would refute it.

## Items, in the review's order

**1. What Resler (HCJ 60/77) held, and which law it concerned.** Settled.
- Landau P., in Agudat Derekh Eretz v. Broadcasting Authority (HCJ 246/81, 1981), restates the holding. `[attested: Versa translation, p. 9]` Resler concluded that the 1969 Confirmation Law "indeed ratified 'the election Laws' mentioned therein by virtue of the absolute majority with which it was passed consonantly with the concluding portion of section 4 and section 46 of Basic Law: The Knesset". He adds: "But it says nothing with respect to the question whether the validity of the election Laws or any of their provisions ... was in any event consistent with the equality principle in section 4".
- This matches the project's reading in change log (i) and (n). The draft email on Resler in the earlier version of this file is withdrawn.

**2. The faction breakdown of the 23 March 2023 Incapacity final vote.** Not settled.
- The amendment passed "with 61 MKs voting in favor and 47 against". Absent were Mansour Abbas (Ra'am) and the Likud members David Amsalem and David Bitan, the two Likud members "in protest at the removal of a bill proposal by Amsalem from the plenum agenda". `[attested: Eliav Breuer and Jerusalem Post staff, 23 March 2023]` No member-by-member record was found.
- If the coalition held 64 seats and three coalition members were absent, as a further report has it (Shas's Moshe Abutbul), 61 is the coalition's full remaining strength. This is consistent with a coalition-only vote but does not show it. `[conjectural; refuted by any opposition member among the 61]`
- To settle it: the Knesset's own vote record. Two routes were tried on 4 November:
  - Open Knesset's vote tables (`production.oknesset.org`) and the Knesset's own open-data service (`knesset.gov.il/Odata/Votes.svc`, which Open Knesset mirrors) both answer, but both end on 13 July 2021.
  - `main.knesset.gov.il` and `fs.knesset.gov.il` answer automated requests with a bot-check page (code 247), which was not circumvented.
  - The vote page for the plenum sitting of 22–23 March 2023, opened in a browser and saved, would settle it. Issues 19 and 6.

**3. Whether a Knesset statute with no commencement clause takes effect on publication.** Not settled.
- `[MT-triage]` The Interpretation Law, 5741-1981, has no general commencement default. Its s. 21 sets only the hour (00:01 of the commencement day).
- `[MT-triage]` The Law and Administration Ordinance, 5708-1948, s. 10(a), gives a publication-day default. But it speaks of an "ordinance", and s. 10(c) extends it to regulations. Whether it reaches Knesset statutes is not settled by the text, which is where issue 1 already stood.
- Both texts are from Hebrew Wikisource. To settle it: an English authority (a treatise, or a ruling applying s. 10(a) to a statute) or a scholar.

**4. Rafi Peretz's faction on 24 August 2020.** Settled.
- Open Knesset, from the Knesset's parliamentary-information interface, records Peretz in the 23rd Knesset in Yamina from 16 March to 14 July 2020 and in the Jewish Home faction from 14 July 2020 to 6 April 2021. It also records him as a minister from 17 May 2020 to 6 April 2021. `[attested: Open Knesset, member page 30716]`
- On 24 August 2020 he therefore sat in the coalition, as a minister. A vote by him for the budget-deadline amendment is not an opposition vote, and the 2020 row's `coalition_only` Yes stands.

**5. Whether Meatrael (HCJ 4676/94) narrowed the 1994 amendment or applied it literally.** Settled: narrowed. `[attested: English translation, translator not named, supplied by the author from a Masaryk University course copy]`
- Barak P., for a unanimous bench of nine; delivered 25 November 1996. The heading cites 50(5) P.D. 16 (1997).
- Para. 18: a deviating Act "gains constitutional protection within Basic-Law: Freedom of Occupation. For that reason alone, it does not acquire constitutional protection within Basic-Law: Human Dignity and Liberty too. Therefore, situations can arise where a deviating Act ... will be found not valid with regard to Basic-Law: Human Dignity and Liberty".
- Paras. 21–22: the override's protection extends to rights in Human Dignity and Liberty only under three cumulative conditions. The infringement must be a natural consequence of the infringement on occupation, secondary to it, and not serious of itself.
- Para. 15: the override cannot be used "to give force to an Act that negates or totally abolishes freedom of occupation as a constitutional right".
- Paras. 23–24: the conditions were met, and the petition was rejected.
- This is a narrowing interpretation of the 1994 amendment. The Adverse coding of change log (ag) stands on the text, and its alternative reading is not supported. Applied in change log (aw).
- Earlier, Versa's later translations cited the case only for its outcome: Horev (the petition "was rejected and its constitutionality was upheld"); HCJ 5658/23, para. 205.

**6. The faction breakdown of the 17 March 1992 Human Dignity and Liberty vote.** Not settled.
- Sources agree on 32 for, 21 against, 1 abstaining. `[search-lead]`
- No party-by-party record was reached. The Knesset's vote data, in its own service and on Open Knesset, begins in October 2003, so Divrei HaKnesset for that sitting is needed (issue 6).

**7. Bar-On (HCJ 4908/10): whether it applied the abuse constraint or only announced it.** Settled: announced, not applied. `[attested: Versa, Bar-On v. Knesset]`
- Decided 7 April 2011 by seven justices (Beinisch P., Rivlin D.P., Grunis, Naor, Arbel, Rubinstein and Vogelman JJ.). The petition was denied.
- The Court was "not convinced that the present case justifies unprecedented intervention in the legislation of the Knesset in its function as a constituent authority".
- It said that "In certain circumstances, which cannot be determined in advance, it is possible that the enactment of a basic law as a temporary provision may amount to 'misuse' of the title 'basic law'". It added, in the abstract's translation, that "the Knesset would do better to refrain from using temporary provisions to amend constitutional instructions in the future".
- The note's "2011 warning in Bar-On" is accurate.

**8. The article's acceptance or cut-off date.** Settled as far as the record goes. `[attested: Crossref]`
- Issued 1 April 2026, I·CON 24(2) 681–708; published online 21 May 2026. No acceptance date is in the Crossref record.
- The reply by Issi Rosen-Zvi and Meir H. Yarom, DOI 10.1093/icon/moag054, is in the same issue at pp. 709–722, published online 1 June 2026. It is open access under CC BY. Its abstract argues two things `[abstract: Scite]`:
  - that Medina defines Israel's constitutional identity ambiguously, "privileging liberal sources while sidelining nationalist ones";
  - that the sliding scale's procedural criteria are "empirically and normatively indeterminate".
- Medina's rejoinder is on the ICONnect blog, 27 June 2026. `[search-lead]`
- The reply was read in full from a copy the author supplied (OUP refuses automated requests). `[attested: Rosen-Zvi & Yarom, 2026]` Applied in change log (ax). Points used:
  - the selectivity argument (pp. 717–720) and the indeterminacy of the procedural criteria (pp. 721–722);
  - the Incapacity amendment as stipulating "that only medical reasons can ground the prime minister's incapacity" (p. 710 n. 4);
  - the Court has "overturned many" disqualifications of Arab parties, "not all" (p. 717 n. 30);
  - Hasson "mitigated some of the most problematic consequences" of the Nation-State law (p. 720 n. 46).

**9. The M1 details in finding 28.**
- **The Shin Bet dismissal: settled.** `[attested: Jerusalem Post staff, 21 March 2025]` The report says "The High Court of Justice on Friday froze the government's Thursday decision to fire Shin Bet (Israel Security Agency) chief Ronen Bar until the hearing on the petition against the move", after "the cabinet's unanimous Thursday vote".
  - The cabinet voted on 20 March 2025, and the Court froze the dismissal on 21 March.
  - The 21 May judgment came after the government had rescinded the dismissal, so its lack of an operative order is consistent with the earlier freeze.
  - Change log (aq) was wrong to drop "froze" for the Shin Bet case, and (at) to drop the March date. Both are restored in change log (av).
- **Not re-checked:** the attorney general's freeze (from the Times of Israel, which refuses automated requests), the absence of interim orders in 2026, and the deferred-effect claims.

**10. The prior-art characterizations.**
- **Supported by abstracts** `[abstract: Scite]`:
  - Cox (2008): correlation among components, nonadditivity, adaptive antagonists.
  - Aven & Guikema (2015): adaptation by adversaries as essential to the concept.
  - Grillo, Luo & Nalepa (2024); Bermeo (2016); Riedl, McCoy & Roberts (2024); Landau-Wells (2024); Navot (2023); Hostovsky Brandes & Roznai (2024); Medina & Bloch (2023).
- **Abstract silent on the note's point; the full text is needed:**
  - Roznai & Cohen (2023), on "institutional vulnerability".
  - Roznai, Dixon & Landau (2023), on "effect as prima facie evidence of intent" and "proto-abusive change".
- **Not checked:** Singer (1958). Scite has no abstract and no indexed full text.

**11. Reference metadata.** Settled. `[attested: Crossref]`
- Hostovsky Brandes & Roznai, DOI 10.1017/asjcl.2025.7: issue dated December 2024, AJCL 19(3) 535–555; published online 25 April 2025.
- Riedl, McCoy & Roberts, DOI 10.1177/00027162251319909: issue dated March 2024, ANNALS 712(1) 8–31; published online 21 March 2025.
- Both were published online after the issue they are assigned to, which explains the 2025 in their DOIs. The note's 2024 follows the issue date and stands.
- The other eleven references match the note. None has a retraction, correction or concern notice in Scite.

## Gaps

1. Item 2 needs `production.oknesset.org` allowed, or the Knesset's own site.
2. Item 3 needs an English authority on whether s. 10(a) of the Law and Administration Ordinance governs Knesset statutes. Allowing `www.adalah.org` would give an English Interpretation Law, but that Law has no default, so a treatise or a ruling is the better route.
3. Item 5 is settled from the translation the author supplied (change log (aw)).
4. Item 6 needs Divrei HaKnesset for 17 March 1992.
5. Rosen-Zvi and Yarom has been read in full (change log (ax)). Medina's rejoinder on the ICONnect blog is not yet read.
6. The person to ask about item 3 is Suzie Navot, whose English treatise on the constitution of Israel is the likeliest place for the commencement rule. If she does not reply, Yaniv Roznai.

## Email draft

Subject: One question on commencement — Knesset statutes

Dear Professor [name],

I'm a graduate law student at Vanderbilt and a fellow at Fordham's Center for Jewish Studies, reading on Israeli constitutional amendment without enough Hebrew to work from the sources. Your *The Constitution of Israel* is the closest English treatment I've found.

One question: when a Knesset statute or Basic Law has no commencement clause, does it take effect on the day of publication in Reshumot under section 10(a) of the Law and Administration Ordinance, 1948, or by some other rule? A one-line answer — even "yes, s. 10(a), and the courts apply it to statutes" — would settle it for me; if there is a case on the point, its number is all I need.

With thanks,
Peter

## Sources

**Layer 1, English texts of decisions (Versa):**
- Agudat Derekh Eretz v. Broadcasting Authority: https://versa.cardozo.yu.edu/sites/default/files/upload/opinions/Agudat%20Derekh%20Eretz%20v.%20Broadcasting%20Authority.pdf
- Bar-On v. Knesset: https://versa.cardozo.yu.edu/opinions/bar-v-knesset
- Horev v. Minister of Transportation: https://versa.cardozo.yu.edu/sites/default/files/upload/opinions/Horev%20v.%20Minister%20of%20Transportation_0.pdf
- Movement for Quality Government v. The Knesset (HCJ 5658/23): https://versa.cardozo.yu.edu/sites/default/files/upload/opinions/Movement%20for%20Quality%20Government%20v.%20The%20Knesset.pdf

**Layer 4, the Israeli English-language press:**
- Item 9: https://www.jpost.com/breaking-news/article-847040
- Item 2: https://www.jpost.com/israel-news/politics-and-diplomacy/article-735156

**Knesset data:** https://oknesset.org/members/30716.html

**Hebrew statutes, for triage only:**
- Interpretation Law, 1981: https://he.wikisource.org/wiki/חוק_הפרשנות
- Law and Administration Ordinance, 1948: https://he.wikisource.org/wiki/פקודת_סדרי_השלטון_והמשפט

**Bibliographic records:** Crossref (api.crossref.org) for the DOIs above, and Scite for abstracts and editorial notices.

**Search leads not read:** https://israeled.org/timeline/tenth-basic-law-of-israel-human-dignity-and-liberty ; https://www.iconnectblog.com/democratic-legitimacy-and-constitutional-identity-a-rejoinder/
