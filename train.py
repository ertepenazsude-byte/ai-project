import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import joblib

#veri

df=pd.read_csv("ml_basics/data/tech_dataset.csv")   # dosya yolu verilen csv dosyasını okur.

df["text"] = df["text"].str.strip().str.lower()     # gelen metni temizleyip değişkene atar.
df["label"] = df["label"].str.strip().str.lower()   # label leri temizleyip değişkene atar.
 
df = df.drop_duplicates()    # Veri setindeki tekrar eden satırları kaldırır.

X_text=df["text"]    # Text sütunlarını alır (sorular).
y=df["label"]        # Label sütunlarını al (cevap kategorileri/etiketler)


#train-test split
X_train_text,X_test_text, y_train,y_test=train_test_split(  #X_train_text → modelin öğreneceği metinler, 
                                                            #X_test_text  → modelin daha sonra sınanacağı metinler,
                                                            #y_train      → Eğitim metinlerinin doğru etiketleri,
                                                            #y_test       → Test metinlerinin doğru etiketleri   
    X_text, 
    y, 
    test_size=0.2,    # Test için verinin %20'sini ayırır.
    random_state=42,  # Verilerin bölünürken kullanılan rastgeleliğin sabitlenmesini sağlar.
    
)

#TF-IDF (yeni beyin)
vectorizer=TfidfVectorizer(   # metni modelin kullanabileceği sayısal özelliklere çevirir.
    ngram_range=(1,2), #tek kelime + kelime çiftleri
    min_df=1                  #Bir kelime setinde en az 1 kere geçiyorsa dikkate al.
)
X_train=vectorizer.fit_transform(X_train_text)  #eğitim metnindeki kelimeleri öğrenip metinleri sayısal TF-IDF değerlerine dönüştürüyor.
X_test= vectorizer.transform(X_test_text)       #Vectorizer eğitim verisinden öğrendiği sistemi kullanarak test verisini dönüştürüyor.

#model

from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=2000) # Modelin öğrenme işlemi sırasında yapabileceği max adım sayısını belirler.
model.fit(X_train, y_train) # Modelin eğitim verileri ve doğru etiketler kullanılarak eğitilmesini sağlar.

#tahmin
y_pred=model.predict(X_test)  # Model test verilerine bakarak kategorileri tahmin eder.

#accuracy
acc=accuracy_score(y_test, y_pred) # Modelin yaptığı tahminlerin ne kadarının doğru olduğunu ölçer.
print("accuracy:",acc)             # Accuracy sonucunu ekrana yazdırır.

#confidence(proba)
proba=model.predict_proba(X_test)  # Kategorilere bakaraak hangisinin olasılığı daha yüksek onu hesaplar
for p in proba:                    #  Her test metninin kategori olasılıklarını alır.
 print("Confidence:", max(p))      # Kategoriler arasındaki en yüksek olasılığı bulup ekrana yazdırır.

#kaydet
joblib.dump(model, "models/tech_model.pkl")      #Eğitilen model .pkl dosyasına kaydedilir.
joblib.dump(vectorizer,"models/vectorizer.pkl")  #güncellenen vectorizer .pkl dosyasına kaydediliir

print("model güncellendi")  # modelin güncellendiği  bilgisi ekrana yazdırılır.