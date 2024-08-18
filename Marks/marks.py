x= int(input())


records = {}

for i in range(x):
    name = input()
    mark = int(input())
    records.update({name:mark})


records = dict(sorted(records.items()))

for key,value in records.items():
    print(f'{key} : {value}')

  
