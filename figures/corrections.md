# Corrections to the figures before publication

On 28 October 2026, before the figures were committed, a separate reader tested every title, caption, label, alt text, ledger row and errors row against the sources. The reader was a language-model agent given the files and the article, not the reasoning behind the drafts. It found 40 problems: 3 that changed what a sentence means, 19 that weakened a claim, and 18 that cost attention. Each finding was checked against its source before it was acted on, and every one was confirmed. This file records each finding and what changed.

Three of the findings trace to the repository's own prose rather than the figures. They were corrected the same day in the note's change log item (aq), as was the README glossary's "rushed" (finding A6); the errors list records all four:
- the note's evidence item 9 and matrix M1's 2025 row;
- the note's evidence item 6;
- the codebook README's sentence on the first run.

## Changed what a sentence means

| Finding | What was wrong | What changed |
|---|---|---|
| C1 | Ledger row E9 said the Court froze and annulled two dismissals. The cited timeline records that the Shin Bet chief's dismissal was held unlawful after the government had rescinded it, with no operative order; only the attorney general's was frozen and annulled. | E9 now says what the timeline says. The note's own wording, which the row had copied, is in the errors list (entry 24) and was corrected in change log (aq). |
| C2 | Figure 4 said T1's rule was fixed before outcomes were seen. The revision was written after nine rows' outcomes were known, and was fixed before the blind recoding. | Figure 4's subtitle says so. The ledger's status is renamed "Inconclusive under a rule set before the run". |
| C3 | The jigsaw's centre called Claims A to D all parts of Medina's sentence. Claim D, about Capability × Intent, is the project's own. | The centre now reads "Medina's three claims (A to C) and the project's model claim (D)". |

## Weakened a claim

| Finding | What was wrong | What changed |
|---|---|---|
| W1 | Jigsaw piece PA asked whether the package would remove "every check", broader than Claim A. | It now asks about "the institutional checks that make Israel a democracy". |
| W2 | Ledger row E4 was marked Contested, but its basis contests the project's coding, not Medina's statement. | Now Unclear: it rests on the paper, and the judgment is unread (issue 12). |
| W3 | Ledger row R2 was marked Contested, though the note records it as refuted and no source contests that. | Now Refuted, with the note's basis. This reverses a default proposed when the figures were planned. |
| W4 | Figure 4 said the first run had all 5 laws Adverse. It had 4 of 5; the fifth came from the later recoding of the 1994 row. | The note under figure 4 gives both configurations, from results.md. |
| W5 | Figure 4's floor of six Adverse outcomes relies on two codes flagged as contestable, and its count of 11 rows dropped "provisional". | A row for K = 5 is added, labelled as reachable only if a contestable code were reversed. The note names the two codes and restores "provisional". |
| W6 | The errors list missed at least eight errors that meet its own rule. | Nine entries added (12, 14, 15, 16, 18, 19, 21, 23 and 24), and entry 31 expanded. |
| W7 | Errors entry 10 was marked Corrected, but matrix M2 still lacks an interpretation row. | Restated as the wrong statement in change log (p), and marked "Recorded, not undone". |
| W8 | Errors entry 17 (now 37) cited the wrong commit, and its "what caught it" had no source. | It cites old commit 0c53bc7 and the rewritten fc6b81b, and says that what caught it is not recorded. |
| W9 | Two README errors were filed as review errors. | Moved to research. Reviews now hold 2 entries. |
| W10 | Errors entry 19 (now 26) was marked Corrected, but the same words survive in the codebook README. | Marked open. |
| W11 | The figures README and the script said no number was typed by hand. Many are, in the curated files and as fixed values. | Both now say which numbers are computed, which are curated, and which fixed values are set in the script. |
| W12 | The ledger, the errors list and figure 4 carried the label MEASURED. | They now carry FROM THE RECORD and CALCULATION. |
| W13 | Figures 3 and 5 called the sampled laws "never challenged", dropping the hedge. | Now "no challenge found", with the searches' limits stated. |
| W14 | Figure 3 called the signs "the Court's" without "as Medina reports", and counted five signs while also saying four. | It now says "the four warning signs Medina reports the Court uses", with the beneficiary sign in two versions, and that the thresholds are the project's own. |
| W15 | Figure 5 said the coders did not see the judgments, leaving out that they saw outcomes in search snippets. | The footer now says both, and that outcome-blindness is not claimed for those laws. |
| W16 | Figure 5 ordered Entrenches after None on an axis of departure; the codebook README calls Entrenches the lowest step. | Entrenches now comes first, and the axis label says that both it and None contradict no value. |
| W17 | Ledger row E1 dropped the October 7 war, which Medina gives as halting the plan, and called the 2023 amendments the plan's measures. | Both corrected from p. 687. |
| W18 | The ledger listed the situated sign's successful recheck but not its first, failed check, and its caption said "every claim and result". | Rows F10a and F9a added, and the caption narrowed. |
| W19 | Ledger row RE read as though Hirschl's and Gavison's thesis itself had been tested. | It now says "as this project operationalizes it", citing issue 21. |

## Cost attention

| Finding | What was wrong | What changed |
|---|---|---|
| A1 | Figure 2 turned "no ruling found by 21 October 2026" into "pending as of 22 October", for both pending rows. | Each row now uses its own source's words: the timeline's for the 2025 law, and the challenge record's for the 2026 law. |
| A2 | Figure 2's label for HCJ 8948/22 listed reasons that do not apply. | It now gives the challenge reader's recorded reason: the Court found it unnecessary to rule on the amendment. |
| A3 | Figures 1 and 8 counted Human Dignity and Liberty as "challenged"; its binding force was decided, and it was not petitioned against. | "Came before the Court" is used, with the distinction stated. |
| A4 | Jigsaw thread 2 called laws "changes" and presented 1958 and 1959 as a decade. | Corrected. |
| A5 | Figure 5's footer gave the sliding scale as the Court's, and as weighing breadth of support only. | It is now Medina's reading, with his own list of procedural factors (pp. 681, 702, 708). |
| A6 | "Rushed through" was pejorative, and "ordinary" risked confusion with ordinary statutes. | "Expedited", Medina's word, is used, and "ordinary" is dropped. |
| A7 | Figure 3's situated-sign label dropped the condition added when the list was tightened. | Restored: "in a way others would not share". |
| A8 | Scope statements left gaps. | Added: the unchecked window from December 2025 to October 2026, and the period and jurisdiction on figures 3 and 5. |
| A9 | "Judged after 1995" left out Mizrahi Bank itself. | "Decided from Mizrahi Bank (1995) onward". |
| A10 | Ledger row E2 said the blind coding "confirms" Medina's statement. | It now says what was coded, and how. |
| A11 | The errors list's rule left out open and recorded entries, and said flatly that the record holds no mistranslation. | Both restated. |
| A12 | Errors entries for the 1994 cell and the merge defect gave the wrong cause, or joined two errors. | Corrected and split (entries 20, 22 and 23). |
| A13 | Errors entry 3 repeated an imprecise count from the change log. | Qualified. |
| A14 | The ledger said its rows were grouped by section of the note, but one group comes from other records. | The subtitle says so. |
| A15 | Ledger row F3 was marked Contested, though no one contests the figure. | Now Unclear. |
| A16 | Ledger row F8 marked an established fact as not yet checkable. | It now names the expectation that cannot yet be checked. |
| A17 | Ledger row F1's "every law accounted for" could be read as a claim of completeness. | Reworded, with a pointer to F2. |
| A18 | The jigsaw's subtitle invited reading a fill as progress, and "settled" was used two ways. | The rule and labels now say "established or refuted", and that a fill is not progress toward an answer. |
