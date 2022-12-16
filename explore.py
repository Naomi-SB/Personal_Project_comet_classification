import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats


def orbit_type_by_peri_year(train):
    HYP = train[train.orbit == 'HYP']
    PAR = train[train.orbit == 'PAR']
    
    sns.set()
    plt.figure(figsize = (20, 8))
    
    plt.subplot(221)
    plt.hist(HYP['time_of_peri'])
    plt.title("hyperbolic by perihelion year")
    
    plt.subplot(222)
    plt.hist(PAR['time_of_peri'])
    plt.title("parabolic by perihelion year")
    
    plt.show()
    
def orbit_type_by_node(train):
    HYP = train[train.orbit == 'HYP']
    PAR = train[train.orbit == 'PAR']
    
    sns.set()
    plt.figure(figsize = (20, 8))
    
    plt.subplot(221)
    plt.hist(HYP['node'])
    plt.title("hyperbolic by node degree")
    
    plt.subplot(222)
    plt.hist(PAR['time_of_peri'])
    plt.title("parabolic by node degree")
    
    plt.show()
    
def orbit_type_by_distance(train):
    HYP = train[train.orbit == 'HYP']
    PAR = train[train.orbit == 'PAR']
    
    sns.set()
    plt.figure(figsize = (20, 8))
    
    plt.subplot(221)
    plt.hist(HYP['peri_distance'])
    plt.title("hyperbolic by perihelion distance")
    
    plt.subplot(222)
    plt.hist(PAR['peri_distance'])
    plt.title("parabolic by perihelion distance")
    
    plt.show()    
    
def orbit_type_by_peri(train):
    HYP = train[train.orbit == 'HYP']
    PAR = train[train.orbit == 'PAR']
    
    sns.set()
    plt.figure(figsize = (20, 8))
    
    plt.subplot(221)
    plt.hist(HYP['perihelion'])
    plt.title("hyperbolic by perihelion degree")
    
    plt.subplot(222)
    plt.hist(PAR['perihelion'])
    plt.title("parabolic by perihelion degree")
    
    plt.show()
    
def display_stat(df):
    num_cols = ['peri_distance','inclination','node', 'perihelion', 'time_of_peri', 'days_of_data_arc']
    stuff = []
    for col in num_cols:
        mean = df[col].mean()
        std = df[col].std()
        skew = df[col].skew()
        kurtosis = df[col].kurtosis()
        
        output = {
            "Feature": col,
            "Mean": mean,
            "Standard Deviation":std,
            "Skew":skew,
            "Sharpness":kurtosis
        }
        stuff.append(output)
        
    stat_display = pd.DataFrame(stuff)
    return stat_display
        
        
def Mann_Whitney_stats(train):

    HYP = train[train.orbit == 'HYP']
    PAR = train[train.orbit == 'PAR']
    cont_cols = ['peri_distance', 'inclination', 'node', 'perihelion', 'time_of_peri', 'days_of_data_arc']
    stuff = []
    for col in cont_cols:
        stat, p = stats.mannwhitneyu(HYP[col], PAR[col], method="asymptotic")
        output = {
            "Feature": col,
            "t-stat": stat,
            "p-value": p
        }

        stuff.append(output)

    df_stat = pd.DataFrame(stuff)
    return df_stat



















