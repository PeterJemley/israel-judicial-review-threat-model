# Israel judicial review as a threat model

Maintained by Peter Jemley.

This project tests an argument in Barak Medina's 2026 article in the *International Journal of Constitutional Law* (I·CON), "On constitutional identity, democratic legitimacy, and judicial review in times of democratic backsliding: The case of Israel" (https://doi.org/10.1093/icon/moag052). Its main document, [the note](medina-threat-conjecture-note.md), treats the argument as a set of conjectures: guesses to be tested, each stated with the evidence that would prove it wrong. The note is updated as the work goes on, and every change is dated in its change log. Issi Rosen-Zvi and Meir Yarom published a reply to the article in the same issue, and Medina answered them on the journal's blog. The project records that exchange, and says where its own work bears on it ([The published reply to Medina, and his answer](#the-published-reply-to-medina-and-his-answer)).

Medina warns that Israel's democracy, and Israel itself, are at risk. The note's analyses rest on one formula from threat assessment: **Threat = Capability × Intent**. A threat is the product of what an actor can do and what it means to do, so it disappears if either is zero. Capability here is the governing coalition's power to change the Basic Laws, measured both on paper, by its seats, and in practice, after what can stop it, such as the Court, mass protest and foreign allies. Intent is what the coalition means to do with that power, and the warning signs that, according to Medina, the Court looks for (explained below) are the note's evidence of it. The note splits Medina's warning into three claims, adds a fourth that asks whether the formula itself fits this case, names the other explanations for the same evidence, and proposes tests. Tables at the end of the note lay out the threat, starting with capability against intent over time. The data, which score Basic Laws on those warning signs, are in the [codebook](codebook/) folder.

**New here?** Start with [What this project is about](#what-this-project-is-about), in plain language. The list of files just below is for readers who want to check the work.

## Contents

- [medina-threat-conjecture-note.md](medina-threat-conjecture-note.md): the note. Its last section is a dated change log.
- [codebook/m4-codebook.csv](codebook/m4-codebook.csv): the M4 codebook as data, blind-recoded on 22 October 2026 under the revised T1; a blank cell is a value no permitted source settled. Since then the 1994 outcome was settled on the judgment's text, the Incapacity amendment's coalition-only cell was coded from the Knesset's roll call, and a tenth row was added for the March 2025 Judicial Selection amendment, whose outcome is Pending. The table it replaced is kept beside it as `m4-codebook-illustrative-2026-10-22.csv`. See [codebook/README.md](codebook/README.md).
- [codebook/m4-descriptive.csv](codebook/m4-descriptive.csv): descriptive columns for each codebook row: days from first reading to final vote, votes for, and the opposition's share of them, each with its source.
- [analysis/](analysis/): the exact permutation test, the detectability check, the script that assembles the codebook from the coding files, the frame's change counts (`frame_counts.py`), the descriptive columns (`descriptive.py`), and `check_numbers.py`, which fails if the prose drifts from the data.
- [research/coding-2026-10-22/](research/coding-2026-10-22/): the coding sheet, both coders' sheets, the adjudications, the docket reader's outcomes, and [results.md](research/coding-2026-10-22/results.md), the first run's result: inconclusive before outcomes, on one discordant row against a minimum of six.
- [codebook/comparison-sample.csv](codebook/comparison-sample.csv): the comparison sample, 39 unchallenged laws titled Basic Law, every third from the first in chronological order, coded on the same columns. See [research/coding-sample-2026-10-22/README.md](research/coding-sample-2026-10-22/README.md).
- [research/frame/](research/frame/): the frame of every law titled Basic Law since 1958 (130 rows), the challenges marked, the draw and its verification.
- [research/coding-sample-2026-10-22/](research/coding-sample-2026-10-22/): the comparison sample's coding sheets, every role's reports, the adjudications and the one-vote check.
- [research/coding-2026-11-04-incapacity/](research/coding-2026-11-04-incapacity/) and [research/coding-2026-11-04-row10/](research/coding-2026-11-04-row10/): the Incapacity amendment's roll call and its coding, and every role's sheet and report for the 2025 row.
- [research/](research/): working notes from source searches, kept for provenance. They are unverified until applied to the note. Among them:
  - the verification of the round-1 review's external claims ([2026-11-04-external-claims.md](research/2026-11-04-external-claims.md));
  - the Knesset-record check of reading dates and tallies ([verification-2026-11-04-issue15/](research/verification-2026-11-04-issue15/README.md));
  - an evaluation of Amos Harel's Haaretz analysis of 4 November 2026, with predictions recorded before they resolve ([2026-11-05-harel-evaluation.md](research/2026-11-05-harel-evaluation.md)), and a companion setting the checks in the United States and Israel side by side after their elections of autumn 2026 ([2026-11-05-us-israel-juxtaposition.md](research/2026-11-05-us-israel-juxtaposition.md));
  - the author's Westlaw, Lexis and Bloomberg Law run of 5 November 2026 on ten open questions, with what each finding changes ([legal-db-2026-11-05/](research/legal-db-2026-11-05/README.md)); it changes no coded cell or verdict;
  - a reading of the Reasonableness and Incapacity judgments for where the Court states its signs of abuse ([2026-11-05-court-signs.md](research/2026-11-05-court-signs.md)): neither states the four signs as a set, and the lead opinion in the Incapacity case speaks of a presumption of constitutionality, not of abuse;
  - the published exchange on Medina's article, Rosen-Zvi and Yarom's reply and Medina's rejoinder, objection by objection ([2026-11-09-reply-and-rejoinder.md](research/2026-11-09-reply-and-rejoinder.md)).

## How to use this repository to stay informed

This section is for you if you want to understand what this project says and keep up with it. You do not need any technical skills. If you want to check the work yourself, the next section explains how.

### What this project is about

Israel does not have a single written constitution. Instead, its parliament, called the Knesset, has passed a set of special laws called Basic Laws. Israel's Supreme Court treats these Basic Laws as the country's constitution.

The Knesset can change a Basic Law fairly easily. Most parts of a Basic Law can be changed by a simple majority vote. Because of this, the Supreme Court has said that it can step in when the Knesset misuses its power to change Basic Laws. It first did so in a 2017 case on a budget law, and set out tests for it in a 2021 case, *Shafir*. One example would be changing a Basic Law to help the government in office rather than to set a lasting rule for everyone. The Court calls this "abuse of constituent power", meaning misuse of the power to make constitutional law.

This project studies an article by Professor Barak Medina, published in 2026. Medina argues that the government's 2023 plan to change the courts, often called the judicial overhaul, put Israel's democracy at risk. Since the Court's 1995 decision that it may strike down laws that conflict with the Basic Laws (*United Mizrahi Bank*), critics of the Court have said its approach serves elites who want to keep their dominant position. Medina disagrees, for two reasons (pages 684–685):
- The Court does not stop the public from pressing for change. It requires only that a change to Israel's constitutional identity be made by an explicit amendment, one with broad and lasting public support, passed by a majority that crosses party lines. Such a rule can at least slow a slide away from democracy. Medina takes this as an answer to the claim that the Court serves elites.
- The 2023 plan was about more than the courts.
  - On its face it dealt with judicial appointments and judicial review. But Medina states that its purpose was to change Israel's constitutional identity, its basic character, and he points to strong signs of that aim.
  - Removing an independent judiciary and judicial review, he argues, is meant to make that change possible without formally amending the texts that define it, such as the Declaration of Independence.
  - He is concerned that the government means, among other things, to allow banning parties that represent the Arab-Palestinian minority and to discriminate against women and that minority.
  - Judicial review guards the most basic parts of a democracy, including the right to vote, equal treatment of all citizens and at least a minimal separation of powers. Threats to these, he says, are threats not to the interests or ideas of a liberal elite but to Israel's existence as a democracy.

This project tests one question that the evidence could answer either way. When the Court rules on a Basic Law, does it follow the warning signs that, according to Medina, it looks for? Or does it follow the law's politics, as critics of the Court say? The full argument is in [the note](medina-threat-conjecture-note.md).

Medina's account has also drawn a published reply. The next section sets it out, with his answer and what this test can and cannot say about it.

### The published reply to Medina, and his answer

**Medina's idea in one line.** The further a change to a Basic Law departs from the state's basic values, the broader the support it needs. An amendment "that results from a bipartisan compromise, adopted with overwhelming political and public support", he writes, "may suffice to validate it even if it contradicts the unwritten constitution" (page 702).

**Who answered.** In the same issue of I·CON, Issi Rosen-Zvi and Meir Yarom of Tel Aviv University published "Constitutional methodology and the perils of positivity" (pages 709–722, [free to read](https://doi.org/10.1093/icon/moag054)). They "share Medina's concern over a potentially unruly Knesset" (page 710), and describe the 2023 overhaul as an attempt "to fundamentally reshape Israel's democratic regime" (page 712). Their objection is to his account of the Court's doctrine. Medina answered in a [post on the journal's blog](https://www.iconnectblog.com/democratic-legitimacy-and-constitutional-identity-a-rejoinder/), dated 27 June 2026 on the page and 1 July 2026 in its own suggested citation. The project reports the exchange. It takes no side, except where its own evidence bears on a point.

- **Which values count.** Medina draws Israel's constitutional identity chiefly from three sources: the Declaration of Independence, the ban on parties that deny Israel is a Jewish and democratic state, and Basic Law: Human Dignity and Liberty.
  - *The reply:* this leaves out laws on the Jewish side of Israel's "Jewish and democratic" formula. It names ordinary laws such as the Law of Return and the Absentees' Property Law; Basic Law: Jerusalem; Basic Law: Israel Lands; and the Nation-State law (pages 717–720).
  - *Medina:* those sources are "chief among the relevant formal sources, but definitely not exclusive ones". Basic Law: Human Dignity and Liberty (1992), "along with contemporaneous policy shifts and changes in public sentiment", marked a turn "toward a more liberal identity". He grants that Israel "remains far from the liberal democratic ideal", but finds the Court's reading "plausible—albeit contestable".
  - *Where the project's evidence bears:* the project scores each law against five democratic values, and takes this objection to bear on that list too; that is the project's inference, not the reply's.
    - The scorers coded Basic Law: Jerusalem (1980) as strengthening a value, because of its clause protecting the holy places. They coded its 2000 amendment, on the city's borders and on handing over authority, as touching none of the five.
    - The reply reads the law's "complete and united" capital clause and those 2000 provisions as reinforcing Israeli rule over East Jerusalem's Palestinians. It grants that their effect on rights is "mostly indirect" (page 718).
    - [Issue 33](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/33) rescored them on a list of values widened along the reply's lines. The reply proposes no list, so the widened list is the project's own construction.
    - Two scorers, working separately, agreed on every score: all four Jerusalem laws become a limited, illiberal departure, and the Nation-State law a sharp one.
    - T1's result does not change, but the sample's count of laws that do not depart from the values falls from 27 to 23.
    - The check is exploratory, because it was set after the scores were seen, and the primary scores stand unless the author decides otherwise ([results](research/recode-2026-11-09-issue33/results.md)).
- **What broad support means.**
  - *The reply:* it is unclear what "overwhelming" support means, or how a court could measure public support, and Knesset votes alone "cannot suffice" as evidence of it (page 721). In a Knesset of many parties, bipartisan decision-making "correlates only weakly with minority protection, especially for the Arab minority" (page 722).
  - *Medina:* where a change "affects interests in conflict between Jewish and Arab citizens", the support required "could—indeed should—be interpreted to include support from parties representing the Arab-Palestinian minority". He does not say how a court would measure public support.
  - *Where the project's evidence bears:* the project counts one opposition vote as cross-party support. [Issue 34](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/34) will test a variant drawn from Medina's answer: for laws touching Jewish–Arab interests, the sign is met only if an Arab party voted for. Which parties count is still to be defined there, and the check is exploratory.
- **Would the rule protect minorities?**
  - *The reply:* if a Knesset mustered "an overwhelming (Jewish) majority in favor of restricting minority rights", the logic "would require the Court to uphold such a measure". So the proposal "may, in fact, place them at risk" (page 722).
  - *Medina:* the model should be compared with its alternatives. Israel's formal procedural rules are minimal. A judge-made ban on changing core values "risks undermining public trust in the judiciary". Reading strong procedural requirements into the existing law "may well be a superior alternative".
- **The Nation-State law.** Both sides say the Court's 2021 ruling, *Hasson*, narrowed the law. They disagree on how far.
  - *Medina:* the Court "effectively neutralized" the law (blog). It interpreted the law's clause on Jewish settlement "in a way that rendered it ineffective" (page 698).
  - *The reply:* the ruling "constrained article 7" and "mitigated some of the most problematic consequences" of the law, but "can hardly be said to have neutralized them entirely" (page 720, note 46).
  - *Where the project's evidence bears:* the project counts *Hasson* as a ruling against the law, because the Court read it narrowly. [Issue 12](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/12) keeps that open until the judgment itself is read.
- **Description or theory.**
  - *The reply:* the article shows "apparent vacillation between description and justification", which the reply ties to Dworkin's method (page 714, note 19).
  - *Medina:* "my argument primarily seeks to explain the approach adopted by the Israeli Supreme Court. While the Court has not articulated its reasoning in precisely the terms I offer, the theory aligns with the rationale expressed in its decisions."
  - *Where the project's evidence bears:* only on the four warning signs (listed under "Words you will see"). In the Reasonableness and Incapacity judgments, the Court weighs a longer, open list of signs and does not state the four together ([issue 13](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/13)). The project has not tested the rest of Medina's account.

The full list of the reply's objections, each with Medina's answer, is in [research/2026-11-09-reply-and-rejoinder.md](research/2026-11-09-reply-and-rejoinder.md).

### Words you will see

- **Basic Law:** a law whose title begins "Basic Law", such as "Basic Law: The Knesset". A later law changes it, with the same title and a number, such as "Basic Law: The Knesset (Amendment No. 37)".
- **Temporary Basic Law:** a Basic Law, or a change to one, that lasts only for a set time or a single occasion. Budget laws for named years are a common example.
- **Warning signs:** four features that, according to Medina, the Court treats as signs of misuse (page 699). He writes that a change showing all four is "likely" to be found an abuse "unless proven otherwise". In the two judgments the project has read, the Court weighs a longer, open list of signs, not these four as a set (issue 13). The four are:
  - the law helps the government in office, or a particular officeholder;
  - it takes effect right away;
  - only members of the governing parties voted for it;
  - it was passed on an expedited schedule.
- **Democratic values:** the five values the Court has said a Basic Law must not undermine: free and equal elections, basic human rights and equality, separation of powers, the rule of law, and independent courts. The project records how far each law moves away from these values, if at all. Rosen-Zvi and Yarom argue that Medina's account of Israel's identity leaves out its Jewish side, and the project takes that to bear on this list too; see [The published reply to Medina, and his answer](#the-published-reply-to-medina-and-his-answer).
- **Constitutional identity:** the basic character of the state. In Medina's account, a Basic Law may depart from it only with broad support. What it contains is disputed; see [The published reply to Medina, and his answer](#the-published-reply-to-medina-and-his-answer).
- **The full list:** this project's list of every Basic Law and every change to one since 1958. It is in [research/frame](research/frame/). The project's files call it "the frame".
- **The 39 unchallenged laws:** a group of 39 laws from the full list that no one ever took to court. They show what an ordinary Basic Law looks like, for comparison. The project's files call them "the comparison sample".
- **Scoring:** for each law, two scorers worked separately, without seeing how the Court ruled. They recorded which warning signs the law shows. Where they disagreed, a third reviewer decided, and wrote down why.
- **Conjecture:** a guess the project sets out to test, stated with the evidence that would prove it wrong. Nothing in the project is yet a confirmed finding. Two guesses have been shown wrong, but only on evidence seen after the guesses were made, so those results are labelled exploratory (see Status).

### What the information shows so far

**How often the Basic Laws change.** From February 1958 to July 2026, the Knesset passed 130 Basic Laws or changes to them. Most of these concern two Basic Laws: Basic Law: The Knesset (48) and Basic Law: The Government (30). Changes became much more frequent from the 1990s on:

| Decade | Basic Laws and changes passed |
|---|---|
| 1950s | 4 |
| 1960s | 5 |
| 1970s | 5 |
| 1980s | 12 |
| 1990s | 34 |
| 2000s | 25 |
| 2010s | 23 |
| 2020s, to July 2026 | 22 |

**What happened in court.** Fourteen of the 130 have come before the Supreme Court. The Court has struck down one: the 2023 change to Basic Law: The Judiciary, which limited the Court's power to review government decisions as "unreasonable". It did so in January 2024. In the other cases it has decided, the Court did one of four things. It let the law stand but delayed when it would take effect. It warned that repeating a practice could lead it to strike a law down. It let the law stand, sometimes while reading it narrowly. Or it declined to decide. For the 2021 ruling on the Nation-State law, Medina and Rosen-Zvi and Yarom agree that the Court narrowed the law but disagree on how far ([issue 12](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/12)). Two cases are still waiting for a ruling. One is against a 2025 change to the committee that chooses judges. The other is against Basic Law: Torah Study, passed in July 2026.

**The first test.** The project ran its test once, on nine laws, and the result could not settle the question either way. To tell the two explanations apart, the test needs laws where they point in different directions. Only one of the nine laws did, and the test needs at least six. Since then the final vote on the 2023 Incapacity amendment, which limited how a sitting prime minister can be declared unfit for office, has been coded from the Knesset's record. The project now has two laws where the warning signs and the law's politics point different ways: still four short. The test counts a law as having cross-party support if a single opposition member voted for it. Rosen-Zvi and Yarom argue that such support says little about protection for the Arab minority (page 722). [Issue 34](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/34) will test, as an exploratory check, counting only an Arab party's vote for laws touching Jewish–Arab interests.

**The 39 unchallenged laws.** Most of them are routine changes about how the Knesset and the government work:
- 27 did not move away from the democratic values, or made them stronger;
- 12 moved away from them a little, and none moved away a lot;
- only 3 helped the government that was in office at the time.

These scores measure distance from the five democratic values. Rosen-Zvi and Yarom's objection that Medina leaves out the Jewish side of Israel's constitution bears on some of them, such as the scores for Basic Law: Jerusalem; see [The published reply to Medina, and his answer](#the-published-reply-to-medina-and-his-answer) and [issue 33](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/33). Rescored on a widened reading of equality, in an exploratory check, the sample's count of laws that do not depart from the values falls from 27 to 23 ([results](research/recode-2026-11-09-issue33/results.md)).

For 26 of the 39 laws, the surviving records do not show how each member voted. This is mostly true of votes held before October 2003. So for those laws, one warning sign cannot yet be checked.

**What this does and does not mean.** None of this proves anything yet. The project treats each of its ideas as a guess to be tested, and it says what evidence would show each guess wrong. A score is a judgment, and each score comes with its reasons and its source. A blank space in the data means "not yet known", not "no".

### How the Basic Laws change, and how this project keeps track

You can follow the history of any one Basic Law in the full list:
1. Open [the full list](research/frame/basic-law-frame.csv) in a spreadsheet program such as Excel or Google Sheets.
2. Filter the "subject" column to the Basic Law you want, for example "Knesset".
3. Read the rows in date order.

The "challenged" column says whether the change was taken to court. The "challenge_case" and "challenge_outcome" columns name the case and say briefly what the Court did. These short summaries were recorded early and are not final. The project's own score for each court case is in the [codebook](codebook/m4-codebook.csv), and it can differ from the summary. For example, under the project's rule a law the Court "upheld" while limiting how it applies counts as a ruling against the law. In one such case, the Nation-State law, how far the Court's reading limited the law is open ([issue 12](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/12)); Medina and the reply disagree on it ([The published reply to Medina, and his answer](#the-published-reply-to-medina-and-his-answer)).

When the Knesset passes a new Basic Law, the project adds it to the full list. If someone takes it to court, the project scores it like the others and marks its outcome "Pending" until the Court rules. The 2025 change to the committee that chooses judges has been scored this way and is marked Pending. Basic Law: Torah Study, challenged in 2026, is not yet scored (issue 8).

The full list was last updated on 22 October 2026. Its newest entry is Basic Law: Torah Study of 13 July 2026. Since 4 November 2026 the project can read the Knesset's open-data service, but not its main website, which blocks automated requests (issue 6). The list's entries after December 2025 have not yet been checked against the Knesset's official records.

### How to keep up to date

- **Read the "Status" section** of this page. In short: the project's one test has run once and could not settle the question either way, because it needs more cases. The Status section gives the detail. The "First in the queue" section below it says what is being worked on next.
- **Read the change log.** It is a dated list, at the end of [the note](medina-threat-conjecture-note.md), of every change the project has made and why. It is the best single place to see what is new.
- **Look at the open questions.** The [issues page](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues) works like a public to-do list. Each issue describes one open question and what would answer it. Comments on an issue record progress. When a question is answered, the issue is closed.
- **Get notified on GitHub.** If you have a free GitHub account, click the "Watch" button at the top of the repository page. Choose "All Activity" to be notified about every new issue and comment.
- **Follow changes in a news reader app.** GitHub records every change to the project's files. If you use a news reader app that accepts RSS or Atom feeds, add this address to follow those changes: https://github.com/PeterJemley/israel-judicial-review-threat-model/commits/main.atom
- **Look at dates in folder names.** A folder whose name includes a date, such as "coding-2026-10-22", holds work done on that day. New work goes into new folders, and older folders are kept as a record.

### Following the laws and the Court yourself

This project is not a news service. It is updated when the work is done, so it can be behind current events. To follow the Basic Laws and the Court directly, you can use the same sources the project uses:

- **Hebrew Wikisource** has the current text of each Basic Law, with a list of its changes, in Hebrew: https://he.wikisource.org
- **The Knesset's website** has the official laws and voting records: https://main.knesset.gov.il. It blocks automated requests, so this project reads the Knesset's open-data service instead, but you can open the site in a browser.
- **Open Knesset** is a volunteer project that copies the Knesset's public data on bills and votes: https://oknesset.org
- **Versa**, run by Cardozo School of Law, publishes English translations of many Israeli Supreme Court rulings: https://versa.cardozo.yu.edu
- **The published debate on Medina's article:** Rosen-Zvi and Yarom's reply ([free to read](https://doi.org/10.1093/icon/moag054)) and Medina's answer ([his blog post](https://www.iconnectblog.com/democratic-legitimacy-and-constitutional-identity-a-rejoinder/)).
- **The Israel Democracy Institute**, a Jerusalem think tank, publishes explanations in English of new Basic Laws and court rulings: https://en.idi.org.il

## How to use this repository to check the work

This section is for anyone who wants to read the argument closely, look at the data, check a single value, rerun the numbers, or report a mistake. Readers who want only to follow what the repository says, and how it changes, can use the section above instead. Reading needs only a web browser. Rerunning the numbers needs Python 3.9 or later and nothing else, because the scripts use only Python's standard library.

### Read the argument

1. Open [the note](medina-threat-conjecture-note.md). Read "The question", "Conjectures" and "Rivals" first. They say what is claimed, and what else could explain the same evidence. "Prior art" summarises the published reply to Medina and his answer.
2. Read "T1 as revised on 2026-10-22". T1 is the first test. It asks whether the warning signs that, according to Medina, the Court looks for predict how the Court ruled. The section fixed the rule for reading the result before any result was seen.
3. Read "What each outcome would teach" and "What this note does not claim". Nothing in the note is a finding yet.
4. The change log at the end of the note records every change of design, with its date and reason, as lettered items: (a), (b) and so on. Other files cite those letters, so the change log is where to look when a file says "under (ah)".

### Look at the data

The data are plain CSV files, one row per law.

- [codebook/m4-codebook.csv](codebook/m4-codebook.csv) holds the challenged laws that T1 tests.
- [codebook/comparison-sample.csv](codebook/comparison-sample.csv) holds 39 laws that were never challenged, coded the same way, for comparison.
- [research/frame/basic-law-frame.csv](research/frame/basic-law-frame.csv) lists every law titled Basic Law since 1958, 130 in all, and marks the ones challenged before the Court.

The files contain Hebrew and are saved as UTF-8. Double-clicking a file can garble the Hebrew, so open it this way:

- **Excel:** choose Data, then From Text/CSV, and set the file origin to UTF-8.
- **Google Sheets:** choose File, then Import, and upload the file.
- **Numbers on a Mac:** open the file directly.

Three rules for reading a row:

- **A blank cell is not a No.** It means no permitted source settled the value. Blanks are never filled in from what seems likely.
- **The provenance column says how each cell was settled.** "Agreed" means both coders gave the same value. "Adjudicated" means they differed and the adjudicator decided. "Both blank" means neither coder found a source. The situated_beneficiary cell names the circumstances reader, and any ruling that changed its value.
- **The codebook README explains every column.** Its section "How to read a row" walks through two rows in detail: see [codebook/README.md](codebook/README.md).

### Check a single value

Every value can be traced to the source it came from. As an example, take the 2015 budget extension, row 95 of the comparison sample, and its coalition_only cell, which reads Yes.

1. In codebook/comparison-sample.csv, find the row whose seq is 95. Its batch is 6 and its coded_seq is 95. Its provenance reads "coalition_only: agreed".
2. Open [research/coding-sample-2026-10-22/coder-A-b6.json](research/coding-sample-2026-10-22/coder-A-b6.json). Find the entry "95" and, inside it, "coalition_only". It gives the value, the source (here the Knesset's vote tables, vote 22148), a short quotation or data point that supports the value, and a note. The file coder-B-b6.json gives Coder B's version of the same cell.
3. Open the source and check that it says what the support says.

Where the provenance says "adjudicated", the ruling and its reasons are in the file adjudications-b6.json, using the row's batch number, in the same folder. Two columns tell you which files to open for a comparison-sample row. "batch" is the batch whose files hold the coding. "coded_seq" is the number the row is filed under. The two can differ: rows kept from the first draw keep that draw's numbering, so row 76 is filed in batch 2 under the number 70. The file [rows-redraw.json](research/coding-sample-2026-10-22/rows-redraw.json) lists this for all 39 rows. For the challenged laws in m4-codebook.csv, the coders' files are in [research/coding-2026-10-22](research/coding-2026-10-22/) and have no batch numbers.

### Rerun the numbers

These commands rebuild the data files from the coders' reports and run the test's checks. Once the repository is downloaded, they need no internet connection. On Windows, type `py` where the commands say `python3`.

1. Download the repository and move into its folder:

```bash
git clone https://github.com/PeterJemley/israel-judicial-review-threat-model.git
```

```bash
cd israel-judicial-review-threat-model
```

Without git, use the green Code button on the repository's GitHub page, choose Download ZIP, unzip it, and open a terminal in the unzipped folder.

2. Check that Python is 3.9 or later:

```bash
python3 --version
```

3. Make a folder for the output, so nothing in the repository is overwritten:

```bash
mkdir out
```

4. Rebuild the codebook of challenged laws from the coders' reports:

```bash
python3 analysis/assemble.py research/coding-2026-10-22 out/m4-codebook.csv
```

5. Rebuild the comparison sample:

```bash
python3 analysis/assemble_sample.py research/coding-sample-2026-10-22 out/comparison-sample.csv rows-redraw.json research/frame/basic-law-frame.csv
```

The script looks for `rows-redraw.json` inside the coding folder named first.

6. Check that the rebuilt files match the ones in the repository. `cmp` prints nothing when two files are identical. On Windows, use `fc /b` instead.

```bash
cmp codebook/m4-codebook.csv out/m4-codebook.csv
```

```bash
cmp codebook/comparison-sample.csv out/comparison-sample.csv
```

7. Rebuild the frame of every Basic Law and redraw the sample from it:

```bash
python3 analysis/build_frame.py research/frame out/basic-law-frame.csv --draw
```

It prints a summary that should read 130 rows, 14 challenged, 116 unchallenged and 39 sampled. The rebuilt file has only the frame's core columns. The committed frame also records the first draw and each row's verification, so compare the two files' sampled column, not the whole file.

8. Run the test's check on whether any result could be decisive:

```bash
python3 analysis/t1_revised.py detect 5 5 1 0
python3 analysis/t1_revised.py detect 6 6 2 0
```

The first line's four numbers come from the first run of T1, on the five of its nine laws that had every cell the test needs (four had a blank cell and were left out as uncoded), and the second's from the rows coded now, after the Incapacity amendment's coalition-only cell was filled on 4 November 2026 (change log (az)). In order, they are the rows in the test, the rows among them the Court ruled against, and two counts of the rows on which T1's two predictions disagree: those where the decision rule predicts an adverse ruling, and those where it predicts the opposite. The check prints "Inconclusive, declared before outcomes", which is the result recorded in [results.md](research/coding-2026-10-22/results.md).

9. Two more checks:

```bash
python3 analysis/t1_revised.py predict codebook/m4-codebook.csv
```

```bash
python3 analysis/t1_revised.py kappa research/coding-2026-10-22/coder-A.json research/coding-2026-10-22/coder-B.json
```

The first applies T1's prediction table to each row. The second measures how far the two coders agreed, variable by variable.

The first lines of each script in [analysis/](analysis/) say what it reads and what it writes.

### What the repository cannot do yet

- **Read the Knesset's main website automatically.** Its open-data service and specific gazette files can be read, but the main site shows a bot check, so bill pages and explanatory notes are read in a browser (issue 6). Votes come from the Knesset's open data and the Open Knesset mirror, both from October 2003 on. The script analysis/vote_extracts.py needs tables downloaded from that mirror, and its first lines say which.
- **Score most laws passed before October 2003.** Final-reading votes from before then rarely name the voters, so many rows have a blank coalition_only cell and cannot be scored.
- **Settle which values a law is measured against.** The scores measure distance from five democratic values. Rosen-Zvi and Yarom argue that Israel's constitution also includes laws on the Jewish side of its "Jewish and democratic" formula. The project records that dispute and has tested one alternative ([issue 33](https://github.com/PeterJemley/israel-judicial-review-threat-model/issues/33), exploratory). That alternative changes how the comparison sample looks, but not T1's result. The dispute itself the project cannot settle.
- **Measure public support.** Medina's account asks for "overwhelming political and public support" for some changes (page 702). The project counts votes in the Knesset only. The reply doubts a court can measure public support, and says Knesset votes alone cannot stand in for it (page 721).
- **Fully blind its coders.** The coders, readers and adjudicators were separate language-model agents, each given only its written sheet. Withholding documents does not remove what a model already knows. [results.md](research/coding-2026-10-22/results.md) sets out that limit.

### Report a mistake

Open an issue on GitHub. Name the file, the row (its seq or id), the column, the value you think is wrong, and the source that shows it, with what the source says. A source that refutes a value is as welcome as one that confirms it. Look at the open issues first: many cells already have an issue saying what would settle them. The issues labelled `verification` are the research queue.

## Status

Conjecture. Nothing in the note is a confirmed finding; two refutations are recorded, both exploratory (change log (ar)). T1 was run once, on 22 October 2026, on nine blind-recoded rows, and was inconclusive under its rule: one discordant row against a minimum of six. Because those rows shaped the rule, the run is exploratory (change log (as)). With the Incapacity amendment's coalition-only cell coded from the Knesset's roll call on 4 November 2026, two rows are discordant: still Inconclusive (change log (az)). T2 has been restated so that a move is judged by its aim, not only its target (change log (be)). The published reply to Medina by Rosen-Zvi and Yarom, and Medina's rejoinder, have been read and recorded; two of their points became exploratory issues, 33 and 34 (change log (bk)). Issue 33 has been run: under a widened reading of equality, the Jerusalem and Nation-State scores rise, and T1's result is unchanged (change log (bl)). The verdict was computed by code from the count of rows, the count of rulings against the law and the fixed predictions alone, not from which laws those were, although the person assembling the table had already seen them (change log (ab)). The other three tests are designs. Each revision is a commit; substantive changes are also logged in the note's change log with the date and reason.

## First in the queue

Issue 6, pinned: the Knesset's own records. Since 4 November 2026 the Knesset's open-data service and specific files on its file server can be read, and they settled the Incapacity amendment's roll call (issue 19) and the reading dates and tallies of issue 15. Two things remain: the main Knesset site shows a bot check to automated requests, so bill pages and explanatory notes are browser-only; and the vote data begin in October 2003, so the 1992 and 1969 roll calls, and those of the twenty sampled rows passed between 1959 and 2003, still need the Knesset record itself. The court-database checks on three sampled rows also remain, since the Supreme Court's site does not answer.

The rest of the research queue is the open issues labelled `verification` (as of 5 November 2026, issues 4, 8, 9, 11 to 14 and 22 besides issue 6: the unit, the comparison sample, judgments still unread, the Court's stated signs checked against the judgments, docket searches, tertiary sources to replace, and the question on the commencement default put to a scholar) and one discussion (issue 21). Closed since 25 October: issue 2 (Resler, change log (av)), issue 10 (the 2025 row, (bb)), issue 15 (reading dates and tallies, (ba)), issue 16 (descriptive columns, (bd)), issue 17 (what it means for the Court to have closed an instrument, (ar)), issue 19 (the Incapacity amendment's coalition-only cell, (az)), issue 20 (the frame's change counts, (bc)) and issue 23 (T2's target and aim, (be)). Each issue states the cells affected, the problem, the check, and the stopping rule.

## Criticism

Medina's article has drawn a published reply, set out in [The published reply to Medina, and his answer](#the-published-reply-to-medina-and-his-answer). Criticism of this project is welcome too: open an issue. A refutation is worth as much as a confirmation here, and the note says what would count as one for each conjecture.
