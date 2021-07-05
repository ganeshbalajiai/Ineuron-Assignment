import sqlite3
import pandas as pd
import redis
class basicassignment_20:
    def question1(self,t1):
        t1 = t1
        global f
        f = open("test.txt", "w")
        f.write(t1)
        f.close()
        return f
    def question2(self):
        f = open("test.txt", "r")
        f.seek(0)
        l = f.read()
        return l
    def question3(self,val):
        f = open("book.csv", "w")
        f.write(val)
        f.close()
    def question4(self,db,tablename,fields):
        global con
        con = sqlite3.connect(db)
        cursor = con.cursor()
        cursor.execute("create table if not exists " + tablename + "(" + fields + ")")
        return con
    def question5(self,tablename):
        f = pd.read_csv("book.csv")
        f.to_sql(tablename, con, if_exists = "replace", index = False)
    def question6(self,tablename,cname):
        cursor = con.cursor()
        cursor = cursor.execute("select " + cname + " from " + tablename)
        l = []
        for i in cursor:
            l.append(i[0])
        return l
    def question7(self,tablename):
        cursor = con.cursor()
        cursor = cursor.execute("select * from " + tablename)
        l = []
        for i in cursor:
            l.append(i)
        return l
    def question8(self,dbname):
        con = sqlite3.connect(dbname)
        return con
    def question9(self,hashName):
        redisClient = redis.StrictRedis(host='localhost',port=6379,db=0)
        redisClient.hset(hashName, 1, "Fester Bestertester")
        val = redisClient.hgetall(hashName)
        return val
    def question10(self,hashName):
        redisClient = redis.StrictRedis(host='localhost',port=6379,db=0)
        redisClient.hincrby(hashName, key = "Fester Bestertester", amount = 2 )
        val = redisClient.hgetall(hashName)
        return val
    def __init__(self):
        return """
                1. Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.
                2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?
                3. Create a CSV file called books.csv by using these lines:
                title,author,year
                The Weirdstone of Brisingamen,Alan Garner,1960
                Perdido Street Station,China Miéville,2000
                Thud!,Terry Pratchett,2005
                The Spellman Files,Lisa Lutz,2007
                Small Gods,Terry Pratchett,1992
                4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).
                5. Read books.csv and insert its data into the book table.
                6. Select and print the title column from the book table in alphabetical order.
                7. From the book table, select and print all columns in the order of publication.
                8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.
                9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.
                10. Increment the count field of test and print it.
                """
if __name__ == "__main__":
    a20 = basicassignment_20()
    t1 = 'This is a test of the emergency text system,'
    q = a20.question1(t1)
    f = a20.question2()
    print(t1,f) #both prints the same text.
    val = """title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992"""
    a20.question3(val)
    cursor = a20.question4("books.db", "books", "title text, author text,year integer")
    a20.question5("books")
    titles = a20.question6("books", "title")
    titles.sort(reverse= False)
    print("Question 6: ", titles)
    val = a20.question7("books")
    def myfunc(e):
        return e[2]
    val.sort(key = myfunc, reverse = True)
    print("Question 7:", val)
    print("Question 8:", a20.question8("books"))
    val = a20.question9("test")
    print(val)
    val = a20.question10("test")
    print(val)