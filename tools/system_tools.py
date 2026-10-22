import datetime    # Tarih ve saat bilgilerini import eder.
 
def system_tool(text):   # Saat hakında bilgilendiren fonksiyonu tanımlar
    if "saat" in text:   # eğer text te saat geçiyorsa;
        return datetime.datetime.now().strftime("%H:%M:%S") # Saat bilgisini ver. (o anki saat bilgisini verir.)
    return None # Eğer texxtte saat demezse none döndür.
