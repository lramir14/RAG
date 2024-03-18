#using command line to setup the apikey:
#for /f "delims=" %x in (openaiapikey.txt) do set OPENAI_API_KEY=%x
import pytesseract
from pdf2image import convert_from_path
import fitz
import os

api_key_file = 'open_ai_key2.txt'
with open(api_key_file, 'r') as file:
    openai_api_key = file.read().strip()

from langchain_openai import ChatOpenAI
model = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-3.5-turbo")

#Run a test, but right now I don't have any tokens available. model.invoke("Who is the Mexican President in 2024?")
#So we continue with the code
#function to extract text from pdf
#def extract_text_from_pdf(pdf_path):
 #   doc = fitz.open(pdf_path)
  #  text = ""
   # for page in doc:
    #    text += page.get_text()
    #return text
#pdf_text = extract_text_from_pdf('path/to/document.pdf')
#build multivector retriever to produce summaries of tables and, optionally, text.
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain import hub

obj = hub.pull("rlm/multi-vector-retriever-summarization")

# Prompt
prompt_text = """You are an assistant tasked with summarizing tables and text. \ 
Give a concise summary of the table or text. Table or text chunk: {element} """
prompt = ChatPromptTemplate.from_template(prompt_text)

# Summary chain
model = ChatOpenAI(temperature=0, model="gpt-4")
summarize_chain = {"element": lambda x: x} | prompt | model | StrOutputParser()