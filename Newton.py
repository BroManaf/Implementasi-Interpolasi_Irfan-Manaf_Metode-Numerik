import numpy as np
import matplotlib.pyplot as plt

# Membaca jumlah titik data
n = int(input('Enter number of data points: '))

# Membuat array numpy untuk menyimpan x dan y serta perbedaan terbagi
x = np.zeros((n))
y = np.zeros((n))
div_diff = np.zeros((n, n))

# Membaca titik data
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input('x[' + str(i) + ']='))
    y[i] = float(input('y[' + str(i) + ']='))

# Membaca titik interpolasi
xp = float(input('Enter interpolation point: '))

# Mengisi tabel perbedaan terbagi
for i in range(n):
    div_diff[i][0] = y[i]

for j in range(1, n):
    for i in range(n - j):
        div_diff[i][j] = (div_diff[i + 1][j - 1] - div_diff[i][j - 1]) / (x[i + j] - x[i])

# Menampilkan tabel perbedaan terbagi
print("\nDivided Difference Table:")
for i in range(n):
    print(f"{x[i]:.3f}", end=" ")
    for j in range(n - i):
        print(f"{div_diff[i][j]:.3f}", end=" ")
    print()

# Menghitung nilai interpolasi
yp = div_diff[0][0]
product_term = 1
print("\nStep-by-step Newton interpolation computation:")
for i in range(1, n):
    product_term *= (xp - x[i - 1])
    yp += div_diff[0][i] * product_term
    print(f"Adding term {div_diff[0][i]:.3f} * {product_term:.3f}")

# Menampilkan hasil interpolasi
print('\nInterpolated value at %.3f is %.3f.' % (xp, yp))

# Generate values untuk plotting
x_plot = np.linspace(min(x), max(x), 400)
y_plot = np.zeros_like(x_plot)

# Menghitung nilai interpolasi untuk plot
for i in range(len(x_plot)):
    product_term = 1
    y_plot[i] = div_diff[0][0]
    for j in range(1, n):
        product_term *= (x_plot[i] - x[j - 1])
        y_plot[i] += div_diff[0][j] * product_term

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, label='Interpolasi Newton', color='blue')
plt.scatter(x, y, color='red', label='Data Asli')
plt.scatter(xp, yp, color='green', label=f'Interpolasi di x={xp}', zorder=5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolasi Newton')
plt.legend()
plt.grid(True)
plt.show()
