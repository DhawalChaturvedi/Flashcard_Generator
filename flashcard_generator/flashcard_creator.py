from .llm_model import generate_llm_output
import re

def parse_flashcards(output_text: str):
    flashcards = []
    matches = re.findall(r"Q:\s*(.*?)\s*A:\s*(.*?)(?=\nQ:|\Z)", output_text, re.DOTALL)    #using regex to find Q/A pairs
    for question, answer in matches:                                                       #gives a tuple of Q&A
        question = question.strip()                                                        #removes whitespace from question
        answer = answer.strip()                                                            #removes whitespace from answer
        if question and answer:
            flashcards.append({"question": question, "answer": answer})
    return flashcards

def chunk_text(text, max_words=500):
    words = text.split()    #Splits the text
    return [' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)] #creates chunks of less than 500 words

def create_flashcards_from_text(text: str, subject: str = "General"):      #function to create flashcards
    chunks = chunk_text(text)      #words are stored as max 500 word chunk
    all_flashcards = []            #stores cards

    for idx, chunk in enumerate(chunks):
        print(f"Processing chunk {idx + 1} of {len(chunks)}...")
        raw_text = generate_llm_output(chunk, subject)  #chunk is sent to LLM
        parsed = parse_flashcards(raw_text)             #o/p in the form of Q&A
        all_flashcards.extend(parsed)                   #these are added to the list above

    return all_flashcards
