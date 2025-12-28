"""
Ödev 5: Python Kafe Sipariş Sistemi (Genel Tekrar)
Konular: file read/write, input, while, dict, list, tuple, f-string
"""

MENU_DOSYASI = "data/menu.txt"
CIKIS_DOSYASI = "adisyon.txt"

# TODO[1]: Menüyü dosyadan okuyup sözlük olarak döndüren fonksiyonu yazın.
def menuyu_oku(dosya_yolu):
    """
    Parametre: dosya_yolu (str)
    Dosya formatı: "Urun, Fiyat" (örn: "Cay, 15.0")
    Bu dosyayı okur, satırları parçalar ve şu sözlüğü döndürür:
    {"Cay": 15.0, "Tost": 60.0, ...}
    Return: dict
    """
    # Kod buraya gelecek
    pass

# TODO[2]: Kullanıcıdan input alarak sipariş listesi oluşturan fonksiyonu yazın.
def siparis_al(menu):
    """
    Parametre: menu (dict)
    İşleyiş:
      - Sonsuz döngü (while True) kurun.
      - Kullanıcıya "Ürün seç (Çıkış için 'q'):" diye sorun (input).
      - 'q' veya 'Q' girilirse döngüyü kırın (break).
      - Girilen ürün menüde varsa listeye ekleyin, "Eklendi" yazın.
      - Yoksa "Menüde yok!" yazın.
    Return: Sipariş listesi (list of str) -> örn: ["Cay", "Tost"]
    """
    # Kod buraya gelecek
    pass

# TODO[3]: Siparişlerin toplam tutarını ve adedini hesaplayan fonksiyonu yazın.
def hesabi_hesapla(siparis_listesi, menu):
    """
    Parametreler: siparis_listesi (list), menu (dict)
    Return: (toplam_tutar, urun_adedi) şeklinde TUPLE
    """
    # Kod buraya gelecek
    pass

# TODO[4]: Fiş metnini formatlı şekilde hazırlayan fonksiyonu yazın.
def fisi_metne_dok(siparis_listesi, menu, toplam_tutar):
    """
    Siparişleri ve toplamı şık bir string haline getirir.
    f-string ile hizalama kullanın (örn: f"{fiyat:>10.2f}").
    
    Örnek çıktı (string içinde \n karakterleri olmalı):
    --- PYTHON KAFE ---
    Cay            15.00
    Tost           60.00
    -------------------
    TOPLAM:        75.00
    """
    # Kod buraya gelecek
    pass

# TODO[5]: Fiş metnini dosyaya yazan fonksiyonu yazın.
def fisi_kaydet(fis_metni):
    """
    Parametre: fis_metni (str)
    'adisyon.txt' dosyasına yazma modunda (w) kaydeder.
    Return: None
    """
    # Kod buraya gelecek
    pass


# --- ANA PROGRAM ---
if __name__ == "__main__":
    print("--- Hoşgeldiniz ---")
    
    # 1. Menüyü Dosyadan Oku
    menu = menuyu_oku(MENU_DOSYASI)
    
    # Eğer dosya okunamazsa veya boşsa hata vermemesi için kontrol
    if menu:
        print("MENÜ:", menu)
        
        # 2. Siparişleri al
        siparisler = siparis_al(menu)
        
        # 3. Hesapla
        tutar, adet = hesabi_hesapla(siparisler, menu)
        
        # 4. Fiş metnini hazırla
        metin = fisi_metne_dok(siparisler, menu, tutar)
        
        # Ekrana da basalım
        print("\n--- ÖNİZLEME ---")
        print(metin)
        
        # 5. Dosyaya kaydet
        fisi_kaydet(metin)
        print(f"\nFiş '{CIKIS_DOSYASI}' dosyasına kaydedildi.")
    else:
        print("Menü yüklenemedi, program sonlanıyor.")