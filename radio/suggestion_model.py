import scipy.spatial
import numpy as np
from db_controller import read_rating_database, form_rating_database, create_rating_database, rating_generator
import pprint


def cos_distance(weightMatrix, index):
    cosDist = list()
    for i in range(len(weightMatrix[:,0])):
        cosDist.append((i, scipy.spatial.distance.cosine(weightMatrix[index], weightMatrix[i])))
    return cosDist


def ratin_transformation(ratingList, similarityDict, percent=0.1):
    ratingListNew = list()
    for k in similarityDict.keys():
        sortedList = similarityDict[k][:int(len(similarityDict[k])*percent)] # 20%
        if sortedList:
            modifiedRating = np.array([0.0 for _ in ratingList[0]])
            for i in range(1, len(sortedList)):
                modifiedRating += np.array(ratingList[sortedList[i][0]])
            modifiedRating = modifiedRating/(len(sortedList)-1)
            print("#" * 30)
            print(ratingList[sortedList[0][0]])
            modifiedRating += np.array(ratingList[sortedList[0][0]])
            ratingListNew.append(list(modifiedRating))
        else:
            ratingListNew = ratingList
    return np.array(ratingListNew)


def data_analisation(ratingList):
    ratingList = np.array(ratingList)
    filesFame = list()
    similarityDict = dict()

    for i in range(len(ratingList[0])):
        filesFame.append(sum(ratingList[:,i]))

    filesFame = np.array(filesFame)/len(ratingList[:,0])
    print(filesFame)

    for j in range(len(ratingList[:, 0])):
        #similarityList.append((j, cos_distance(ratingList, j)))
        #similarityList.append([j, sorted(cos_distance(ratingList, j), key=lambda cosDist: cosDist[1])])
        similarityDict[j] = sorted(cos_distance(ratingList, j), key=lambda cosDist: cosDist[1])

    pprint.pprint(similarityDict)
    similarityList = ratin_transformation(ratingList, similarityDict)
    print(similarityList)

    return similarityList + filesFame


if __name__ == '__main__':
    #ratingList = np.array(rating_generator())
    ratingList, userIdList, itemIdList = read_rating_database()
    predictedWeight = data_analisation(ratingList)
    predictedRatingDatabase = form_rating_database(predictedWeight, userIdList, itemIdList)
    create_rating_database(predictedRatingDatabase, 'Predicted Rating Database.txt')
    pprint.pprint(predictedRatingDatabase)





