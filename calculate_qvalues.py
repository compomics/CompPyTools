__author__ = "Ralf Gabriels"
__copyright__ = "CompOmics, VIB-UGent Center for Medical Biotechnology"
__license__ = "Apache License, Version 2.0"


def calculate_qvalues(df_in, decoy_col='decoy', score_col='score',
                      lower_score_is_better=False):
    """
    Calculate q-values using the Target-Decoy Approach.

    Positional arguments:
    df_in -- pandas.DataFrame object containing at least the following columns:
    1. Search engine scores, as int or float
    2. Booleans for every search engine score: True if the score corresponds to
    a decoy, False if the score corresponds to a target.

    Keyword arguments:
    score_col -- String with the column name for the search engine scores
    (default: 'score')
    decoy_col -- String with the column name for the decoy booleans
    (default: 'decoy')
    lower_score_is_better -- True if a lower search engine score is better.
    (default: False)

    More info: Aggarwal,S. and Yadav,A. (2015) In Statistical Analysis in
    Proteomics. https://doi.org/10.1007/978-1-4939-3106-4_7, Chapter 3.1,
    Formulae 1 and 3.

    Returns:
    A Pandas Series with the calculated q-values, sorted by the original index.
    """

    df = df_in.sort_values(score_col, ascending=lower_score_is_better)

    df['decoy_cumsum'] = df[decoy_col].cumsum()
    df['target_cumsum'] = (~df[decoy_col]).cumsum()
    df['q_value'] = (df['decoy_cumsum'] / df['target_cumsum'])

    return df['q_value'].sort_index()
