__author__ = "Ralf Gabriels"
__copyright__ = "CompOmics 2018"
__license__ = "Apache License, Version 2.0"


import pandas as pd


def calculate_qvalues(df_in, decoy_col='Decoy', score_col='Score',
                      lower_score_is_better=False, correct_pi_zero=True):
    """
    Calculate q-values using the Target-Decoy Approach.

    Positional arguments:
    df_in -- pandas.DataFrame object containing at least the following columns:
    1. Search engine scores, as int or float
    2. Booleans for every search engine score: True if the score corresponds to
    a decoy, False if the score corresponds to a target.

    Keyword arguments:
    score_col -- String with the column name for the search engine scores
    (default: 'Score')
    decoy_col -- String with the column name for the decoy booleans
    (default: 'Decoy')
    lower_score_is_better -- True if a lower search engine score is better.
    (default: False)
    correct_pi_zero -- True of correction for pi-zero should be performed.
    Pi-zero correction is necessary if the a priori change of matching a decoy
    peptide is not equal to matching a target peptide. This happens, for
    instance, if the target library is not the same size as the decoy library.
    (default: True)

    Returns:
    A pandas.Series with the calculated q-values, sorted by the original index.
    """

    df = df_in.sort_values(score_col, ascending=lower_score_is_better)

    if correct_pi_zero:
        pi_zero_correction = df[decoy_col].value_counts()[False] / df[decoy_col].value_counts()[True]
    else:
        pi_zero_correction = 1

    df['Decoy CumSum'] = df[decoy_col].cumsum()
    df['Target CumSum'] = (~df[decoy_col]).cumsum()
    df['Qval'] = (df['Decoy CumSum'] / df['Target CumSum']) * pi_zero_correction

    return df['Qval'].sort_index()
