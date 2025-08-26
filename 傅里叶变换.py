import numpy as np
import matplotlib.pyplot as plt

# 1. 定义非周期函数
def f(t):
    return np.exp(-t)  # 指数衰减函数

# 2. 采样参数
fs = 20        # 采样率 Hz
T = 5           # 总时长 2 秒
t = np.linspace(0, T, int(T*fs), endpoint=False)
x = f(t)  # 离散采样信号

# 3. 傅里叶变换
X = np.fft.fft(x)
freqs = np.fft.fftfreq(len(x), d=1/fs)

# 只取正频率部分
half_N = len(x)//2
freqs_pos = freqs[:half_N]
X_pos = X[:half_N]

# 4. 绘图
plt.figure(figsize=(12,5))

# 时域信号
plt.subplot(1,2,1)
plt.plot(t, x)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Non-periodic Time Domain Signal")

# 频域幅度谱（兼容新版 Matplotlib）
plt.subplot(1,2,2)
markerline, stemlines, baseline = plt.stem(freqs_pos, np.abs(X_pos), basefmt=" ")
plt.setp(markerline, color='r', marker='o')
plt.setp(stemlines, color='b')
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.title("Frequency Domain (FFT)")

plt.tight_layout()
plt.show()
