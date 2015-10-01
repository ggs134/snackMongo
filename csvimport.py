#-*- coding: utf-8 -*-

import csv
from pymongo import MongoClient

client = MongoClient('103.49.44.44',27017)
#client = MongoClient()
db = client.snack
postsCollection = db.posts
mainCollection = db.main
commentsCollection = db.comments
userCollection = db.users


def main():
    with open('nongsim.csv','r') as csvFile:
        reader = csv.reader(csvFile)
        for row in csv.reader(csvFile):
            nut_cont = listToNutDic(deliToList(row[2]))
            #data = {"snack_name" :row[1].decode('utf-8').encode('utf-8')}
            postsData={"snack_name" :row[1],"manufacturer":"농심","ingredient":nut_cont, "avr_grade":None, "comments": None}
            mainData={"manufacturer":"농심","snack_name":row[1], "avr_grade":None}
            userData = {"email": None, "password": None, "phone_number": None, "intruduction" : None, "nickname": None, "join_date":None, "Comments":None}
            commentsData = {"by":{"id": None, "nickname": None}, "text": None, "grade": None, "c_timestamp": None, "snack_name": None }
            
            postsCollection.insert(postsData)
            mainCollection.insert(mainData)

    userCollection.insert(userData)
    commentsCollection.insert(commentsData)


def arrToDic(arr):
    dic = {}
    for a in arr:
        dic[a]="null"
    return dic

def deliToList(deliStr):
    a=deliStr.split(',')
    return [value for value in a]

def listToNutDic(lists):
    return [{"ing_name":value , "ing_amount": None }for value in lists]

if __name__=="__main__":
    client.drop_database("snack")		
    main()
    print mainCollection.count()
    print commentsCollection.count()
    print userCollection.count()
    print postsCollection.count()
