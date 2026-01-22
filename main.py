import streamlit as st
import requests

st.title("🤖 Document AI Екатеринбург")

# Твой токен (спрячем позже)
GIGACHAT_TOKEN = "ТВОЙ_GIGACHAT_ТОКЕН"

url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

text = st.text_area("Вставь договор:", height=300)

if st.button("🔍 АНАЛИЗ"):
    headers = {
        "Authorization": f"Bearer {GIGACHAT_TOKEN}",
        "Content-Type": "application/json"
    }
    payload
