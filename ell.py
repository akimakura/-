import eel

# Путь к HTML форме
eel.init("web")

@eel.expose
def minus(one_number, two_number):
    try:
        # Для начала используем числа, чтобы проверить вводимые данные
        one_number = int(one_number)
        two_number = int(two_number)

        # Ограничение чисел(НЕ отрицательное, НЕ более 256 символов)
        if one_number < 0 or two_number < 0 or len(str(one_number)) > 256 or len(str(two_number)) > 256:
            raise ValueError("Число отрицательное или превышает 256 символов.")

        # Преобразуем числа в строки
        one_number = str(one_number)
        two_number = str(two_number)

        # Находим большее число для правильности рассчета
        max_len = max(len(one_number), len(two_number))

        # Добавляем нули в недотсающих местах, в случаях, когда одно число длиннее первого
        one_number = one_number.zfill(max_len)
        two_number = two_number.zfill(max_len)

        negativity = False

        # Ищем наименьшее число для вычетания из большого меньшее
        if one_number < two_number:
            one_number, two_number = two_number, one_number
            negativity = True

        result = []
        ten = 0  # Для взятия следуещего десятка при рассчете

        for i in range(max_len - 1, -1, -1):
            one_iter = int(one_number[i])
            two_iter = int(two_number[i])

            one_iter -= ten

            if one_iter < two_iter:
                one_iter += 10
                ten = 1
            else:
                ten = 0

            result.append(str(one_iter - two_iter))

        result.reverse()  # Разворачиваем строку
        final_result = ''.join(result).lstrip('0')  # Удаляем нули слева

        if not final_result:
            final_result = '0'
        elif negativity:
            final_result = '-' + final_result
        return final_result

    except ValueError:
        return f"Ошибка: не верный формат введенных данных"

# Запуск веб-интерфейса
eel.start("main.html", size=(700, 700))
