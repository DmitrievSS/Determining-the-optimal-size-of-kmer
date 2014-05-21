import random
import math
from matplotlib.colors import ListedColormap
import pylab as pl

__author__ = 'serg'


class kNN():
    def __init__(self):
        self.data = []
        self.min_kmer = 20
        self.new_data = []
        self.number_of_classes = 20
        self.k = 5
        with open("DATA", "r") as file_data:
            for line in file_data:
                line = line.split(' ')
                self.data.append([map(lambda x: int(x), line[:-1]), int(line[-1])])


    def showData(self):
        classColormap = ListedColormap(['#FF0000', '#00FF00', '#FFFFFF', '#000000',
                                        '#AA0000'])
        pl.scatter([self.data[i][0][0] for i in range(len(self.data))],
                   [self.data[i][0][3] for i in range(len(self.data))],
                   c=[self.data[i][1] for i in range(len(self.data))],
                   cmap=classColormap)
        pl.show()

    def separate(self, testPercent):
        trainData = []
        testData  = []
        for row in self.data:
            if random.random() < testPercent:
                testData.append(row)
            else:
                trainData.append(row)
        return trainData, testData

    def dist(self, x, y):
        return reduce(lambda a, b: math.sqrt(a*a+b*b), map(lambda i, j: i - j, x, y))

    def classifyKNN(self, point):
        testLabels = []
        #Claculate distances between test point and all of the train points
        testDist = [[self.dist(point, i[0]), i[1]] for i in self.data]
        #How many points of each class among nearest K
        stat = [0 for i in range(self.number_of_classes)]
        for d in sorted(testDist)[0:self.k]:
            stat[d[1]-self.min_kmer] += 1

        #Assign a class with the most number of occurences among K nearest neighbours
        t = sorted(zip(stat, range(self.number_of_classes)), reverse=True)
        # print t
        return t[0][1] + self.min_kmer



test = kNN()
test.showData()
print test.classifyKNN([10000000, 89, 90, 26])