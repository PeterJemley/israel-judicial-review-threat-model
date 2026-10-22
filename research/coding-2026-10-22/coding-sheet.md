# Coding sheet, 2026-10-22

You are one of two independent coders. Code every enactment below on the variables defined in the protocol section, from the permitted sources only. Record, for every cell, the value, the source (URL or document) and a short quotation or data point that supports it. Where no permitted source settles a cell, leave it blank and say what you looked for. Do not infer a value from what seems likely.

## Rules of the sheet

- Permitted sources: the enactment's text as published (Hebrew Wikisource or Nevo law pages are acceptable copies of the gazette text); Knesset voting data (the extracts below, drawn from the Knesset's vote tables as mirrored by Open Knesset, or press reports of the recorded tally where the extracts do not cover the enactment); records of the government's composition on the day of the vote (the Knesset's own records, or an encyclopedia article on that government where the Knesset site is unreachable); dates of the first and final readings (Knesset records, or press reports of the readings); the bill's explanatory notes where reachable.
- Forbidden sources: any court judgment, any translation or summary of a judgment, any article or page whose subject is litigation about the enactment, any commentary that discusses how a court treated it, and any file in the repository this sheet comes from. If a page you open turns out to be about a court case, close it and do not use anything from it. Say in your notes if that happened.
- Do not use your own recollection of how any of these enactments fared in court. Code the enactment as a text and a legislative event only.
- Identify enactments by the titles below. Do not add case names.

## Variables

- `named_beneficiary`: Yes if the enactment addresses a specific interest of the sitting government or an identified officeholder, from its text and explanatory notes; otherwise No. Name the beneficiary if Yes.
- `immediate_effect`: Deferred if the text fixes effect after the next general election, or more than twelve months after publication; otherwise Yes, whether the text states effect on publication, on an earlier date (retroactive effect included), or within twelve months, or states no commencement clause at all. Record the basis: "stated", "retroactive", "within twelve months", or "by absence of a clause". Deferred takes precedence where both could apply.
- `coalition_only`: Yes if no member of an opposition faction voted for the enactment at its final reading; No if at least one did; blank if the vote record is unavailable. Record the tally and any cross-party votes by name and faction.
- `expedited`: Yes if the final vote came within thirty days of the first reading, or if a special procedure shortened the committee stage; No otherwise. Record the dates of first reading and final vote and the number of days.
- `scope`: Yes if the enactment removes a check on the government or a protected right, or renders it practically inoperative, and in either case provides no alternative mechanism; No otherwise. A one-time exemption from a rule is No. Say which check or right, and whether an alternative mechanism exists, in your own words from the text.
- `temporary_provision`: Yes if the enactment was passed as a temporary provision or applies to a single instance; No otherwise.
- `targets_judiciary`: Yes if the enactment's subject is judicial review, judicial appointments or judicial independence; No otherwise.
- `required_majority_met`: for enactments 2 and 3 only: Yes if the enactment passed its final reading with at least sixty-one votes in favor; No otherwise; blank if the tally is unavailable.
- `deviation_tier`: None if the enactment's text engages none of the five protected values (free and equal elections; core human rights and equality; separation of powers; rule of law; an independent judiciary); Entrenches if it entrenches one or more of them and contradicts none; Limited if it contradicts one to a limited extent; Sharp if it contradicts one sharply. Record which values are engaged and which is the principal subject. Contradiction takes precedence over entrenchment, and the more severe contradiction over the less.
- `direction`: Illiberal if the text or stated purpose moves the constitutional order toward preferring Jewish identity over equal citizenship, restricts the rights of minorities or women, or narrows judicial review or judicial independence; Liberal if it moves the other way on any of those; Neutral if it does none of these, which includes fiscal, procedural and electoral housekeeping measures. Record every axis engaged and code from the principal subject.

## Enactments

1. Basic Law: Human Dignity and Liberty, passed 17 March 1992. Text: https://he.wikisource.org/wiki/חוק-יסוד:_כבוד_האדם_וחירותו
2. Knesset and Local Authorities Elections (Financing, Limitation of Expenses and Audit) Law, 5729-1969, as originally enacted in February 1969 (not its later amendments). Text: the original 1969 enactment; Hebrew Wikisource or Nevo may show only the consolidated later text, in which case say so.
3. Elections (Confirmation of Validity of Laws) Law, 5729-1969, enacted July or August 1969. Text: https://www.nevo.co.il/law_html/law01/190_035.htm
4. Basic Law: Freedom of Occupation (Amendment), 1994, the amendment that added the override ("notwithstanding") clause. Text: https://he.wikisource.org/wiki/חוק-יסוד:_חופש_העיסוק
5. Basic Law: State Budget for 2017 and 2018 (Special Provisions) (Temporary Provision), passed 2 August 2016. Text: https://he.wikisource.org/wiki/חוק-יסוד:_תקציב_המדינה_לשנים_2017_ו-2018_(הוראות_מיוחדות)_(הוראת_שעה)
6. Basic Law: The Knesset (Amendment No. 50, Temporary Provision), with the indirect amendment of Basic Law: The State Economy, passed 24 August 2020. Text: the temporary provision as published in Sefer HaHukkim 2845 (24 August 2020); https://he.wikisource.org/wiki/חוק-יסוד:_הכנסת shows the consolidated law.
7. Basic Law: Israel, the Nation State of the Jewish People, passed 19 July 2018. Text: https://he.wikisource.org/wiki/חוק-יסוד:_ישראל_–_מדינת_הלאום_של_העם_היהודי
8. Basic Law: The Government (Amendment No. 12), passed 23 March 2023, on the conditions for declaring a prime minister incapacitated. Text: https://he.wikisource.org/wiki/חוק-יסוד:_הממשלה shows the consolidated law.
9. Basic Law: The Judiciary (Amendment No. 3), passed 24 July 2023, on the reasonableness standard. Text: https://he.wikisource.org/wiki/חוק-יסוד:_השפיטה shows the consolidated law; the amendment's text may appear as a note.

## Vote extracts from the Knesset's vote tables (Open Knesset mirror, files dated 20 and 22 October 2026)

- Enactment 5, final approval ("אישור החוק"), 2 August 2016, 19:19, vote 25188: 50 for, 44 against, 0 abstain. For: Likud 20, Kulanu 9, Jewish Home 7, United Torah Judaism 6, Yisrael Beytenu 4, Shas 3, Zionist Union 1 (Nachman Shai). Against: Zionist Union 19, Joint List 10, Yesh Atid 10, Meretz 4, listed Yisrael Beytenu 1 (Orly Levy-Abekasis). Did not vote: Joint List 1.
- Enactment 7, final approval, 19 July 2018, 02:46, vote 31013: 62 for, 55 against, 2 abstain. For: Likud 28, Kulanu 9, Jewish Home 8, Shas 7, United Torah Judaism 6, Yisrael Beytenu 4. Against: Zionist Union 24, Joint List 13, Yesh Atid 11, Meretz 5, Kulanu 1 (Akram Hasson), Yisrael Beytenu 1 (Hamed Amar). Abstain: Likud 1 (Benny Begin), no faction listed 1 (Orly Levy-Abekasis).
- Enactment 6, final approval, 24 August 2020, 21:56, vote 33337: 67 for, 37 against, 0 abstain. For: Likud 34, Blue and White 13, Shas 9, United Torah Judaism 5, Labor 2, Derekh Eretz 2, Gesher 1, Yamina 1 (Rafi Peretz). Against: Yesh Atid-Telem 15, Joint List 12, Yisrael Beytenu 6, Meretz 3, Labor 1 (Merav Michaeli).
- The vote tables cover 20 October 2003 to 13 July 2021. For enactments 1 to 4, 8 and 9, find the recorded tally from Knesset records or press reports of the vote, and say which.

## Output

Return one JSON object with a key for each enactment number 1 to 9. Each value is an object with the variables above as keys. Each variable's value is an object with "value", "source" (URL or document name), "support" (a quotation of at most 25 words or a data point), and "note" (optional). Add a top-level "deviations" list describing any page you had to close, any source outside the permitted list you used and why, and anything you could not find.
