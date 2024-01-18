import numpy as np
import matplotlib.pyplot as plt

# サンプル数
num_samples = 1000

# 確率変数列の発生
samples = np.random.uniform(size=(num_samples,))

# X_N の実現値を計算
cumulative_sum = np.cumsum(samples) / np.arange(1, num_samples + 1)

# グラフの表示
plt.plot(np.arange(1, num_samples + 1), cumulative_sum, label='X_N')
plt.axhline(y=0.5, color='r', linestyle='--', label='True Mean')  # 一様分布の平均は0.5

# グラフの装飾
plt.xlabel('N')
plt.ylabel('X_N')
plt.title('Law of Large Numbers')
plt.legend()
plt.show()
