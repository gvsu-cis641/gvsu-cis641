class Singleton:
   __instance = None

   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
#      Singleton.__instance = self

# https://python-patterns.guide/gang-of-four/singleton/
#   def __new__(cls):
#     if cls.__instance == None:
#       cls.__instance = super(Singleton,cls).__new__(cls)
#     return cls.__instance

s = Singleton()
print(s)

s_new = Singleton()
print(s_new)

s1 = Singleton.getInstance()
print(s1)

s2 = Singleton.getInstance()
print(s2)


