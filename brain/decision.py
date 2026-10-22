def decide(results): # Modelden gelen sonuçlara göre hangi cevabın verileceğini belirleyen fonksiyon.
    best,conf=results[0] # Model sonuçlarındaki ilk soncu alıp tamini best, güven oranını conf değişkenine atar.

    if conf > 0.80:  # Güven oranı %80 den büyükse;
        return f"Eminim -> {best}" # Eminim yazdır.
    elif conf >0.50: # Güven oranı %50 den büyükse ama ilk koşula girmemişse;
        return f"Büyük İhtimal->{best}" # Büyük ihtimal yazdır.
    else: # Hiçbiri uymuyorsa
        return "Bundan emin değilim, biraz daha açar mısınız?" # Bu mesajı döndür.
    
    