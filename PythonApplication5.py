def sum_dig_pow(a, b): #функция определяет равна ли сумма цифр,где каждая из которых возведена в степень своего порядка,числа самому числу
    listes = [] #итоговый список таких чисел
    t = [] #список для цифр числа
    n = 1 #счётчик для порядка цифры(для возведения в степень)
    sumka = 0 #сумма этих цифр
    copi = 0 #копия изначального числа
    d1 = 0 #цифра возведённая в n-ую степень
    for i in range(a,b+1):
        sumka = 0
        copi = i
        if (i<10):
            listes.append(i)
            continue
        elif(i>=10):
            t = [int(a) for a in str(i)]
            for j in t:
                d1 = j**n
                sumka = sumka + d1
                n = n + 1
                continue
            n = 1
            if (copi == sumka):
                listes.append(sumka)
                
            else:
                sumka = 0


    listes.sort()
    return listes

m = sum_dig_pow(1, 100)
print(m)