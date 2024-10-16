import operator
import pandas as pd
import numpy as np
from scipy import spatial

def ComputeDistance(a, b):
    dataA = a[1]
    dataB = b[1]

    AttributeDistance = spatial.distance.cosine(dataA, dataB)

    return AttributeDistance

def getNeighbors(carID, K):

    distances = []
    for car in carDict:
        if (car != carID):
            dist = ComputeDistance(carDict[carID], carDict[car])
            distances.append((car, dist))
    distances.sort(key=operator.itemgetter(1))

    neighbors = []
    for x in range(K):
        neighbors.append((distances[x][0], distances[x][1]))

    return neighbors

# load dataset CSV file
pd_df = pd.read_csv('datacar_dataset.jason')

pd_df0 = pd_df.iloc[:, [0, 2]]

pd_df1 = pd_df.iloc[:, [3, 4, 5, 6, 7, 8]]

pd_df1 = pd.get_dummies(pd_df1)

pd_df2 = pd.concat([pd_df0, pd_df1], axis=1, sort=False)

df_array = pd_df2.to_numpy()


carDict = {}

for d in df_array:
    carID = int(d[0])
    name = d[1]
    attributes = d[2:]
    attributes = map(int, attributes)
    carDict[carID] = (name, np.array(list(attributes)))

K = 10
selectedID = 5

print("selected car:", carDict[selectedID][0])

neighbors = getNeighbors(selectedID, K)

for neighbor in neighbors:
    print(str(neighbor[0]) + " | " + carDict[neighbor[0]][0] + " | " + str(neighbor[1]))