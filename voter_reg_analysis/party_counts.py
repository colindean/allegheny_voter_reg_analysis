#!/usr/bin/env python3
from pathlib import Path

import sys

from .commons.dates import beginning_of_eight_years_ago
from .pandas.loader import load_enhanced_data
from .pandas.facts_and_filters import (
    only_wilkinsburg,
    only_active_voters,
    only_party,
    PoliticalParty,
    not_parties,
)


def party_counts():

    # headers on, ascii tab separated file with some encoding errors expected
    all_voters = load_enhanced_data(Path(sys.argv[1]))
    wilkinsburg_voters = only_wilkinsburg(all_voters)
    wilkinsburg_active = only_active_voters(
        wilkinsburg_voters, start_of_active=beginning_of_eight_years_ago()
    )

    dems = only_party(wilkinsburg_active, PoliticalParty.Democrat)
    reps = only_party(wilkinsburg_active, PoliticalParty.Republican)
    third_party = not_parties(
        wilkinsburg_active, [PoliticalParty.Democrat, PoliticalParty.Republican]
    )

    tpcounts = (
        third_party.groupby(["Political_Party"], sort=False)
        .size()
        .reset_index(name="counts")
    )
    tpcounts_sorted = tpcounts.sort_values(by=["counts"], ascending=False)

    print(
        {
            "total": len(wilkinsburg_voters),
            "total active": len(wilkinsburg_active),
            "dems": len(dems),
            "reps": len(reps),
            "third_party": len(third_party),
            "3p%": 100 * (float(len(third_party)) / float(len(wilkinsburg_active))),
            "third_party_counts": tpcounts_sorted.to_json(orient="records"),
        }
    )


if __name__ == "__main__":
    party_counts()
