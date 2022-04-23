import tensorflow as tf
import pandas as pd
from keras.models import Model, load_model
from keras import preprocessing

# 데이터 읽어오기 1
train_file = "./chatbot_data.csv"
data = pd.read_csv(train_file, delimiter=',')
features = data['Q'].tolist()
labels = data['label'].tolist()

# 단어 인덱스 시퀀스 벡터 2
corpus = [preprocessing.text.text_to_word_sequence(text) for text in features]
tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(corpus)
sequences = tokenizer.texts_to_sequences(corpus)

MAX_SEQ_LEN = 15 # 단어 시퀀스 벡터 크기
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

# 테스트용 데이터셋 생성 3
ds = tf.data.Dataset.from_tensor_slices((padded_seqs, labels))
ds = ds.shuffle(len(features))
test_ds = ds.take(200).batch(20) # 테스트 데이터 셋

# 감정 분류 CNN 모델 불러오기 4
model = load_model('cnn_model.h5')
model.summary()
model.evaluate(test_ds, verbose=2)

# 테스트용 데이터셋의 10212번째 데이터 출력 5
IDX = 10212
print("단어 시퀀스 : ", corpus[IDX])
print("단어 인덱스 시퀀스 : ", padded_seqs[IDX])
print("문장 분류(정답) : ", labels[IDX])

# 테스트용 데이터셋의 10212번째 테이터 감정 에측 6
picks = [IDX]
predict = model.predict(padded_seqs[picks])
predict_class = tf.math.argmax(predict, axis=1)
print("감정 예측 점수 : ", predict)
print("감정 예측 클래스 : ", predict_class.numpy())