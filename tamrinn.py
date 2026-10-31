import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import axvline


# tamrin 1 : line plot
def plot_line(x, y, title):
    # first set fig and ax
    fig, ax = plt.subplots(figsize=(10,8))
    # seconde: plot
    ax.plot(x,
            y,
            color="red",
            linestyle="--",
            linewidth=5,
    )
    # set title and grid
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    plt.show()
# create x and y
x_values = [1,5,6,9,8,25,29,35,45,50]
y_values = [3,6,14,25,42,20,31,15,24,21]
"""plot_line(x_values,y_values, "tamrin 1")"""


# tmrin 2 :scatter plotter
class ScatterPlot:
    # first: create init def
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # seconde:create  def plot
    def plot(self, color= "blue", size= 30):
        plt.scatter(self.x, self.y, color=color, s=size)
    # third :create another def, to add labels
    def add_labels(self, x_label, y_label, title):
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
# forth : create data
data_x = [5,3,9,2,4]
data_y = [10,24,5,15,18]
scaterr = ScatterPlot(data_x, data_y)
scaterr.plot()
scaterr.add_labels("mv", "ly", "ai")
"""plt.show()"""


# tamrin 3:bar plot
# first create parent class
class BaseChart:
    def show(self):
        plt.show()
# seconde create child class
class BarChart(BaseChart):
    # third : create init def
    def __int__(self, x, y):
        self.x = x
        self.y = y
    # forth : create def plot
    def plot(self):
        plt.bar(self.x, self.y)
        plt.xlabel("category")
        plt.ylabel("value")
# fifth : create value and category
cat = ['benz', 'bmw', 'Lamborghini', 'lancer', 'gtr']
val = [300000, 250000, 350000, 150000, 200000]

ba = BarChart(cat,val)
ba.plot()
ba.show()


# tamrin 4: histogram

def plot_histogram(data, bins = 10, color = "green"):
    # first set fig and ax
    fig, ax = plt.subplots(figsize=(10, 8))
    # seconde: plot histogram
    ax.hist(data,
            bins = bins,
            color = color,
            density=True
            )
    # loc and std
    axvline(100,color="red")
    ax.set_title("std")
    #set y and x
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.show()

# create data
data_1 = np.random.normal(
    loc = 100,
    scale = 10,
    size = 1000
)
"""plot_histogram(data_1)"""


# tamrin 5: boxplot
def plot_boxplot(data, labels):
    # first set plot
    plt.subplots(figsize=(10, 8))
    # seconde: boxplot
    plt.boxplot(data,
               tick_labels=labels,
               patch_artist=True,
               flierprops=dict(marker='o', markersize=10,markerfacecolor='red'),
               )
    # set title
    plt.title("boxplot")
    plt.grid(True)
    plt.show()

# create data
data_2 = [
    [1,20,5,7,9],
    [2,4,30,8,10],
    [5,7,4,2,12],
]
labels_1 = ["d1", "d2", "d3"]
"""plot_boxplot(data_2, labels_1)"""