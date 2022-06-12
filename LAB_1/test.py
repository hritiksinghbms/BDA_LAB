from pymongo import MongoClient

# creation of MongoClient
#client=MongoClient(
client = MongoClient('localhost', 27017)
mydatabase = client['gfg']
mycollection=mydatabase['student']



print("Hey there!")
while True:
    print()
    print()
    print("This is python script to add and retrive data from db")
    print('1. Add data')
    print('2. Retrive all data')
    print('3. Exit')
    ch = int(input())
    if ch == 1:
        name = input("Enter name:")
        usn = input("Enter usn:")
        record = mycollection.insert_one(
            {
                'name': name,
                'usn': usn
            }
        )
        print()
        print('Inserted data')
        print()
    if ch == 2:
        cursor = mycollection.find()
        for record in cursor:
            print()
            print(record)
        print()
        print()
    if ch==3:
        print("Ok bye!")
        quit()