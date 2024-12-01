opt_set = {'/', '*', '+', '-'}

def calcPol(expression):
    if len(expression) == 1:
        return expression[0]
    
    exp = expression[:]
    for i in range(len(exp) - 2):
        if exp[i] in opt_set and exp[i + 1] not in opt_set and exp[i + 2] not in opt_set:
            new_str = str(eval(exp[i + 1] + exp[i] + exp[i + 2]))
            for _ in range(3):
                del exp[i]
            exp.insert(i, new_str)
            break
        
    return calcPol(exp)

if __name__ == "__main__":
    exp_list = list(input().split())
    print(calcPol('%.6f' % float(calcPol(exp_list))))