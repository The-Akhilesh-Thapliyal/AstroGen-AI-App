# Contains functionality to create and save vector embeddings for astrological documents using FAISS.

import pickle
import time
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from components.exception import CustomException
import sys

def create_vector_embedding(output_path="vector_embedding.pkl", documents_path="knowledge_base", model_name="nomic-embed-text"):
    """
    Creates vector embeddings from documents and saves them as a pickle file.
    Parameters:
        output_path (str): Path to save the embeddings.
        documents_path (str): Path to the directory containing documents.
        model_name (str): Name of the embedding model.
    """
    try:
        start_time = time.time()
        
        embeddings = OllamaEmbeddings(model=model_name)

        loader = PyPDFDirectoryLoader(documents_path)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        final_documents = text_splitter.split_documents(docs)

        vectors = FAISS.from_documents(final_documents, embeddings)

        with open(output_path, "wb") as f:
            pickle.dump(vectors, f)

        print(f"Vector embeddings saved to {output_path}")

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Time taken for execution: {elapsed_time:.2f} seconds")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        create_vector_embedding(output_path="vector_embedding.pkl", documents_path="knowledge_base", model_name="nomic-embed-text")
    except Exception as e:
        raise CustomException(e, sys)