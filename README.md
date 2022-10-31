# Allegheny County Voter Registration Analysis Tools

This is a collection of programs for generating reports given the
semi-annual data dumps of voter registration data from the
Allegheny County Elections Division.

## How to contribute

This is not seriously developed or maintained.
It's a side project used for learning some data science tooling.

You'll need a Python -- anything 3.10 or newer will do.

Install `pipenv` with:

    pip install -U pipenv

Then install the dependencies with

    pipenv sync --dev

Then you can run individual modules in the `voter_reg_analysis` module with:

    pipenv run voter_reg_analysis.<module> VOTERS.TXT

where `VOTERS.TXT` is one of the TSV files provided by ACED.

## Notes on data

You can request the data from the Allegheny County elections division.
The data is not permitted to be distributed freely available online because it
contains personally identifiable information on voters.
While that information is considered public record, the wide availability of that
information is considered bad thing.

You may need to convert data from ASCII to UTF-8 to use some of these programs.

    iconv -c -f ascii -t utf8 VOTERS.TXT -o VOTERS-utf8.txt

Pandas-using programs are more tolerant of ASCII-format data but the
world has moved on to UTF-8, and the Polars programs can use only it.
