# Issue 34: results (9 November 2026; exploratory)

**What was run.**
- **Fixed first.** The qualifying rule, the definition of an Arab party and the expectations were committed (5ab6cda) before any roll call was read. They are in [README.md](README.md).
- **The roll calls** come from the Knesset's open-data service: the member-by-member results of each final-reading vote, and each member's faction on that date. They are extracted to [roll-calls.json](roll-calls.json).
- **The results** come from `python3 analysis/variant_issue34.py`.

## The roll calls

| Law | Final-reading vote | For, against, abstaining | Yes-votes by faction | Members of an Arab party voting for |
|---|---|---|---|---|
| Row 7, the Nation-State law | vote 31013, 19 July 2018 | 62, 55, 2 | Likud 27, Kulanu 9, Jewish Home 8, Shas 6, Yisrael Beiteinu 4, United Torah Judaism 4, faction not in the data 4 | None |
| Seq 103, Jerusalem (Amendment No. 2) | vote 28383, 2 January 2018 | 64, 51, 1 | Likud 28, Kulanu 10, Jewish Home 8, Yisrael Beiteinu 5, Shas 5, United Torah Judaism 4, faction not in the data 4 | None |
| Seq 127, Jerusalem (Amendment No. 3) | vote 41927, 29 October 2024 | 29, 7, 0 | Likud 8, Shas 5, United Torah Judaism 4, Religious Zionism 3, Otzma Yehudit 2, New Hope (הימין הממלכתי) 2, Yisrael Beiteinu 2, Yesh Atid 1, National Unity (המחנה הממלכתי) 1, faction not in the data 1 | None |

`[attested: roll-calls.json, from KNS_PlenumVoteResult and KNS_PersonToPosition]`

**Five yes-voters have no faction entry for the vote date in the data.** In the 2018 votes they are Benjamin Netanyahu, Moshe Gafni, Yaakov Litzman and Yitzhak Vaknin. In 2024 it is Ze'ev Elkin. None of them sat for an Arab party. `[conjectural: from general knowledge of their parties, recorded because the data leave the field empty]`

**The expectation held.** No member of an Arab party voted for any qualifying law that has a roll call.

## The variant sign

| Row | Primary `coalition_only` | `coalition_only_arab` | Why |
|---|---|---|---|
| Codebook row 1, Human Dignity and Liberty (1992) | blank | blank | No member-by-member roll call in the data |
| Codebook row 7, the Nation-State law (2018) | Yes | Yes | No opposition member, and no Arab-party member, voted for |
| Sample seq 1, Basic Law: The Knesset (1958) | No | blank | No member-by-member roll call in the data |
| Sample seq 16, Basic Law: Jerusalem (1980) | No | blank | No member-by-member roll call in the data |
| Sample seq 64, Jerusalem (Amendment), 2000 | blank | blank | No member-by-member roll call in the data |
| Sample seq 103, Jerusalem (Amendment No. 2), 2018 | Yes | Yes | No opposition member, and no Arab-party member, voted for |
| Sample seq 127, Jerusalem (Amendment No. 3), 2024 | No | **Yes** | Its cross-party support came only from Jewish opposition parties (Yesh Atid, Yisrael Beiteinu, National Unity); no Arab-party member voted for |

**Seq 1 and 16 lose their codes.** Their primary codes came from records other than a member-by-member roll call. The rule fixed in advance leaves the variant blank without one, so the variant does not use those records.

## What changes, and what does not

**T1 does not change.** Its current configuration is the same both ways:
- six rows in the primary analysis;
- six of them ruled against by the Court;
- two discordant rows, both with the decision rule predicting Adverse.

It stays Inconclusive. Row 7's sign was already Yes, and row 1 is uncoded.

**The comparison sample changes in three rows:**

| Comparison sample (39 laws) | Primary | Variant |
|---|---|---|
| `coalition_only` No | 8 | 5 |
| `coalition_only` Yes | 5 | 6 |
| `coalition_only` blank | 26 | 28 |
| Predicted classes (concordant, discordant, undetermined, uncoded) | 8, 3, 1, 27 | 7, 3, 1, 28 |

**Combined with issue 33's recode.** Both are exploratory. With the widened reading of equality from issue 33 and this variant together, seq 103 and seq 127 are each predicted Adverse by both the decision rule and the elite thesis, and neither law was ever challenged. T1 is unchanged in this combination too.

## What this shows, and its limits

- **Where the variant bites.** It matters only where a law that touches Jewish–Arab interests drew its cross-party support from Jewish opposition parties alone. In the project's data that is one law, the 2024 Jerusalem amendment. It does not reach T1's result, because the one qualifying law that went to the Court, the Nation-State law, had no opposition support of any kind. `[conjectural]`
- **It cannot reach earlier votes.** It cannot be applied to votes before October 2003, for want of member-by-member roll calls in the data. Those are four of the seven qualifying rows.
- **Its definitions are the project's own.** The qualifying rule leans on the project's existing direction notes, and the list of Arab parties is the project's own. Another definition could qualify other laws.
- **It is exploratory.** It was defined after the data were seen, and the primary sign is unchanged unless the author decides otherwise.
