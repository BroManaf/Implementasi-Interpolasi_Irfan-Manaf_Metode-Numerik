import numpy as np
import matplotlib.pyplot as plt

# Meminta data
n = int(input('Enter number of data points: '))

# Membuat array numpy dengan ukuran n & n x n dan diinisialisasikan
x = np.zeros((n))
y = np.zeros((n))

# Membaca titik data
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input('x['+str(i)+']=')) 
    y[i] = float(input('y['+str(i)+']='))

# Membaca titik interpolasi
xp = float(input('Enter interpolation point: '))

# Tetapkan nilai 0 interpolasi di awal
yp = 0

# Mengimplementasi Interpolasi Lagrange
print("\nStep-by-step Lagrange interpolation computation:")
for i in range(n):
    p = 1
    print(f"\nComputing term for i={i}:")
    for j in range(n):
        if i != j:
            p *= (xp - x[j]) / (x[i] - x[j])
            print(f"  Term for j={j}: (xp - x[{j}]) / (x[{i}] - x[{j}]) = ({xp} - {x[j]}) / ({x[i]} - {x[j]})")
    yp += p * y[i]
    print(f"  y[{i}] * product of terms = {y[i]} * {p} = {y[i] * p}")

# Menampilkan output
print('\nInterpolated value at %.3f is %.3f.' % (xp, yp))

# Generate nilai untuk plotting
x_plot = np.linspace(min(x), max(x), 400)
y_plot = np.zeros_like(x_plot)

# Hitung nilai interpolasi untuk plot
for i in range(len(x_plot)):
    for j in range(n):
        p = 1
        for k in range(n):
            if j != k:
                p *= (x_plot[i] - x[k]) / (x[j] - x[k])
        y_plot[i] += p * y[j]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, label='Interpolasi Lagrange', color='blue')
plt.scatter(x, y, color='red', label='Data Asli')
plt.scatter(xp, yp, color='green', label=f'Interpolasi di x={xp}', zorder=5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolasi Lagrange')
plt.legend()
plt.grid(True)
plt.show()
