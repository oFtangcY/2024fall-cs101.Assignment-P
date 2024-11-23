from math import sqrt

def dfs(a):
    digits = ''
    for digit in a:
        digits += digit
        num = int(digits)
        if num > 0 and int(sqrt(num))**2 == num:
            if digits == a:
                return 1
            elif dfs(a[len(digits):]):
                return 1
            
    return 0

if __name__ == "__main__":
    A = input()

    print(['No', 'Yes'][dfs(A)])