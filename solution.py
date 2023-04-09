import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 409995141 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    t = x.max() - 0.035
    n = len(x)
    return 0.035 + t / ((1 - alpha / 2)**(1 / n)), \
           0.035 + t / ((alpha / 2)**(1 / n))
