import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 20, 400)
n_large = np.linspace(1, 10, 400)
O_n3 = n ** 3
Omega_n3 = n ** 3
O_n2logn = n ** 2 * np.log(n)
Theta_n2logn = n ** 2 * np.log(n)
O_2n = 2 ** n_large

plt.figure(figsize=(10, 8))

plt.plot(n, O_n3, label='O(n^3)')
plt.plot(n, Omega_n3, label='Ω(n^3)', linestyle='--')
plt.plot(n, O_n2logn, label='O(n^2 log n)')
plt.plot(n, Theta_n2logn, label='Θ(n^2 log n)', linestyle='-.')
plt.plot(n_large, O_2n, label='O(2^n)', color='red')

plt.ylim(0, 5000)
plt.xlabel('n')
plt.ylabel('Time Complexity')
plt.title('Comparison of Time Complexities')
plt.legend()
plt.grid(True)
plt.show()