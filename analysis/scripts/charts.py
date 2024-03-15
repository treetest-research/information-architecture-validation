import matplotlib as mpl
import seaborn as sns
import statsmodels.api as sm
import pandas as pd
from IPython.display import HTML
import matplotlib.pyplot as plt

sns.set_style({'font.family':"sans-serif"})
sns.set_style('darkgrid')

# chart methods
def my_pie(data, group, title, ax=None, figsize=None):
    data.groupby([group]).size().plot.pie(
        title=title, ylabel='', 
        autopct=lambda p:'{:.1f}% ({:.0f})'.format(p, (p/100)*data.groupby([group]).size().sum()),
        figsize=figsize, ax=ax
    )

def my_bar(data, group, title, ax=None, figsize=(6, 5), order=None):
    if(not ax):
        _, ax_t = mpl.pyplot.subplots(figsize=figsize)
    ax_t = sns.countplot(y = group, data = data, order = order, ax=ax, legend=False)
    ax_t.bar_label(ax_t.containers[0])
    ax_t.set_title(title)

def my_bars(data, col, figSize=(20, 10), order=None):
    _, [[ax1, ax2, ax3], [ax4, ax5, ax6]] = plt.subplots(ncols=3, nrows=2, figsize=figSize)
    my_bar(data[data.variant == 'TP'], col, col + ' across variant 1 study', ax1, None, order)
    my_bar(data[data.variant == 'TC'], col, col + ' across variant 2 study', ax2, None, order)
    my_bar(data[data.variant == 'TO'], col, col + ' across variant 3 study', ax3, None, order)
    my_bar(data[data.variant == 'WTC'], col, col + ' across variant 4 study', ax4, None, order)
    my_bar(data[data.variant == 'WTCI'], col, col + ' across variant 5 study', ax5, None, order)
    my_bar(data[data.variant == 'WM'], col, col + ' across variant 6 study', ax6, None, order)

def my_hist_with_qq(data, column, title, xlabel, figsize=(15, 6)):
    fig, (ax1, ax2) = mpl.pyplot.subplots(ncols=2, figsize=figsize)
    data[column].plot.hist(title=title, ax=ax1)
    ax1.set_xlabel(xlabel)
    
    with mpl.rc_context():
        mpl.rc("figure", figsize=(3,3))
        sm.qqplot(data[column], line ='45', fit=True, ax=ax2)
