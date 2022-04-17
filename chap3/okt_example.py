from konlpy.tag import Okt

okt = Okt()

text = "가려던 카페가 문을 닫았습니다."

# 형태소 추출
morphs = okt.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = okt.pos(text)
print(pos)

# 명사만 추출
nouns = okt.nouns(text)
print(nouns)

# 정규화, 어구 추출
text = "오늘 날씨가 좋아욬ㅋ ㅋ"
print(okt.normalize(text))
print(okt.phrases(text))