import streamlit as st
import pandas as pd

st.write('''
# My first app
Hello *world!*
''')

nome = st.text_input('Digite o seu nome: ')
if len(nome) > 0:
  st.write ('Que nome legal!')
