"""
===================================
Box plot vs. violin plot comparison
===================================

Note that although violin plots are closely related to Tukey's (1977)
box plots, they add useful information such as the distribution of the
sample data (density trace).

By default, box plots show data points outside 1.5 * the inter-quartile
range as outliers above or below the whiskers whereas violin plots show
the whole range of the data.

A good general reference on boxplots and their history can be found
here: http://vita.had.co.nz/papers/boxplots.pdf

Violin plots require matplotlib >= 1.4.

For more information on violin plots, the scikit-learn docs have a great
section: http://scikit-learn.org/stable/modules/density.html
"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(figsize=(5.5, 4))



#   AQUILLION ONE
all_data = [

        #    [2.3, 4, 1, 3.3, 3, 3, 3, 4.25, 2, 4, 5.6],
        #    [2, 3, 2.5, 2.5, 2.5, 2.5, 2.5, 4],
        #    [2, 4.5, 4, 4, 4, 4],
            [4.30, 4.60, 4.10, 4.30, 5.5, 3.7],# cuello
            [5.20, 5, 4, 5.20, 4.5, 4.6, 5.20], # Columna cervical
            [4.30, 4.60, 4.10, 4.10, 4.30, 4.30, 4.10, 5.8, 3.5],# cuello torax
            [5.20, 4.60, 4.50, 4.80, 4.10, 4.90, 4.60, 9.00, 17.10, 4.90, 6.30, 4.30],# Cuello torax abdomen
            [2.5, 6.8, 14.50, 3.00, 2.3]# Via Aerea
            ]
        #    [5, 5.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 7.4, 7.4],
        #    [3, 4.5, 5, 5, 5, 5, 6]


#      VCT
all_data1 = [

            [9.20, 8.51, 11.66, 10.27, 12.42, 10.67, 10.73],# cuello
            [5.20+1, 5+1, 4+1, 5.20+2, 4.5+2, 4.6+1, 5.20+1], # Columna cervical
            [6.71, 6.71, 6.71, 6.71, 7.5, 4.8],# cuello torax
            [19.22, 19.22, 19.22, 19.22, 20, 15],# Cuello torax abdomen
            [8.83, 8.83, 8.83, 9, 7, 12]# Via Aerea

            ]

all_data2 = [

            [7.5, 8, 8, 8.81, 9, 8.76],
            [-1],
            [-1],
            [-1],
            [-1]

            ]





# plot violin plot
axes.violinplot(all_data,
                   showmeans=False,points=100,
                   showmedians=True)

axes.violinplot(all_data1,
                   showmeans=False,
                   showmedians=True)
#
axes.violinplot(all_data2,
                   showmeans=False,
                   showmedians=True)

axes.set_title('Cuello')
axes.set_ylim([1.5,21])

# plot box plot
#axes[1].boxplot(all_data)
#axes[1].set_title('box plot')

# adding horizontal grid lines
#for ax in axes:
axes.yaxis.grid(True)
axes.set_xticks([y+1 for y in range(len(all_data))])
axes.set_xlabel('')
axes.axhline(y=19,c="hotpink",zorder=2, linestyle='-', linewidth=2)## ACR DIR
#axes.axhline(y=60,c="indianred",zorder=2, linestyle='-.', linewidth=1.6)## EU
#axes.set_ylabel('CTDI$_{\mathrm{VOL}}$ (mGy$\cdot$cm)')
#axes.set_ylabel('CTDI$_{\mathrm{VOL}}$ (mGy)')

# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
         xticklabels=['Cuello', 'Columna\nCervical', 'Cuello\nTórax', 'Cuello Tórax\nAbdomen', 'Vía\nAerea'])

fig.savefig('ctdi_neck.svg', format='svg')
plt.show()
