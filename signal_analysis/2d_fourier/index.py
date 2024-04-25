import numpy as np
import matplotlib.pyplot as plt

SIGMA = 13
FREQ = 5
def main():
  #continuous example
  RADIUS = 30
  x_domain = np.linspace(-RADIUS, RADIUS, 200)
  y_domain = np.linspace(-RADIUS, RADIUS, 200)
  xv, yv = np.meshgrid(x_domain, y_domain)
  values = np.sin(xv + yv)
  ft = np.fft.fft2(values)
  plt.imshow(np.log(np.abs(np.fft.fftshift(ft))))
  # plt.contourf(x_domain, y_domain, values)
  plt.colorbar()
  plt.show()
  exit()


  sin = lambda x: np.sin(x)
  identity = lambda x: x
  exp = lambda x: np.exp(-x)
  func = lambda x: np.exp(-(x ** 2 / SIGMA)) * np.sin(FREQ * x)
  func2 = lambda x: np.exp(-(x ** 2 / SIGMA * 3)) * np.sin(FREQ * x)
  freq = np.linspace(1, 10, 100)
  # plt.plot(freq, values * 10)
  # plt.plot(freq, values2 * 10)
  domain = np.linspace(0, 10, 100)
  # plt.plot(domain, [func(val) for val in domain])
  # plt.plot(domain, [func2(val) for val in domain])
  plt.xscale("log")
  plt.yscale("log")
  # plt.show()
  # exit()
  #discrete example
  _args = np.linspace(0, 10, 1000)
  _sin = np.sin(_args * 2 * np.pi)
  _sin = _sin - _sin.mean()
  res = fourier(_sin, 10, 1000)
  freq = fourier_freq(10, 1000)
  # print(res, freq)
  plt.plot(freq, res)
  # plt.plot(_args, _sin)
  plt.show()

if __name__ == "__main__":
  main()

