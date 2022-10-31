from collections import defaultdict
from pathlib import Path
import logging

import pandas as pd


def constant_factory(value):
    return lambda: value


# (1,12,19,29,30,39,43,44)
# TODO: Use this if we need to specify types ever
MANUAL_TYPE_SPECS = defaultdict(default_factory=constant_factory("str")) | {
    "ID_Number": "str",
    "Political_Party": "str",
    "State": "str",
    "Dist1": "str",
    "Dist10": "str",
    "Dist13": "str",
    "Dist15": "str",
}

# TODO: find a parser that can parse these a lot faster
# it takes like a minute on my 5950X to parse all of these fields
DATE_FIELDS = [
    # 'Date_Of_Birth',
    # 'Date_Registered',
    # 'StatusChangeDate',
    # 'Date_Last_Changed',
    "Last_Date_Voted",
]


def read_csv(path: Path) -> pd.DataFrame:
    logging.info(f"Reading voter data from {path} with pandas")
    logging.info(f"Treating fields as dates: {DATE_FIELDS}")
    return pd.read_csv(
        path,
        sep="\t",
        header=0,
        encoding="ascii",
        encoding_errors="ignore",
        index_col="ID_Number",
        dtype="str",
        parse_dates=DATE_FIELDS,
    )


def load_enhanced_data(path: Path) -> pd.DataFrame:
    df = read_csv(path)
    return clean_and_enhance(df)


def clean_and_enhance(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Enhancing data to make it easier to work with")
    logging.info("-> Aliasing column Dist4 to MuniCode")
    df["MuniCode"] = df["Dist4"]
    return df
