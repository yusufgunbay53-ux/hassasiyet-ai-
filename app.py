import streamlit as st
import google.generativeai as genai
import time

# Sayfa Ayarları
st.set_page_config(page_title="PUBG Kod Bulucu", page_icon="🎯")

st.title("🎯 PUBG Mobile Hassasiyet Sorgu")
st.write("Sadece ünlü ismini girin.")

# Secrets kısmından API anahtarını alıyoruz
try:
    API_KEY = st.secrets["API_KEY"]
except Exception:
    st.error("Hata: Secrets kısmında API_KEY bulunamadı!")
    st.stop()

# İstek sınırı için zaman kontrolü
if 'last_request_time' not in st.session_state:
    st.session_state.last_request_time = 0

current_time = time.time()
cooldown = 180 # 3 dakika (180 saniye)

user_input = st.text_input("Ünlü İsmi:", placeholder="Örn: Ersin Yekin")

if st.button("KODU GETİR"):
    elapsed = current_time - st.session_state.last_request_time
    
    if elapsed < cooldown:
        kalan_sure = int((cooldown - elapsed) / 60)
        st.warning(f"Lütfen tekrar istek atmak için {kalan_sure + 1} dakika bekleyin.")
    elif user_input:
        try:
            # Google AI Yapılandırması
            genai.configure(api_key=API_KEY)
            
            # Hata aldığın 1.5-flash yerine en kararlı gemini-pro modelini kullanıyoruz
            model = genai.GenerativeModel('gemini-pro')
            
            sistem_komutu = f"Sen sadece PUBG Mobile hassasiyet kodu bulmakla görevli bir yapay zekasın. Kullanıcı ismi: {user_input}. Sadece 21 rakamdan oluşan X-XXXX-XXXXX-XXXX-XXXX-XXXX formatındaki kodu ver. Başka bir şey yazma."
            
            with st.spinner('Sorgulanıyor...'):
                response = model.generate_content(sistem_komutu)
                st.session_state.last_request_time = current_time
                
                # Sonucu ekrana yazdır
                st.success(f"{user_input} için bulunan kod:")
                st.code(response.text)
                
        except Exception as e:
            # Hata olursa ne olduğunu ekranda göster
            st.error(f"Hata detayı: {e}")
    else:
        st.warning("Lütfen bir isim girin.")

st.markdown("---")
st.caption("Not: Her 3 dakikada bir 1 istek atma hakkınız vardır.")
