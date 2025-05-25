# Session 7

import numpy as np

def demo_numpy_ops():
    print("--- NumPy Array Examples ---")

    a = np.array([10, 20, 30, 40, 50])
    b = np.linspace(0, 100, 5)
    c = np.arange(5, 25, 5)

    print("Array a:", a)
    print("Array b (linspace):", b)
    print("Array c (arange):", c)

    print("\nFilter a > 25:", a[a > 25])
    print("Fancy index a[[0, 3]]:", a[[0, 3]])

    print("\na squared:", a**2)
    print("a + c[:5]:", a + c[:5])

    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\nMatrix:\n", mat)
    print("Last column:", mat[:, -1])
    print("Reversed rows:\n", mat[::-1, :])

if __name__ == '__main__':
    demo_numpy_ops()