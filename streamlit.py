import streamlit as st

st.title("Hello")

num1 = st.number_input("Digite o primeiro número: ")
num2 = st.number_input("Digite o segundo número: ")

if st.button("Soma"):
    resultado = num1 + num2
    st.text("Resultado")
    st.title(resultado)

elif st.button("Subtração"):
    resultado = num1 - num2
    st.text("Resultado")
    st.title(resultado)

elif st.button("Multiplicação"):
    resultado = num1 * num2
    st.text("Resultado")
    st.title(resultado)

elif st.button("Divisão"):
    resultado = num1 - num2
    st.text("Resultado")
    st.title(resultado)