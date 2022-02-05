# This is an example of how python reference values in memory


def reference_demo(x):
    print(f'Before the assigning: x= {x}, id = {id(x)}')
    x = 8
    print(f'After the assigning:  x= {x}, id = {id(x)}')


if '__main__' == __name__:
    x = 1
    print(f'Before the call:      x= {x}, id = {id(x)}')
    reference_demo(x)
    print(f'After the call:       x= {x}, id = {id(x)}')


""""
 Result:
    Before the call:      x= 1, id = 140518914922800
    Before the assigning: x= 1, id = 140518914922800
    After the assigning:  x= 8, id = 140518914923024  // create a new object after assigning
    After the call:       x= 1, id = 140518914922800
"""