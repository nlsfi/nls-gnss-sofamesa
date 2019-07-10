def define_table3_df(np, pd, all_table1s, all_table2s, table3_df, weights):
    weights = weights.apply(lambda x: round(x * 100, 3))
    i = 1
    j = 1
    k = 1
    l = 2
    column_names = list(all_table1s.columns.values)
    n = 1
    columns_length = all_table1s.shape[1]
    while i < columns_length:
        column_name = column_names[n]
        table3_df['{}'.format(column_name)] = [round(float(all_table1s.iloc[2, j].split('%')[0]), 2),                                                         round(float(all_table1s.iloc[16, j].split('%')[0]), 2),                                                         round(float(all_table1s.iloc[18, j].split('%')[0]), 2),                                                         all_table1s.iloc[27, j],                                                         all_table1s.iloc[29, j],                                                         all_table2s.iloc[0, k],                                                         all_table2s.iloc[1, k],                                                         all_table2s.iloc[0, l],                                                         all_table2s.iloc[1, l],                                                         all_table2s.iloc[4, k],                                                         all_table2s.iloc[5, k],                                                         all_table2s.iloc[6, k]]
        i += 1
        j += 1
        k += 2
        l += 2
        n += 1
    table3_df['Weighing %'] = [weights.iloc[0, 0], weights.iloc[1, 0], weights.iloc[2, 0], weights.iloc[3, 0], weights.iloc[4, 0], weights.iloc[5, 0], weights.iloc[6, 0], weights.iloc[7, 0], weights.iloc[8, 0], weights.iloc[9, 0], weights.iloc[10, 0], weights.iloc[11, 0]] 
    return table3_df