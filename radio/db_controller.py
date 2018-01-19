import numpy as np
import random
import pprint
import json
import ast

FILES_NUMBER = 10

def  rating_generator(userIdList=[1]):
    possibleValues = [-1, -0.5]*2 + [i/10 for i in range(1, 11)] + [float(0) for _ in range(50)]
    ratingList = list()

    for _ in userIdList:
        ratingList.append(random.choice(possibleValues) for _ in range(FILES_NUMBER))
        #ratingList.append((id, zip([i for i in range(FILES_NUMBER)], [random.choice(possibleValues) for _ in range(FILES_NUMBER)])))
    itemIdList = [i for i in range(FILES_NUMBER)]
    return ratingList, userIdList, itemIdList


def form_rating_database(ratingList, userIdList, itemIdList):
    '''
    Database = {
        'users': [{
            'user_id': 0,
            'items': [{
                'item_id': 1,
                'mark': 0.5
            }]
        }]
    }
    '''
    users = list()
    for user in zip(userIdList, ratingList):
        items = list()
        for item in zip(itemIdList, user[1]):
            items.append({'item_id': item[0],
                          'mark': item[1]})
        users.append({'user_id': user[0],
                      'items': items})
    return {'users': users}


def create_rating_database(rating, ratingPath='Rating Database.txt'):
    with open(ratingPath, 'w') as out:
        out.write(json.dumps(rating))


def add_rating_database(ratingList, ratingPath='Rating Database.txt'):
    with open(ratingPath, 'a') as out:
        for row in ratingList:
            out.write(row)


def like(user_id, item_id, step=1.0):
    with open('Rating Database.txt', 'r', encoding='UTF-8') as ratingDatabase:
        ratingDict = json.loads(ratingDatabase.read())
    for user in ratingDict['users']:
        if user['user_id'] == user_id:
            for item in user['items']:
                if item['item_id'] == item_id:
                    item['mark'] += step
    with open('Rating Database.txt', 'w') as ratingDatabase:
        ratingDatabase.write(json.dumps(ratingDict))


def dislike(user_id, item_id, step=-0.5):
    with open('Rating Database.txt', 'r', encoding='UTF-8') as ratingDatabase:
        ratingDict = json.loads(ratingDatabase.read())
    for user in ratingDict['users']:
        if user['user_id'] == user_id:
            for item in user['items']:
                if item['item_id'] == item_id:
                    item['mark'] += step
    with open('Rating Database.txt', 'w') as ratingDatabase:
        ratingDatabase.write(json.dumps(ratingDict))


def listened(user_id, item_id, step=0.1):
    with open('Rating Database.txt', 'r', encoding='UTF-8') as ratingDatabase:
        ratingDict = json.loads(ratingDatabase.read())
    for user in ratingDict['users']:
        if user['user_id'] == user_id:
            for item in user['items']:
                if item['item_id'] == item_id:
                    item['mark'] += step
    with open('Rating Database.txt', 'w') as ratingDatabase:
        ratingDatabase.write(json.dumps(ratingDict))
    for user in ratingDict['users']:
        if user['user_id'] == user_id:
            for item in user['items']:
                if item['item_id'] == item_id:
                    item['mark'] += step


def read_rating_database(path='Rating Database.txt'):
    userIdList = list()
    itemIdList = list()
    ratingList = list()
    with open(path, 'r', encoding='UTF-8') as ratingDatabase:
        ratingDict = json.loads(ratingDatabase.read())
    for item in ratingDict['users'][0]['items']:
        itemIdList.append(item['item_id'])
    for user in ratingDict['users']:
        userIdList.append(user['user_id'])
        itemsList = list()
        for item in user['items']:
            itemsList.append(item['mark'])
        ratingList.append(itemsList)
    return ratingList, userIdList, itemIdList


def get_recommendations(user_id, path='Predicted Rating Database.txt'):
    itemList = list()
    with open(path, 'r', encoding='UTF-8') as ratingDatabase:
        ratingDict = json.loads(ratingDatabase.read())
    for user in ratingDict['users']:
        if user['user_id'] == user_id:
            for item in user['items']:
                itemList.append((item['item_id'], item['mark']))
    itemList = filter(lambda x: x[1]>= 0, sorted(itemList, key=lambda itemList: -itemList[1]))
    return itemList


if __name__ == '__main__':
    #ratingList = rating_generator([1, 2, 3, 4])

    #rating = form_rating_database(ratingList)
    #create_rating_database(rating)
    #ratingList, userIdList, itemIdList = read_rating_database()
    #form_rating_database(ratingList, userIdList, itemIdList)

    recomendation = get_recommendations(3)
    for i in recomendation:
        print(i)
    #like(1, 1)
    #dislike(1, 1)
    #listened(1, 1)
    #like(user_id, audio_id)
    #listened(user_id, audio_id)
    #dislike(user_id, audio_id)
    #get_recommendations(user_id)