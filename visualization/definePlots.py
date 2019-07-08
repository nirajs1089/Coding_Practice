import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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
