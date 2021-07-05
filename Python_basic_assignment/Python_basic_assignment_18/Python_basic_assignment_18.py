
from collections import OrderedDict, defaultdict
from zoo import zoo as menageria
import zoo
class basicassignment_18:
    def question1_2(self):
        z = menageria()
        val = z.hours()
        return val
    def question3_4(self):
        z = zoo.zoo()
        info = z.hours()
        return info
    def question5(self,d):
        d = dict(d)
        return d
    def question6(self,d):
        d = OrderedDict(d)
        return d
    def question7(self):
        dict_of_lists = defaultdict()
        l = [dict_of_lists,]
        l[0]['a'] = []
        l[0]['a'].append("something for a")
        return dict_of_lists['a']
    def __str__(self):
        return """
                1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.
                2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
                3. Using the interpreter, explicitly import and call the hours() function from zoo.
                4. Import the hours() function as info and call it.
                5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.
                6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?
                7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].
                """
if __name__ == "__main__":
    a18 = basicassignment_18()
    print("Question 1 and 2: ", a18.question1_2())
    print("Question 3 and 4: ", a18.question3_4())
    d = {'a': 1, 'b': 2,'c': 3}
    print("Question 5:", a18.question5(d))
    print("Question 6:", a18.question6(d))
    # dict prints the values in key,value pairs
    # ordereddict prints the value in list of tuples
    print("Question 7:", a18.question7())


