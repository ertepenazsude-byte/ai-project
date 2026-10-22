import json
import os
import subprocess
from pathlib import Path
from win32com.client import Dispatch
#------WİNDOWS UYGULAMALRINI BULMA, AÇMA VE KAPATMA İŞLEMLERİNİ YAPAN MODÜL-------

APP_FILE = "config/app.json"  # Uygulama bilgilerinin tutulduğu JSON dosyasının yolu.

# APP.JSON DOSYSINAKİ UYGULAMA BİLGİLERİNİ OKUR VE DOSYA YOKSA BOŞ SÖZLÜK DÖNDÜRÜR.
def load_apps():

    if os.path.exists(APP_FILE): # app.json dosyası bulunuyorsa içeriğini okur ve döndürür, yoksa boş bir sözlük döndürür.
        with open(APP_FILE, "r", encoding="utf-8") as file: ## app.json dosyasını UTF-8 kodlamasıyla okuma modunda açar.
            data = json.load(file)# JSON dosyasındaki bilgileri okuyup Python'daki data değişkenine aktarır.
        return data # Okunan uygulama bilgilerini fonksiyonu çağıran yere döndürür.
    else:
        return {}  # app.json dosyası yoksa boş bir sözlük döndürür.


# ---------- UYGULAMA AÇMA FONKSİYONU-----------
def open_app(app_name):  # Verilen uygulamanın yolunu bulur ve uygulamayı çalıştırır.
    data = load_apps()  # app.json dosyasından uygulama bilgilerini yükler.
    apps = data["apps"] # Uygulama bilgilerini içeren sözlüğü alır.

    for app in apps:  # Sözlükteki uygulama isimlerini (key'leri) tek tek dolaşır.
        if app.lower() == app_name.lower():  # Uygulama adlarını küçük harfe çevirerek büyük/küçük harf duyarsız karşılaştırma yapar.
            path = apps[app]["path"]  # Seçilen uygulamanın çalıştırılacağı dosya yolunu alır.

            if path:   # Uygulama için tanımlanmış bir dosya yolu olup olmadığını kontrol eder.
                if os.path.exists(path):  # Uygulamanın belirtilen dosya yolunun gerçekten var olup olmadığını kontrol eder.
                    try:   # Uygulamayı açma işlemini hata oluşma ihtimaline karşı dener.
                        os.startfile(path)  # Belirtilen dosya yolundaki uygulamayı çalıştırır.

                        return {"success": True, "message": f"{app_name} açıldı."}  # Uygulamanın başarıyla açıldığını belirten sonucu döndürür.

                    except Exception as e: 
                        return {"success": False, "message": str(e)} # Uygulama açılırken oluşan hatayı yakalayıp hata mesajını döndürür.

                else:
                    return {"success": False, "message": "Uygulama dosyası bulunamadı."}  # Uygulamanın dosya yolu bulunamazsa hata mesajı döndürür.

            else: 
                return {"success": False, "message": "Uygulama yolu tanımlanmamış."}  # Uygulama için dosya yolu tanımlanmamışsa hata mesajı döndürür.

    return {"success": False, "message": "Uygulama bulunamadı."}   # Kayıtlı uygulamalar arasında eşleşme bulunamazsa hata mesajı döndürür.


# -----------KAPATMA FONKSİYONU-------------
def close_app(app_name):  # Verilen uygulamanın yolunu bulur ve uygulamayı çalıştırır.
    data = load_apps()  # app.json dosyasından uygulama bilgilerini yükler.
    apps = data["apps"] # Uygulama bilgilerini içeren sözlüğü alır.

    for app in apps:# Sözlükteki uygulama isimlerini (key'leri) tek tek dolaşır.
        if app.lower() == app_name.lower(): # Uygulama adlarını küçük harfe çevirerek büyük/küçük harf duyarsız karşılaştırma yapar.
            process = apps[app]["process"]  # Uygulamanın çalıştırılacağı process adını alır.
            process = process.replace(".exe", "")  # Uygulama process adından ".exe" uzantısını kaldırır.

            if process:  # Uygulamanın process bilgisinin tanımlı olup olmadığını kontrol eder.
                try:  # Uygulama kapama işlemini hata oluşma ihtimaline karşı dener.
                    result = subprocess.run(  # PowerShell komutunu çalıştırır ve sonucunu result değişkenine kaydeder.
                        [
                            "powershell",  #Powershell'i çalıştırır.
                            "-Command",    #Ardından verilen ifadeyi Powershell komutu olarak çalıştırmasını sağlar.
                            f"Stop-Process -Name {process} -Force", #Belirtilen process adını zorla durdurur ve kapatır.
                        ],
                        capture_output=True,  #Komutun çıktı ve hata mesajlarını yakalar.
                        text=True,  #Komut çıktsını metin olarak işler.
                    )
                    if result.returncode != 0:  # Process'i kapatma komutunun başarısız olup olmadığını kontrol eder.
                        return {    # Process kapatılamazsa uygulamanın açık olmadığını belirten sonuç döndürür.
                            "success": False,
                            "message": f"{app_name} zaten açık değil.",
                        }
                    return {"success": True, "message": f"{app_name} kapandı."}# Uygulamanın başarıyla kapatıldığını belirten sonucu döndürür.
                except Exception as e:
                    return {"success": False, "message": str(e)}  # Oluşan hatayı yakalar ve hata mesajını döndürür.
            else:
                return {
                    "success": False,
                    "message": "Uygulama process yolu tanımlanmamış.",  # Uygulamanın process bilgisi tanımlanmamışsa hata mesajı döndürür.
                }

    return {"success": False, "message": "Uygulama bulunamadı."}  # Kayıtlı uygulamalar arasında eşleşme bulunamazsa hata mesajı döndürür.


def discover_apps():  # Windows'taki uygulama kısayollarını bulur ve uygulama bilgilerini sözlük olarak oluşturur.
    locations = [  # Uygulama kısayollarının aranacağı klasörleri belirler.
        Path.home() / "Desktop",  
        Path.home() / "AppData/Roaming/Microsoft/Windows/Start Menu/Programs",
        Path("C:/ProgramData/Microsoft/Windows/Start Menu/Programs"),
    ]
    apps = {} # Bulunan uygulamaların bilgilerini saklamak için boş sözlük oluşturur.

    for location in locations:  # Belirlenen klasör konumlarını tek tek tarar.
        if not location.exists():  # Klasör mevcut değilse bu konumu atlayıp sonraki konuma geçer.
            continue

        for file in location.rglob("*"):  # Klasör ve alt klasörlerdeki tüm dosya ve klasörleri tarar.
            if file.suffix.lower() == ".lnk": # Sadece ".lnk" uzantılı kısayol dosyalarını dikkate alır.
                name = file.stem.lower()  # Kısayol dosyasının adını küçük harfe çevirerek alır ve uygulama adı olarak kullanır.

                if name not in apps:   #Uygulamanın  daha önce eklenip eklenmediğini kontrol eder.
                    target_process, target_path = get_shortcut_target(str(file)) # Kısayolun hedef process adını ve hedef dosya yolunu alır.
                    if not target_path:  # Hedef dosya yolu bulunamazsa bu kısayolu atlayıp sonraki dosyaya geçer.
                        continue
                    if Path(target_path).suffix.lower() != ".exe":  # Hedef dosya yolu ".exe" değilse bu kısayolu atlayıp sonraki dosyaya geçer.
                        continue
                    apps[name] = {"process": target_process, "path": target_path} # Bulunan uygulamanın adını, process bilgisini ve dosya yolunu sözlüğe kaydeder.

    return apps  #Bulunan tüm uygulamaların bilgilerini sözlük olarak döndürür.


def get_shortcut_target(shortcut):  #Verilen ".lnk" kısayolunun hedef bilgilerini bulmak için kullanılan fonksiyon.
    shell = Dispatch("WScript.Shell") #Windows Shell nesnesi oluşturarak kısayol bilgilerine erişmeyi sağlar
    shortcut = shell.CreateShortCut(shortcut)  #Verilen .lnk kısayolunu Windows Shell kısayol nesnesine dönüştürür.
    target_path = shortcut.Targetpath # Kısayolun hedefindeki uygulamanın dosya yolunu alır.
    target_process = Path(shortcut.Targetpath).name  #Uygulamanın dosya yolundan process adını alır.
    return target_process, target_path  #Uygulamanın Process adını ve dosya yolunu döndürür.


if __name__ == "__main__":
    apps = discover_apps()
    for name, info in apps.items():
        print(name, "->", info["target_path"])
