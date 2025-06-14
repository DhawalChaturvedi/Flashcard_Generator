# flashcard_generator/llm_model.py

import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),                     #gets the API key
    base_url="https://api.groq.com/openai/v1"              #points to OpenAI compatible endpoint
)

def generate_llm_output(content, subject="General"):
    prompt = f"""
You are a helpful assistant that generates educational flashcards.               #A prompt to convert the input into Q&A format

Generate 10–15 flashcards in this format:

Q: What is the capital of France?
A: Paris.

Q: Who discovered gravity?
A: Isaac Newton.

Now generate flashcards from the following content:

{content}
"""

    try:
        print("Calling Groq API (LLaMA-3)...")
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=700                       #limits output size
        )
        output = response.choices[0].message.content.strip()    #gets the response from the model and removes and space from it
        print("Groq Output Sample:\n", output[:500])
        return output
    except Exception as e:
        print("Groq API Error:", e)             #if there is an error , then it prints and empty string
        return ""
