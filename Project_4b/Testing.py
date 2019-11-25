from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle
from math import pow, sqrt
from XOR import buildExamplesFromXORData

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData()
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

xorData = buildExamplesFromXORData()
def testXORData(hiddenLayers = [10]):
    return buildNeuralNet(xorData,maxItr = 200,hiddenLayerList = hiddenLayers)

def analysisQ5Pen():
    print("\nQ5 Pen Data Test")
    penData = []
    for i in range(5):
        penData += [testPenData()[1]]
        print "Pen Data Max: ", max(penData)
        print "Pen Data Avg: ", average(penData)
        print "Pen Data SD: ", stDeviation(penData)

def analysisQ5Car():
    print("\nQ5 Car Data Test")
    carData = []
    for i in range(5):
        carData += [testCarData()[1]]
        print "Car Data Max: ", max(carData)
        print "Car Data Avg: ", average(carData)
        print "Car Data SD: ", stDeviation(carData)

def analysisQ6():
    perceptrons = 0
    print "\nANALYSIS Q6"
    print "Pen Data Test"
    while perceptrons < 41:
        penData = []
        for i in range (0,5):
            penData.append(testPenData(hiddenLayers=[perceptrons])[1])
        print "Perceptrons: ", perceptrons
        print "Pen Data Max: ", max(penData)
        print "Pen Data Avg: ", average(penData)
        print "Pen Data SD: ", stDeviation(penData)
        perceptrons += 5

    perceptrons = 0
    print "\nCar Data Test"
    while perceptrons < 41:
        carData = []
        for i in range (0,5):
            carData.append(testCarData(hiddenLayers=[perceptrons])[1])
        print "Perceptrons: ", perceptrons
        print "Car Data Max: ", max(carData)
        print "Car Data Avg: ", average(carData)
        print "Car Data SD: ", stDeviation(carData)
        perceptrons += 5

def analysisQ7():
    print "\n XOR Test"
    tempMax = 0.0;
    xorData = []
    perceptrons = 0
    while tempMax < 1:
        for i in range (5):
            xorData.append(testXORData(hiddenLayers=[perceptrons])[1])
        print "Perceptrons: ", perceptrons
        print "XOR Data Max: ", max(xorData)
        print "XOR Data Avg: ", average(xorData)
        print "XOR Data SD: ", stDeviation(xorData)
        tempMax = max(xorData)
        perceptrons +=1

# analysisQ5Pen()
# analysisQ5Car()
# analysisQ6()
analysisQ7()
