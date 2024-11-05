## 거듭제곱(축소 정복 기법) ##
def power(x, n) :
    if n == 0 :
        return 1
    elif(n % 2) == 0 :
        return power(x*x, n//2)
    else :
        return x * power(x*x, (n-1)//2)