# Issue 15: reading dates and tallies checked against the Knesset's record, 4 November 2026

**Question.** Issue 15 lists the cells whose reading dates and tallies came from press snippets or proxied pages: rows 1, 5, 8 and 9 of codebook/m4-codebook.csv, and the `expedited` and `coalition_only` cells that depend on them. Each is checked here against the Knesset's own record.

**Source.** The Knesset's open-data service, `https://knesset.gov.il/OdataV4/ParliamentInfo/`, tables `KNS_PlenumVote` (each plenum vote, with date, method and the question put) and `KNS_PlenumVoteResult` (each member's vote). Faction on the day is taken from `KNS_PersonToPosition`. The bills are found by their Knesset bill ID in `KNS_Bill`. `[attested: Knesset open data]` The raw results of the final-reading queries are in final-votes-raw.json. Any query below can be rerun from the service, for example `KNS_PlenumVote?$filter=ItemID eq 2207472`.

**Result.** Every coded value holds. Only reading notes outside the coded cells change.

## Row 5: Basic Law: The State Budget for 2017 and 2018 (Special Provisions) (Temporary Provision), 2016

- **Bill:** ID 2006018, published 11 August 2016.
- **First reading:** vote 24994, 19 July 2016 at 22:34, 58 to 46.
- **Final reading:** vote 25188, 2 August 2016 at 19:19, 50 to 44, one member present and not voting.
- **`expedited` Yes stands:** 14 days, matching both coders.
- **`coalition_only` No stands.** One opposition member, Nachman Shai (Zionist Union), voted for, as coder A recorded. Orly Levy-Abekasis (Yisrael Beytenu, then a coalition faction) voted against, as coder B recorded.
- **By faction at the final reading:**
  - Likud 20 for; Kulanu 9 for; Jewish Home 7 for; United Torah Judaism 6 for; Shas 3 for.
  - Yisrael Beytenu 4 for, 1 against.
  - Zionist Union 19 against, 1 for.
  - Joint List 10 against, 1 present; Yesh Atid 10 against; Meretz 4 against.

## Row 8: Basic Law: The Government (Amendment No. 12), 2023

- **Bill:** ID 2201424, published 27 March 2023.
- **Preliminary reading:** vote 38360, 1 March 2023 (roll call).
- **First reading:** vote 38391, 13 March 2023 (roll call).
- **Final reading:** vote 38567, 23 March 2023 at 05:40, roll call, 61 to 47. Coded under issue 19 (research/coding-2026-11-04-incapacity/; change log (az)).
- **`expedited` Yes stands:** 10 days. Coder B's "overnight 13–14 March" is consistent with a first-reading sitting dated 13 March in the record.

## Row 9: Basic Law: The Judiciary (Amendment No. 3), 2023

- **Bill:** ID 2207472, published 26 July 2023.
- **First reading:** vote 39566, 11 July 2023, roll call, 64 to 56.
  - Coalition factions 64 for: Likud 32, Shas 11, United Torah Judaism 7, Religious Zionism 7, Otzma Yehudit 6, Noam 1.
  - Opposition factions 56 against: Yesh Atid 24, National Unity 12, Yisrael Beytenu 6, Ra'am 5, Hadash-Ta'al 5, Labor 4.
  - Coder A's "64–54" for this reading was wrong by two; the reading is not a coded cell.
- **Final reading:** vote 39785, 24 July 2023 at 15:45, roll call, 64 to 0. All 64 votes for came from the six coalition factions, and no opposition member voted.
- **`expedited` Yes and `coalition_only` Yes stand:** 13 days, matching both coders.

## Row 1: Basic Law: Human Dignity and Liberty, 1992

- **Not checkable here.** The Knesset's vote data, in its own service and on Open Knesset, begins in October 2003.
- The tally (32 to 21, one abstaining), the December 1991 first reading and the `expedited` No therefore stay on press sources.
- They are marked "press snippet only" in the codebook's provenance column, as issue 15's stopping rule requires.
- The route to them is Divrei HaKnesset for 17 March 1992 and the first reading (issue 6, route 4).
