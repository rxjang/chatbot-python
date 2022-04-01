import matplotlib.pyplot as plt

# 2차 함수 정의
# f(x) = x^2
f = lambda x : x ** 2

x = [x for x in range(-10, 10)]
y = [f(y) for y in range(-10, 10)]

print('x축', x)
print('y축', y)

plt.plot(x, y)
plt.show()