import joblib  
import numpy as np

model=joblib.load("models/tech_model.pkl")  # Eğitilmiş modeli .pkl dosyasından yükleyip model değşişkenine atar.
vectorizer=joblib.load("models/vectorizer.pkl") # Eğitilmiş TF-IDF vectorizer'ı .pkl dosyasından yükler.

def predict(text):   # Gelen metni sınıflandırmak için predict fonksiyonunu tanımlar.
    X=vectorizer.transform([text]) # Gelen text'i TF-IDF değerlerine dönüştürür.
    proba=model.predict_proba(X)[0] # Modelin gelen text için oluşturduğu sınıf olasılıklarını proba değişkenine atar.
    classes=model.classes_ # Modelin bildiği sınıf isimlerini classes değişkenine atar.

    idx=np.argsort(proba)[::-1] # Olasılıkların indislerini büyükten küçüğe sıralayıp idx değişkenine atar.
    return[(classes[i],proba[i])for i in idx[:3]] # İlk 3 indisi gezerek sınıf adı ve olasılık değerlerinden yeni bir liste oluşturur.
    