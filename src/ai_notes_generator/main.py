import streamlit as st
from mysql.connector import IntegrityError

from ai_notes_generator.ai_service import generate_notes
from ai_notes_generator.auth_service import login_user, register_user
from ai_notes_generator.pdf_utils import extract_text


def show_register() -> None:
    username = st.text_input("Username", key="reg_user")
    password = st.text_input("Password", type="password", key="reg_pass")

    if st.button("Register"):
        if not username or not password:
            st.warning("Please enter username and password.")
            return

        try:
            register_user(username, password)
            st.success("Registered successfully.")
        except IntegrityError:
            st.error("Username already exists.")
        except Exception as exc:
            st.error(f"Registration failed: {exc}")


def show_login() -> None:
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        try:
            user = login_user(username, password)
            if user:
                st.session_state["user"] = username
                st.success("Logged in successfully.")
            else:
                st.error("Invalid username or password.")
        except Exception as exc:
            st.error(f"Login failed: {exc}")


def show_notes_generator() -> None:
    st.subheader(f"Welcome, {st.session_state['user']}")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        if st.button("Generate Notes"):
            try:
                text = extract_text(uploaded_file)

                if not text:
                    st.error("Could not extract text from this PDF.")
                    return

                with st.spinner("Generating notes with Mistral AI..."):
                    notes = generate_notes(text)

                st.success("Notes generated successfully.")
                st.write(notes)

            except Exception as exc:
                st.error(f"Note generation failed: {exc}")


def run_app() -> None:
    st.set_page_config(page_title="AI Notes Generator", page_icon="📄")
    st.title("AI Notes Generator")

    menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

    if menu == "Register":
        show_register()

    if menu == "Login":
        show_login()

    if "user" in st.session_state:
        show_notes_generator()


if __name__ == "__main__":
    run_app()