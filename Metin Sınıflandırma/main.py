# Gerekli kütüphaneleri içe aktarma

import json

from google.cloud import translate_v2 as translate

# Dosyayı okuyarak kimlik bilgilerini alma

json_file_path = "kimlik.json"

with open(json_file_path) as json_file:

    credentials = json.load(json_file)

# API'ye bağlanma

translate_client = translate.Client.from_service_account_json("kimlik.json")

# Veri kümesini yükleme ve liste olarak tanımlama

veri_kumesi = [

    ("Ted'le tanıştın mı?", "How I Met Your Mother"),

    ("Tehlikede değilim, tehlike benim.", "Breaking Bad"),

    ("Vay anam babam be, burası resmen bir harika!", "The Walking Dead"),

]

# Veri kümesini genişletme

yeni_veri_kumesi = []

for metin, sinif in veri_kumesi:

    # Türkçe metni İngilizce'ye çevirme

    ceviri_1 = translate_client.translate(metin, target_language="en")["translatedText"]

    # İngilizce metni tekrar Türkçe'ye çevirme

    ceviri_2 = translate_client.translate(ceviri_1, target_language="tr")["translatedText"]

    # Oluşan çevirileri veri kümesine ekleme

    yeni_veri_kumesi.append((ceviri_1, sinif))

    yeni_veri_kumesi.append((ceviri_2, sinif))

# Genişletilmiş veri kümesinin kontrolü

for veri in yeni_veri_kumesi:

    print(veri)