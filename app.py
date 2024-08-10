import streamlit as st
import string
import secrets

def generate_password(length, uppercase, lowercase, numbers, special_chars):
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if numbers:
        chars += string.digits
    if special_chars:
        chars += string.punctuation
    
    if chars == '':
        return "Selecciona al menos un tipo de carácter."  # Error message kept in Spanish
    
    return ''.join(secrets.choice(chars) for _ in range(length))

st.set_page_config(page_title="Random Password Generator", page_icon="👁️‍🗨️", layout="centered")

with st.container():
    st.header("Hola👋")  # Greeting kept in Spanish
    st.title('Generador de Contraseñas Aleatorias')  # Title kept in Spanish

    length = st.slider('Longitud de la Contraseña', min_value=8, max_value=32, value=12)  # Slider label kept in Spanish
    uppercase = st.checkbox('Incluir letras mayúsculas', value=True)  # Checkbox label kept in Spanish
    lowercase = st.checkbox('Incluir letras minúsculas', value=True)  # Checkbox label kept in Spanish
    numbers = st.checkbox('Incluir números', value=True)  # Checkbox label kept in Spanish
    special_chars = st.checkbox('Incluir caracteres especiales', value=True)  # Checkbox label kept in Spanish

    # Button to generate password
    if st.button('Generar Contraseña'):  # Button text kept in Spanish
        password = generate_password(length, uppercase, lowercase, numbers, special_chars)
        st.session_state.password = password  # Store in session state

    # Display the generated password if it exists
    if 'password' in st.session_state:
        st.text_input('Contraseña Generada', st.session_state.password, key='password_display', disabled=True)  # Label kept in Spanish
        if st.button('Aceptar contraseña'):  # Button text kept in Spanish
            st.write(st.session_state.password)