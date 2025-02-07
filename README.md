# Multiple_pdf_Chatbot
This repository contains a PDF Question Answering System built using Streamlit, LangChain, ChromaDB, Google Generative AI Embeddings, and Groq LLM. It allows users to upload PDF documents and ask questions based on their content. The system retrieves relevant information using vector embeddings and provides accurate responses.
# PDF Question Answering System

This repository contains a **PDF-based Question Answering System** that enables users to upload PDF files and ask questions based on their content. The system leverages **LangChain, ChromaDB, Google Generative AI Embeddings, and Groq LLM** to retrieve and answer queries accurately.

## 🚀 Features
- **Context-based Question Answering**: Answers queries only from the provided documents.
- **Efficient Retrieval**: Uses **ChromaDB** and **Google Generative AI Embeddings** for semantic search.
- **Powerful LLM (Llama3-8b-8192)**: Provides detailed and relevant answers.
- **Interactive UI with Streamlit**: Simple and user-friendly interface.

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yashrj1310/PDF-QA-System.git
cd PDF-QA-System
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Set Up API Keys
Create a .env file in the root directory and add:
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
4️⃣ Run the Application
streamlit run app.py

📌 How It Works
Place your PDF files inside the specified folder.
The system embeds and indexes the PDFs using ChromaDB.
Enter a question in the UI.
The system retrieves relevant information and answers the question using Llama3-8b-8192.
📄 Example Queries
"Who is the president of India?"
"What is the SEBI circular?"
"Summarize the attention mechanism PDF."
🤝 Contributing
Feel free to fork this repository, make changes, and submit a pull request.
