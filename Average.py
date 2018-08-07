ages =[ 1, 2 , 3 , 4 , 5]
# print(ages)

# for numbers in ages:
# print(numbers)
i=0
sum=0
for age in ages:
    print("age",age)
    sum = sum + age
    print("current sum",sum)

print("Final sum", sum)

length=len(ages)
print(length)

Average = sum / length
print(Average)
