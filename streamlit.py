import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('输入一种动物')

if st.button('检查可用性'):
    have_it = animal.lower() in animal_shelter
    '我们有这种动物！' if have_it else '我们没有这种动物。'