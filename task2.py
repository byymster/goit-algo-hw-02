from collections import deque

def is_palindrome(s: str) -> bool:
    # Приводимо рядок до нижнього регістру і видаляємо пробіли
    s = ''.join(c.lower() for c in s if c.isalnum())
    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

user_input = input("Введіть рядок: ")
if is_palindrome(user_input):
    print("Рядок є паліндромом")
else:
    print("Рядок не є паліндромом")
