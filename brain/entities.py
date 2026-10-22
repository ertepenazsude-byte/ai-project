import os
import json
from brain.intent import normalize_text

ENTITIES_FILE="config/entities.json"

def load_entities(): # Entities bilgilerini yükleyen fonksiyondur.
    if os.path.exists(ENTITIES_FILE):  #config/entities.json dosyası var mı diye kontrol ediyor.
        with open(ENTITIES_FILE,"r", encoding="utf-8") as file: #entities.json dosyasını okuma modunda("r") açıp file değiişkenine bağlıyor.
          data=json.load(file)  #Açılan json dosyasındaki veriyi okuyup Python verisine çevirerek data değişkenine atıyor.
          return data #Fonksiyonunoluşturduğu data değerini fonksiyonu çağıran yere geri döndürüyor.
    else:
       return{} # Veri olmadığı için boş döndürüyor.
    
def extract_entity(text):
  text=normalize_text(text)  #Gelen metni normalize ediyor.
  entity=load_entities()  # entities.json içindeki verileri yüklüyor ve entity değişkenine koyuyor.
  apps=entity["apps"]     #Yüklenen verinin içindeki "apps" bölümünü alıp apps değişkenine atıyor.

  for app in apps:  # apps sözlüğünün anahtarları(key'leri) üzerinde tek tek döner.
    app=normalize_text(app) #Uygulama adını da normalize ediyor.

    if app in text:  #appdeğişkenindeki uygulama adı, kullanıcının yazdığı text içinde geçiyor mu diye kontrol eder.
        return{
           "entity":app, #Hangi uygulamayı bulduğunu söylüyor.
           "confidence":0.95 # Bu bulduğu uygulama olduğuna ne kadar güvendiğini belirtiyor.
        }
  return{   # "Hangi uygulama olduğunu bulamadım." anlamında sonuç  döndürüyor ve return çalıştığı anda fonksiyondan çıkıyor.
      "entity":"unknown", 
        "confidence":0.0
            } 
     


