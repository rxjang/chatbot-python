import matplotlib.pyplot as plt

# x, y축 데이터 정의
x = [a for a in range(0, 11)]
y = list(range(0, 11))

print('x축', x)
print('y축', y)

plt.plot(x, y)
plt.show()