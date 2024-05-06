numDays = int(input("How many day's temperatures? "))
i = 1
day_temp = []
while i <= numDays:
    temp = int(input("Day " + str(i) + "'s high temp: "))
    day_temp.append(temp)
    i += 1
average = sum(day_temp) / len(day_temp)
print("\nAverage = " + str(average))

dayCount = 0
for i in day_temp:
    if i > average:
        dayCount += 1
        print("Days " + str(dayCount) + "'s high temp: " + str(i))
print("No. of days greater than average are: " + str(dayCount))
