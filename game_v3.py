import numpy as np


def riddle(minimum:int, maximum:int) -> int:
    """Функция загадыватель случайного числа.

    Args:
        minimum (int): Минимальное число.
        maximum (int): Максимальное число.

    Returns:
        int: Загаданное случайное число
    """
    
    np.random.seed(75) # фиксируем сид для воспроизводимости
    number = np.random.randint(minimum, maximum + 1) # генерируем случайное число
    
    return number


def random_predict(number:int, minimum:int, maximum:int) -> int:
    """Функция, реализующая алгоритм угадывания числа менее чем за 20 попыток.

    Args:
        number (int): Загаданное число, получаем из функции riddle.

    Returns:
        int: Количество попыток
    """
    
    count = 0
    num_list = list(range(minimum,maximum + 1))
    x = int(maximum/2) # начинаем с середины списка, что бы сразу откинуть половину чисел

    while x != number:
        
        if count > 20: #защита от вечного цикла
            raise ValueError('Не удалось отгадать число с 20 попыток')
        
        count += 1
        
        # после каждой попытки откидываем половину списка:
        if number < x:
            num_list = num_list[0 : round(len(num_list)/2)]
            x = num_list[round(len(num_list)/2)]
            
        else:
            num_list = num_list[round(len(num_list)/2) : len(num_list)+1]
            x = num_list[round(len(num_list)/2)]
     
    # Возвращаем количество попыток(int)       
    return count


def score_game(riddle, random_predict, minimum:int = int(input('Min number: ')), maximum:int = int(input('Max number: '))) -> int:
    """Функция, вычисляющая среднее (из 1000 повторений) количество попыток,
        которое понадобится, что бы угадать число.

    Args:
        riddle (function): Функция загадывания числа.
        random_predict (function): Функция угадывания числа.
        minimum (int): Минимальное значение числа.
        maximum (int): Максимальное значение числа.

    Returns:
        int: Среднее кол-во попыток за 1000 раз.
    """
    
    count_lst = [] # список с количеством попыток
        
    for i in range(0,1000):
        count_lst.append(random_predict(riddle(minimum, maximum), minimum, maximum)) # 1000 попыток
        
    average_score = int(np.mean(count_lst)) # среднее количество попыток
    print('Программа угадывает число в среднем c {} попытки'.format(average_score))
   
    return average_score # возвращаем среднее кол-во попыток за 1000 раз (int)


#RUN
if __name__ == '__main__':
    score_game(riddle, random_predict)