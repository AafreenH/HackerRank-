n=int(input())
ud= input()
ar= []
ar = ud.split()
sea_level= 0
valley=0
previous=0
for i in ar:
    if i=='U':
        sea_level+=1
    elif i=='D':
        sea_level-=1
    if sea_level == 0:
        if previous < sea_level:
            valley+=1
    previous = sea_level
print(valley)