# Flashcard_Generator
Flashcard Generator with LLM (Groq)

An AI-powered Streamlit application that generates educational flashcards from uploaded files content using LLaMA-3 via the Groq API.

---

#Features

- Upload `.txt` or `.pdf` educational content
- Paste text manually if preferred
- Choose an optional subject for context
- Generate 10–15 flashcards using LLaMA-3 (via Groq API)
- Display and export generated flashcards
- Session memory for consistent experience

---

#Setup Instructions

##1. Clone the Repository
```bash
git clone https://github.com/DhawalChaturvedi/Flashcard_Generator.git
cd flashcard-generator
```

##2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate     # For Windows: venv\Scripts\activate
```

##3. Install Dependencies
```bash
pip install -r requirements.txt
```

##4. Configure API Key
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

> Get your key from: https://console.groq.com/keys

---

##Usage

## Run the Streamlit App
```bash
streamlit run app.py
```

## In the browser:
- Upload a `.txt` or `.pdf` file **or** paste content into the text box
- Select a subject if desired (e.g., Biology, History)
- Click `Generate Flashcards`
- View the flashcards below
- Export them as text or CSV

---

##  File Structure

```
├── app.py
├── requirements.txt
├── .env                # (excluded from Git via .gitignore)
├── flashcard_generator/
│   ├── __init__.py
│   ├── file_processor.py
│   ├── flashcard_creator.py
│   ├── exporter.py
│   ├── database.py
│   └── llm_model.py
```

---

##  Sample Output

**Input Text:**
```
Newton's laws of motion describe the relationship between a body and the forces acting on it.
```

**Generated Flashcards:**
```
Q: What do Newton's laws of motion describe?
A: The relationship between a body and the forces acting on it.

Q: How many laws of motion did Newton propose?
A: Three.
```

---

## Security Notes

- Your API key should be stored in a `.env` file.
- Add `.env` to your `.gitignore` to prevent accidental uploads.
- Revoke and regenerate keys if accidentally committed.

---

##  License

This project is licensed under the [MIT License](LICENSE).

---

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request.
