# Константа NUМ_DAYS содержит количество дней,
# за которые мы соберем данные продаж.
NUМ_DAYS = 5


def main():
    sales = [0] * NUМ_DAYS
    # Создать переменную, которая будет содержать индекс.
    index = 0
    print("Введите продажи за каждый день: ")


    while index < NUМ_DAYS:
         print('День № ', index + 1, ': ',
          sep=' ', end=' ')
         sales[index] = float(input())
         index += 1
    print('Boт значения, которые были введены:')
    for value in sales:
        print(value)
main()
