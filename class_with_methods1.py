"""
    CLASS WITH METHODS - PART 1 - ONLY INIT FUNCTION
                Author: KrishnaMoorthy12
"""

class initClass:
    def __init__(inst, att1, att2):
        inst.first = att1;
        inst.second = att2;

try:
    instance1 = initClass()
    instance1.first = 'Krishna'
    instance1.second = 'Moorthy'
except Exception as we:
    print(we)
    instance1 = initClass('Krishna', 'Moorthy')

print('Name:', instance1.first + ' ' + instance1.second)
