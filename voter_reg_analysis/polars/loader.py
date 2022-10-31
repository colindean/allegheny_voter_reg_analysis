from collections import defaultdict
from pathlib import Path
import logging

import polars as pl


def read_csv(path: Path) -> pl.DataFrame:
    logging.info(f"Reading voter data from {path} with polars")
    return pl.read_csv(
        path,
        has_header=True,
        sep="\t",
        parse_dates=False,
        dtype={"House__": str, "CustomData1": str, "Zip_Code": str},
        # ignore_errors=True
    ).with_column(
        pl.col("Last_Date_Voted")
        .str.strptime(pl.Date, "%-m/%-d/%Y", strict=False)
        .alias("Last_Date_Voted")
    )


def load_enhanced_data(path: Path) -> pl.DataFrame:
    df = read_csv(path)
    return clean_and_enhance(df)


def clean_and_enhance(df: pl.DataFrame) -> pl.DataFrame:
    return df.rename({"Dist4": "MuniCode"})
