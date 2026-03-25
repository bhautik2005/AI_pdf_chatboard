from dotenv import load_dotenv
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma 
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings



load_dotenv()

# embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2-preview")
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriver = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":4,
        "fetch_k":10,
        "lambda_mult":0.5}, 
    
)


llm = ChatMistralAI(model="mistral-small-2506")

#prompt template
promt = ChatPromptTemplate.from_messages(
    [("system",
        """You are a helpful assistant for answering questions about deep learning. Use the following retrieved documents to answer the question. If you don't know the answer, say you don't know."""  ),
     ("human",
      """Context:{context}
      Question :{question}
      """ )
         ]
    
)
print("\n===== RAG system =====\n")

print("press 0 to extit")

while True:
    query = input("\nEnter your question: ")
    if query == "0":
        print("Exiting...")
        break
    
    docs = retriver.invoke(query)
    
    context = "\n".join([doc.page_content for doc in docs])
    
    # answer = llm(promt.format(context=context, question=query))
    
    # print("\nAnswer: ", answer)
    
    final_prompt = promt.invoke({
        "context": context, "question":query})
    
    response = llm.invoke(final_prompt)
    
    print(f"\nAI: {response.content}")

