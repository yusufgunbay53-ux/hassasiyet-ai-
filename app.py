import streamlit as st
import requests

st.title("🎯 PUBG Hassasiyet")
api_key = st.secrets.get("API_KEY")
user_input = st.text_input("Ünlü İsmi:")

if st.button("GETİR"):
    # Google'ın "yok" diyemeyeceği tüm kombinasyonlar
    yollar = [
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent",
        "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent",
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    ]
    
    basarili = False
    for url in yollar:
        try:
            full_url = f"{url}?key={api_key}"
            payload = {"contents": [{"parts": [{"text": f"{user_input} PUBG code 21 digits"}]}]}
            r = requests.post(full_url, json=payload, timeout=10)
            res = r.json()
            
            if "candidates" in res:
                st.code(res["candidates"][0]["content"]["parts"][0]["text"])
                st.success(f"Bağlantı Kuruldu!")
                basarili = True
                break
        except:
            continue
            
    if not basarili:
        st.error("Google şu an senin API anahtarını tüm modellerden kısıtlamış. Lütfen 1 saat bekleyip tekrar dene.")
        
