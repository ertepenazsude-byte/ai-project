import re  # Metin içerisinden matematik işlemi gibi belirli ifadeleri bulmak için re modülünü içeri aktarır.

def calc(text): # Gelen metindeki matematik işlemini hesaplayan calc fonksiyonunu tanımlar.
    try:  # Aşağıdaki kodu çalıştırmayı dener.
        expr=re.findall(r"[0-9+\-*/(). ]+",text) # Text içerisindeki sayıları ve matematiksel işlem karakterlerini bulur.
        if expr: # Matematiksel bir ifade bulunup bulunmadığını kontrol eder.
            return eval(expr[0]) # Bulunan matematiksel ifadeyi hesaplayıp sonucu geri döndürür.
    except: # try bloğunda hata olursa çalışır.
        return "Hesaplanamadı!" # Hata durumunda hata mesajını geri döndürür.
        