"""
1. Add the current date to the text file today.txt as a string.
2. Read the text file today.txt into the string today_string
3. Parse the date from today_string.
4. List the files in your current directory
5. Create a list of all of the files in your parent directory (minimum five files should be available).
6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
7. Create a date object of your day of birth.
8. What day of the week was your day of birth?
9. When will you be (or when were you) 10,000 days old?
"""
import datetime
import os
from threading import *
from time import sleep
class basicassignment21:
    def question1(self):
        f = open("today.txt", "w")
        f.write(str(datetime.date.today()))
        f.close()
    def question2(self):
        f = open("today.txt", "r")
        today_string = f.read()
        return today_string
    def question3(self,d):
        date = datetime.datetime.strptime(str(d), "%Y-%m-%d").strftime("%d")
        return date
    def question4(self):
        return os.listdir()
    def question5(self):
        lists = basicassignment21().question4()
        return lists
    def question6(self):
        class p1(Thread):
            def run(self):
                time = datetime.datetime.now().strftime("%H:%M:%S")
                print(str(time))
        class p2(Thread):
            def run(self):
                time = datetime.datetime.now().strftime("%H:%M:%S")
                print(str(time))
        class p3(Thread):
            def run(self):
                time = datetime.datetime.now().strftime("%H:%M:%S")
                print(str(time))
        process1 = p1()
        process2 = p2()
        process3 = p3()
        return process1, process2, process3   
    def question7(self):
        class birth:
            def dob(self):
                return "1998-09-12"
        b = birth()
        return b.dob()
    def question8(self,d):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
        day = datetime.datetime.strptime(str(d), "%Y-%m-%d").weekday()
        return days[day]
    def question9(self,d,n):
        date = datetime.datetime.strptime(str(d), "%Y-%m-%d") + datetime.timedelta(days = n)
        return str(date)
    def __str__(self):
        return """
                1. Add the current date to the text file today.txt as a string.
                2. Read the text file today.txt into the string today_string
                3. Parse the date from today_string.
                4. List the files in your current directory
                5. Create a list of all of the files in your parent directory (minimum five files should be available).
                6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
                7. Create a date object of your day of birth.
                8. What day of the week was your day of birth?
                9. When will you be (or when were you) 10,000 days old?
                """

if __name__ == "__main__":
    a21 = basicassignment21()
    a21.question1()
    today_string = a21.question2()
    print("Question 2 : ", today_string)
    date = a21.question3(today_string)
    print("Question 3 : ", date)
    print("Question 4 :", a21.question4())
    print("Question 5 :", a21.question5())
    print("Question 6 :")
    p1, p2, p3 = a21.question6()
    p1.start()
    #sleep(2)
    p2.start()
    #sleep(3)
    p3.start()
    p1.join()
    p2.join()
    p3.join() #to make wait for main thread running.
    dob = a21.question7()
    print("Question 7 :", dob)
    birthday_Day = a21.question8(dob)
    print("Question 8 :", birthday_Day)
    print("Question 9 :", a21.question9(dob,10000))