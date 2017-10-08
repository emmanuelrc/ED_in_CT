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

        #    [5, 5.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 7.4, 7.4],
        #    [3, 4.5, 5, 5, 5, 5, 6]


#      VCT
all_data = [

        #    [2.3, 4, 1, 3.3, 3, 3, 3, 4.25, 2, 4, 5.6],
        #    [2, 3, 2.5, 2.5, 2.5, 2.5, 2.5, 4],
        #    [2, 4.5, 4, 4, 4, 4],
            [3.40+0.08, 3.41+0.08, 3.39+0.08],#RODILLA
        [3.40-0.04, 3.41-0.04, 3.39-0.04],#RODILLA
            [3.40-0.08, 3.41-0.08, 3.39-0.08],#RODILLA
            [3.40+0.06, 3.41+0.06, 3.39+0.06],#RODILLA
            [3.40, 3.41, 3.39],#RODILLA

            ]


all_data2 = [

            [-1],
            [-1],
            [-1],
            [-1],
            [-1]

            ]




all_data1 = [

        #    [2.3, 4, 1, 3.3, 3, 3, 3, 4.25, 2, 4, 5.6],
        #    [2, 3, 2.5, 2.5, 2.5, 2.5, 2.5, 4],
        #    [2, 4.5, 4, 4, 4, 4],
            [-1],
            [-1],
            [-1],
            [-1],
            [-1]

            ]

all_data3 = [

        #    [2.3, 4, 1, 3.3, 3, 3, 3, 4.25, 2, 4, 5.6],
        #    [2, 3, 2.5, 2.5, 2.5, 2.5, 2.5, 4],
        #    [2, 4.5, 4, 4, 4, 4],
            [183, 183+338, 183-338],#RODILLA
            [89, 89+141, 89-141],#CODO VOLUMEN
            [102, 102+105, 102-105],# ANGIO MMII
            [95, 95+124, 95-124],#HOMBRO
            [273, 273+222, 273-222]#MANO

            ]






# plot violin plot
# axes.violinplot(all_data,
#                    showmeans=False,points=100,
#                    showmedians=True)
#
# axes.violinplot(all_data1,
#                    showmeans=False,
#                    showmedians=True)
#
# axes.violinplot(all_data2,
#                   showmeans=False,
#                   showmedians=True)

axes.set_title('FluoroCT')


# plot box plot
axes.violinplot(all_data,
                    showmeans=False, points=2
                    )
axes.violinplot(all_data2,
                    showmeans=True, showextrema=False
                    )

axes.violinplot(all_data1,
                    showmeans=True, points=2, showextrema=False
                    )
# axes.violinplot(all_data3,
#                     showmeans=True, points=2,  widths=0.4, showextrema=False
#                     )



axes.set_title('FluoroCT')
axes.set_ylim([3,4])
# adding horizontal grid lines
#for ax in axes:
axes.yaxis.grid(True)
axes.set_xticks([y+1 for y in range(len(all_data))])
axes.set_xlabel('')
#axes.set_ylabel('CTDI$_{\mathrm{VOL}}$ (mGy$\cdot$cm)')
axes.set_ylabel('CTDI$_{\mathrm{VOL}}$ (mGy)')

# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
         xticklabels=['Ablación', 'Aspiración', 'Biopsia', 'Drenaje','Inyección'])


plt.show()
#fig.savefig('ctdi_fluo.svg', format='svg')
