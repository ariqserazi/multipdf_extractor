

import streamlit as st
import os
import google.generativeai as genai
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv() #loading all the env variables

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))



def get_pdf_text(pdf_docs):
   text = ""
   for pdf in pdf_docs:
      pdf_reader = PdfReader(pdf)
      for page in pdf_reader.pages:
         text+=page.extract_text()
   return text
def get_text_chunks(text):
   text_spilitter = RecursiveCharacterTextSplitter(chunk_size = 10000, chunk_overlap = 200)
   chunks = text_spilitter.split_text(text)
   return chunks
def get_vectore_store(text_chunks):
   embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
   vector_store  = FAISS.from_texts(text_chunks, embeddings)
   vector_store.save_local("faiss_index")
def get_conversational_chain():
   prompt_template = """
   Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in 
   provided context just say, "answer is not available in the context", dont't provide the the wrong answer \n \n
   Context: \n {context}?\n
   Question: \n{question}\n
   Answer:
   """
   llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-pro")  # Validate the model name
   prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
   chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
   return chain
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    new_db = FAISS.load_local("faiss_index",embeddings, allow_dangerous_deserialization= True)
    docs = new_db.similarity_search(user_question)
    
    chain  = get_conversational_chain()

    response = chain({
       "input_documents":docs, "question" : user_question}, return_only_outputs= True
    )
    print(response)
    st.write("Reply: ", response["output_text"])
def main():
   st.set_page_config("chat with multiple PDF")
   st.header("Chat With Multiple PDF using Gemini")
   user_question = st.text_input("Ask A Question From the Multiple Pdf files you have entered")
   models = genai.list_models()
   print([model.name for model in models])
      
   with st.sidebar:
      st.title("Menu: ")
      pdfdocs = st.file_uploader("Please upload as many pdfs as you want", accept_multiple_files=True)
      if st.button("Submit and Process"):
         with st.spinner("Processing...."):
            raw_text = get_pdf_text(pdfdocs)
            chunks = get_text_chunks(raw_text)
            get_vectore_store(chunks)

               
            st.success("Done")
   if user_question:
      user_input(user_question)




main()

# def get_gemini_response(input):
#    response = model.generate_content(input)
#    return response.text