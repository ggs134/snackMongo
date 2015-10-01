#-*- coding: utf-8 -*-

import csv
from pymongo import MongoClient

#Maro
#client = MongoClient('103.49.44.44',27017)
#local
client = MongoClient()
#Hwi
#client = MongoClient('52.69.236.246',27017)
db = client.snack
postsCollection = db.posts
mainCollection = db.main
commentsCollection = db.comments
userCollection = db.users


def main():
    with open('nongsim.csv','r') as csvFile:
        reader = csv.reader(csvFile)
        for row in csv.reader(csvFile):
            ing_cont = listToIngDic(deliToList(row[2]))
            #data = {"snack_name" :row[1].decode('utf-8').encode('utf-8')}
            postsData={"snack_name" :row[1],"manufacturer":"농심","nutrition": makeNutrition(row),"ingredient":ing_cont, "avr_grade":None, "comments": []}
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

def listToIngDic(lists):
    return [{"ing_name":value , "ing_amount": None , "ing_recommanded": None}for value in lists]

def makeNutrition(lst):
    lists=[]

    lists.append({"열량": lst[6]})
    lists.append({ "탄수화물": lst[7]})
    lists.append({"단백질": lst[8]})
    lists.append({"지방": lst[9]})
    lists.append({"당류" :lst[10]})
    lists.append({ "나트륨" : lst[11]})
    lists.append({"콜레스테롤" : lst[12]})
    lists.append({"포화지방산" :lst[13]})
    lists.append({"트렌스지방산" :lst[14]})
    lists.append({ "칼슙" :lst[15] })

    return lists
if __name__=="__main__":
    client.drop_database("snack")		
    main()
    print mainCollection.count()
    print commentsCollection.count()
    print userCollection.count()
    print postsCollection.count()
