from textwrap import indent
import pandas as pd

# 인덱스를 생략한 시리즈 객체
numbers = pd.Series([100, 200, 300])
print(numbers)

# 인덱스를 지정한 시리즈 객체
scores = pd.Series([90, 80, 99], index=['국어', '수학', '영어'])
print(scores)

# 시리즈 객체의 인덱스 출력
print(scores.index)

# 시리즈 객체의 데이터 값 출력
print(scores.values)

# 원하는 위치의 인덱스, 데이터 값 출력
print(scores.index[1], scores.values[1])