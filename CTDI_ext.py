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
            [6.00, 8.50, 8.50, 8.50, 8.50, 8.50, 9.50],#RODILLA
            [4.60, 5.40, 4.70, 4.80, 4.80, 4.80, 3.90, 7.60, 5.20, 5.20],#CODO VOLUMEN
            [4.10, 6.60, 6.00, 6.60, 6.30, 6.00, 7.30],# ANGIO MMII
            [16.40, 16.40, 16.40, 16.40, 16.40, 17.20, 18, 15 ],#HOMBRO
            [5.60, 7.60, 7.60, 7.60, 7.60, 7.60, 7.60, 7.60, 7.60, 7.60, 7.60, 7.00, 7.00, 7.00, 9.00,  7.80]#MANO

            ]
        #    [5, 5.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 7.4, 7.4],
        #    [3, 4.5, 5, 5, 5, 5, 6]


#      VCT
all_data1 = [

            [7.81, 9.81, 9.81, 9.81, 9.81, 9.81, 9.81, 9.81, 13.08, 13.08],#RODILLA
            [15.82, 15.82, 15.82, 15.82, 19.30, 16.30, 16.30, 11.00, 15.00, 15.00],#CODO
            [5.55, 7.55, 6.90, 7.55, 7.55, 7.55, 10.90 ],# ANGIO MMII
            [17.15, 19.34, 19.15, 19.15, 25.51, 19.15, 19.15, 19.67],#HOMBRO
            [20.70, 20.72, 20.72, 27.97, 20.72, 20.72, 20.72, 20.72, 12.77, 25.23]#MANO

            ]

all_data2 = [

            [7.51, 7.51, 7, 6, 10],
            [4.51, 6, 4, 4, 3],
            [3.55, 4, 5+1, 2+2],
            [-1],
            [3.31, 5, 6, 4, 4]

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

axes.set_title('Extremidades')
axes.set_ylim([3,29])

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

# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
         xticklabels=['Rodilla', 'Codo', 'Femur', 'Hombro','Mano\nMuñeca'])

#fig.savefig('ext_levels.svg', format='svg')
plt.show()
