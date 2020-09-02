from task_1 import Stack


def is_balanced(text):
    left = ['(', '[', '{']
    right = [')', ']', '}']
    stack = Stack()
    for character in text:
        if character in left:
            stack.push(left.index(character))
            # print(f'{character} added to stack')
            # print('stack: ' + str(stack.stack))
        elif character in right:
            if stack.stack and (stack.peek() == right.index(character)):
                # print(f'{stack.pop()} removed from stack')
                stack.pop()
            else:
                return 'Несбалансированно'
    return 'Сбалансированно'


if __name__ == '__main__':
    print(is_balanced('[([])((([[[]]])))]{()}'))