# Coding sheet, 2026-11-04 (issue 10)

The rules and variable definitions are those of research/coding-2026-10-22/coding-sheet.md, given here in full to each coder, for one enactment.

**Enactment 10.** Basic Law: The Judiciary (Amendment No. 4) (composition of the Judicial Selection Committee); final reading 27 March 2025.

**Vote record** (vote-extract.json, from the Knesset's vote tables via Open Knesset and the Knesset's own open-data service):
- **First reading:** vote 38298, 20 February 2023, roll call, 63 for and 47 against.
- **Final reading:** vote 43884, 27 March 2025 at 07:36, roll call, 67 for, 1 against, none abstaining.
  - For: Likud 32, Shas 11, Otzma Yehudit 7, United Torah Judaism 6, Religious Zionism 6, HaYamin HaMamlachti 4, Noam 1.
  - Against: Yesh Atid 1.
  - Present and not voting: Ra'am 1, Labor 1.
- **Bill:** Knesset bill ID 2201200, published 1 April 2025.

**Variables:** named_beneficiary, immediate_effect, coalition_only, expedited, scope, temporary_provision, targets_judiciary, deviation_tier, direction, as defined in the 22 October sheet. required_majority_met applies only to enactments 2 and 3 and is left blank.

**Access:** `knesset.gov.il/OdataV4/ParliamentInfo/` answers; `main.knesset.gov.il` and `fs.knesset.gov.il` show a bot check to automated requests, which coders must not try to get around.

**Output:** one JSON object with key "10", in the 22 October format.
