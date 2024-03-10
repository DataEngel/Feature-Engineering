'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example

N = 4 
append 1
append 2
insert 3 1 
print
* Append 1: to the list
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
'''

import sys

if __name__ == '__main__':
    N = int(input())

my_list = []
inputs  = []

for line in sys.stdin:
    inputs.append(line)

for item in inputs:
    if item[0:5] == 'print':
        print(my_list)
    elif item[0:2] == 'in':
        inserts = [s for s in item.split()][1:3]
        inserts = list(map(int, inserts))
        my_list.insert(inserts[0], inserts[1])
    elif item[0:3] == 'rem':
        inserts = list(map(int, [s for s in item.split()][1]))
        my_list.remove(inserts[0])
    elif item[0:2] == 'ap':
        inserts = list(map(int, [s for s in item.split()][1]))
        my_list.append(inserts[0])
    elif item[0:4] == 'sort':
        my_list.sort()
    elif item[0:3] == 'pop':
        my_list.pop()
    elif item[0:7] == 'reverse':
        my_list.reverse()
