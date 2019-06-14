"""
    JUST A USELESS FILE WITH ABSOLUTELY NOTHING
     EXCEPT JUST A DUMMY CLASS AND AN INSTANCE
             Author: KrishnaMoorthy12
"""

class MyClass:
    pass

obj = MyClass()

obj.something = 1
obj.what_the_hell = 'test string'

obj2 = MyClass()

print('something is ', obj.something)
print('what_the_hell is ', obj.what_the_hell)

try:
    print('something from obj2: ', obj2.something)
except Exception as e:
    print('not a class variable', e)
