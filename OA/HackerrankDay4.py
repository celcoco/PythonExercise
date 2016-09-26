class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            self.age = 0
            print 'Age is not valid, setting age to 0.'
        else:
            self.age = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age >= 18:
            print 'You are old.'
        else:
            if self.age >= 13:
                print 'You are teenage.'
            else:
                print 'You are young.'
    def yearPasses(self):
        # Increment the age of the person in here
        self.age = self.age + 1
        #print self.age,age



t = int(raw_input())
for i in range(0, t):
    age = int(raw_input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")