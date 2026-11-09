# Recoding sheet: two columns, five enactments (issue 33, 9 November 2026)

**Your role.** You are a coder. Code each enactment below on two columns, `deviation_tier` and `direction`, under the rules on this sheet.
- Read the enacted text at the sources given.
- Do not open any other file in this repository.
- Do not look up how anyone else has coded or judged these laws, including any court ruling or commentary on them.
- Work alone.

## The columns

**`deviation_tier`** is measured against five protected values: free and equal elections; core human rights and equality; separation of powers; the rule of law; an independent judiciary. The codes are:
- **None** if the enactment's text engages none of the five values;
- **Entrenches** if it entrenches one or more of them and, read as below, contradicts none;
- **Limited** if it contradicts one to a limited extent;
- **Sharp** if it contradicts one sharply.

Contradiction takes precedence over entrenchment, and the more severe contradiction over the less. Record which values are engaged and which is the principal subject.

**The widened reading of "core human rights and equality", which is what this sheet tests.**
- **What engages the value.** A provision engages it if it regulates a right on its face. It also engages it if its foreseeable effect falls differently on Jewish and Arab citizens, or on Palestinians living under Israeli rule, through any of: territory, land, political status, language, or a right or preference reserved to one national group.
- **What counts.** Effects that are indirect count. So does entrenchment that makes such a provision harder to change, for example a special majority required to amend it.
- **Limited** where the departure from equal treatment is indirect or declaratory.
- **Sharp** where a provision directly authorizes or requires different treatment by national group.

**`direction`** has three codes:
- **Illiberal** if the text or stated purpose moves the constitutional order toward preferring Jewish identity over equal citizenship, restricts the rights of minorities or women, or narrows judicial review or judicial independence;
- **Liberal** if it moves the other way on any of those;
- **Neutral** if it does none of these, which includes fiscal, procedural and electoral housekeeping measures.

Read "preferring Jewish identity over equal citizenship" under the same widened reading: indirect, group-differential effects count. Record every axis engaged, and code from the principal subject.

**For an amendment, code what the amendment itself adds or changes,** not the whole Basic Law as it stands after the amendment.

## The enactments

- **"16"**: חוק-יסוד: ירושלים בירת ישראל — Basic Law: Jerusalem, Capital of Israel. Passed 30 July 1980; ס"ח 980, תש"ם, עמ' 186 (5.8.1980); kind: enactment.
  - Text: https://he.wikisource.org/wiki/חוק-יסוד:_ירושלים_בירת_ישראל
  - https://web.archive.org/web/20230714204041/https://fs.knesset.gov.il/9/law/9_lsr_208452.pdf
- **"64"**: חוק-יסוד: ירושלים בירת ישראל (תיקון) — Basic Law: Jerusalem, Capital of Israel (Amendment). Passed 27 November 2000; ס"ח 1760, תשס"א, עמ' 28 (7.12.2000); kind: amendment.
  - Text: https://web.archive.org/web/20250604031008/https://fs.knesset.gov.il/15/law/15_lsr_300277.pdf
  - https://he.wikisource.org/wiki/חוק-יסוד:_ירושלים_בירת_ישראל
- **"103"**: חוק-יסוד: ירושלים בירת ישראל (תיקון מס' 2) — Basic Law: Jerusalem, Capital of Israel (Amendment No. 2). Passed 2 January 2018; ס"ח 2680, תשע"ח, עמ' 94 (7.1.2018); kind: amendment.
  - Text: https://web.archive.org/web/20240627011752/https://fs.knesset.gov.il/20/law/20_lsr_457849.pdf
  - https://he.wikisource.org/wiki/חוק-יסוד:_ירושלים_בירת_ישראל
- **"127"**: חוק-יסוד: ירושלים בירת ישראל (תיקון מס' 3) — Basic Law: Jerusalem, Capital of Israel (Amendment No. 3). Passed 29 October 2024; ס"ח 3299, תשפ"ה, עמ' 10 (30.10.2024); kind: amendment.
  - Text: https://web.archive.org/web/20251211054901/https://fs.knesset.gov.il/25/law/25_lsr_5106966.pdf
  - https://he.wikisource.org/wiki/חוק-יסוד:_ירושלים_בירת_ישראל
- **"row7"**: חוק-יסוד: ישראל – מדינת הלאום של העם היהודי — Basic Law: Israel, the Nation State of the Jewish People. Passed 19 July 2018; kind: enactment.
  - Text: https://he.wikisource.org/wiki/חוק-יסוד:_ישראל_–_מדינת_הלאום_של_העם_היהודי

## What to return

One JSON object, keyed "16", "64", "103", "127" and "row7". Each value is an object with `deviation_tier` and `direction`. Each of those has four fields:
- `value`: one of the codes above;
- `source`: the URL you read;
- `support`: the provision, quoted in Hebrew with its section number;
- `note`: the values or axes engaged, the principal subject, and, where the call was close, the reading you rejected.

If you cannot reach a text, say so in `note`, and leave `value` blank. Do not code from memory.
