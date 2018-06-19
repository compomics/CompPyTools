def CalcQval(df_in, decoy_col='Decoy', score_col='Score', better_score='higher', correct_pi_zero=True):
    if better_score == 'higher':
        sort_ascending = False
    elif better_score == 'lower':
        sort_ascending = True

    df = df_in.sort_values(score_col, ascending=sort_ascending)

    if correct_pi_zero:
        pi_zero_correction = df[decoy_col].value_counts()[False] / df[decoy_col].value_counts()[True]
    else:
        pi_zero_correction = 1

    df['Decoy CumSum'] = df[decoy_col].cumsum()
    df['Target CumSum'] = (~df[decoy_col]).cumsum()
    df['Qval'] = (df['Decoy CumSum'] / df['Target CumSum']) * pi_zero_correction

    return df['Qval'].sort_index()
