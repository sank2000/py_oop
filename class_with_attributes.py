"""
THIS IS A PROGRAM THAT CONTAINS A CLASS WITH ATTRIBUTES
               Author: KrishnaMoorthy12
"""

class Class_with_Attributes:
    common_attribute = 60

print('the common attribute is', Class_with_Attributes.common_attribute)

Class_with_Attributes.secondThing = 'second'

#declaration of individual attributes

instance1 = Class_with_Attributes()
instance1.attribute2 = 'this is an individual attribute'

print('second common attribute of the class, as aquired by instance1:', instance1.secondThing)
print('individual attribute is:', instance1.attribute2)

try:
    print('check if attribute2 is in class itself:', Class_with_Attributes.attribute2)
except Exception as e:
    print('No, it is not present in the class itself,\nError description:', e)
finally:
    print('Success!')
