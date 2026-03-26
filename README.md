# 📄 AI PDF Chatboard (RAG Base Chatbot)

An intelligent **PDF Question-Answering Chatbot** built using **LangChain + ChromaDB + Mistral AI**.
Upload any PDF and interact with it using natural language — just like ChatGPT! 🤖

---
## Application Screenshots
<table>
<tr>
<td align="center">
<img src="https://github.com/bhautik2005/AI_pdf_chatboard/blob/6e1c0a0b87b63b6767edd06bc26154b07aa0a029/Screenshot%202026-03-25%20204939.png" width="450"><br>
 
</td>

<td align="center">
<img src="https://github.com/bhautik2005/AI_pdf_chatboard/blob/6e1c0a0b87b63b6767edd06bc26154b07aa0a029/Screenshot%202026-03-25%20211018.png" width="450"><br>
 
</td>
</tr>

<tr>
<td align="center">
<img src="https://github.com/bhautik2005/AI_pdf_chatboard/blob/6e1c0a0b87b63b6767edd06bc26154b07aa0a029/Screenshot%202026-03-25%20211035.png" width="450"><br>
 
</td>

<td align="center">
<img src="https://github.com/bhautik2005/AI_pdf_chatboard/blob/6e1c0a0b87b63b6767edd06bc26154b07aa0a029/Screenshot%202026-03-25%20211212.png" width="450"><br>
 
</td>
</tr>
</table>


## 🚀 Features

* 📂 Upload any PDF document
* 🧠 Automatic text chunking & embeddings
* 🔍 Semantic search using **ChromaDB**
* 💬 Ask questions and get accurate answers from PDF
* ⚡ Fast and efficient **RAG (Retrieval-Augmented Generation)** pipeline
* 🎯 Clean UI built with **Streamlit**

---

## 🧠 Tech Stack

### 🔗 LangChain Ecosystem

* langchain
* langchain-core
* langchain-community

### 🤖 LLM Providers

* langchain-mistralai
* langchain-openai
* langchain_google_genai
* openai
* mistralai

### 📦 Vector Database

* chromadb

### 🧩 Embeddings

* sentence-transformers (`all-MiniLM-L6-v2`)

### 📄 Document Processing

* pypdf
* unstructured
* beautifulsoup4
* lxml

### 📝 Text Processing

* tiktoken

### ⚙️ Backend & Environment

* python-dotenv
* pandas
* numpy

 

### 🎨 UI

* streamlit

---

## 🏗️ Project Structure

```
RAG_project/
│
├── app.py                  # Streamlit UI
├── main.py                 # CLI-based chatbot
├── create_database.py      # PDF → Embeddings → ChromaDB
├── chroma_db/              # Vector database
├── requirements.txt        # Dependencies
└── .env                    # API keys (not pushed)
```

---

## ⚙️ How It Works (RAG Pipeline)

1. 📄 Load PDF using PyPDFLoader
2. ✂️ Split text into chunks
3. 🧠 Convert text → embeddings
4. 📦 Store embeddings in ChromaDB
5. 🔍 Retrieve relevant chunks
6. 🤖 Send context to LLM (Mistral)
7. 💬 Generate final answer

---

## ▶️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI_pdf_chatboard.git
cd AI_pdf_chatboard
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create `.env` file:

```
MISTRAL_API_KEY=your_api_key_here
OPENAI_API_KEY=your_api_key_here
GOOGLE_API_KEY=your_api_key_here
```

---

## 🚀 Run the Application

### 🔹 Streamlit UI

```bash
streamlit run app.py
```

### 🔹 CLI Version

```bash
python main.py
```

---

## 💬 Example Usage

* Upload a PDF
* Ask questions like:

  * “What is deep learning?”
  * “Summarize chapter 2”
  * “Explain neural networks”

---

## 🔥 Future Improvements

* ✅ Multi-PDF support
* ✅ Chat history storage
* ✅ Authentication system
* ✅ Streaming responses (typing effect)
* ✅ Deployment (Streamlit Cloud / Render)

---

## 👨‍💻 Author

**Bhautik Gondaliya**
🚀 Aspiring AI Engineer | Backend Developer

---

## ⭐ Support

If you like this project:

👉 Star ⭐ the repository
👉 Share with others
👉 Contribute improvements

---
