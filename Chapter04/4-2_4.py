## 거듭제곱(억지 기법) ##
def slow_power(x, n) :
    result = 1.0
    for i in range(n) :
        result = result * x
    return result