import streamlit as st
import requests
import os

st.title("🤖 Document AI")

# Токен из секретов
GIGACHAT_TOKEN = os.getenv("GIGACHAT_TOKEN")

if not GIGACHAT_TOKEN:
    st.error("❌ Нет токена GIGACHAT_TOKEN в секретах!")
    st.stop()

text = st.text_area("Договор:")

if st.button("АНАЛИЗ"):
    st.info("Анализирую...")
    url
