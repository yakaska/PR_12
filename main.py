# https://observablehq.com/@rreusser/half-precision-floating-point-visualized

def convert_half_precision(n):
    sign = n >> 15
    exponent = (n >> 10) & 0b011111
    mantissa = n & (2 ** 10 - 1)
    if exponent == 0:
        if mantissa == 0:
            return -0.0 if sign else 0.0
        else:
            return (-1) ** sign * 2 ** (-14) * mantissa / 2 ** 10  # ненормализованное
    elif exponent == 0b11111:
        if mantissa == 0:
            return float('-inf') if sign else float('inf')
        else:
            return float('nan')
    return (-1) ** sign * 2 ** (exponent - 15) * (1 + mantissa / 2 ** 10)


def get_hex():
    while True:
        hex_value = input("Введите число в формате половинной точности в 16-ичном виде.\n")
        if len(hex_value) == 4:
            try:
                int(hex_value, 16)
            except ValueError:
                print("[Ошибка] число " + hex_value + " не является числом половинной точности в 16 виде.")
            else:
                return hex_value
        else:
            print("[Ошибка] число представлено недостаточным количеством бит")


def get_size():
    while True:
        size = input("Введите размер массива от 1 до 5\n")
        if size.isdigit():
            if 1 <= int(size) <= 5:
                return int(size)
            else:
                print("[Ошибка] введенное число вне диапозона [1;5]")
        else:
            print("[Ошибка] введенное значение не является числом")


if __name__ == '__main__':
    n = get_size()
    numbers = [' '] * n
    for i in range(n):
        numbers[i] = get_hex()
    for i in range(0, len(numbers)):
        bits = int(numbers[i], 16)
        numbers[i] = convert_half_precision(bits)
    numbers.sort(reverse=True)
    print("Массив, отсортированный по убыванию: " + str(numbers))
