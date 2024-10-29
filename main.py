import random
import random as rnd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import time




class Algoritm():
    lst = []
    for i in range(100):
        lst.append(rnd.randint(0, 100))
    print(lst)
    def o_1(self):# в данной функции мы перебираем определнное количество шагов (10), поэтому O(1)
        dct = {}
        for i in range(1, 11):  # O(1)
            dct[i] = self.lst[i-1]
        print("O(1): ", dct)

        get_last_value = next(reversed(dct.values()))  #O(1) так как выбираем только 1 последнее значение
        print(get_last_value)
    def o_n(self, n):
        try:
            n = int(n)
            sum_lst = 0
            for i in range(len(self.lst)):  # O(1)
                sum_lst += int(self.lst[i])

            if n > 0:
                while n != 0:  # O(n)
                    sum_lst *= sum_lst
                    n -= 1
            else:
                raise Exception('n < 0')

            if sum_lst > 10000000000000000000000000:
                print("Use a number 'n' less than")
            else:
                print(sum_lst)

        except ValueError:
            print('Use int n')
        except KeyboardInterrupt:
            print('KeyboardInterrupt - прерываение процесса')
        except Exception:
            print('n<0')
        finally:
            print('Finally')

    def o_n_3(self, n, k, m):
        start_1 = time.time()
        start = datetime.datetime.now()
        #  Создаем 3 матрицы: основную, вппомогательную и результат их умножения
        arr_main_float = np.ones((n, k))
        arr_second_float = np.ones((k, m))
        arr_result_float = np.ones((n, m))

        #  Переводим значения матриц из флоат в инт
        arr_main_int = arr_main_float.astype(int)
        arr_second_int = arr_second_float.astype(int)
        arr_result_int = arr_result_float.astype(int)

        #  В первой матрице меняем значения с единиц на 1-15 попорядку
        num_arr = 1
        for i in range(n):  #O(n^2)
            for j in range(k):
                arr_main_int[i, j] = num_arr
                num_arr += 1
        #print("Основная матрица", n, " x ", k, ':', arr_main_int)

        #  В вспомогательной матрице изменяем на случайные значения
        for i in range(k):  #O(n^2)
            for j in range(m):
                arr_second_int[i, j] = random.randint(0, 10)
        #print("Вторая матрица матрица", k, " x ", m, ':', arr_second_int)

        # Произведение матриц
        # при произведении матриц новая получается с числом строк первой и числом сотолбцов 2
        for i in range(len(arr_main_int)):
            for j in range(len(arr_second_int[0])):
                for k in range(len(arr_second_int)):
                    arr_result_int[i][j] += arr_main_int[i][k] * arr_second_int[k][j]
        #print("Произведение матриц", arr_result_int)

        finish = datetime.datetime.now()
        #print('Время работы: ' + str(finish - start))
        #time_result = float(str(finish-start)[5:])/60
        result_time = time.time() - start_1
        print(result_time)

        #print('*********************************')
        #print(time_result)
        #print('*********************************')
        return result_time

alg = Algoritm()
#alg.o_1()
#alg.o_n(input('Input number: '))
#alg.o_n_3(100, 200, 30)

def diagram():
    dct = {}
    n = 0
    k = 0
    m = 0
    for i in range(1, 50):
        if i == 1:
            dct[0] = alg.o_n_3(n, k, m)
        else:
            dct[n] = alg.o_n_3(n, k, m)
        n += 10
        k += 10
        m += 10
    print(dct)
    plt.plot(dct.keys(), dct.values())
    plt.show()

diagram()




