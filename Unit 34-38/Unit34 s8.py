# object oriented programming / OOP (intro)
    # OOP allows progrmmers to create their own objects that have methods and attributes.
    # Recall that after defining a string, list, dictionary, or other objects,
     # you were able to call methods off of them with the .method_name() syntax.
      # this methods act as functions that use information about the objects, as well the object itself to return results, or changethe current object. 
    # Example: this incluedes appending to a list, or counting the occurences of an element in a tupple.

    
class NameOfClass():
  def __init__(self,param1,param2):
      self.param1 = param1
      self.param2 = param2
  def some_methods(self):
    # perform some actions
    print(self.param1)


# param1/param2 = parameters that Python expects you to pass when you actually create an instance of this object.
# __init__ = allows you to create an instance of the actual object.