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
        [3.60, 3.00, 3.70, 4.70, 5.90, 2.70, 3.00],#torax rutina
        [10, 10, 10, 7, 13], #torax abdomen
        [3.70, 2.70, 4.60 , 4.60 , 4.60],# Nodulo Pulmonar
        [5.20, 8.30, 5.90, 11.50, ],## Angio aorta toracica
        [1.70, 0.80, 1.90, 1.90, 2.10, 1.60, 1.40]# # torax pedit
            ]
        #    [5, 5.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 7.4, 7.4],
        #    [3, 4.5, 5, 5, 5, 5, 6]


#      VCT
all_data1 = [

            [10, 10, 10, 15.86, 12, 15, 15, 15, 15],# torax rutina
            [16.1, 16.1, 16.1, 16.1, 19, 15], # torax abdomen
            [19.28, 19.28, 19.28, 15.40, 21],# Nódulo pulmonar
            [12.07, 12.07, 12.07, 12.07, 14.0, 11.5],# Angio aorta toracica
            [3.41, 3.41, 3.41, 3.41, 3.7, 2.9 ]# torax pedit

            ]

all_data2 = [

            [7.57, 8.41, 7, 7, 9],
            [7.92, 11, 7.91, 7.8, 7.5, 9.52, 7.39, 9.81],
            [-1],
            [-1],
            [1.14, 4, 2, 2],

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

axes.set_title('Tórax')
axes.set_ylim([0,21.5])

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
axes.axhline(y=12,c="hotpink",zorder=2, linestyle='-', linewidth=2)## ACR DIR
axes.axhline(y=10,c="orangered",zorder=2, linestyle='--', linewidth=2)## EU
# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
         xticklabels=['Tórax', 'Tórax\nAbdomen', 'Nódulo\nPulmonar', 'Angio Aorta\nToracica', 'Tórax\nPediátrico'])

#fig.savefig('ctdi_chest_levels.svg', format='svg')
plt.show()
