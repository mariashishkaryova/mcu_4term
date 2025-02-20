import matplotlib.pyplot as plt

data_adc = 'adc.txt'

adc_values = []

# Чтение файла
with open(data_adc, 'r') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:  # Нечётные строки по счёту
            adc_values.append(float(line.strip()))  # Добавляем значение в список

# Построение графика
plt.plot(adc_values)
plt.title('График значений АЦП')
plt.ylabel('Значение АЦП')
plt.savefig('Значения АЦП.png')
plt.show()