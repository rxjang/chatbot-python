from konlpy.tag import Komoran

komoran = Komoran(userdic = './user_dic.tsv')
text = "우리 챗봇은 엔엘피를 좋아해."
pos = komoran.pos(text)
print(pos)

text2 = "홍길동 says: 나는 내일, 어제의 너와 만난다"
pos2 = komoran.pos(text2)
print(pos2)

noun = komoran.nouns(text2)
print(noun)