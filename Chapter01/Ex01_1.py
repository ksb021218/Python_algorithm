import math

def solve_quadratic(a, b, c):
    # 판별식 계산
    discriminant = b**2 - 4 * a * c

    # 판별식이 양수일 경우: 서로 다른 두 실근
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2

    # 판별식이 0일 경우: 중근
    elif discriminant == 0:
        x = -b / (2 * a)
        return x, x

    # 판별식이 음수일 경우: 서로 다른 두 복소수 근
    else:
        real_part = -b / (2 * a)
        imaginary_part = sqrt(-discriminant) / (2 * a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        return x1, x2

# 예를 들어, a=1, b=-3, c=2인 경우
result = solve_quadratic(1, -3, 2)
print(result)  # 결과: (2.0, 1.0)
