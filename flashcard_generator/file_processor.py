import PyPDF2

def process_input(uploaded_file, input_text):                   #Function to process the input and extract meaningful chunks
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):                #checks if it is pdf or not  
            pdf_reader = PyPDF2.PdfReader(uploaded_file)       #reads the pdf file
            return "\n".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())   #extracts the text and joins them together
        else:
            return uploaded_file.read().decode("utf-8")      #reads the content of a txt file and decodes the bytes into string
    return input_text
