'''

https://www.codewars.com/kata/523f5d21c841566fde000009

DESCRIPTION:
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

'''

# Solution
def array_diff(a, b):
    if a == []:
        return []
    else:
        for i in b:
            while i in a:
                a.remove(i)
        return a

# Testing
print(array_diff([1,2,2,2,3],[2]))