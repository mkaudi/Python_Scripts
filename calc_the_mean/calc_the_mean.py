x = float(input())

count = 0
sum_nums = 0

while x != -1:
    count +=1
    sum_nums +=x
    x = float(input())
    

mean = sum_nums/count
print(f'count: {count}' )
print(f'sum_nums: {sum_nums}')
print(f'mean: {mean}')
