# M4 codebook

One row per Basic Law enactment or amendment that reached the Israeli Supreme Court, coded on the six form indicators the Court uses to detect abuse of constituent power (Medina, 2026, pp. 699–700), plus opposition support, deviation tier and outcome.

Columns:

- `case`: short case or enactment name
- `year`: year of enactment
- `named_beneficiary`: who the amendment specifically served, or "No"
- `immediate_effect`: Yes, No (deferred or provisional), or blank
- `coalition_only`: Yes, No, or blank; notes in parentheses
- `expedited`: Yes, No, or blank
- `sweeping_scope`: Narrow, Provisional, Broad, Sweeping
- `litigation_timing`: whether enacted in response to or shortly before pending litigation
- `deviation_tier`: Entrenches, Limited, Near sharp, Sharp
- `outcome`: the Court's disposition
- `source`: where each row's values come from

A blank cell means not yet coded. Values taken from the article are cited by page. Values from other sources are cited by URL in the note's change log when added.

The first row is the must-match control: an enactment that should score low on every abuse indicator and be coded valid.
