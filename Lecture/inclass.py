

class MyClass:

    # class variable
    listlength = 5

    # instance method
    def __init__(self):

            #instance attribute
            self.data = None
    
    # class method ## more of a general method, not specific to an instance. often used to instantiate # of objects
    @classmethod
    def list_of_objects(cls):
        result = []
        for i in range(cls.listlength):
            newobj= cls() ##same as example = MyClass().. this is creating an instance
            result.append(newobj)
        return result


result = MyClass.list_of_objects()
print(result)
