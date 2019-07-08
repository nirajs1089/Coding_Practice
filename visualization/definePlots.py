import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rc



def bar_graph(label,no_movies): #dim,measure
    # this is for plotting purpose
    index = np.arange(len(label))
    plt.bar(index, no_movies)
    plt.xlabel('Genre', fontsize=5)
    plt.ylabel('No of Movies', fontsize=5)
    plt.xticks(index, label, fontsize=5, rotation=30)
    plt.title('Market Share for Each Genre 1995-2017')
    plt.show()
    
    
def scatter_plot(srs_x,srs_y):
  plt.plot(srs_x,srs_y,color = 'black',marker = '.',linestyle = 'None')
  plt.show()


def stacked_bar_graph():
    
    # y-axis in bold
    rc('font', weight='bold')

    # Values of each group
    bars1 = [12, 28, 1, 8, 22]
    bars2 = [28, 7, 16, 4, 10]
    bars3 = [25, 3, 23, 25, 17]

    # Heights of bars1 + bars2
    bars = np.add(bars1, bars2).tolist()

    # The position of the bars on the x-axis
    r = [0,1,2,3,4]

    # Names of group and bar width
    names = ['A','B','C','D','E']
    barWidth = 1

    # Create brown bars
    plt.bar(r, bars1, color='#7f6d5f', edgecolor='white', width=barWidth)
    # Create green bars (middle), on top of the firs ones
    plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=barWidth)
    # Create green bars (top)
    plt.bar(r, bars3, bottom=bars, color='#2d7f5e', edgecolor='white', width=barWidth)

    # Custom X axis
    plt.xticks(r, names, fontweight='bold')
    plt.xlabel("group")

    # Show graphic
    plt.show()

def grouped_barplot(values,firstlevel_din,secondlevel_din): #side by side bars 

    # set width of bar
    dict_color = {0:'#7f6d5f',1:'#557f2d',2:'#2d7f5e'}

    barWidth = 0.25

    # Set position of bar on X axis
    pos_x = []
    pos_x.append(np.arange(len(values[0])))
    counter = 0

    for b in values:
        pos_x.append([x + barWidth for x in pos_x[counter]])
    counter += 1


    # Make the plot
    counter = 0
    for b in values:
        plt.bar(pos_x[counter], b, color=dict_color[counter], width=barWidth, edgecolor='white', label=secondlevel_din[counter])
        counter +=1


    # Add xticks on the middle of the group bars
    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(values[0]))],firstlevel_din,rotation=30,fontsize=6)

    # Create legend & Show graphic
    plt.legend()
    plt.show()
  

#----------bar_graph-----------------
label = ['A', 'B', 'C']
no_movies = [
    1,
    14,
    176]
    
bar_graph(label,no_movies) 
 
 
 #----------scatter_plot-----------------
srs_x = np.array([1,2,3,4,5])
srs_y = np.array([1,2,3,4,5])
 
 scatter_plot(srs_x,srs_y)

#------------grouped_barplot--------

values = [[12, 28, 1, 8, 22],
         [28, 7, 16, 4, 10]]

# stacked_bar_graph()
grouped_barplot(values, ['A', 'B', 'C', 'D', 'E'])
