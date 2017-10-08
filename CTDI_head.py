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
        [47.50, 47.50, 47.50, 47.50, 47.50, 47.50, 80.00, 53.70, 43.00, ],#CRANEO
        [38.00, 42.20, 47.50, 38.00, 38.00, 38.00], #CRANEO PEDIATRICO
        [36.10, 36.10, 36.10, 38.10, 72.10, 54.10],# OIDOS
        [20.40, 20.40, 20.40, 22.90, 22.90, 22.90, 22.90, 22.90, 13.70],#SPN
        [47.50, 47.50, 47.50, 47.50, 47.50, 54.0, 42.0]#Craneo con contraste
            ]
        #    [5, 5.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 7.4, 7.4],
        #    [3, 4.5, 5, 5, 5, 5, 6]


#      VCT
all_data1 = [

            [86.75, 96.05,  96.05,  96.05,  96.05,  96.05, 99.0 ],# CRANEO
            [58.49, 35.19, 58.49, 58.49, 58.49, 58.49, 58.49, 61.5], # CRANEO PEDIATRICO
            [112.29, 83.55, 112.29, 112.29, 112.29, 112.29,   ],# OIDOS
            [24.87, 24.87, 24.87, 24.87, 29.4, 30.4, 22.90],# SPN
            [96.05, 95.05, 96.05, 90.0, 99.0, ]# Craneo con contraste

            ]

all_data2 = [

            [38.83, 38.83, 38.83, 47, 33],
            [-1],
            [64, 60, 60, 60, 50, 70],
            [10.11, 9.93, 9.58, 15, 19, 17, 17],
            [-1],

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

axes.set_title('Cabeza')
axes.set_ylim([6,120])

# plot box plot
#axes[1].boxplot(all_data)
#axes[1].set_title('box plot')

# adding horizontal grid lines
#for ax in axes:
axes.yaxis.grid(True)
axes.set_xticks([y+1 for y in range(len(all_data))])
axes.set_xlabel('')
#axes.set_ylabel('CTDI$_{\mathrm{VOL}}$ (mGy$\cdot$cm)')
axes.set_ylabel('CTDI$_{\mathrm{VOL}}$ (mGy)')
axes.axhline(y=56,c="hotpink",zorder=0, linestyle='-', linewidth=2)## ACR DIR
axes.axhline(y=60,c="orangered",zorder=2, linestyle='--', linewidth=2)## EU
# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
         xticklabels=['Craneo\nAdulto', 'Craneo \n Pediátrico', 'Oidos', 'SPN', 'Craneo con\n Contraste'])

fig.savefig('ctdi_head_levels.svg', format='svg')
plt.show()


#fig.savefig('ctdi_head.svg', format='svg')
