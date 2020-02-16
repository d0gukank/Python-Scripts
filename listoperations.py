"""
A = [1,2,3,4]
B = [2,5]

A - B = [1,3,4]
B - A = [5]
"""
def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]
        
        
