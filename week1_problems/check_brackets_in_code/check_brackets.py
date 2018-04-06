# python3
import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def isBalanced(text):
    stack = []

    for index, char in enumerate(text, start=1):
        print('----------------------')
        print(f'index: {index}, char: {char}')
        print(f'text: {text}')
        print(f'stack: {stack}')

        if char in ("[", "(", "{"):
            print(f'\nappending Bracket(char, index). char: {char}, index: {index}')
            stack.append(Bracket(char, index))
        elif char in ["]", ")", "}"]:
            if len(stack) == 0:
                print(f'stack is length 0. char: {char}, index: {index}')
                return index

            top = stack.pop()
            print(f'top: {top}, char: {char}, index: {index}')
            if not top.match(char):
                print(f'\nNot a match.')
                return index

    if stack:
        print(f'\non line 42. stack: {stack}')
        top = stack.pop()
        print(f'top: {top}')
        print(f'top.bracket_type: {top.bracket_type}, top.position: {top.position}')
        return top.position

    return 'Success'


print(isBalanced('{[]}bl(ahah')) # 7
# print(isBalanced('{[]}bl)ahah')) # 7
# print(isBalanced('{[]}()')) # Success
# print(isBalanced('{[}')) # 3
# print(isBalanced('{[}()')) # 3
# print(isBalanced('foo(bar[i);')) # 10
# print(isBalanced('foo(bar);')) # Success
# print(isBalanced('([]]()')) # 4
# print(isBalanced('}')) # 1
# print(isBalanced('{')) # 1
# print(isBalanced('[]')) # Success
# print(isBalanced('}()')) # 1
# print(isBalanced('{}()]')) # 5
# print(isBalanced('(())')) # Success
# print(isBalanced('[()]')) # Success
# print(isBalanced('{}[]')) # Success
# print(isBalanced('[]')) # Success
# print(isBalanced('[](()')) # 3


# if __name__ == "__main__":
#     text = sys.stdin.read().rstrip()
#     print(isBalanced(text))
