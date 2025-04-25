import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.stats.diagnostic import lilliefors
from statsmodels.stats.stattools import jarque_bera
from pyod.models.ecod import ECOD

def test_normality(data, label):
    if len(data) < 8:
        return pd.Series({
            'group': label,
            'n_samples': len(data),
            'shapiro_stat': np.nan,
            'shapiro_p': np.nan,
            'ks_stat': np.nan,
            'ks_p': np.nan,
            'ad_stat': np.nan,
            'ad_critical_values': np.nan,
            'dagostino_stat': np.nan,
            'dagostino_p': np.nan,
            'jarque_bera_stat': np.nan,
            'jarque_bera_p': np.nan,
            'skewness': np.nan,
            'kurtosis': np.nan,
            'lilliefors_stat': np.nan,
            'lilliefors_p': np.nan
        })

    results = {}
    results['group'] = label
    results['n_samples'] = len(data)
    
    # Shapiro-Wilk
    shapiro_stat, shapiro_p = stats.shapiro(data)
    results['shapiro_stat'] = shapiro_stat
    results['shapiro_p'] = shapiro_p
    
    # Kolmogorov-Smirnov
    ks_stat, ks_p = stats.kstest(data, 'norm', args=(data.mean(), data.std()))
    results['ks_stat'] = ks_stat
    results['ks_p'] = ks_p
    
    # Anderson-Darling
    ad_result = stats.anderson(data)
    results['ad_stat'] = ad_result.statistic
    results['ad_critical_values'] = str(ad_result.critical_values.tolist())
    
    # D'Agostino
    dag_stat, dag_p = stats.normaltest(data)
    results['dagostino_stat'] = dag_stat
    results['dagostino_p'] = dag_p
    
    # Jarque-Bera
    jb_stat, jb_p, jb_skew, jb_kurt = jarque_bera(data)
    results['jarque_bera_stat'] = jb_stat
    results['jarque_bera_p'] = jb_p
    results['skewness'] = jb_skew
    results['kurtosis'] = jb_kurt
    
    # Lilliefors
    lillie_stat, lillie_p = lilliefors(data)
    results['lilliefors_stat'] = lillie_stat
    results['lilliefors_p'] = lillie_p
    
    return pd.Series(results)

def detect_outliers(data, column, threshold=1.5):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, data[~data.index.isin(outliers.index)]

def detect_outliers_ecod(data, features, percentile=95):
    data_clean = data.dropna(subset=features)
    X = data_clean[features].values
    detector = ECOD()
    detector.fit(X)
    anomaly_scores = detector.decision_scores_
    threshold = np.percentile(anomaly_scores, percentile)
    outlier_flags = anomaly_scores > threshold
    filtered_data = data_clean[~outlier_flags]
    return filtered_data

# Lista para armazenar resultados
all_results = []

# Agrupamento e Testes
metrics = ['median_plv_diff', 'median_pli_diff', 'median_cf_plm_diff']
grouped_data = {
    'EEG_EEG': df[df['channel_group'] == 'EEG_EEG'],
    'EEG_ECG': df[df['channel_group'] == 'EEG_ECG']
}

for group, group_df in grouped_data.items():
    for metric in metrics:
        if metric not in group_df.columns:
            continue
            
        # Dados originais
        results = test_normality(group_df[metric].dropna(), 
                               f'{group}_{metric}_original')
        results['outlier_removal'] = 'none'
        all_results.append(results)
        
        # Após remoção IQR
        _, filtered_df = detect_outliers(group_df, metric)
        results = test_normality(filtered_df[metric].dropna(), 
                               f'{group}_{metric}_iqr')
        results['outlier_removal'] = 'iqr'
        all_results.append(results)
        
        # Após remoção ECOD
        filtered_group_df = detect_outliers_ecod(group_df, [metric], percentile=95)
        results = test_normality(filtered_group_df[metric].dropna(), 
                               f'{group}_{metric}_ecod')
        results['outlier_removal'] = 'ecod'
        all_results.append(results)

# Criar DataFrame com todos os resultados
results_df = pd.DataFrame(all_results)

# Salvar resultados
results_df.to_csv('normality_test_results.csv', index=False)

# Criar tabela formatada para LaTeX
latex_table = results_df.to_latex(
    float_format=lambda x: '{:.5f}'.format(x) if isinstance(x, (float, np.float64)) else str(x),
    index=False,
    escape=True
)

# Salvar tabela LaTeX
with open('normality_test_results.tex', 'w') as f:
    f.write(latex_table)