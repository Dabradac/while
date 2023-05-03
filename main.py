largestNumber = -99999999
counter = 0
while True:
 number = int(input("Введите число и напишите -1 для завершения программы: "))
 if number == -1:
    break
    counter += 1
    if number > largestNumber:
            largestNumber = number
            if counter != 0:
                print("Наибольшее число", largestNumber)
            else:
                    print("Вы не ввели число.")