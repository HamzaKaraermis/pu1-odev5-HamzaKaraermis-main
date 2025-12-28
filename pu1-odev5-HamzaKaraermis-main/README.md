[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/klEOC1SD)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22112345)
# P1-Ödev5 — Python Kafe Sipariş Sistemi 

Bu ödev, dönem boyunca öğrendiğimiz **dosya okuma ve YAZMA**, **input ile veri alma**, **döngüler (while)**, **sözlük (dict)** ve **f-string ile formatlama** konularını pekiştirmek için hazırlanmış kapsamlı bir tekrar ödevidir.

**Girdi:** Menü Dosyası (`data/menu.txt`) ve Kullanıcı Seçimleri (Konsol)  
**Çıktı:** Sipariş Fişi Dosyası (`adisyon.txt`)

---

## 📌 Teslim Bilgileri

- **Teslim tarihi:** 30.12.2025 Çarşamba 23:59 (Europe/Istanbul)  
- **Puan:** 5 puan (dönem toplamına %5 etkili)

---

## 1) Depo Yapısı

```
README.md                ← Talimatlar (DEĞİŞTİRMEYİN)
src/main.py              ← KODUNUZU YAZACAĞINIZ DOSYA (TODO'ları doldurun)
tests/test_main.py       ← Otomatik testler (DEĞİŞTİRMEYİN)
requirements.txt         ← Gerekli Python paketleri (DEĞİŞTİRMEYİN)
data/menu.txt            ← OKUNACAK MENÜ DOSYASI (DEĞİŞTİRMEYİN)
adisyon.txt              ← (Kodunuz bu dosyayı OLUŞTURACAKTIR)
```

> ⚠️ **Sadece `src/main.py` dosyasını düzenleyin.**

---

## 2) Veri Dosyası Biçimi (`data/menu.txt`)

Menü dosyasında her satır bir ürünü temsil eder ve ürün adı ile fiyat **virgül (,)** ile ayrılmıştır.

```
Cay, 15.0
Kahve, 45.0
Tost, 60.0
Pasta, 75.0
```

*Dosya okurken virgüllere ve boşluklara dikkat ederek parse işlemi yapmalısınız.*

---

## 3) Görevler (TODO Listesi)

`src/main.py` içinde tamamlamanız gereken **5 fonksiyon** vardır.

### TODO[1] — `menuyu_oku`

- **Parametre:** Dosya yolu (`str`)
- Belirtilen dosyayı okur ve satırları parçalar.
- Ürün adlarını anahtar, fiyatları değer (`float`) yaparak bir **SÖZLÜK (Dictionary)** oluşturur.
- Sözlüğü döndürür.

### TODO[2] — `siparis_al`

- **Parametre:** Menü sözlüğü
- `input()` ile kullanıcıdan sürekli ürün ismi ister (sonsuz döngü).
- `"q"` veya `"Q"` ile çıkış yapılır.

### TODO[3] — `hesabi_hesapla`

- **Parametre:** Sipariş listesi, Menü sözlüğü
- Sonuç: `(toplam_tutar, urun_adedi)`

### TODO[4] — `fisi_metne_dok`

- **Parametre:** Sipariş listesi, Menü sözlüğü, Toplam tutar
- `f-string` hizalama kullanılacaktır.

### TODO[5] — `fisi_kaydet`

- **Parametre:** Fiş metni (`str`)
- `adisyon.txt` dosyasına yazar.

---

## 4) Çalışma Ortamı

### A) GitHub Codespaces
1. **Code ▸ Codespaces ▸ Create codespace on main**
2. Terminal:
```bash
pytest -q
```

### B) Lokal (Miniconda + VSCode)
```bash
git clone <REPO-URL>
cd <repo-adi>
pip install -r requirements.txt
pytest -q
```

---

## 5) Programı Çalıştırma

```bash
python src/main.py
```

Program kullanıcıdan giriş almaz, veriyi doğrudan dosyadan okur.

---

## 6) Teslim

- Son **push**: **30 Aralık 2025 Pazar 23:59 (Europe/Istanbul)** öncesi.
- **EDERS yükleme:**
  - GitHub’dan **Download ZIP**
  - Zip içeriği:
    - `src/main.py`
    - `tests/`
    - `requirements.txt`
    - `README.md`
    - `.gitignore`

📌 **İki teslim zorunludur (GitHub Classroom + EDERS).**

---

---

## 7) Değerlendirme (5 puan)

| Görev | Puan |
|------|------|
| TODO[1] | 1.0 |
| TODO[2] | 1.0 |
| TODO[3] | 1.0 |
| TODO[4] | 1.0 |
| TODO[5] | 1.0 |
