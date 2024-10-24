def is_balanced(s: str) -> bool:
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in brackets.values():
            stack.append(char)  # Відкриваючі дужки в стек
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack


user_input = input("Введіть рядок з дужками: ")
if is_balanced(user_input):
    print("Симетрично розставлені дужки")
else:
    print("Несиметрично розставлені дужки")
