import streamlit as st
import google.generativeai as genai
import time

# Sayfa yapılandırması
st.set_page_config(page_title="PUBG Kod Bulucu", page_icon="🎯")

# --- KULLANICI ARAYÜZÜ ---
st.title("🎯 PUBG Mobile Hassasiyet Sorgu")
st.write("Sadece ünlü ismini girin.")

# API ANAHTARIN (Kodun içine sabitlendi)
API_KEY = "AIzaSyC1SjL_kcah61pvh8Buxgj1lalHmO-v32A"

# --- 3 DAKİKA KURALI (Hız Sınırı) ---
if 'last_request_time' not in st.session_state:
    st.session_state.last_request_time = 0

current_time = time.time()
cooldown = 180  # 3 dakika (180 saniye)

# --- ANA İŞLEM ---
user_input = st.text_input("Ünlü İsmi:", placeholder="Örn: Ersin Yekin")

if st.button("KODU GETİR"):
    # Zaman kontrolü
    elapsed = current_time - st.session_state.last_request_time
    
    if elapsed < cooldown:
        kalan_sure = int((cooldown - elapsed) / 60)
        st.warning(f"Lütfen tekrar istek atmak için {kalan_sure + 1} dakika bekleyin.")
    elif user_input:
        try:
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel('gemini-pro')
            
            # SENİN HAZIRLADIĞIN ÖZEL KOMUT (SYSTEM PROMPT)
            sistem_komutu = f"""
            Sen sadece PUBG Mobile hassasiyet kodu bulmakla görevli bir yapay zekâsın.
            Başka hiçbir konuda cevap vermezsin.

            KULLANICI DAVRANIŞI:
            - Kullanıcı sadece bir ünlü ismi yazar: {user_input}
            - Sen bu ismi olduğu gibi alırsın.

            ZORUNLU İŞ AKIŞI:
            1) Arama motoru sorgusu oluştur: "@ {user_input} PUBG Mobile hassasiyet kodları"
            2) Bu sorguya göre bulunan içerikleri analiz et.
            3) Sadece 21 rakamdan oluşan X-XXXX-XXXXX-XXXX-XXXX-XXXX formatındaki kodu ver.
            4) Harf, metin, açıklama ekleme. Sadece kodu yaz.
            5) Kod bulunamazsa SADECE şunu yaz: KOD_BULUNAMADI
            6) Ünlüyü bulamazsan rütben (@) ile başlayarak kullanıcının ismine başla.
            """
            
            with st.spinner('Sorgulanıyor...'):
                response = model.generate_content(sistem_komutu)
                st.session_state.last_request_time = current_time # Zamanı güncelle
                
                # Sonucu ekrana yazdır
                st.code(response.text)
                
        except Exception:
            st.error("ters bir şey oldu") # Senin hata notun
    else:
        st.warning("Lütfen bir isim girin.")

# --- TASARIM NOTU ---
st.markdown("---")
st.caption("Not: Her 3 dakikada bir 1 istek atma hakkınız vardır.")
