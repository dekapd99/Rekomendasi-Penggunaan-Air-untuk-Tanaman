def klasifikasi(suhu, cuaca):
    hasil = []
    if cuaca.lower() == 'cerah':
        hasil.append(0)
    elif cuaca.lower() == 'panas':
        hasil.append(1)
    elif cuaca.lower() == 'berawan':
        hasil.append(2)
    elif cuaca.lower() == 'mendung':
        hasil.append(3)
    elif cuaca.lower() == 'hujan':
        hasil.append(4)

    if suhu >= 26 and suhu <= 31:
        hasil.append(0)
    elif suhu > 31:
        hasil.append(1)
    elif suhu < 26:
        hasil.append(2)
    return hasil

def preprocess(data_train):
    elemen = []
    features = []
    for single_data in data_train:
        elemen.append(tuple(klasifikasi(single_data[1],single_data[0])))

        if single_data[2] >= 50 and single_data[2] <= 80:
            features.append(0)
        elif single_data[2] > 80 and single_data[2] <= 125:
            features.append(1)
        elif single_data[2] > 125:
            features.append(2)
        elif single_data[2] < 50:
            features.append(3)

    return elemen, features

def dataValid(suhu, cuaca):
    if ((cuaca.lower() == 'cerah' or cuaca.lower() == 'panas'
        or cuaca.lower() == 'berawan' or cuaca.lower() == 'mendung'
        or cuaca.lower() == 'hujan') and suhu.isdigit()):
            return True
    return False

import pandas as pd

data_train = pd.read_excel('dataset.xlsx').values.tolist()

elemen, features = preprocess(data_train)

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(elemen, features)

while(True):
    print("Program Rekomendasi Volume Air Penyiraman Tanaman")
    print("Masukan Cuaca (cerah/panas/berawan/mendung/hujan):")
    cuaca = input()
    print("Masukan Suhu (Celcius):")
    suhu = input()
    if(dataValid(suhu, cuaca)):
        pred = model.predict([klasifikasi(int(suhu), cuaca)]).tolist()
        print("Rekomendasi volume penyiraman air: ", end='')
        if pred[0] == 0:
            print("50-80 Ml")
        elif pred[0] == 1:
            print("81-125 Ml")
        elif pred[0] == 2:
            print("Diatas 125 Ml")
        elif pred[0] == 3:
            print("Dibawah 50 Ml")
    else:
        print("Maaf, data yang anda masukan tidak valid!")
    pilih = input("Tekan 't' untuk keluar dan tekan 'y' untuk lanjut: ")
    print()
    if(pilih.lower() == 't'):
        break
