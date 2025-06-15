import streamlit as st
from clima import pegar_clima

API_KEY = "4fb40ee2aebbc14f7794f2d3fbb22f4a"

st.title("🌦️ Dashboard de Clima")

cidade = st.text_input("Digite o nome da cidade")

if cidade:
    dados = pegar_clima(cidade, API_KEY)

    if dados:
        st.subheader(f"Clima em {dados['cidade']}")
        st.metric("🌡️ Temperatura", f"{dados['temperatura']}°C")
        st.metric("🥵 Sensação Térmica", f"{dados['sensacao']}°C")
        st.metric("💧 Umidade", f"{dados['umidade']}%")
        st.success(f"Descrição: {dados['descricao']}")

else:
    st.error("Cidade não encontrada ou erro na API")  