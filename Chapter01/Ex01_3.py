# 스택을 리스트로 사용하여 구현
stack = []

# 사용자로부터 문자열 입력받기
string = input("문자열을 입력하세요: ")

# 문자열의 각 문자를 스택에 넣기
for char in string:
    stack.append(char)

# 스택에서 문자를 하나씩 꺼내면서 출력 (역순으로 출력됨)
reversed_string = ''
while stack:
    reversed_string += stack.pop()

print("역순 문자열:", reversed_string)