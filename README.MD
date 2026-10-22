JARVIS
Modüler Masaüstü Yapay Zeka Asistanı

Proje Türü: Masaüstü Yapay Zeka Asistanı
Programlama Dili: Python
Platform: Windows
Python Sürümü: Python 3.13+
Proje Durumu: Aktif Geliştirme
Geliştirici: Sudenaz ERTEPE

------------1.PROJE TANIMI----------
    JARVIS, Python programlama dili kullanılarak geliştirilen, kullanıcıdan
    alınan doğal dil tabanlı metinleri analiz ederek uygun işlemleri gerçekleştirmeyi amaçlayan modüler bir yapay zeka asistanı projesidir.
    
    Projenin temel amacı; doğal dil işleme, makine öğrenmesi, kullanıcı hafızası komut yönlendirme ve işletim sistemi araçlarını tek bir yazılım mimarisi içerisinde bir araya getirmektir.
    
    JARVIS'in mevcut mimarisi, farklı görevlerin bağımsız modüllere ayrılması prensibine dayanmaktadır. Bu yapı sayesinde sistemin yeni özzelliklerle genişletilmesi ve mevcut bileşenlerin ayrı ayrı geliştirilmesi hedeflenmektedir.

------------2.PROJENİN AMACI----------
    Projenin temel amaçları aşağıdaki şekilde sıralanabilir:
    1.Kullanıcıdan alınan metinleri analiz etmek.
    2.Kullanıcının gerçekleştirmek istediği işlemi belirlemek.
    3.Komut içerisinde belirtilen uygulama veya varlıkları tespit etmek.
    4.Kullanıcı komutlarını uygun sistem aracını yönlendirmek.
    5.Teknik konularla ilgili kullanıcı soruları makine öğrenmesi kullanarak sınıflandırmak.
    6.Model tahminlerinin güven seviyelerini değerlendirmek.
    7.Kullanıcıya ait belirli bilgileri kalıcı olarak saklamak.
    8.Windows işletim sistemi üzerinde çeşitli işlemleri gerçekleştirmek.
    9.Sistemi ilerleyen aşamalarda sesli asistan ve görev tabanlı agent mimarisi ile genişletmek.

------------3.PROJENİN KAPSAMI----------
    JARVIS projesi aşağıdaki temel bileşenleri kapsamaktadır:
    
    -Metin tabanlı kullanıcı etkileşimi
    -Intent analizi
    -Entity analizi
    -Komut yönlendirme
    -Makine öğrenmesi tabanlı sınıflandırma
    -TF-IDF tabanlı özellik çıkarımı
    -Logistic Regression sınıflandırma modeli
    -JSON tabanlı kullanıcı hafızası
    -Windows uygulama yönetimi
    -Medya kontrolü
    -Sistem araçları
    -Matematiksel hesaplama
    -Uygulama keşfi
    -Dataset tabanlı model eğitimi

------------4.SİSTEM MİMARİSİ----------    
    JARVIS modüler bir yazılım mimarisine sahiptir.
    Genel işlem akışı aşağıdaki gibidir:
    Kullanıcı 
    │ 
    ▼ 
    main.py 
    │ ├───────────────┐ 
    │                 │ 
    ▼                 ▼ 
    Memory          Router 
    │                  │ 
    │           ┌──────┼──────┐ 
    │            
    │           │      │      │ 
    |           ▼      ▼      ▼ 
    │         Intent Entity Tools 
    │ 
    ▼ 
    Kullanıcı Bilgileri

    Teknik Sorular İçin: 
    Kullanıcı Metni 
          │ 
          ▼ 
    TfidfVectorizer 
          │ 
          ▼ 
    TF-IDF Özellikleri 
          │ 
          ▼ 
    Logistic Regression 
          │ 
          ▼ 
    Sınıf Olasılıkları 
          │ 
          ▼ 
    En Yüksek 3 Tahmin 
          │ 
          ▼ 
    Decision 
          │ 
          ▼ 
    Sistem Yanıtı

    Bu mimaride her bileşenin belirli bir sorumluluğu bulunmaktadır.

------------5.MAKİNE ÖĞRENMESİ SİSTEMİ----------
    JARVIS içerisinde teknik konuların sııflandırılması amacıyla makine öğrenmesi tabanlı bir sistem kullanılmaktadır.

    Makine öğrenmesi süreci iki temel bileşenden oluşmaktadır:
    1.Metin özellik çıkarımı
    2.Sınıflandırma

    5.1. Metin Özellik Çıkarımı
    Metinlerin makine öğrenmesi modeli tarafından işlenebilmesi için TF-IDF (Term Frequency-Inverse Document Frequency) yöntemi kullanılmaktadır.

    Bu işlem TfidfVectorizer sınıfı aracılığıyla gerçekleştirilir.
    
    Ham Metin 
       │ 
       ▼ 
    TfidfVectorizer 
       │ 
       ▼ 
    TF-IDF Özellik Matrisi

    TfidfVectorizer, metin bilgilerini TF-IDF özelliklerinden oluşan sayısal bir bir matrise dönüştürmektedir.
    Bu sayede:
    "Python'da liste nasıl oluşturulur?"
    gibi bir kullanıcı girdisi doğrudan modele verilemk yerine, modelin işleyebileceği sayısal özelliklere dönüştürülmektedir.

------------6.KULLANILAN MAKİNE ÖĞRENMESİ MODELİ----------
    JARVIS'ın mevcut teknik konu sınıflandırma sisteminde Logistic Regression modeli kullanılmaktadır.

    Model:
    LogisticRegression

    Scikit-learn kütüphanesindeki Logistic Regression sınıflandırıcısı, çok sınıflı sınıflandırma problemlerinde kullanılabilmektedir. 

    Modelin amacı,kullanıcı tarafından girilen teknik bir metnin hangi konu kategorisine ait olduğu tahmin etmektir.
    
    Örnek kategoriler:
    -Python
    -C++
    -Database
    -Linux
    -Web
    -Artifical Intelligence
    -Algorithms
    -Data Structures
    -Cybersecurity

    Modelin ürettiği sonuçlar olasılık değerleri ile birlikte değerlendirilir.

    Örnek:
    Python    -> 0.92
    Database  -> 0.05
    Web       -> 0.02

------------7.MODEL VE VECTORİZER DOSYALARI----------
    Eğitim tamamlandıktan sonra model ve vectorizer ayrı dosyalarda saklanmaktadır.
    models/
    │ 
    ├── tech_model.pkl 
    └── vectorizer.pkl
    
    7.1.tech_model.pkl
    Bu dosya eğitilmiş Logistic Regression modelini içermektedir.
    Görevi:
      Kullanıcı metninin hangi sınıfa ait olduğunu tahmin etmek.

    7.2. vectorizer.pkl
    Bu dosya eğitim sırasında kullanılan TF-IDF vectorizer nesnesini içermektedir.
    Görevi:
      Kullanıcı tarafından gönderilen yeni metni, modelin eğitim sırasında kullandığı özellik uzayına dönüştürmek.

    Model ve vectorizer çalışma sırasında joblib kullanılarak yüklenmektedir.

------------8.CLASSİFİER MODÜLÜ----------
    Dosya:
    brain/classifier.py

    Classifier modülü makine öğrenmesi modelin çalışma aşamasından sorumludur.

    Temel görevleri:
    1.Eğitilmiş modeli yüklemek.
    2.TF-IDF vectorizer'ı yüklemek.
    3.Kullanıcı metnini dönüştürmek.
    4.Modelden sınıf olasılıklarını almak.
    5.Sınıf isimlerini belirlemek.
    6.Sonuçları olasılık değerlerine göre sıralamak
    7.En yüksek 3 tahmini sisteme göndermek.

    Örnek çıktı:
    [
        ("python",0.92),
        ("database",0.05),
        ("web",0.02)
    ]
    Classifier yalnızca tahmin üretmektedir. Tahminin kullanıcıya nasıl aktarılacağına decision.py karar vermektedir.

------------9.DECİSİON MODÜLÜ----------  
    Dosya:
    brain/decision.py

    Decision modülünün görevi, classifier tarafından üretilen tahminleri güven seviyelerine göre değerlendirmektir.

    Mevcut karar yapısı:
    
    Güven Değeri      Sistem Yanıtı
    > 0.80             Eminim
    > 0.50             Büyük ihtimal
    ≤ 0.50             Yeterli güven yok

    Örneğin model:
    
    python-> 0.92 
    sonucunu üretirse sistem:
    Eminim -> Python 
    şeklinde bir sonuç oluşturabilir.

    Burada classifier ve decision farklı görevler üstlenmektedir.

    classifier.py
          ↓
    Tahmin üretir   

    decision.py
       ↓
    Tahmin güvenini değerlendirir.  

------------10.INTENT ANALİZİ----------  
    Dosya:
    brain/intent.py
    Intent sistemi, kullanıcının gerçekleştirmek istediği işlemi belirlemek amacıyla kullanılmaktadır.

    Örneğin:
    "Chrome'u aç"
    girdisi için:

    Intent → command
    Action → open

    şeklinde bir sonuç üretilebilir.

    
    Başka bir örnek:
    "Sonraki şarkıya geç"
    girdisi:
    
    Intent → media
    Action → next
    şeklinde değerlendirilebilir.

    Intent tanımları:
    config/intent.csv
    dosyasında tutulmaktadır.

    Intent anaizinden önce kullanıcı normalize edilmektedir. Bu işlem büyük/küçük harf farklılıklarının ve gereksiz noktalama işaretlerinin azaltılmasını sağlar.

------------11.ENTİTY ANALİZİ----------    
    Dosya:
    brain/entities.py

    Entity sistemi, kullanıcı mesajında işlem yapılacak nesne veya uygulamayı tespit etmek amacıyla kullanılmaktadır.

    Örneğin:

    "Chrome'u aç"

    ifadesinde:

    Intent → command
    Action → open
    Entity → Chrome

    şeklinde bir yapı oluşmaktadır.

    Entity bilgileri:

    config/entities.json

    dosyasından alınmaktadır.

    Intent ve Entity arasındaki temel fark:

    Intent
    → Kullanıcı ne yapmak istiyor?

    Entity
    → Bu işlemi ne üzerinde yapmak istiyor?

------------12.ROUTER MODÜLÜ----------
    Dosya:

    brain/router.py

    Router modülü, analiz sonucunda elde edilen intent ve entity bilgilerini kullanarak isteği uygun araca yönlendirmektedir.

    Örnek akış:

    "Chrome'u aç"
        │
        ▼
    Intent Analysis
        │
        ├── intent = command
        └── action = open
        │
        ▼
    Entity Analysis
        │
        └── entity = Chrome
        │
        ▼
    Router
        │
        ▼
    app_manager.py
        │
        ▼
    Chrome açılır

    Router, doğrudan tüm işlemleri gerçekleştirmek yerine ilgili modülü çağırarak sistem içerisindeki görev dağılımını sağlamaktadır.

------------13.HAFIZA SİSTEMİ ----------

    Dosya:

    brain/memory.py

    JARVIS kullanıcıya ait belirli bilgilerin kalıcı olarak saklanabilmesi için JSON tabanlı bir hafıza sistemi kullanmaktadır.

    -Ana hafıza dosyası:

    memory/user_profile.json

    Temel veri yapısı:

    {
        "user": {
            "name": ""
        },
        "skills": [],
        "preferences": {},
        "habits": [],
        "memories": [],
        "history": {
            "skill_history": [],
            "preference_history": [],
            "system_history": []
        }
    }

    Hafıza sistemi içerisinde aşağıdaki veri türleri bulunmaktadır:

    Kullanıcı bilgileri
    Beceriler
    Tercihler
    Alışkanlıklar
    Genel hafıza kayıtları
    Sistem geçmişi
    Beceri geçmişi

    Verilerin JSON formatında tutulması, mevcut proje aşamasında harici bir veritabanına ihtiyaç duyulmadan yapılandırılmış veri saklanmasına olanak sağlamaktadır.

------------14. TOOL KATMANI ----------

    JARVIS'ın işletim sistemi üzerinde gerçekleştirdiği işlemler tools/ klasörü altında bulunmaktadır.

    14.1. app_manager.py

        Windows uygulamalarının yönetilmesini sağlar.

        Temel görevleri:

        Uygulama açma
        Uygulama kapatma
        Uygulama keşfi
        .lnk kısayollarının incelenmesi
    
    14.2. media_manager.py

        Medya işlemlerinin gerçekleştirilmesinden sorumludur.

        Örnek işlemler:

        Oynatma
        Duraklatma
        Sonraki parça
        Önceki parça
        Tekrarlama
    
    14.3. calculator.py

        Matematiksel ifadelerin hesaplanması amacıyla kullanılmaktadır.

    14.4. system_tools.py

        İşletim sistemi ile ilişkili yardımcı işlemleri içermektedir.

    14.5. clock.py

        Zaman ve saat ile ilgili işlemler için kullanılmaktadır.

------------15.UYGULAMA KEŞİF SİSTEMİ----------

    JARVIS'ın uygulama yönetiminde yalnızca sabit bir uygulama listesine bağlı kalmaması amacıyla uygulama keşif mekanizması geliştirilmiştir.

    Sistem Windows üzerindeki belirli konumlarda bulunan uygulama kısayollarını tarayabilmektedir.

    Genel süreç:

    Windows Uygulama Konumları
            │
            ▼
        Tarama
            │
            ▼
        .lnk dosyaları
            │
            ▼
    Kısayol hedefini bul
            │
            ▼
        .exe yolu
            │
            ▼
        Uygulama bilgisi

    Bu yapı sayesinde uygulama yönetiminin ilerleyen aşamalarda daha dinamik hale getirilmesi amaçlanmaktadır.

------------16.VERİ SETLERİ ----------
    Makine öğrenmesi modelinin eğitiminde farklı teknik konulara yönelik veri setleri kullanılmaktadır.

    datasets/
    │
    ├── ai/
    ├── algorithms/
    ├── cpp/
    ├── cybersecurity/
    ├── data_structures/
    ├── database/
    ├── linux/
    ├── python/
    ├── tech_dataset/
    └── web/

    Veri setlerinin temel amacı, modelin farklı teknik konu kategorilerini birbirinden ayırt edebilmesini sağlamaktır.

    Model eğitim süreci:

    Dataset
    │
    ▼
    Metin Verileri
    │
    ▼
    TF-IDF
    │
    ▼
    Özellik Matrisi
    │
    ▼
    Logistic Regression
    │
    ▼
    Eğitilmiş Model
    │
    ▼
    tech_model.pkl

------------17.PROJE DOSYA YAPISI ----------
    ai project/
    │
    ├── brain/
    │   ├── behavior.py
    │   ├── classifier.py
    │   ├── decision.py
    │   ├── entities.py
    │   ├── intent.py
    │   ├── memory.py
    │   └── router.py
    │
    ├── config/
    │   ├── app.json
    │   ├── entities.json
    │   ├── intent.csv
    │   └── intent.json
    │
    ├── datasets/
    │   ├── ai/
    │   ├── algorithms/
    │   ├── cpp/
    │   ├── cybersecurity/
    │   ├── data_structures/
    │   ├── database/
    │   ├── linux/
    │   ├── python/
    │   ├── tech_dataset/
    │   └── web/
    │
    ├── memory/
    │   └── user_profile.json
    │
    ├── models/
    │   ├── tech_model.pkl
    │   └── vectorizer.pkl
    │
    ├── tools/
    │   ├── app_manager.py
    │   ├── calculator.py
    │   ├── clock.py
    │   ├── media_manager.py
    │   └── system_tools.py
    │
    ├── main.py
    ├── train.py
    └── test.py

------------18.MODÜL SORUMLULUKLARI ----------
    
      Modül	                        Sorumluluk
    main.py	            → Uygulamanın ana çalışma akışını yönetir
    classifier.py       → Makine öğrenmesi ile metin sınıflandırması yapar
    decision.py	        → Model tahminlerini güven seviyesine göre değerlendirir
    intent.py	        → Kullanıcının amacını belirler
    entities.py	        → Kullanıcı mesajındaki ilgili varlığı belirler
    router.py	        → İsteği uygun işlem modülüne yönlendirir
    memory.py	        → Kullanıcı hafızasını yönetir
    app_manager.py	    → Windows uygulamalarını yönetir
    media_manager.py	→ Medya işlemlerini yönetir
    calculator.py	    → Matematiksel hesaplama işlemlerini gerçekleştirir
    system_tools.py	    → Sistem araçlarını sağlar
    clock.py	        → Zaman işlemlerini sağlar
    train.py	        → Makine öğrenmesi modelinin eğitim sürecini yürütür
    test.py	            → Proje bileşenlerinin test edilmesi amacıyla kullanılır

------------19.KULLANILAN TEKNOLOJİLER ----------
    Teknoloji / Kütüphane	Kullanım Alanı
    Python 3.13	            Ana programlama dili
    scikit-learn	        Makine öğrenmesi
    TfidfVectorizer	        Metin özellik çıkarımı
    LogisticRegression	    Metin sınıflandırması
    NumPy	                Sayısal işlemler ve sıralama
    Joblib	                Model ve vectorizer yükleme/kaydetme
    JSON	                Hafıza ve yapılandırma
    CSV	                    Intent ve veri setleri
    Windows araçları	    İşletim sistemi işlemleri
    Git	                    Sürüm kontrolü

------------20.KURUM----------
    20.1. Gereksinimler

    Projeyi çalıştırmak için:

    Windows işletim sistemi
    Python 3.13 veya üzeri
    pip
    Gerekli Python kütüphaneleri

    gerekmektedir.

    20.2. Kütüphanelerin Kurulması

    Proje dizininde aşağıdaki komut kullanılabilir:

    python -m pip install numpy joblib scikit-learn
    20.3. Projenin Çalıştırılması

    Ana program:

    python main.py

    Modelin yeniden eğitilmesi:

    python train.py

------------21.MEVCUT AGENT YAKLAŞIMI ----------

    Projenin mevcut sürümünde bağımsız yapay zekâ agent'ları bulunmamaktadır.

    Mevcut yapı daha çok modüler katman mimarisi üzerine kuruludur.

    Intent
    ↓
    Entity
    ↓
    Router
    ↓
    Tool

    Makine öğrenmesi ise ayrı bir sınıflandırma mekanizması olarak çalışmaktadır.

    İlerleyen sürümlerde görevlerin daha bağımsız hale getirilmesi ve aşağıdaki gibi görev tabanlı agent yapısına geçilmesi planlanmaktadır:

                        JARVIS
                        │
            ┌──────────────┼──────────────┐
            │              │              │
            ▼              ▼              ▼
    Memory Agent   System Agent   Media Agent
            │              │              │
            └──────────────┼──────────────┘
                        │
                        ▼
                    Task Management

    Bu yapı şu an proje içerisinde tamamlanmış bir özellik değil, gelecek mimari geliştirme planıdır.

------------22.GÜVENLİK VE KULLANICI ONAYI ----------

    Sistem üzerinde gerçekleştirilecek işlemlerin kullanıcı kontrolünde olması hedeflenmektedir.

    Özellikle:

    Dosya işlemleri
    Sistem değişiklikleri
    Uygulama yönetimi
    Hafıza değişiklikleri

    gibi işlemlerde sistemin gerektiğinde kullanıcıdan onay alması planlanmaktadır.

    Amaç, asistanın kullanıcı adına kontrolsüz işlemler gerçekleştirmesini önlemek ve kullanıcıya işlem üzerinde kontrol sağlamaktır.

------------23.GELECEK GELİŞTİRMELER----------

    Projenin sonraki geliştirme aşamalarında aşağıdaki özelliklerin eklenmesi planlanmaktadır:

    -Yapay Zekâ
        Daha kapsamlı veri setleri
        Model performansının geliştirilmesi
        Daha gelişmiş doğal dil işleme
        Online ve offline çalışma desteği
        LLM entegrasyonu
    
    -Hafıza
        Hafıza güncelleme sistemi
        Hafıza silme sistemi
        Bilgi değişikliklerinde kullanıcı onayı
        Daha gelişmiş kullanıcı profili
        Hafıza geçmişinin daha ayrıntılı tutulması
    
    -Agent Sistemi
        Memory Agent
        System Agent
        Media Agent
        Coding Agent
        Araştırma/Research Agent
        Merkezi görev yönetimi
    
    -Etkileşim
        Sesli komut desteği
        Wake-word sistemi
        Sesli yanıt sistemi
        Grafik kullanıcı arayüzü
    
    -Sistem Entegrasyonları
        Daha gelişmiş uygulama yönetimi
        Spotify entegrasyonu
        Dosya yönetimi
        Masaüstü organizasyonu

------------24.PROJENİN MEVCUT DURUMU----------

    JARVIS aktif olarak geliştirilen bir yazılım projesidir.

    Mevcut sürümde:

    Modüler Python mimarisi oluşturulmuştur.
    Intent sistemi oluşturulmuştur.
    Entity sistemi oluşturulmuştur.
    Router sistemi oluşturulmuştur.
    JSON tabanlı hafıza sistemi oluşturulmuştur.
    Windows uygulama yönetimi geliştirilmiştir.
    Uygulama keşif mekanizması geliştirilmiştir.
    TF-IDF tabanlı metin işleme sistemi oluşturulmuştur.
    Logistic Regression tabanlı sınıflandırma modeli oluşturulmuştur.
    Model ve vectorizer dosyaları oluşturulmuştur.
    Model tahminlerinin güven seviyesini değerlendiren decision sistemi oluşturulmuştur.

    Proje geliştirme süreci devam etmektedir.

------------25.SONUÇ----------

    JARVIS projesi; Python programlama dili, makine öğrenmesi, doğal dil tabanlı komut analizi, hafıza yönetimi ve işletim sistemi araçlarının bir arada kullanıldığı modüler bir masaüstü asistanı geliştirmeyi amaçlamaktadır.

    Projenin mevcut mimarisi, sistemin farklı bileşenlerinin birbirinden ayrılmasını ve bağımsız olarak geliştirilebilmesini sağlamaktadır.

    Makine öğrenmesi tarafında TF-IDF ve Logistic Regression kullanılarak teknik metinlerin sınıflandırılması gerçekleştirilirken; intent, entity ve router katmanları kullanıcı komutlarının analiz edilerek uygun araçlara yönlendirilmesini sağlamaktadır.

    Projenin ilerleyen aşamalarında hafıza sisteminin geliştirilmesi, sesli etkileşim özelliklerinin eklenmesi ve görev tabanlı agent mimarisine geçilmesi planlanmaktadır.

    Bu doğrultuda JARVIS, yalnızca belirli komutları yerine getiren bir program olmaktan ziyade; modüler, genişletilebilir ve kullanıcı odaklı bir yapay zekâ asistanı mimarisine dönüştürülmek üzere geliştirilmektedir.

    Git ve GitHub öğrenme çalışmalarım devam ediyor.
    Yeni model geliştirmeleri ayrı bir branch üzerinde deneniyor.

    Git öğrenme çalışması: dosya geçmişi ve değişiklik karşılaştırması.