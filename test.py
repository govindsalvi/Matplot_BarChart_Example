import numpy as np
import os
import matplotlib.pyplot as plt
from plotData import *
data = plotData



# Accuracy = {
#     "BM1":{
#         "Traditional": 10,
#         "AnyStore":20,
#         "LS":30,
#         "Anystore Replay" : 40,
#         "LS Replay": 50
#     },
#     "BM2":{
#         "Traditional": 10,
#         "AnyStore":20,
#         "LS":30,
#         "Anystore Replay" : 40,
#         "LS Replay": 50
#     },
#     "BM3":{
#         "Traditional": 10,
#         "AnyStore":20,
#         "LS":30,
#         "Anystore Replay" : 40,
#         "LS Replay": 50
#     },
#     "BM4":{
#         "Traditional": 10,
#         "AnyStore":20,
#         "LS":30,
#         "Anystore Replay" : 40,
#         "LS Replay": 50
#     },
#     "BM5":{
#         "Traditional": 10,
#         "AnyStore":20,
#         "LS":30,
#         "Anystore Replay" : 40,
#         "LS Replay": 50
#     }
# }

# L2Miss = {
#     "BM1":{
#         "Traditional": 10,
#         "AnyStore":20,
#         "LS":30,
#         "Anystore Replay" : 40,
#         "LS Replay": 50
#     },
#     "BM2":{
#         "Traditional": 10,
#         "AnyStore":20,
#         "LS":30,
#         "Anystore Replay" : 40,
#         "LS Replay": 50
#     },
#     "BM3":{
#         "Traditional": 10,
#         "AnyStore":20,
#         "LS":30,
#         "Anystore Replay" : 40,
#         "LS Replay": 50
#     },
#     "BM4":{
#         "Traditional": 10,
#         "AnyStore":20,
#         "LS":30,
#         "Anystore Replay" : 40,
#         "LS Replay": 50
#     },
#     "BM5":{
#         "Traditional": 10,
#         "AnyStore":20,
#         "LS":30,
#         "Anystore Replay" : 40,
#         "LS Replay": 50
#     }
# }


# data = {
#     "Accuracy":Accuracy,
#     "L2 Miss":L2Miss
   
# }

# data  = plotData



bars = {}

for index ,barName in enumerate(predictor):
    br = [i + index*barWidth for i in range(len(Benchmark))]
    bars[barName] = br

for gType in graph:
    fig = plt.subplots(figsize =(20, 10))
    for index, barName in enumerate(bars.keys()):
        nData = []
        for bm, bmv in data[gType].items():
            nData.append(bmv[barName])
        plt.bar(bars[barName], nData, color = color[index], width = barWidth,edgecolor ='grey', label = barName)
   
    plt.xlabel('Benchmark', fontweight ='bold', fontsize = 15)
    plt.ylabel(gType, fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(Benchmark))],Benchmark)
    plt.legend()
    plt.savefig(os.path.join('plots', gType + '.pdf'))  
    # plt.show()