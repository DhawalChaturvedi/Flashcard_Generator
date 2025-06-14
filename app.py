import streamlit as st
from flashcard_generator.file_processor import process_input
from flashcard_generator.flashcard_creator import create_flashcards_from_text
from flashcard_generator.exporter import export_flashcards
from flashcard_generator.database import save_flashcards, load_flashcards

st.title("Flashcard Generator")

uploaded_file = st.file_uploader("Upload .txt or .pdf", type=["txt", "pdf"])
input_text = st.text_area("paste content here:", height=200)
subject = st.selectbox("Optional: Select Subject", ["", "Biology", "History", "Computer Science"])

if st.button("Generate Flashcards"):
    with st.spinner("Generating flashcards..."):
        text = process_input(uploaded_file, input_text)    #Checks which type of file 
        flashcards = create_flashcards_from_text(text, subject) #creates the content
        save_flashcards(flashcards) #saves flashcards
        st.session_state["flashcards"] = flashcards

if "flashcards" in st.session_state:              #checks if flashcards exists
    flashcards = st.session_state["flashcards"]
    
    st.subheader("Generated Flashcards")
    for i, card in enumerate(flashcards):          #Displays each flashcards
        with st.expander(f"Flashcard {i+1}"):
            st.markdown(f"**Q:** {card['question']}")
            st.markdown(f"**A:** {card['answer']}")

    st.subheader("Export Options")
    export_flashcards(flashcards)

