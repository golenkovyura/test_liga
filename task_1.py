def decode(arr: list) -> int:
    """
    Функция получения ответа на самый главный вопрос!
    """
    index = 0
    result = 0
    while index < len(arr):
        try:
            if arr[index] == 1:
                result += arr[index + 1] + arr[index + 2]
                index += 2
            elif arr[index] == 2:
                result += arr[index + 1] * arr[index + 2]
                index += 2
            elif arr[index] == 99:
                break
            else:
                index += 1
        except IndexError:
            return 'Недостаточно элементов в списке для выполнения операций'
    return result


# тестовые данные
print(decode([1, 2, 4, 2, 3, 3, 2, 9, 3, 99, 2, 1, 24]))
print(decode([]))
print(decode([1, 2, 4, 2, 3, 3, 2, 9, 3, 2, 99, 1]))
