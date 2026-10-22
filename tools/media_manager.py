import ctypes  # Windows API fonksiyonlarını Python üzerinden kullanmak için ctypes modülünü içe aktarır.

def next_track(): # Bir sonraki şarkıya geçme işlemini yapan fonksiyonu tanımlar.
    try: # Aşağıdaki kodu çalıştırmayı dener.

        ctypes.windll.user32.keybd_event(0xB0,0,0,0) # Windows'a 0xB0 koduyla bir klavye olayı gönderir.
        ctypes.windll.user32.keybd_event(0xB0,0,0x0002,0) # Tuşun bırakıldığını belirtir.
        return{             # İşlem başarılıysa sonucu geri döndürür.
            "success":True, # İşlemin başarılı olduğunu belirtir.
            "message":"Sonraki parçaya geçildi."} # Gerçekleştirilen işlemin sonucunu açıklayan mesajı tutar.

    except Exception as e:  # Try bloğunda hata oluşursa hatayı yakalar ve e değişkenine aktarır.
        return{
            "success":False, # İşlemin başarısız olduğunu bildirir.
            "message":str(e) # e içinde yakalanan hata bilgisini str() ile metne çevirip mesaj olarak geri gönderir.
        }

def previous_track():  # Bir  önceki şarkıya geçme işlemini yapan fonksiyonu tanımlar.
    try: # Aşağıdakii kod bloğunu çalıştırmayı dener.
        ctypes.windll.user32.keybd_event(0xB1,0,0,0) # Windows'a 0xB1 koduyla bir klavye olayı gönderir.
        ctypes.windll.user32.keybd_event(0xB1,0,0x0002,0) # Tuşun bırakıldığını belirtir
        return{  # İşlem başarılıysa sonucu geri döndürür.
            "success":True, # İşlemin başarılı olduğunu belirtir.
            "message":"Önceki parçaya geçildi." # Gerçekleştirilen işlemin sonucunu açıklayan mesajı tutar.
        }
    except Exception as e:       # try bloğunda hata oluşursa hatayı yakalar ve e değişkenine aktarır.
        return{                  #
            "success":False,     # İşlemin başarısız olduğunu belirtir.
            "message":str(e)     # e içinde yakalanan hata bilgisini str() ile metne çevirip mesaj olarak geri gönderir.
        }

def play_track():   # şarkıyı oynatma fonksiyonunu tanımlar
    try:    # Aşağıdaki kod bloğunu çalıştırmayı dener.
        ctypes.windll.user32.keybd_event(0xB3,0,0,0) # Windows'a 0xB3 koduyla bir klavye olayı gönderir.
        ctypes.windll.user32.keybd_event(0xB3,0,0x0002,0) # Tuşun bırakıldığını belirtir.
        return{    # İşlem başarılıysa sonucu döndürür.
              "success":True,  # İşlemin başarılı olduğunu belirtir.
              "message":"parça oynatıldı." # Gerçekleştirilen işlemin sonucunu açıklayan mesajı tutar.
          }
    except Exception as e:    # try bloğunda hata oluşursa hatayı yakalar ve e değişkenine aktarır.
        return{               # 
            "success":False,  # İşlemin başarısız olduğunu belirtir.
            "message":str(e)  # e içinde yakalanan hata bilgisini str() ile metne çevirip mesaj olarak geri gönderir.
        }

def pause_track():  # Şarkıyı durdurma fonksiyonunu tanımlar
    try:   #   Aşağıdaki kod bloklarını çalıştırmayı dener.
        ctypes.windll.user32.keybd_event(0xB3,0,0,0) # Windows'a 0xB3 koduyla bir klavye olayı gönderir.
        ctypes.windll.user32.keybd_event(0xB3,0,0X0002,0) #Tuşun bırakıldığını belirtir.
        return{               # İşlem başarılıysa sonucu döndürür.
            "success":True,   # İşlemin başarılı olduğunu belirtir.
            "message":"parça duraklatıldı."  # Gerçekleştirilen işlemin sonucunu açıklayan mesajı tutar.
        }
    except Exception as e:    # try bloğunda hata oluşursa hatayı yakalar ve e değişkenine atar.
        return{               # 
            "success":False,  # İşlemin başarısız olduğunu belirtir.
            "message":str(e)  # e içinde yakalanan hata bilgisini str() ile metne çevirip mesaj olarak geri gönderir.
        }


def repeat_track():  # Şarkıyı tekrar ettiren fonksiyonu tanımlar.
    try:   # try bloğundaki kodları çalıştırmayı dener.
        ctypes.windll.user32.keybd_event(0x11,0,0,0) # Windows'a 0x11 koduyla bir klavye olayı gönderir.
        ctypes.windll.user32.keybd_event(0x52,0,0,0) # Windows'a 0x52 koduyla bir klavye olayı gönderir.
        ctypes.windll.user32.keybd_event(0x52,0,0x0002,0) # Tuşun bırakıldığını gösterir.
        ctypes.windll.user32.keybd_event(0x11,0,0x0002,0) # Tuşun bırakıldığını gösterir.
        return{    # İşlem başarılıysa sonucu döndürür.
            "success":True, # İşlemin başarılı olduğunu belirtir.
            "message":"parça tekrarlandı." # Gerçekleştirilen işlemin sonucunu açıklayan mesajı tutar.
        }          
    except Exception as e:    # try bloğunda hata oluşursa hatayı yakalar ve e değişkenine atar.
        return{               #
            "success":False,  # İşlemin başarısız olduğunu belirtir.
            "message":str(e)  # e içinde yakalanan hata bilgisini str() ile metne çevirip mesaj olarak geri gönderir.
        }