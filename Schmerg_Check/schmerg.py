import math

def schmerg(x, y):
    '''

    :param x:
    :param y:
    :return:
    '''
    
    result = ((x * y)+ (math.sin(x) * math.cos(x) * math.tan(x)) + ((x + int("0xff22",0)) / (96 * y))) / ((math.pow(x, 2)*math.pow(y,-3)) + math.log(y + 12))

    return result          

x = float(input())

a = schmerg(0.5 * x, 0.7 *x)
b = schmerg(x + 1, x - 1)
c = schmerg(x, a)

final_ans = schmerg(c, b)

print(final_ans)
