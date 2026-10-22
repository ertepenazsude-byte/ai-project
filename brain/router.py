from brain.entities import extract_entity
from brain.intent import find_intent
from tools.app_manager import close_app, open_app
from tools.media_manager import (
    next_track,
    pause_track,
    play_track,
    previous_track,
    repeat_track,
)


def route(text):
    intent = find_intent(text)  # Kullanıcının metnindeki intent ve action bilgisini bulur.

    if intent["intent"] == "media":   # Bulunan intent bilgisinin "media" olup olmadığını kontrol ediyor.
        if intent["action"] == "next": # eğer komut next ise;
            return next_track() # bir sonraki şarkıya geçer.
        elif intent["action"] == "previous": # Bulunn komut previous ise;
            return previous_track() # bir önceki şarkıya geçer.
        elif intent["action"] == "play":  # Bulunan komut play ise;
            return play_track()  #şarkıyı oynatır.
        elif intent["action"] == "pause": # Bulunan komut pause ise;
            return pause_track() # şarkıyı durdurur.
        elif intent["action"] == "repeat": # Bulunan komut  repeat ise ;
            return repeat_track() # şarkıyı tekrara alır.

    if intent["intent"] == "command": # Uygulama komutu olduğunu algılar.
        entity = extract_entity(text) # Metinden hangi uygulama olduğunu belirler.

        if not entity: # Eğer uygulamayı bulamazsa ;
            return {"success": False, "message": "Hangi uygulama olduğunu anlayamadım."} # bu mesajı yolluyor
        app_name = entity["entity"]  # Bulunan uygulama adını app_name değişkenine alır.

        if intent["action"] == "open": # eğer komut open sa;
            return open_app(app_name)  # uygulma açılır.
        elif intent["action"] == "close": # eğer komut close ise;
            return close_app(app_name)    # uygulama kapanır.
    return {"success": False, "message": "Komut anlaşılmadı."}  # eğer girilen komut hiç anlaşılmazsa o zaman bu mesajı verir.
