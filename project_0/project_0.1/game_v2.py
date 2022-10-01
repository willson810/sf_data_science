"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

from ftplib import error_temp
import numpy as np
import statistics

def random_predict(number: int = 1) -> int:
    """Угадываем число заданное рендомно. 
    Каждый раз находим среднее значение из возможного 
    минимального и максимального числа сравнивая с искомым числом,
    изменяя максиальное или минимальное число на ранее
    найденное среднее.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 1
    max_number = 101
    while True:
        count += 1
        mid = (min_number + max_number) // 2  
        if mid > number:
           max_number = mid
        elif mid < number:
            min_number = mid
        elif mid == number:
            #print(f"{count} попыток. {number} = {mid}")
            break  # выход из цикла если угадали
        elif mid != number:
            print('Значение не найдено--------------------------------------------')
            break  # выход из цикла если не угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
