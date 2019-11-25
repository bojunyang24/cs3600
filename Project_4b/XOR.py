import random
from NeuralNetUtil import getList

def getNNXorData(fileString="datasets/xordata.txt", limit=100000):
    examples = []
    attrValues = {}
    data = open(fileString)
    attrs = ['A', 'B']
    attr_values = [['0', '1'], ['0', '1']]

    attrNNList = [('A', {'0' : getList(1,2), '1' : getList(2,2)}),
                 ('B', {'0' : getList(1,2), '1' : getList(2,2)})]

    classNNList = {'0': [1, 0], '1': [0, 1]}

    for index in range(len(attrs)):
        attrValues[attrs[index]] = attrNNList[index][1]
    for line in data:
        inVec = []
        outVec = []
        count = 0
        for val in line.split(','):
            if count == 2:
                outVec = classNNList[val.strip()]
            else:
                inVec.append(attrValues[attrs[count]][val])
            count+=1
        examples.append((inVec, outVec))
    random.shuffle(examples)
    return examples

def buildExamplesFromXORData(size=4):
    xorData = getNNXorData()
    XORDataTrainList = []
    for cdRec in xorData:
        tmpInVec = []
        for cdInRec in cdRec[0]:
            for val in cdInRec:
                tmpInVec.append(val)
        tmpList = [tmpInVec, cdRec[1]]
        XORDataTrainList.append(tmpList)
    XORDataTestList = XORDataTrainList[-size:]
    #XORDataTrainList = xorDataTrainList[:-size]
    return XORDataTrainList, XORDataTestList
