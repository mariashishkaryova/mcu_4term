import matplotlib.pyplot as plt
import numpy as np

humidity = []
pressure = []
temperature = []

with open('bme.txt', 'r') as data:
    for line in data:
        # Разделяем значения и добавляем их в списки
        values = line.strip().split(';')
        humidity.append(values[0])
        pressure.append(values[1])
        temperature.append(values[2])

print('влажность =', humidity, '%')
print('давление =', pressure, 'Па')
print('температуро =', temperature, 'С')



fig, ax = plt.subplots(figsize=(16, 8))

plt.subplot(2, 2, 1)
plt.plot(humidity)
plt.ylabel('humidity')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(pressure)
plt.ylabel('pressure')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(temperature)
plt.ylabel('temperature')
plt.grid()
plt.savefig('bme.png')
plt.show()