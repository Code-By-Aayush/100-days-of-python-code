fruits = ["Apple", "Peach", "Pear"]
for items in fruits:
    print(items)
    print(items + " pie")

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# Sum Function on List
print(sum(student_scores))
sum_user = 0
for score in student_scores:
    sum_user += score
print(sum_user)

# Max Function on List
print(max(student_scores))
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
    else:
        pass
print(max_score)

#Min Function on List
print(min(student_scores))
min_score = max(student_scores)
for score in student_scores:
    if score < min_score:
        min_score = score
    else:
        pass
print(min_score)

# Sum of 1 + 2 + 3 + 4 + 5 .... 99 + 100
total = 0
for i in range(1,101):
    total += i
print(total)

for i in range(2,20,2):
    print(i)
print()
print("Fizz Buzz Game !!!👽👽👽\n")
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0 :
        print("Buzz")
    else:
        print(i)

