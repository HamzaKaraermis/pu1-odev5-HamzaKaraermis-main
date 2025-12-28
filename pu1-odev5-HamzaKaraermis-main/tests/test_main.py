import pytest
import sys
import os
from pathlib import Path
from unittest.mock import patch

# src klasörünü path'e ekle
sys.path.append(str(Path(__file__).parent.parent / "src"))

import main

# Test sırasında oluşturulacak geçici dosyalar
TEMP_MENU = "test_menu.txt"
TEMP_ADISYON = "adisyon.txt"

def setup_module(module):
    """Test modülü başlarken geçici bir menü dosyası oluştur."""
    with open(TEMP_MENU, "w", encoding="utf-8") as f:
        f.write("TestUrun, 10.0\n")
        f.write("PahaliUrun, 100.50\n")

def teardown_module(module):
    """Testler bitince temizlik yap."""
    if os.path.exists(TEMP_MENU):
        os.remove(TEMP_MENU)
    if os.path.exists(TEMP_ADISYON):
        os.remove(TEMP_ADISYON)

def test_todo1_menuyu_oku():
    """TODO[1]: Menüyü dosyadan okuma ve parse etme testi"""
    menu = main.menuyu_oku(TEMP_MENU)
    
    assert isinstance(menu, dict), "Dönüş tipi sözlük (dict) olmalı"
    assert "TestUrun" in menu
    assert menu["TestUrun"] == 10.0
    assert "PahaliUrun" in menu
    assert menu["PahaliUrun"] == 100.50

def test_todo2_siparis_al():
    """TODO[2]: Input döngüsü testi (Mock kullanılarak)"""
    menu = {"Cay": 15.0, "Tost": 60.0}
    
    # Kullanıcı sırasıyla: "Cay", "YanlisUrun", "Tost", "q" girmiş
    inputs = ["Cay", "YanlisUrun", "Tost", "q"]
    
    with patch('builtins.input', side_effect=inputs):
        siparisler = main.siparis_al(menu)
    
    assert isinstance(siparisler, list)
    assert "Cay" in siparisler
    assert "Tost" in siparisler
    assert "YanlisUrun" not in siparisler
    assert len(siparisler) == 2

def test_todo3_hesabi_hesapla():
    """TODO[3]: Hesaplama ve Tuple dönüşü testi"""
    menu = {"Cay": 15.0, "Tost": 60.0}
    siparisler = ["Cay", "Cay", "Tost"] # 15 + 15 + 60 = 90
    
    sonuc = main.hesabi_hesapla(siparisler, menu)
    
    assert isinstance(sonuc, tuple), "Sonuç (toplam, adet) şeklinde tuple olmalı"
    toplam, adet = sonuc
    
    assert adet == 3
    assert abs(toplam - 90.0) < 0.001

def test_todo4_fisi_metne_dok():
    """TODO[4]: Fiş formatlama (String işlemi) testi"""
    menu = {"Cay": 10.0}
    siparisler = ["Cay"]
    toplam = 10.0
    
    metin = main.fisi_metne_dok(siparisler, menu, toplam)
    
    assert isinstance(metin, str)
    assert "PYTHON KAFE" in metin
    assert "Cay" in metin
    assert "10.00" in metin # .2f format kontrolü
    assert "TOPLAM" in metin

def test_todo5_fisi_kaydet():
    """TODO[5]: Dosya oluşturma testi"""
    # Önce varsa silelim
    if os.path.exists(TEMP_ADISYON):
        os.remove(TEMP_ADISYON)
        
    fake_content = "TEST FISI ICERIGI"
    main.fisi_kaydet(fake_content)
    
    assert os.path.exists(TEMP_ADISYON), "Dosya oluşturulmadı"
    
    with open(TEMP_ADISYON, "r", encoding="utf-8") as f:
        icerik = f.read()
    
    assert icerik == fake_content