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

if __name__ == '__main__':

    N = int(input())

    List=[];

    for i in range(N):

        command=input().split();

        if command[0] == "insert":

            List.insert(int(command[1]),int(command[2]))

        elif command[0] == "append":

            List.append(int(command[1]))

        elif command[0] == "pop":

            List.pop();

        elif command[0] == "print":

            print(List)

        elif command[0] == "remove":

            List.remove(int(command[1]))

        elif command[0] == "sort":

            List.sort();

        else:

            List.reverse();

'''
Steps Used in solving the problem -
Step 1: First, n will take input for the total command lines.

Step 2: then, we created a list to store the elements.

Step 3: After this, we created a for loop.

Step 4: inside for loop, we have taken an input of the command.

Step 5: then we used if and elif conditions to identify the command. After, the command gets identified an appropriate operation is performed.
'''
