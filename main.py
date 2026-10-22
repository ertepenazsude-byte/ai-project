from brain.classifier import predict
from brain.decision import decide
from brain.memory import add_memory,check_memory, extract_skill, get_skills ,show_memory, add_skill,answer_skill_question, extract_user_name,set_user_name,answer_user_name_question,extract_preference,add_preference,answer_preference_question
from tools.calculator import calc
from tools.system_tools import system_tool
from brain.router import route


while True:               # True olduğu sürece döngüyü devam ettirir.
    
    text=input("\nSen:")  # kullanıcıdan input değerini alıp text değişkenine atar.
    if text=="memory":    # eğer text değişkeni memory'e eşitse;
        show_memory()     # fonksiyonu çalıştır.
        continue          # devam et
    
    name_answer=answer_user_name_question(text) #Kullanıcının yazdığı metni fonksiyona gönderir ve kullanıcı adıyla ilgili cevabı name_answer değişkenine alır.
    if name_answer: # Eğer cevap varsa;
        print("Jarvis:", name_answer) # cevabı ekrana yazdır.
        continue                      # devam et
    
    name=extract_user_name(text)      # Kullanıcının adı text te geçiyor mu kontrol eder ve name değişkenine atar.
    if name:                          # eğer isim bulunursa;
            set_user_name(name)       # Kullanıcının adını hafızaya kaydeder.
            continue                  # devam et
            
    skill_answer=answer_skill_question(text)  # Kullanıcının girdiği textte becerilerle alakalı bir şey var mı kontrol eder.
    if skill_answer:     #Eğer varsa 
        print("Jarvis:",skill_answer) # Cevap verir.
        continue                      # devam eder.

    preference_answer=answer_preference_question(text)
    if preference_answer:
        print("jarvis:",preference_answer)
        continue
    
    skill=extract_skill(text)      # Kullanıcının girdisinde herhangi bir beceri bilgisi verildi mi kontrol eder
    if skill:                      # eğer varsa;
        add_skill(skill,"orta")    # Beceriyi orta seviyesinde kaydeder.
        continue                   # devam eder.
    
    preference=extract_preference(text)  # Kullanıcının girdisinde herhangi bir tercih bilgisi verildi mi kontrol eder
    if preference:                      # eğer varsa;
     add_preference(preference["category"],preference["value"])    # Tercihi kaydeder.
     continue

    result=route(text)   # Kullanıcının girdiği metinden komutu alır ve result değişkenine atar.

    if result["success"]:  # eğer komut başarılıysa 
        print("Jarvis:",result["message"])  # result başarılı mesajı yollar.
        continue                            # devam eder.
    
    memory_result=check_memory(text) # Kullanıcı geçmiş mesajlardan bahsetmiş mi diye kontrol eder.
    if memory_result:    # eğer bahsetmişse;
        print("Jarvis:",memory_result) # cevabı yazdırır.
        continue   # devam eder.
    
    #MEMORY KOMUTU
    
    #TOOL 1: SYSTEM
    sys=system_tool(text)     # kullanıcı saat bilgisi istedi mi diye kontrol eder.
    if sys:                   # eğer istemişse;
        print("Jarvis:",sys)  # saati söyler ve,
        add_memory(text,sys)  # hafızaya ekler.
        continue              # devam eder.

    #TOOL 2: CALCULATOR
    if any(c.isdigit()for c in text):    # Text'in içinde matematik ifadesi veya işlemi varsa;
        result=calc(text)                # fonksiyonu çağırır.
        print("jarvis:",result)          # sonucu yazdırır ve
        add_memory(text,result)          # Hafızaya ekler.
        continue                         # devam eder.

    #TOOL 3: AI BRAİN
    results=predict(text)      # metin hangi sınıfa ait onu belirler.
    response=decide(results)   # hangisine uyumlu kontrol eder.

    print("Jarvis:",response)  # response değerini ekrana yazdırır.
    add_memory(text,response)  # hafızaya kaydeder.