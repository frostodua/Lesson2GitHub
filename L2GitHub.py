#1. Користувач вводить три цифри з клавіатури.
# Залежно від вибору користувача програма виводить на екран
# максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел.

# 2. Користувач вводить з клавіатури кількість метрів.
# Залежно від вибору користувача програма переводить метри милі, дюйми або ярди.

number = int(input("Введіть три цифри: "))
n1 = number // 100
n2 = number // 10 % 10
n3 = number % 10

if n1>=n2 and n1>=n3:
    resultMax=n1
elif n2>=n1 and n2>=n3:
    resultMax=n2
else:
    resultMax=n3

if n1<=n2 and n1<=n3:
    resultMin=n1
elif n2<=n1 and n2<=n3:
    resultMin=n2
else:
    resultMin=n3

resultAV=(n1+n2+n3)//3

num=int(input("Якщо бажаєте порахувати максимальну цифру - натисніть цифру 1, "
                 "якщо мінімальну - натисніть 2, якщо середньоарифметичне - натисніть 3: "))
if num==1:
    print(f"Максимальна цифра: {resultMax}")
elif num==2:
    print(f"Мінімальна цифра: {resultMin}")
elif num==3:
    print(f"Середньоарифметичне: {resultAV}")
else:
    print("Ви помилилися, натисніть 1,2 або 3")

num2=int(input("Введіть кількість метрів(до 3х цифр): "))
num3=int(input("Якщо бажаєте порахувати милі - натисніть цифру 1, "
                 "якщо ярди - натисніть 2, якщо дюйми - натисніть 3: "))

if num3==1:
    resultMiles=num2*0.00062137
    print(f"Милі: {resultMiles}")
elif num3==2:
    resultYards = num2 * 1.0936
    print(f"Ярди: {resultYards}")
elif num3==3:
    resultInches = num2 * 39.370
    print(f"Дюйми: {resultInches}")
else:
    print("Ви помилилися, натисніть 1,2 або 3")