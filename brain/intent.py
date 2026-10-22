import csv
import os
import string

INTENT_FILE = "config/intent.csv"   #Uygulama bilgilerinin tutulduğu CSV dosyasının yolu.


def load_intents(): 
    if os.path.exists(INTENT_FILE): # intent dosyasına bakar bulur.
        with open(INTENT_FILE, "r", encoding="utf-8") as file: # bulduğu dosyayı 
            reader = csv.DictReader(file)  # CSV dosyasını okuyup satırları sözlük formatında okuyacak okuyucu nesnesini oluşturuyor.
            data = list(reader) #reader içindeki btün satırları alıp listeye çeviriyor.
        return data # Bu listeyi fonksiyonu çağıran yere döndürüyor.
    else:
        return []


def normalize_text(text):  
    text = text.lower()   #  Büyük harfleri küçültür.
    text = text.split()   #  Metni boşluklrından ayırarak listeye döndürür.
    text = " ".join(text) #  Lisstedeki parçaları aralarına boşluk ekleyerek tek bir string haline getirir.
    clean_text = ""       #  Temizlenmiş metin buray geliyor.
    punctuation = string.punctuation.replace("'", "")  # Bütün noktalama işaretlerini siler ve sadece apostrof'u bırakır.
    for char in text:  
        if char not in punctuation:  # Karakter noktalama işaretleri arasında değilse;
            clean_text += char  # Noktalama işaretleri çıkarılmış temiz metin

    return clean_text # clean_text değerini normalize_text fonksiyonunu çağıran yere geri döndürüyor.

def find_intent(text):
    text = normalize_text(text)  # Gelen metni normalize eder.

    intents = load_intents() # intents'leri load_intents fonksiyonuna yollar.
    best_match = None # Henüz hiç bir eşleşme bulunmadığını belirtmek için başlangıç değeri.
    best_length = 0 # Şu ana kadarki eşleşmenin Kelime uzunluğunu tutmak için başlangıç değeri.

    for item in intents: # intents'in içindeki itemlere göre;
        if item["word"] in text and len(item["word"]) > best_length: #eğer textin içindeki itemler varsa ve bu itemlerin karakter sayısı best_length ten büyükse;
            best_match = { # 
                "intent": item["intent"], #komutun kategorisi 
                "action": item["action"], #yapılacak eylemi belirtiyor
                "confidence": 0.95,       #güvenilebilirlik yüzdesi
                "matched_word": item["word"], # Eşleşmeyi sağlayan kelimeyi/ifadeyi sonuçta saklıyor.
            }
            best_length = len(item["word"]) # Bulduğumuz mevcut eşleşmenin karakter uzunluğunu best_length içine kaydediyor.

    if best_match:
        return best_match # Eğer bir eşleşme bulunuyorsa bulunan en iyi eşleşmeyi geri döndürüyor.

    return {"intent": "conversation", # eşleşme olmadığı için conversation (sohbet) algılıyo.
            "confidence": 0.30,  # eşleşme olmadığı için güven seviyesini düşük tutuyor.
            "matched_word": None} # Hiç bir kelime eşleşmedi kaydedilecek kelime yok.
