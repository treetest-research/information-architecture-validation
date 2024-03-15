import pandas as pd, numpy as np
from scipy import stats
from itertools import combinations
from statsmodels.sandbox.stats.multicomp import multipletests
from scikit_posthocs import posthoc_dunn
from scipy.stats import f_oneway, tukey_hsd

# chi-squared test
def my_chi(data, columns, variant_column, variants, merge_index=False, merge_cols=False):
    
    # create named pairs and result dataframe
    named_pairs = [(a, b) for idx, a in enumerate(variants) for b in variants[idx + 1:]]
    results = pd.DataFrame(columns=['Property', 'Significant', 'p', 'Chi2', 'v', 'd', 'n'] + 
        [str(x[0])+'__'+str(x[1]) for x in named_pairs])
    
    # iterate over all columns
    for column in columns:
        counts = data[data[variant_column].isin(variants)].groupby([column, variant_column]).size().unstack().fillna(0)
        
        # merge some column values together if defined
        if(merge_index):
            for index in merge_index:
                for index2 in merge_index[index]:
                    counts.loc[index] = counts.loc[index] + counts.loc[index2]
                    counts = counts.drop(axis=0, index=[index2])

        # merge some variants together if defined    
        if(merge_cols):
            for col in merge_cols:
                for col2 in merge_cols[col]:
                    counts.loc[:, col] = counts.loc[:, col] + counts.loc[:, col2]
                    counts = counts.drop(axis=1, columns=[col2])

        # calculate the chi squared test
        stat, p, d, exp = stats.chi2_contingency(counts)
        n = counts.sum().sum()
        
        # post hoc tests
        post_hoc = [np.nan for x in range(len(named_pairs))]

        try:
            if(p < 0.05):
                p_vals = []
                for comb in named_pairs:
                    new_df = counts[[comb[0], comb[1]]]
                    _, p_temp, _, _ = stats.chi2_contingency(new_df)
                    p_vals.append(p_temp)
                with np.errstate(divide='ignore'):
                    _, corrected_p_vals = multipletests(p_vals, method='fdr_tsbky')[:2]
                post_hoc = corrected_p_vals
        except:
            pass
        
        # append to dataframe
        results.loc[len(results.index)] = [item for sublist in [[
            column, 
            p < 0.05,
            '< .001' if p <= 0.001 else str(np.round(p, 4)), 
            np.round(stat, 4),
            np.round(np.sqrt(stat*stat/(n*d)), 4), 
            d,
            n,
        ], post_hoc] for item in sublist]
    return results

def my_mann(data, columns, sample_column, sample_names):
    results = pd.DataFrame(columns=['Property', 'U', 'z', 'p', 'r', 'significant'])
    for column in columns:
        samples = [data[data[sample_column] == sample_name][column].dropna().values for sample_name in sample_names]
        if(len(samples[0]) == 0 or len(samples[1]) == 0):
            continue
        stat, p = stats.mannwhitneyu(*samples)
        nx = len(data[data[sample_column] == sample_names[0]][column])
        ny = len(data[data[sample_column] == sample_names[1]][column])
        z = (stat - nx*ny/2 + 0.5) / np.sqrt(nx*ny * (nx + ny + 1)/ 12)
        eff = z/np.sqrt(nx+ny)
        results.loc[len(results.index)] = [
            column, 
            np.round(stat, 4), 
            np.round(z, 4), 
            '< .001' if p <= 0.001 else str(np.round(p, 4)), 
            np.round(eff, 4), 
            p < 0.05
        ]
    return results

def my_kruskal(data, columns, sample_column, sample_names):
    pairs = [(a, b) for idx, a in enumerate([x for x in range(len(sample_names))]) for b in [x for x in range(len(sample_names))][idx + 1:]]
    named_pairs = [(a, b) for idx, a in enumerate(sample_names) for b in sample_names[idx + 1:]]
    posthoc_columns = [str(x[0])+'__'+str(x[1]) for x in named_pairs]
    results = pd.DataFrame(columns=['feature', 'significant', 'p', 'H', 'eta', 'd', 'n'] + posthoc_columns)                   
    for column in columns:
        samples = [data[data[sample_column] == sample_name][column].values for sample_name in sample_names]
        stat, p = stats.kruskal(*samples)
        post_hoc = [None for x in range(len(named_pairs))]
        n = len(np.concatenate([x for x in samples]))
        k = len(samples)
        if(p < 0.05):
            post_hoc = posthoc_dunn(samples)
            post_hoc = ['< .001' if post_hoc.iloc[x[0],x[1]] <= 0.001 else str(np.round(post_hoc.iloc[x[0],x[1]], 4)) for x in pairs]
        results.loc[len(results.index)] = [item for sublist in [[
            column, 
            p < 0.05,
            '< .001' if p <= 0.001 else str(np.round(p, 4)), 
            np.round(stat, 4), 
            str(np.round((stat - k + 1)/(n - k), 4)),
            k - 1,
            n
        ], post_hoc] for item in sublist]
    return results

def my_anova(data, columns, sample_column, sample_names):
    pairs = [(a, b) for idx, a in enumerate([x for x in range(len(sample_names))]) for b in [x for x in range(len(sample_names))][idx + 1:]]
    named_pairs = [(a, b) for idx, a in enumerate(sample_names) for b in sample_names[idx + 1:]]
    posthoc_columns = [str(x[0])+'__'+str(x[1]) for x in named_pairs]
    results = pd.DataFrame(columns=['feature', 'p', 'F', 'significant', 'n', 'd'] + posthoc_columns)                   
    for column in columns:
        samples = [data[data[sample_column] == sample_name][column] for sample_name in sample_names]
        stat, p = f_oneway(*samples)
        post_hoc = [None for x in range(len(named_pairs))]
        if(p < 0.05):
            post_hoc = tukey_hsd(*samples)
            post_hoc = ['< .001' if post_hoc.pvalue[x[0]][x[1]] <= 0.001 else str(np.round(post_hoc.pvalue[x[0]][x[1]], 3)) for x in pairs]
        results.loc[len(results.index)] = [item for sublist in [[
            column, 
            '< .001' if p <= 0.001 else str(np.round(p, 4)), 
            np.round(stat, 4), 
            p < 0.05,
            len(np.concatenate([x for x in samples])),
            len(samples) - 1
        ], post_hoc] for item in sublist]
    return results