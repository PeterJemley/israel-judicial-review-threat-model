# Issue 34: an Arab-party variant of the cross-party sign (exploratory)

**Author.** Peter Jemley, who maintains this project.

**What this is.** A secondary analysis, run at the author's direction on 9 November 2026 ([issue 34](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/34)).
- **The sign it varies.** The project's cross-party sign is `coalition_only`. It is Yes when only coalition members voted for a law at its final reading, which is one of the four warning signs. It is No when at least one opposition member voted for.
- **The variant.** For laws that touch interests in conflict between Jewish and Arab citizens, the variant counts cross-party support as present only if a member of an Arab party voted for.
- **Why it is exploratory.** It was defined after the project's data were seen, so the result is assessed after the data were known. The primary sign is unchanged.

**Why.**
- **The reply.** Rosen-Zvi and Yarom argue that in Israel bipartisan decision-making "correlates only weakly with minority protection, especially for the Arab minority". They add that "a unified bloc of Jewish MKs can readily satisfy this condition" (I·CON 24 (2026), p. 722).
- **Medina's answer.** Where an amendment "affects interests in conflict between Jewish and Arab citizens, the procedural requirement could—indeed should—be interpreted to include support from parties representing the Arab-Palestinian minority" (rejoinder, I·CON blog, June 2026).

See [2026-11-09-reply-and-rejoinder.md](../2026-11-09-reply-and-rejoinder.md), objections O9 to O11.

## Fixed before any vote was looked at (committed before the roll calls were read)

**Which rows qualify.** The rule is fixed from the project's existing codes, which were scored from the law texts, not from votes. A row in the codebook or the comparison sample qualifies if either holds:
- **(a)** it was recoded under issue 33, the laws Rosen-Zvi and Yarom name on the Jewish side of the formula;
- **(b)** either of its original coders' `direction` notes names the axis "preferring Jewish identity over equal citizenship", or the axis of minority rights or equal citizenship, as engaged in either direction.

Applied mechanically, the rule gives:
- the codebook's **row 1**, Basic Law: Human Dignity and Liberty, 1992, by (b);
- the codebook's **row 7**, the Nation-State law, 2018, by (a) and (b);
- comparison-sample **seq 1**, Basic Law: The Knesset, 1958, by (b);
- comparison-sample **seq 16, 64, 103 and 127**, Basic Law: Jerusalem and its amendments, by (a).

`[attested: research/coding-2026-10-22/coder-A.json, coder-B.json; research/coding-sample-2026-10-22/coder-*-b*.json; research/recode-2026-11-09-issue33/final.json]`

**What counts as an Arab party.** A Knesset faction of a list that mainly represents Arab citizens:
- Hadash; Ra'am (the United Arab List); Balad; Ta'al; the Arab Democratic Party;
- their joint lists, among them the Joint List, Hadash–Ta'al and Ra'am–Balad;
- earlier Arab-majority lists, such as the Progressive List for Peace.

An Arab member of a party that is not an Arab party does not count, following Medina's phrase "parties representing the Arab-Palestinian minority". An Arab party's vote counts whether the party was in the coalition or in opposition.

**The variant sign, `coalition_only_arab`.**
- **For a qualifying row:**
  - **No** (cross-party support present) if at least one member of an Arab party voted for at the final reading;
  - **Yes** if the member-by-member roll call shows that none did;
  - **blank** if no member-by-member roll call is available.
- **For any other row:** the same as `coalition_only`.

**The source.** The Knesset's open-data service: the member-by-member results of the final-reading vote (KNS_PlenumVoteResult), and each member's faction on that date (KNS_PersonToPosition). The service holds roll calls from October 2003 on. Earlier votes have no roll call by member in it, so rows 1 and seq 1, 16 and 64 are expected to stay blank.

**Expectations, recorded before reading any vote.**
- No member of an Arab party voted for any qualifying law that has a roll call: row 7 (2018), seq 103 (2018) and seq 127 (2024). Confidence is high for the first two and moderately high for seq 127.
- **T1 does not change.** Row 7's `coalition_only` is already Yes, so the variant cannot change it, and row 1 is uncoded.
- **The comparison sample may change.** Any qualifying row whose primary `coalition_only` is No, meaning only Jewish opposition parties gave cross-party support, flips to Yes under the variant. The primary codes for seq 103 and 127 had not been looked at when this was written.
