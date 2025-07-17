import fitz
import requests
import json

# === 1. Extrage textul din PDF ===
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# === 2. Trimite contextul + întrebarea la Ollama ===
def ask_ollama(context, question, model="llama3"):
    prompt = f"""
Tu ești un asistent AI. Răspunde pe scurt și clar.

Context:
\"\"\"
{context}
\"\"\"

Întrebare: {question}
Răspuns:"""

url= "http://localhost:11434",

headers= {
    "Content-type": "application/json"
}

data= {
        "model": "llama2",
        "prompt": "Send a question?",
        "stream": False
    }

response= requests.post(url, headers= headers, data= json.dumps(data))

if response.status_code== 200:
    response_text= response.text
    data= json.loads(response_text)
    print(actual_response)
else:
    print("Error:", response.status_code, response.text)

# === 3. Exemplu de utilizare ===
if __name__ == "__main__":
    # Încarcă PDF-ul
    pdf_path = "C:\\Users\\asus\\Documents\\Scenariu Film.txt"
    context_text = extract_text_from_pdf(pdf_path)

    print("PDF încărcat. Pune o întrebare sau scrie 'exit' pentru a ieși.")

    while True:
        question = input("Tu: ")
        if question.lower() in ['exit', 'quit']:
            break
        answer = ask_ollama(context_text, question)
        print(f"Ollama: {answer}")
