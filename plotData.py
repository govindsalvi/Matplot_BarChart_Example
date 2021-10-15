import numpy as np
import os
import matplotlib.pyplot as plt
from BM1 import *
from BM2 import *
from BM3 import *
from BM4 import *
from BM5 import *

color = ['r', 'g', 'b', 'c', 'm', 'y']
AllData = {
    "BM1":  BM1,
    "BM2":  BM2,
    "BM3":  BM3,
    "BM4":  BM4,
    "BM5":  BM5
    }

Benchmark = AllData.keys()
predictor = BM1.keys()
graph = BM1["Traditional"].keys()
gTitle = ["Accuracy", "L2 Miss"]

def parseData():
    plotData = {}
    for tGraph in graph:
        bmData = {}
        for bm in Benchmark:
            data = {}
            for p in predictor:
                data[p] = AllData[bm][p][tGraph]
            bmData[bm] = data
        plotData[tGraph] = bmData
    return plotData


def makeBar(barWidth):
    bars = {}
    for index ,barName in enumerate(predictor):
        br = [i + index*barWidth for i in range(len(Benchmark))]
        bars[barName] = br
    return bars

def makeGraph(title, xlabel, ylabel, bars, barWidth, plotData):
    colorIndex = 0
    for barName, barLoc in bars.items():
        data = [plotData[bm][barName] for bm in Benchmark]
        plt.bar(barLoc, data, color = color[colorIndex], width = barWidth,edgecolor ='grey', label = barName)
        colorIndex += 1

    plt.xlabel(xlabel, fontweight ='bold', fontsize = 15)
    plt.ylabel(ylabel, fontweight ='bold', fontsize = 15)
    plt.title(title, fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(Benchmark))],Benchmark)
    plt.legend()
    plt.show()

def run(x, y, barWidth):
    plotData = parseData()
    bars = makeBar(barWidth)
    for index, gType in enumerate(graph):
        fig = plt.subplots(figsize =(x, y))
        makeGraph(gTitle[index], "Benchmark", gType, bars, barWidth, plotData[gType])

if __name__ == "__main__":
    run(10, 6, .10)



