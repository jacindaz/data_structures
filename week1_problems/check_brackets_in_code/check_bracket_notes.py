# python3
import sys
# import ipdb

# REMEMBER!!!
#  => SMALLEST UNIT OF WORK
#  => create methods for each unit of work, so you can test separately
#  => even if you're not sure if it'll work, just write it and try
#      (to avoid getting stuck in a loop)
#  => WHITEBOARD BEFORE WRITING ANY CODE
#     write out several examples and how to solve on whiteboard
#  => then psuedocode

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position # right now position not used for anything

    def Match(self, something): # Bracket('[', 1).Match(']')
        if self.bracket_type == '[' and something == ']':
            return True
        if self.bracket_type == '{' and something == '}':
            return True
        if self.bracket_type == '(' and something == ')':
            return True
        return False

# from lecture notes
def isBalanced(string):
    stack = []

    for char in string:
        print('\n--------------------\n')
        if char in ['(', '[', '{']:
            stack.Push(char)
        else:
            if stack.Empty():
                return False
            top = stack.Pop()
            if (top=='[' and char!=']') or (top=='(' and char!=')') or (top=='{' and char!='}'):
                return False
    return stack.Empty()

# ipdb.set_trace()


# if __name__ == "__main__":
#     text = sys.stdin.read()

#     opening_brackets_stack = []
#     for i, next in enumerate(text):
#         if next == '(' or next == '[' or next == '{':
#             # Process opening bracket, write your code here
#             print('opening bracket')
#             pass

#         if next == ')' or next == ']' or next == '}':
#             # Process closing bracket, write your code here
#             print('closing bracket')
#             pass

    # Printing answer, write your code here

# Input:
# foo(bar[i);
# Output:
# 10

# Input:
# foo(bar);
# Output:
# Success

# Input:
# {[}
# Output:
# 3

# {[]}()
# Output:
# Success
# Explanation


# python3
# import ipdb

# REMEMBER!!!
#  => SMALLEST UNIT OF WORK
#  => create methods for each unit of work, so you can test separately
#  => even if you're not sure if it'll work, just write it and try
#      (to avoid getting stuck in a loop)
#  => WHITEBOARD BEFORE WRITING ANY CODE
#     write out several examples and how to solve on whiteboard
#  => then psuedocode

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position # right now position not used for anything

    def Match(self, something): # Bracket('[', 1).Match(']')
        if self.bracket_type == '[' and something == ']':
            return True
        if self.bracket_type == '{' and something == '}':
            return True
        if self.bracket_type == '(' and something == ')':
            return True
        return False

# from lecture notes
def isBalanced(string):
    stack = []

    for index, char in enumerate(string):
        print('\n--------------------\n')
        print(f'char: {char}, string: {string}')
        print(f'stack: {stack}')

        # append all opening brackets first into my stack
        if char in ['(', '[', '{']:
            stack.append(char)
            print(f'\npushing onto stack. stack: {stack}')

        # if done appending opening brackets into my stack,
        # check closing brackets
        else:
            if len(stack) == 0: # checking if stack is empty
                print('\nstack is empty, returning index+1.')
                return index+1

            top = stack.pop()
            print(f'\npopping from stack. stack: {stack}, top: {top}')

            if (top=='[' and char!=']') or (top=='(' and char!=')') or (top=='{' and char!='}'):
                print('\n--------------------\n')
                print(f'brackets not matching. index: {index}')
                print(f'top: {top}, char: {char}')
                return index+1

    if len(stack) == 0:
        return 'Success!!!!'
    else:
        print('\nnot balanced!!!!')
        return index+1

# print(isBalanced('{[]}()'))
print(isBalanced('{[}()'))
# print(isBalanced('foo(bar);'))
# print(isBalanced('foo(bar[i);'))

# ipdb.set_trace()

# Input:
# foo(bar[i);
# Output:
# 10

# Input:
# foo(bar);
# Output:
# Success

# Input:
# {[}
# Output:
# 3

# {[]}()
# Output:
# Success
# Explanation
