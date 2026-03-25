# load pdf 
# split into chunks 
# create embeddings 
# store into chroma 

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma 
from dotenv import load_dotenv

load_dotenv()

# Load PDF
data = PyPDFLoader("document_loader/deeplearning.pdf")
docs = data.load()

# Split
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(docs)

# Embeddings (NO LIMIT 🚀)
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Store
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

print("✅ Database created successfully!")