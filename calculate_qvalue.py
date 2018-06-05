def CalcQval(df_in, decoy_col='Decoy', score_col='Score', better_score='higher'):
    if better_score == 'higher':
        sort_ascending = False
    elif better_score == 'lower':
        sort_ascending = True

    df = df_in.sort_values(score_col, ascending=sort_ascending)
    df['Decoy CumSum'] = df[decoy_col].cumsum()
    df['Target CumSum'] = (~df[decoy_col]).cumsum()
    df['Qval'] = df['Decoy CumSum'] / df['Target CumSum']

    return df['Qval'].sort_index()
