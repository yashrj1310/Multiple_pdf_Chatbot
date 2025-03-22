# 📚 Multiple PDF Chatbot

This repository contains a **PDF Question Answering System** built using:
- **Streamlit** for an interactive UI.
- **LangChain** and **ChromaDB** for document retrieval.
- **Google Generative AI Embeddings** for semantic search.
- **Groq LLM (Llama3-8b-8192)** for generating accurate answers.

The system allows users to upload multiple PDF documents and ask context-specific questions based on their content.

---

## 🚀 Features

✅ **Context-based Question Answering**  
   - Answers queries only from the provided documents.  

✅ **Efficient Retrieval**  
   - Uses **ChromaDB** and **Google Generative AI Embeddings** to perform semantic search.  

✅ **Powerful LLM**  
   - Leverages **Llama3-8b-8192** from Groq for generating accurate and relevant responses.  

✅ **Interactive UI with Streamlit**  
   - Simple and user-friendly interface.

---

## 🛠️ Installation & Setup

Follow these steps to set up and run the application:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yashrj1310/PDF-QA-System.git
cd PDF-QA-System
pip install -r requirements.txt
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
streamlit run app.py
