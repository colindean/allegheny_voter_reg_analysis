#!/usr/bin/env python3
import itertools
from pathlib import Path

import sys

from .commons.dates import beginning_of_eight_years_ago
from .polars.loader import load_enhanced_data
from .polars.facts_and_filters import (
    only_wilkinsburg,
    only_active_voters,
    election_columns,
    count_of_notna,
)


def run():

    # headers on, ascii tab separated file with some encoding errors expected
    all_voters = load_enhanced_data(Path(sys.argv[1]))
    wilkinsburg_voters = only_wilkinsburg(all_voters)
    wilkinsburg_active = only_active_voters(
        wilkinsburg_voters, start_of_active=beginning_of_eight_years_ago()
    )

    # import code;
    # code.interact(local=dict(globals(), **locals()))

    elections = election_columns(wilkinsburg_active)
    election_counts = {
        election: count_of_notna(wilkinsburg_active, election) for election in elections
    }

    types = {}
    for key, group in itertools.groupby(election_counts, lambda e: e[0:2]):
        group = list(group)[0]
        if not types.get(key):
            types[key] = {}
        types[key] |= {group: election_counts[group]}

    print(
        {
            "total": len(wilkinsburg_voters),
            "total active": len(wilkinsburg_active),
            "counts per election": election_counts,
            "counts per election per type": types,
        }
    )


if __name__ == "__main__":
    run()
