import numpy as np

# Матрицы весов
weights_input_to_middle = np.random.uniform(-0.5, 0.5, (4, 5))
weights_middle_to_output = np.random.uniform(-0.5, 0.5, (3, 4))

# Нейрон смещения
bias_input_to_middle = np.zeros((4, 1))
bias_middle_to_output = np.zeros((3, 1))
