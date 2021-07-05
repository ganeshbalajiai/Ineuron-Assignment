import random
class programbasic1:
    def question1(self):
        return "Hello Python"
    def question2(self,a,b):
        def add(a,b):
            return a+b
        def div(a,b):
            return a/b
        return add(a,b), div(a,b)
    def question3(self,b,h):
        area_of_triangle = (1/2)*b*h
        return area_of_triangle
    def question4(self,a,b):
        return b,a
    def question5(self):
        return random.random()
    def __str__(self):
        return """
                1.	Write a Python program to print "Hello Python"?
                2.	Write a Python program to do arithmetical operations addition and division.?
                3.	Write a Python program to find the area of a triangle?
                4.	Write a Python program to swap two variables?
                5.	Write a Python program to generate a random number?
                """
if __name__ == "__main__":
    a1 = programbasic1()
    print("Question 1:", a1.question1())
    add,div = a1.question2(4,10)
    print("Question 2 : ", add,div)
    print("Question 3 : ", a1.question3(5,10))
    a,b = a1.question4(1,2)
    print("Question 4 : a = {}, b = {}".format(a,b))
    print("Question 5 : ", a1.question5())
