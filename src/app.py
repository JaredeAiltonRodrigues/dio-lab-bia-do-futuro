import streamlit as st
import pandas as pd
from agente import get_resposta

st.title("💰 EcoDom AI - Gestão Familiar")

# Simulando carga de dados
data = "Saldo: R$ 5.000 | Gastos recentes: Supermercado R$ 450, Streaming R$ 55"

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Como posso te ajudar com o orçamento hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.spinner("Pensando..."):
        resposta = get_resposta(data, prompt)
        st.session_state.messages.append({"role": "assistant", "content": resposta})
        st.chat_message("assistant").write(resposta)