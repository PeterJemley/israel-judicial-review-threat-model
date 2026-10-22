# Circumstances sheet, 2026-10-22

You are the circumstances reader. You code one variable, `situated_beneficiary`, for the nine enactments below. You work alone. You have not seen, and must not seek, any outcome of any court case about these enactments.

## The variable

`situated_beneficiary`: Yes if, on the day of passage, the enactment's operative provision would alter the legal position of an identifiable person then in office, or of the sitting government, in a matter then live; No otherwise.

A matter is live only on facts dated no later than the day of passage, from this closed list:

1. a proceeding pending before a court concerning that person or that matter;
2. a formal step already taken against that person or against the government's measure, such as an attorney general's opinion, an indictment, or a petition served;
3. a fixed deadline that the enactment moves;
4. a single-instance or sunset clause in the enactment itself.

Excluded: judgments on the enactment, commentary, and your own belief about motive. An enactment whose operative provision is general, and whose connection to a live matter rests on motive alone, is No. Where you code Yes, name the person or the government, the matter, the admissible fact, the fact's date, and the source with its date. Where you code No, say what you looked for and where.

## Rules of the sheet

- Permitted sources: court docket records showing case numbers, parties and filing dates; petitions and other filings themselves, dated on or before the day of passage; press reports dated on or before the day of passage; the enactment's text as published (Hebrew Wikisource or Nevo copies are acceptable); Knesset records and bill explanatory notes. A source dated after passage may be used only to establish a fact dated on or before passage, for example a docket listing that shows a filing date, and you must stop reading at any description of what a court decided about the enactment or about the pending matter.
- Forbidden: any judgment on any of these enactments; any text describing how a court treated one of them or what it decided; any file in the repository this sheet comes from, other than this sheet; your own recollection of how any enactment fared in court. If a page you open turns out to describe a decision, close it and say so in your notes.
- Do not infer a value from what seems likely. If no permitted source establishes an admissible fact, code No and describe the search.
- Identify enactments by the titles below. Do not add case names to the enactments.

## Access notes

The Knesset's websites are geo-blocked from here. The NYU Faculty Digital Archive mirrors the Knesset record (Divrei HaKnesset); the Internet Archive holds captures of Knesset gazette and bill PDFs. The judiciary's site may be unreachable. Petitioners often host their own petitions (the Movement for Quality Government, the Association for Civil Rights in Israel, Adalah); institutes' case pages usually summarise decisions, so use them only for filing dates and parties and stop at any decision text. Press archives with dated articles (Times of Israel, Haaretz, Globes, Jerusalem Post, Ynet, Calcalist, JTA) are permitted for reports dated on or before passage.

## Enactments

1. Basic Law: Human Dignity and Liberty, passed 17 March 1992. Text: https://he.wikisource.org/wiki/חוק-יסוד:_כבוד_האדם_וחירותו
2. Knesset and Local Authorities Elections (Financing, Limitation of Expenses and Audit) Law, 5729-1969, passed 19 February 1969 (the original enactment, which financed the factions of the outgoing Knesset for the 1969 elections).
3. Elections (Confirmation of Validity of Laws) Law, 5729-1969, passed 15 July 1969. Text: https://www.nevo.co.il/law_html/law01/190_035.htm
4. Basic Law: Freedom of Occupation (Amendment), 1994, passed 9 March 1994, which added the override ("notwithstanding") clause. Text: https://he.wikisource.org/wiki/חוק-יסוד:_חופש_העיסוק
5. Basic Law: State Budget for 2017 and 2018 (Special Provisions) (Temporary Provision), passed 2 August 2016. Text: https://he.wikisource.org/wiki/חוק-יסוד:_תקציב_המדינה_לשנים_2017_ו-2018_(הוראות_מיוחדות)_(הוראת_שעה)
6. Basic Law: The Knesset (Amendment No. 50, Temporary Provision), with the indirect amendment of Basic Law: The State Economy, passed 24 August 2020, which moved the deadline for passing the 2020 budget.
7. Basic Law: Israel, the Nation State of the Jewish People, passed 19 July 2018. Text: https://he.wikisource.org/wiki/חוק-יסוד:_ישראל_–_מדינת_הלאום_של_העם_היהודי
8. Basic Law: The Government (Amendment No. 12), passed 23 March 2023, on the conditions for declaring a prime minister incapacitated. Text: https://he.wikisource.org/wiki/חוק-יסוד:_הממשלה (consolidated).
9. Basic Law: The Judiciary (Amendment No. 3), passed 24 July 2023, on the reasonableness standard. Text: https://he.wikisource.org/wiki/חוק-יסוד:_השפיטה (consolidated).

## Output

Return one JSON object with a key for each enactment number 1 to 9. Each value is an object with one key, `situated_beneficiary`, whose value is an object with: "value" (Yes or No), "person_or_government", "matter", "admissible_fact" (which item of the closed list, and the fact), "fact_date", "source" (URL or document name), "source_date", "support" (a quotation of at most 25 words or a data point), and "note" (optional; for No, the search made). Add a top-level "deviations" list describing any page you had to close, any source outside the permitted list you used and why, anything you could not find, and any court outcome that reached you through a search-result snippet without your opening the page.
