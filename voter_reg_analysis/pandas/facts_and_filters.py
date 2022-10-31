import datetime
from enum import Enum
from typing import List
import logging

import pandas

WILKINSBURG_MUNICODE = "MN228"
EXPECTED_ELECTION_TYPES_FROM_COLUMN_NAME = ["GN", "PR", "SP"]


class PoliticalParty(Enum):
    Democrat = "D"
    Republican = "R"
    NotAffiliated = "NF"
    Independent = "I"
    NoAffiliation = "NO"
    NonAffiliated = "NON"
    Other = "OTH"
    Libertarian = "LN"
    Green = "GR"


def only_wilkinsburg(df: pandas.DataFrame) -> pandas.DataFrame:
    logging.info(f"Selecting only Wilkinsburg voters ({WILKINSBURG_MUNICODE})")
    return df[df.MuniCode == WILKINSBURG_MUNICODE]


def only_active_voters(
    df: pandas.DataFrame, start_of_active: datetime.datetime
) -> pandas.DataFrame:
    logging.info(f"Selecting voters who've voted since {start_of_active.date()}")
    return df[
        pandas.to_datetime(df["Last_Date_Voted"]) > pandas.to_datetime(start_of_active)
    ]


def only_party(
    df: pandas.DataFrame, party_shortcode: PoliticalParty
) -> pandas.DataFrame:
    logging.info(f"Selecting voters who are {party_shortcode}")
    return df[df["Political_Party"] == party_shortcode.value]


def not_parties(
    df: pandas.DataFrame, party_shortcodes: List[PoliticalParty]
) -> pandas.DataFrame:
    names = list(map(lambda x: x.name, party_shortcodes))
    letters = list(map(lambda x: x.value, party_shortcodes))
    logging.info(f"Selecting voters who are not {names}")

    return df[~df["Political_Party"].isin(letters)]


def election_columns(df: pandas.DataFrame) -> List[str]:
    logging.info("Finding elections for which this data has participation records")
    # get the columns that begin with a marker indicating they are election participation columns
    # but not the Voting Method columns
    return list(
        filter(
            lambda x: (x[0:2] in EXPECTED_ELECTION_TYPES_FROM_COLUMN_NAME)
            and (x[-2:] != "VM"),
            df.columns,
        )
    )


def count_of_notna(df: pandas.DataFrame, column: str) -> int:
    logging.info(f"Counting the number of non-absent values in column {column}")
    return df[df[column].notna()][column].count()
