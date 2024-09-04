import eel

# Путь к HTML форме
eel.init("web")

@eel.expose
def minus(one_number: str, two_number: str) -> str:
    try:
        #  Проверка размера числа
        if len(one_number) >= 256 or len(two_number) >= 256:
            raise ValueError("Число превышает 256 символов.")

        # Находим большее число для правильности расчета
        max_len = max(len(one_number), len(two_number))

        # Добавляем нули в недостающих местах, в случаях, когда одно число длиннее первого
        one_number = one_number.zfill(max_len)
        two_number = two_number.zfill(max_len)

        negativity = False

        # Ищем наименьшее число для вычитания из большого меньшее
        if one_number < two_number:
            one_number, two_number = two_number, one_number
            negativity = True

        result = []
        ten = 0  # Для взятия следующего десятка при расчете

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
