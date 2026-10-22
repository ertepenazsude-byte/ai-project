import json
import os
from unicodedata import category
import uuid

MEMORY_FILE="memory/user_profile.json" 

#Hafıza dosyasındaki kayıtları yükler, dosya yoksa varsayılan hafıza yapısını oluşturur.
def load_memory():
    if os.path.exists(MEMORY_FILE): #Hafıza JSON dosyası var mı diye kontrol ediyor.
        with open(MEMORY_FILE,"r",encoding="utf-8") as file : # Dosya varsa dosyayı okur.
            data=json.load(file) # içeriği data içine alır.

            return data
    else:
        data={
            "user":{
        "name":""
    },
    "skills":[],        # birden fazla beceri kaydı tutulacağı için liste,
    "preferences":{},   # tercihler anahtar-değer şeklinde tutulacağı için sözlük.
    "habits":[],        # birden fazla hafıza kaydı için liste,
    "memories":[],      # birden fazla alışkanlık için liste,
    "history":{         
        "skill_history":[],
        "preference_history":[],
        "system_history":[]
    }}
           
    return data

def save_memory(data):
    memory=load_memory() # mevcut hafızayı yüklüyor.
    data["id"]=str(uuid.uuid4()) # Hafıza kaydına benzersiz bir ID oluşturur.

    if data["type"]=="skill": # Eğer kayıt türü "skill" ise onu;
        memory["skills"].append(data) #memory skills'e ekliyor.
    elif data["type"]=="preference": # Eğer kayıt türü "preference" ise onu;
        memory["preferences"].update(data)
    elif data["type"]=="habit": # Eğer kayıt türü "habit" ise onu;
        memory["habits"].append(data)   
    elif data["type"]=="memory": # Eğer kayıt türü "memory" ise onu;
        memory["memories"].append(data)

    with open(MEMORY_FILE,"w",encoding="utf-8")as file:  # Güncellenen hafızayı JSON dosyasına kaydeder.
     json.dump(memory, file, indent=4,ensure_ascii=False)       

def add_memory(text, response):  # Jarvis'in mevcut hafıza/geçmiş verilerini yükler
    memory=load_memory()
    memory["history"]["system_history"].append({    # Jarvis'in geçmişine yeni bir konuşma kaydı ekleyecek.
        "text":text, # kullanıcının yazdığı yazı
        "response":response # Jarvisin verdiği cevap
    })

    with open(MEMORY_FILE,"w",encoding="utf-8")as file:  # json dosyasını yazmak/güncellemek için açar.
        json.dump(memory,file, indent=4, ensure_ascii=False) # JSON formatına çevirip açık olan dosyaya yazıyor/kaydeder.

def show_memory():  # Hafızayı göstermek için yazılan fonksiyon
    memory=load_memory()  # Mevcut hafızayı JSON dosyasından yükleyip memory değişkenine koyuyor. Çünkü "show_memory()" birazdan bu verinin içinden geçmiş kayıtlarını okuyacak.

    if not memory["history"]["system_history"]:  # Eğer sistem geçmişinde hiç kayıt yoksa;
        print("Henüz bir hafıza kaydı bulunmamaktadır.") # bu satırı yazdırır.
        return    
    for item in memory["history"]["system_history"]:  # system_history listesindeki her kaydı sırayla item değişkenine koyuyor.
        print("Sen:", item["text"]) # Geçmiş kayıtlardaki mesajları alır.
        print("Jarvis:", item["response"])  #Aynı kayıttan Jarvis'in verdiği cevabı alıp gösteriyor.


def check_duplicate_memory(data): # Data olarak kaydın hafızada zaten bulunup bulunmadığını kontrol ediyor.
    memory=load_memory()
    for skill in memory["skills"]:  # memory["skills"] listesindeki becerileri tek tek dolaşıyor ve her seferinde o beceriyi skills değişkenine kaydediyor.
        if skill["name"].lower()==data["name"].lower() and skill["type"].lower()==data["type"].lower():  # "Bu becerinin adı ve türü, eklenecek verinin adı ve türüyle aynı mı?" diye kontrol ediyor.
            return skill # Eşleşen mevcut beceriyi fonksiyonu çağıran yere geri gönderiyor.
        
    return None    # Eğer kayıt bulunamazsa None döndürür.

def upload_memory(old_data,new_data,reason):  #bilgi güncellemek için kullanılan fonksiyon
    memory=load_memory() # mevcut hafızayı güncelliyor.
    old_copy=old_data.copy() # old_data üzerinde daha sonra değişiklik yaparsak, elimizde eski hali bulunsun diye kopyasını alıyor.
    old_copy["reason"]=  reason # Eski bilgiyi gemişe atarken, neden eski bilgi olarak saklandığını da yanında tutmak.
    memory["history"]["skill_history"].append(old_copy) # Eski beceri bilgisini, neden değiştirildiğiyle birlikte beceri geçmişinde saklıyor. .append() ise listeye yeni eleman ekliyor.
    for skill in memory["skills"]: # Hafızadaki becerileri tek tek dolaşıyor.
        if skill["name"].lower()==old_data["name"].lower() and skill["type"].lower()==old_data["type"].lower(): # Eğer hafızadaki beceri, eski beceriyle eşleşiyorsa;
            skill.update(new_data) # Hafızadaki eski beceriyi, yeni beceri bilgisiyle güncelliyor.
            break
    with open(MEMORY_FILE,"w",encoding="utf-8")as file: # Güncellenmiş hafızayı JSON dosyasına kaydediyor.
        json.dump(memory, file, indent=4, ensure_ascii=False)
def check_memory(text): 
    memory=load_memory() # mevcut hafızayı yükler.
    for item in memory["history"]["system_history"]: # Sistem kayıtlarını tek tek dolaşır.
        if text in item["text"]: # "Şu anki text, geçmişteki mesajın içinde geçiyor mu?" diye kontrol eder.
            print("Hafızadan bulundu:", item["text"]) # Aranan metin geçmişte bulunursa "Hafızadan bulundu:" uyarısı veriyor ve yanına bulunan eski mesajı koyuyor.
            return item["response"] #Geçmişteki o kaydın Jaarvis cevabını geri döndürüyor.
    return None # Hiçbir geçmiş kaydında bulunamazsa None döndürür.

def add_skill(name, level): # Yeni beceriyi eklemeden önce, aynı becerinin daha önce eklenip eklenmediğini kontrol eder. Eğer eklenmişse tekrar eklemez, yoksa ekler.
    memory=load_memory() # mevcut hafızayı yükler.
    skill={                  # Eklenecek yeni beceri bilgisini oluşturur.
        "type":"skill",
        "name":name,
        "level":level
        }
    if check_duplicate_memory(skill): # Bu beceri zaten hafızada var mı diye kontrol eder.
        print("bu zaten hafızada mevcut.") # Eğer varsa uyarır ve fonksiyonu bitirir.
        return
    memory["skills"].append(skill) # Yeni beceriyi skills listesine ekler.
    with open(MEMORY_FILE,"w",encoding="utf-8")as file:
        json.dump(memory, file, indent=4, ensure_ascii=False) # Güncellenmiş hafızayı JSON dosyasına kaydeder.
    
def extract_skill(text):
    text=text.lower()  #  Büyük harfleri küçük harfe çevirir.
    if "öğreniyorum" in text: # "öğreniyorum" kelimesi metnin içinde var mı diye kontrol eder.
        words=text.split()    # Metni kelimelerine ayırıyor.
        words=[word.strip(".,!?") for word in words] # Burada words listesindeki her kelimenin başındaki ve sonundaki ".,!?" gibi belirtilen karakterleri temizliyor ve çıkan sonuçlardan yeni bir liste oluşturuyor.(liste comprehension)
        skill=words[words.index("öğreniyorum")-1] # "öğreniyorum" kelimesinden bir önceki kelimeyi beceri olarak alır ve skill değişkenine atar.
        print("öğrenme cümlesi bulundu.") # daha sonra ise "öğrenme cümlesi bulundu yazsını ekrana yazdırır.
        return skill # Bulunan beceriyi fonksiyondan geri döndürür ve fonksiyonu sonlandırır.

def get_skills(): # Hafızadaki becerileri almak için kullanılan fonksiyon.
    memory=load_memory() # Mevcut hafızayı yüklüyor.
    return memory["skills"] # Hafızadaki skills listesini fonksiyonu çağıran yere geri döndürür.

def answer_skill_question(text):  # kaydedilen beceriler hakkında soru sorulduğunda cevap verir.
    
    text=text.lower()  # Büyük harfleri küçültür.
    text=text.replace("\u0307", "") # birleşik nookta karakterini kaldırır.

    memory=load_memory()  # Mevcut hafızayı yükler
    skills=memory["skills"] # hafızadaki skills listesini alır ve skills değişkenine atar.
    skill_names=[skill["name"] for skill in skills] # Skills listesindeki becerilerin adlarını alıp skill_names listesine aktarır.
   
    if "ne öğreniyorum" in text:  # Eğer text içinde "ne öğreniyorum" ifadesi var sa kontrol  eder.
        if skill_names:  # skill_names listesinin boş olup olmadığını kontrol eder.
            return ", ".join(skill_names) + " öğreniyorsun." # Listedeki tüm becerilerin adlarını alıp cevap olarak döndürür.
        else: 
            return "Henüz öğrenmekte olduğun bir beceri bulunmamaktadır." # Beceri listesi boşsa bu mesaı döndürür.
    if "seviyem ne?" in text: # Eğer text içinde "seviyem ne?" ifadesi varsa kontrol eder.
        for skill in skills: # skills listesindeki her beceriyi tek tek gezer.
            if skill["name"].lower() in text: # Eğer textin içinde beceri varsa onu kontrol eder.
                return skill["name"]+" seviyen "+skill["level"]+"."  # Beceri ve seviyesini ekrana yazdırır.
        return "Bu beceri hakkında herhangi bir kayıt bulunamadı." # Beceri hakkında bir şye bulamazsa hata mesajı yazdırır.

def set_user_name(name):  # Kullanıcı adını hafızada tutan fonksiyon
    memory=load_memory()  #  Mevcut hafızayı yükler.
    memory["user"]["name"]=name # name değişkenindeki kullanıcı adını hafızadaki user/name alanına kaydeder.
    with open(MEMORY_FILE,"w",encoding="utf-8") as file: # Json dosyasını yazma modunda açar.
        json.dump(memory, file, indent=4, ensure_ascii=False) #Güncel hafızayı JSON dosaysına kaydeder.

def extract_user_name(text): # Kullanıcını texten adını bulan fonksiyon
    text=text.lower() # Büyük harfleri küçük harflere çevirir.
    if text.endswith("?"): # Metnin sonunda soru işareti var mı diye kontrol eder.
        return None  # return boş döndürür.
    if "benim adım" in text: # Eğer text içinde "benim adım" geçiyorsa;
        words=text.split() #text i kelimelerine ayırır,
        words=[word.strip(".,!?") for word in words] #Sondaki noktalama işaretlerini kaldırır
        user_name=words[words.index("adım")+1] # ve cümledeki adım kelimesinden bir sonraki kelimeyi user_name değişkenine atar.
        return user_name #return user_name yani kullanıcı adını döndürür.
    return None # Eğer benim adım ifadesi kullanılmamışsa None yani boş değer döndürür

def answer_user_name_question(text): # Kullanıcı adı sorulduğu zaman verilecek cevabı yazdıran fonksiyon
    text=text.lower() # Metindeki büyük harfleri küçük harf yapar.
    memory=load_memory() # Mevcut hafızayı yükler.
    name=memory["user"]["name"] # memory den kullanıcı adını çekip name değişkenine atar.
    if "benim adım ne?" in text: # Eğer kullanıcı "benim adım ne?" sorusunu soruyorsa;
        if name: # Eğer isim biilgisi var ise;
            return "senin adın " + name # Kullanıcı adını döndürür.
        else: # Eğer isim bilgisi yoksa;
            return "henüz bu bilgiye sahip değilim." # Bu mesajı döndürür.
    return None    # Eğer "benim adım ne?" sorusu sorulmamışsa None yani boş değer döndürür.

def extract_preference(text):
    text=text.lower()
    if "seviyorum" in text:
        words=text.split()
        words=[word.strip(".,!?") for word in words]
        preferences=words[words.index("seviyorum")-1]
        drink_words=[],
        music_words=[],
        color_words=[],
        if preferences in :

        return{
            "category": "",
            "value": preferences
        }
    return None

def add_preference(category, preference):
    memory=load_memory()
    memory["preferences"][category]=preference

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii=False)

def answer_preference_question(text):
    text=text.lower()
    memory=load_memory()
    preferences=memory["preferences"]
    if "ne içmeyi seviyorum" in text:
        if "drink" in preferences:
            return "senin içmeyi sevdiğin şey " + preferences["drink"]
        else:
            return "henüz bu bilgiye sahip değilim."
    return None        