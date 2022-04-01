import pandas as pd

temperatures = [[3.3, 34.5, 14.2, -10], [7.1, 32.1, 10.7, 2]]
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
regions = ['Seoul', 'Pusan']

# 데이터프레임 객체 생성
data = pd.DataFrame(temperatures, index=regions, columns=seasons)

print(data)
print('=' * 50)
print(data.index)
print(data.columns)
print(data.values)
print('=' * 50)

print(data['Spring']['Seoul'])
print('=' * 50)

# 앞부분에서 2번째 행까지 조회
print(data.head(2))
print('=' * 50)

# 뒷부분에서 1번째 행까지 조회
print(data.tail(1))