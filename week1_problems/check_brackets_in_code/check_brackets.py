# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

# if __name__ == "__main__":
#     text = sys.stdin.read()

#     opening_brackets_stack = []
#     for i, next in enumerate(text):
#         if next == '(' or next == '[' or next == '{':
#             stack.append(next)

#         if next == ')' or next == ']' or next == '}':
#             # Process closing bracket, write your code here
#             pass

    # Printing answer, write your code here


def isBalanced(string):
    stack = []

    for index, char in enumerate(string):
        print('------------------------')
        print(f'char: {char}, index: {index}')
        print(f'stack: {stack}')

        if char in ["(", "[", "{"]:
            stack.append(char)
        elif char not in ["(", ")", "[", "]", "{", "}"]:
            print('char is not a closing or opening bracket.')
            print(f'char: {char}, index: {index}')
        else:
            if len(stack) == 0 and index == len(string):
                print(f'stack length is zero. index: {index}')
                return index
            else:
                stack_last_item = stack.pop()
                print(f'\nstack last item: {stack_last_item}, char: {char}')

                if (stack_last_item=="(" and char!=")") or (stack_last_item=="[" and char!="]") or (stack_last_item=="{" and char!="}"):
                    print(f'\nnot a match! index: {index}')
                    return index+1

    if len(stack) == 0:
        return 'Success'
    else:
        return index

# print(isBalanced('{[]}bl(ah')) # 8
# print(isBalanced('{[]}()')) # Success
# print(isBalanced('{[}')) # 3
# print(isBalanced('{[}()')) # 3
# print(isBalanced('foo(bar);')) # Success
# print(isBalanced('foo(bar[i);')) # 10
# print(isBalanced('([]]()')) # 4
# print(isBalanced('][')) # 1
