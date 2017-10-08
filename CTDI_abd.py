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
        [4.60, 5.60, 4.70, 6.5],# trifassico higado
        [4.10, 4.60, 11.00, 5.00, 12.50, 6.40, 4.90, 5.90, 7.30, 6.30, 4.50], # UroTAC
        [4.60, 4.60, 4.60, 4.90, 4.90, 7, 8],# abdomen
        [7, 7, 6.5, 8],# dinamic pancreas
        [4.70, 5.00, 6.00, 4.80, 6.80 ]# pelvis
            ]
        #    [5, 5.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 7.4, 7.4],
        #    [3, 4.5, 5, 5, 5, 5, 6]


#      VCT
all_data1 = [

            [6.78, 5.83, 11.19, 9, 9, 9, 9, 9, 10.64, 11.63, 8.60, 5.54],# trifassico higado
            [18.67-2, 16.13, 14.71, 11.11, 12.53, 13.86, 10.31, 16.40, 14.08, 18.46-2, 15.91, 17.30, 9.05], # UroTAC sin contraste 2
            [10, 10, 10, 14, 14],# abdomen
            [8.17, 8.17, 8.17, 10.47, 7],# dinamic pancreas
        [4.70+4, 5.00+2, 6.00+2, 4.80+1, 6.80+4 ]# pelvis

            ]

all_data2 = [

            [-1],
            [16.57, 13.21, 10.23, 9, 9, 9, 9],
            [-1],
            [-1],
            [-1]

            ]





# plot violin plot
axes.violinplot(all_data,
                   showmeans=False, points=100,
                   showmedians=True)

axes.violinplot(all_data1,
                   showmeans=False,
                   showmedians=True)
#
axes.violinplot(all_data2,
                   showmeans=False,
                   showmedians=True)

axes.set_title('Abdomen')
axes.set_ylim([3,17.7])

# plot box plot
#axes[1].boxplot(all_data)
#axes[1].set_title('box plot')

# adding horizontal grid lines
#for ax in axes:
axes.yaxis.grid(True)
axes.set_xticks([y+1 for y in range(len(all_data))])
axes.set_xlabel('')
axes.axhline(y=15,c="hotpink",zorder=0, linestyle='-', linewidth=2)## ACR DIR
axes.axhline(y=25,c="orangered",zorder=2, linestyle='--', linewidth=2)## EU
axes.set_ylabel('CTDI$_{\mathrm{VOL}}$ (mGy)')

# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
         xticklabels=['Trifasico\nHígado', 'UroTAC', 'Abdomen', 'Dinámico\nPáncreas', 'Pélvis'])

#fig.savefig('ctdi_abd_levels.svg', format='svg')
plt.show()
