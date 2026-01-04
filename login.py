# app/login.py
import streamlit as st

st.set_page_config(page_title="Login | MMR Consultoria", layout="centered")

st.title("🔐 Acesso Restrito")
st.write("Informe o código da empresa, e-mail e senha.")

codigo = st.text_input("Código da Empresa:")
email = st.text_input("E-mail:")
senha = st.text_input("Senha:", type="password")

if st.button("Entrar"):
    if codigo and email and senha:
        st.success("Login realizado com sucesso!")
        # aqui redirecionar para a página interna / Home.py
    else:
        st.error("Por favor, preencha todos os campos.")
