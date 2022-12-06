import numpy as np
import pandas as pd


def Task1():
    array = np.arange(40, (50 + 1), 1)  # We want to include the no 50 So we did 50+1
    print("The First and Last two Numbers: ", array[0], ",", array[1], "...", array[-2], ",", array[-1])
    pass


def Task2():
    metrix1 = np.random.randint(10, 30, (4, 5))
    metrix2 = np.random.randint(10, 30, (4, 5))
    metrix3 = np.random.randint(10, 30, (4, 5))
    print("Metrix 1: \n", metrix1, "\nMetrix 2: \n", metrix2, "\nMetrix 3: \n", metrix3)

    print("\n")
    metrix1_sum_of_rows = "The Sum of rows of Metrix 1 : " + str(np.sum(metrix1, axis=0))
    metrix1_sum_of_col = "The Sum of columns of Metrix 1 : " + str(np.sum(metrix1, axis=1))
    print(metrix1_sum_of_rows, "  ", metrix1_sum_of_col)

    metrix2_sum_of_rows = "The Sum of rows of Metrix 2 : " + str(np.sum(metrix2, axis=0))
    metrix2_sum_of_col = "The Sum of columns of Metrix 2 : " + str(np.sum(metrix2, axis=1))
    print(metrix2_sum_of_rows, "  ", metrix2_sum_of_col)

    metrix3_sum_of_rows = "The Sum of rows of Metrix 3 : " + str(np.sum(metrix3, axis=0))
    metrix3_sum_of_col = "The Sum of columns of Metrix 3 : " + str(np.sum(metrix3, axis=1))
    print(metrix3_sum_of_rows, "  ", metrix3_sum_of_col)

    print("\n")
    metrix1_prod_of_rows = "The product of rows of Metrix 1 : " + str(np.prod(metrix1, axis=0))
    metrix1_prod_of_col = "The product of columns of Metrix 1 : " + str(np.prod(metrix1, axis=1))
    print(metrix1_prod_of_rows, "  ", metrix1_prod_of_col)

    metrix2_prod_of_rows = "The product of rows of Metrix 2 : " + str(np.prod(metrix2, axis=0))
    metrix2_prod_of_col = "The product of columns of Metrix 2 : " + str(np.prod(metrix2, axis=1))
    print(metrix2_prod_of_rows, "  ", metrix2_prod_of_col)

    metrix3_prod_of_rows = "The product of rows of Metrix 3 : " + str(np.prod(metrix3, axis=0))
    metrix3_prod_of_col = "The product of columns of Metrix 3 : " + str(np.prod(metrix3, axis=1))
    print(metrix3_prod_of_rows, "  ", metrix3_prod_of_col)

    pass


def Task3():
    series_1 = pd.Series(list(range(1, 27)))
    series_2 = pd.Series(
        ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
         "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

    series_3 = pd.concat([series_1, series_2], axis=1)
    print(series_3)


if __name__ == "__main__":
    print(20 * "=", " TASK 1 ", "=" * 20)
    Task1()
    print(20 * "=", " TASK 2 ", "=" * 20)
    Task2()
    print(20 * "=", " TASK 3 ", "=" * 20)
    Task3()
