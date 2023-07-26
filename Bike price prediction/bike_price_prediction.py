from sqlite3 import DatabaseError
from statistics import mode
import pandas as pd
from sklearn.model_selection import train_test_split #modeli ikiye ayırmak için kullanılır
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

dataframe=pd.read_excel("bisiklet_fiyatlari.xlsx")
print(dataframe)
y=dataframe["Fiyat"].values # fiyatları bir değişkene eşitledik
x=dataframe[["BisikletOzellik1","BisikletOzellik2"]].values #ÖZELLİKLERİ DE BAŞKA BİR DİZİYE EŞİTLİYORUZ
x_train, x_test, y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=20)#bölme işlemini yaptık
x_train.shape
x_test.shape
y_test.shape
y_train.shape
print(x_train.shape)

   #   SCALERRRR    (boyutlandırma yapıyoruz )     # 

scaler=MinMaxScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)
print(x_train)

model=Sequential() #model oluşturduk

model.add(Dense(4,activation="relu")) # nöronlar 
model.add(Dense(4,activation="relu"))
model.add(Dense(4,activation="relu"))

model.add(Dense(1)) #output çıktı 
model.compile(optimizer="rmsprop",loss="mse")

model.fit(x_train,y_train,epochs=250)  #modeli eğitiyoruz

a=model.history.history
print(a)

yenibisiklet=[[1760,1780]]
yenibisiklet=scaler.transform(yenibisiklet)
print("tahmin")
yenibisiklett=model.predict(yenibisiklet)#tahmin ettirir
print(yenibisiklett)



