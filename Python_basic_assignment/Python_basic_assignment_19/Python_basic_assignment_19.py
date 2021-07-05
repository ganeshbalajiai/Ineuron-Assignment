

class basicassignment_19:
    def question1(self):
        class Thing:
            pass
        class Thing1:
            def example(self):
                pass
        t = Thing()
        t1 = Thing1()
        return (t,t1,t1.example())
    def question2(self):
        class Thing2:
            letters = "abc"
        t2 = Thing2()
        return t2.letters
    def question3(self):
        class Things3:
            def __init__(self):
                self.letters = "abc"
        t3 = Things3()
        return t3.letters
    def question4(self):
        class Element:
            def __init__(self,n,s,num):
                self.name = n
                self.symbol = s
                self.number = num
        hydrogen = Element("Hydrogen", "H", 1)
    def question5(self):
        class Element:
            def __init__(self, d):
                self.name = d['name']
                self.symbol = d['symbol']
                self.number = d['number']
        d = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
        hydrogen = Element(d)
        return hydrogen
    def question6(self):
        q5 = basicassignment_19().question5()
        def dump():
            return q5.name, q5.symbol, q5.number
        return dump()
    def question7(self):
        class Element:
            def __init__(self, d):
                self.name = d['name']
                self.symbol = d['symbol']
                self.number = d['number']
            def __str__(self):
                return "name {}, symbol {}, number {}".format(self.name, self.symbol, self.number)
        d = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
        hydrogen = Element(d)
        return hydrogen
    def question8(self):
        class Element:
            def __init__(self, d):
                self.__name = d['name']
                self.__symbol = d['symbol']
                self.__number = d['number']
            def __str__(self):
                return "name {}, symbol {}, number {}".format(self.__name, self.__symbol, self.__number)
        d = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
        hydrogen = Element(d)
        return hydrogen
    def question9(self):
        class Beer:
            def eats(self):
                return "Berries"
        class Rabbit:
            def eats(self):
                return "Clover"
        class Octothorpe:
            def eats(self):
                return "Campers"
        beer = Beer()
        rabbit = Rabbit()
        octothorpe = Octothorpe()
        return beer,rabbit,octothorpe
    def question10(self):
        class Laser:
            def does(self):
                return "disintegrate"
        class Claw:
            def does(self):
                return "Crush"
        class Smartphone:
            def does(self):
                return "ring"
        class robot:
            laser = Laser()
            claw = Claw()
            smartphone = Smartphone()
            def does(self):
                return robot.laser.does(),robot.claw.does(),robot.smartphone.does()
        r = robot()
        return r.does()
    def __str__(self):
        return """
            1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?
            2. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.
            3. Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?
            4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1.
            5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.
            6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
            7. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.
            8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.
            9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.
            10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.

            """
        
if __name__ == "__main__":
    a19 = basicassignment_19()
    t,t1,t2 = a19.question1()
    print("Question 1:")
    print( str(t) + "\n" + str(t1)+ "\n" + str(t2))
    #class prints the manually defined class name with their unique hexadecimal id's
    #class inside the function print none. it returns none
    print("Question 2:", a19.question2())
    print("Question 3:", a19.question3()) #we dont need to create anyother object for this, we can use init method for instance attribute.
    a19.question4()
    a19.question5()
    n,s,num = a19.question6()
    print("Question 6: name {}, symbol {}, number {}".format(n,s,num))
    print("Question 7:", a19.question7())
    print("Question 8:", a19.question8())
    beer, rabbit, octothorpe = a19.question9()
    print("Question 9: beer eats {} \n\t rabbit eats {} \n\t octothorpe eats {}".format(beer.eats(), rabbit.eats(),octothorpe.eats()))
    laser, claw,smartphone = a19.question10()
    print("Question 10: laser does {} \n\t claw does {} \n\t smartphone does {}".format(laser,claw,smartphone))