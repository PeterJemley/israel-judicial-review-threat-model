# Working on this repository

The project tests the threat claim in Medina (2026) under Threat = Capability × Intent. The main document is `medina-threat-conjecture-note.md`; `README.md` is the plain-language entry point.

## Responses to the author

- **Put anything the author must do in its own list, under a heading such as "For you to do", at the end of the response.** One action per item, each stating where to do it (a settings page, a GitHub issue, an email to send). Do not leave such actions in running prose. If there is nothing for the author to do, omit the section.
- Keep decisions that are the author's (design choices, interpretive readings) in that list too, phrased as a question with a recommended answer.

## Conventions the record depends on

- **Every substantive change to the note gets a change-log entry**: dated, lettered in sequence (the last letter used is in the note's final entry), saying what changed, why, and whether data, code or verdicts changed. Corrections are made "at the author's direction".
- **Before committing, run `python3 analysis/check_numbers.py`.** It pins numbers and phrases in the prose to the data. If a reworded sentence is pinned, change the check with the text.
- **After changing anything in `figures/sources/` (ledger, errors list, jigsaw), regenerate the figures** with `python3 analysis/make_figures.py`. Add an errors-list entry for each confirmed error found in the project's own work.
- **Results found after seeing the data are labelled exploratory.** Never call a run pre-registered or blind beyond what the run's own records show.
- **Quote Medina only with page numbers, and do not harden his words.** Keep "likely", "may" and "deferred" as he wrote them. If a quotation can't be checked against the article, say so rather than paraphrasing it as his.
- **Research notes in `research/` tag every claim with its source.** Use `[attested: ...]` for a text actually read, `[abstract: ...]`, `[search-lead]` for a search summary not read, and `[conjectural]` for an inference. A search summary is never applied to the note as fact.
- **Commit messages carry no co-author or AI attribution lines** (change log (ao)). The note and README do not mention the AI tools used, beyond the disclosure that the coding roles were language-model agents.
- **Edit CSVs by text, not by rewriting them with a CSV library,** so their hand-written quoting is kept.

## Environment notes

- Cloud sessions here have had restricted network access. When a source host is blocked, record the gap and the host to allow; don't stand in for the missing source.
