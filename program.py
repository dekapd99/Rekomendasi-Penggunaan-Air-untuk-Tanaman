#Numpy digunakan untuk manipulasi array secara mudah dan cepat, bagian dari depedency untuk scikit-learn
#Scikit-learn digunakan untuk membantu melakukan processing data ataupun melakukan training data untuk kebutuhan machine-learning.
#pandas digunakan untuk untuk pengolahan data yang berkaitan dengan dataframe
#xlrd digunakan untuk membaca data mentahan excel menjadi xml yang merupakan bagian dependency dari pandas

def klasifikasi(suhu, cuaca):
    #list merupakan struktur data pada python yang mampu menyimpan lebih dari satu data
    hasil = []
    #append merupakan fungsi untuk menambahkan list baru dari belakang
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
    #for single_data untuk menampung index
    #in data_train berarti rangenya adalah banyak data yang dibuat dalam dataset
    for single_data in data_train:
        #kita membungkus elemen dengan tuple yang berguna untuk menyimpan sekumpulan data yang berisikan berbagai macam nilai dan object
        #sifat tuple adalah immutable artinya tidak bisa diubah/dihapus
        elemen.append(tuple(klasifikasi(single_data[1],single_data[0])))

        if single_data[2] >= 50 and single_data[2] <= 80:
            features.append(0)
        elif single_data[2] > 80 and single_data[2] <= 125:
            features.append(1)
        elif single_data[2] > 125:
            features.append(2)
        elif single_data[2] < 50:
            features.append(3)
    #return value elemen dan features untuk storing define masing-masing
    return elemen, features

#menentukan validasi input yang akan digunakan pada saat menjalankan program
def dataValid(suhu, cuaca):
    if ((cuaca.lower() == 'cerah' or cuaca.lower() == 'panas'
        or cuaca.lower() == 'berawan' or cuaca.lower() == 'mendung'
        or cuaca.lower() == 'hujan') and suhu.isdigit()):
            return True
    return False

#import pandas untuk bisa menggunakan dataframe
import pandas as pd

#read_excel merupakan fungsi dari library xlrd
#values.tolist merupakan fungsi pandas untuk melakukan konversi datafram menjadi list
#DataFrame merupakan struktur data 2 dimensi yang terdiri dari baris dan kolom
data_train = pd.read_excel('dataset.xlsx').values.tolist()

elemen, features = preprocess(data_train)

#penggunaan naive bayes
from sklearn.naive_bayes import GaussianNB
# Mengaktifkan/memanggil/membuat fungsi klasifikasi Naive Bayes
model = GaussianNB()
# Memasukkan data training pada fungsi klasifikasi Naive Bayes
model.fit(elemen, features)

while(True):
    print("Program Rekomendasi Volume Air Penyiraman Tanaman")
    print("Masukan Cuaca (cerah/panas/berawan/mendung/hujan):")
    cuaca = input()
    print("Masukan Suhu (Celcius):")
    suhu = input()
    if(dataValid(suhu, cuaca)):
        # Menentukan hasil prediksi, predict berdasarkan validasi dataset dengan membandingkan dengan data_train yang lalu
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
