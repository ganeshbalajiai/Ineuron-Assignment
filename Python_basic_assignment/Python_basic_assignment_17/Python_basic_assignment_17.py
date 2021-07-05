"""
1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.
2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.
3. Print the following values of the list [3, 2, 1, 0] using a for loop.
4. Use a list comprehension to make a list of the even numbers in range(10)
5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.
6. Construct the set odd from the odd numbers in the range using a set comprehension (10).
7. Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.
8. Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].
9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.
10. Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print 'Caught an oops'.
11. Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].
"""
class basicassignment_17:
    def question1(self, n):
        guess_me = n
        if guess_me == 7:
            return "equal to 7"
        elif guess_me > 7:
            return "too high"
        elif guess_me < 7:
            return "too low"
    def question2(self,n,s):
        if s>n:
            print("Oops")
        else:
            while s<n:
                print("too low")
                s+=1
                if s == n:
                    print("found it")
                    break
    def question3(self):
        l = []
        for i in range(3,-1,-1):
            l.append(i)
        return l
    def question4(self,n):
        l = [i for i in range(n)]
        return l
    def question5(self,n):
        d = {i : i*i for i in range(n)}
        return d
    def question6(self,n):
        s = {s for s in range(n) if s%2 != 0}
        return s
    def question7(self,n):
        return (i for i in range(10))
    def question8(self,n):
        def good(n):
            return n
        return good(n)
    def question9(self,n):
        return (i for i in range(10) if i%2 !=0)
    def question10(self):
        try:
            raise Exception("OopsException")
        except Exception as e:
            return ("Caught an oops!!", str(e))
    def question11(self,a,b):
        return {key : value for (key,value) in zip(a,b)}
    def __str__(self):
        return """
                1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.
                2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.
                3. Print the following values of the list [3, 2, 1, 0] using a for loop.
                4. Use a list comprehension to make a list of the even numbers in range(10)
                5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.
                6. Construct the set odd from the odd numbers in the range using a set comprehension (10).
                7. Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.
                8. Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].
                9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.
                10. Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print 'Caught an oops'.
                11. Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].
                """
if __name__ == "__main__":
    a17 = basicassignment_17()
    print("Question 1 :", a17.question1(7))
    print("Question 2 :")
    a17.question2(3,1)
    print("Question 3 : ", a17.question3())
    print("Question 4 : ", a17.question4(10))
    print("Question 5 : ", a17.question5(10))
    print("Question 6 : ", a17.question6(10))
    val = a17.question7(10)
    print("Question 7 : ")
    print(next(val))
    for i in val:
        print(i)
    print("Question 8 :", a17.question8(['Harry', 'Ron', 'Hermione']))
    get_odds = a17.question9(10)
    l = []
    for i in get_odds:
        l.append(i)
    print("Question 9 :", l[2])
    print("Question 10 :", a17.question10())    
    titles = ['Creature of Habit', 'Crewel Fate']
    plots = ['A nun turns into a monster', 'A haunted yarn shop']
    print("Question 11 :", a17.question11(titles,plots))

