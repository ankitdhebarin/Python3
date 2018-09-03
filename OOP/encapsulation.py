class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._get_age()

    def _get_age(self):
        return self._age

tk = Person('TK', 25)
print(tk.show_age()) # => 25

'''
Here we have a _get_age non-public method and a show_age public method. 
The show_age can be used by our object (out of our class) and the _get_age only used inside our class definition (inside show_age method). 
But again: as a matter of convention.
'''


