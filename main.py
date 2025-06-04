# import chromadb 
# from chromadb.utils import embedding_functions

# default_df = embedding_functions.DefaultEmbeddingFunction()

# chroma_client = chromadb.Client()

# collection = chroma_client.get_or_create_collection(name="my_collection", embedding_function=default_df)

# collection.add(documents=["The weather is nice today", "Cats are very independent pet."], ids=["id1", "id2"])

# result = collection.query(query_texts=["Is today a perfect weather?"], n_results=2)

# print(result)

# main.py

import os
import streamlit as st
from dotenv import load_dotenv

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader


prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a world's best AI Career Advisor with 20+ years of experience.

Answer the user's question using ONLY the following context from the career knowledge base:

------------------
{context}
------------------

Answer clearly and helpfully. Avoid general advice. Be specific.

Question: {question}
Answer:
"""
)

# Load .env
load_dotenv()

# Setup Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)

# Load knowledge from text file
def load_documents_from_txt(path):
    loader = TextLoader(path)
    docs = loader.load()
    
    # Split large text into chunks for better embedding
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    split_docs = splitter.split_documents(docs)
    return split_docs

docs = load_documents_from_txt("career_docs/software_guide.txt")

# Embed using lightweight model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create or load ChromaDB
vectordb = Chroma.from_documents(docs, embedding_model, persist_directory="./chroma_db")
vectordb.persist()

# Retrieval QA
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=False,
    chain_type_kwargs={"prompt": prompt_template}
)

# Streamlit UI
st.set_page_config(page_title="Career Guide AI", page_icon="💼", layout="centered")
st.title("💼 Career Guide AI")

uploaded_file = st.file_uploader("📄 Upload a PDF with career data (optional):", type=["pdf"])

if uploaded_file:
    with open("temp_upload.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    loader = PyPDFLoader("temp_upload.pdf")
    pdf_docs = loader.load_and_split()
    
    # Add to Chroma
    vectordb.add_documents(pdf_docs)
    vectordb.persist()
    

question = st.text_input("🔍 Ask your career question:")

if question:
    with st.spinner("Thinking..."):
        answer = qa_chain.run(question)
        st.markdown("### 💡 Answer:")
        st.write(answer)

    skills = st.text_input("Want personalized advice?", placeholder="Enter your skills..")

    if skills and st.button("Get details"):
        with st.spinner("Analyzing..."):
            response = qa_chain.run(f"My skills are: {skills}. What career roles suit me?")
            st.markdown("### 🎯 Personalized Career Advice:")
            st.write(response)
