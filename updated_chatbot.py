# traditional rag with prompt with ,  st and ,single creating embeddding


import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")
# Load environment variables
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="Llama3-8b-8192"
)

# Define prompt
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.
    
    <context>
    {context}
    <context>
    
    Question: {input}
    """
)

persist_directory = "Chroma_DB_update"

# Function for vector embedding using ChromaDB
def load_or_create_retriever(pdf_folder_path):
    if os.path.exists(persist_directory):
        vectors = Chroma(persist_directory=persist_directory, 
                         embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
        print("Using existing Chroma DB")
        return vectors.as_retriever(search_kwargs={"k": 3})
    
    documents = []
    for file in os.listdir(pdf_folder_path):
        if file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder_path, file)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    chunked_documents = text_splitter.split_documents(documents)
    
    vectors = Chroma.from_documents(
        documents=chunked_documents,
        embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
        persist_directory=persist_directory
    )  
    # vectors.persist()      now updated chroma -> doesnt need to stored in disk by default it is storing ,not happening before
    print("Created new Chroma DB")
    return vectors.as_retriever(search_kwargs={"k": 3})

# Function to process a query using existing retriever
def ask_question(retriever, question):
    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({'input': question})
    return response['answer']

# Streamlit UI setup

pdf_folder_path = r"C:\Users\lenovo\Desktop\Project\Agentic_ai\Static"
retriever = load_or_create_retriever(pdf_folder_path)
q1 ="who is president of india?"
q2="what is attention model?"
q3="what is sebi circular?"
q4 = "what are Core activities of Depositories  mention in document?"
q5 = "can you summarize this attention pdf"
q6 = "can u summarize this CSCRF sebi circular pdf ?"
q7 = "can u summarize this CSCRF sebi circular ?"
q8 = "Can you please summarize sebi document dated Aug 20,2024 ?"
# query = " What's the deadline for implmenting guideliens in CSCRF??"
# answer = ask_question(retriever,q7)

# print("Answer",answer)


# Streamlit UI setup
st.title("PDF Question Answering System")
st.write("Ask a question related to the content of the uploaded PDF documents.")

question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    answer = ask_question(retriever,question)
    st.write("**Answer:**", answer)


