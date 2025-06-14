import streamlit as st
import json
import csv
import io

def export_flashcards(flashcards):      #checks if flashcards are present are not
    if not flashcards:
        st.warning("No flashcards to export.")
        return

    # JSON Export the flashcards
    json_data = json.dumps(flashcards, indent=2)
    st.download_button(
        label="Download as JSON",
        data=json_data,
        file_name="flashcards.json",
        mime="application/json",
        key="download_json"
    )

    #  CSV Export the flashcards
    csv_buffer = io.StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=["question", "answer"])
    writer.writeheader()
    for card in flashcards:
        writer.writerow(card)
    st.download_button(
        label="Download as CSV",
        data=csv_buffer.getvalue(),
        file_name="flashcards.csv",
        mime="text/csv",
        key="download_csv"
    )

    # TXT Export the flashcards
    txt_buffer = io.StringIO()
    for i, card in enumerate(flashcards, start=1):
        txt_buffer.write(f"Q{i}: {card['question']}\nA{i}: {card['answer']}\n\n")
    st.download_button(
        label="Download as TXT",
        data=txt_buffer.getvalue(),
        file_name="flashcards.txt",
        mime="text/plain",
        key="download_txt"
    )
