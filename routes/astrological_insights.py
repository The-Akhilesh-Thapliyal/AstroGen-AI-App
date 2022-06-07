# Defines routes and logic for generating and responding to astrological queries, including birth charts and astrological insights.

from flask import Blueprint, render_template, request, jsonify
import pickle
import os
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from components.birth_chart import generate_birth_chart
from components.exception import CustomException
import sys

def load_vector_store(vector_path):
    """
    Loads the vector store from a pickle file.
    Parameters:
        vector_path (str): Path to the vector store file.
    Returns:
        FAISS: The loaded vector store.
    """
    try:
        with open(vector_path, "rb") as f:
            vector_store = pickle.load(f)
        return vector_store
    except FileNotFoundError as e:
        raise CustomException(e, sys)
    except Exception as e:
        raise CustomException(e, sys)

def create_llm_chain():
    """
    Creates an LLM chain using the Groq API to provide personalized astrological insights.
    Returns the LLM model and the prompt template.
    """
    try:
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ API Key is missing")

        llm = ChatGroq(groq_api_key=groq_api_key, model_name="gpt-3")

        prompt = ChatPromptTemplate.from_template(
            """
            You are an expert astrologer. Given the astrological context from the user's birth chart, planetary effects and related documents, provide a personalized and insightful astrological response to their query.
            
            Birth Chart Details: 
            {birth_chart}
            
            Planetary Effects:
            {effects}
            
            Relevant Astrological Literature Context:
            {context}
            
            Based on the above, respond to the following user query in detail:
            User Query: {input}
            """
        )
        return llm, prompt
    
    except Exception as e:
        raise CustomException(e, sys)

# Blueprint for astrological insights routes
astrological_insights_bp = Blueprint('astrological_insights', __name__)


@astrological_insights_bp.route('/astrological_insights', methods=['GET', 'POST'])
def astrological_insights():
    """
    Handle POST request to generate a birth chart and provide astrological insights.
    Expects user details as input and returns birth chart information along with a detailed astrological response.
    """
    if request.method == 'POST':
        try:
            user_data = {
                'name': request.form['name'],
                'dob': request.form['dob'],
                'time_of_birth': request.form['time_of_birth'],
                'place_of_birth': request.form['place_of_birth'],
                'gender': request.form['gender'],
                'query': request.form['query']
            }

            birth_chart, effects = generate_birth_chart(user_data)

            vector_path = "vector_embedding.pkl"
            vectors = load_vector_store(vector_path)

            llm, prompt = create_llm_chain()
            document_chain = create_stuff_documents_chain(llm, prompt)
            retriever = vectors.as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, document_chain)

            relevant_documents = retriever.get_relevant_documents(user_data['query'])
            context = " ".join([doc.page_content for doc in relevant_documents])

            user_prompt = {
                "birth_chart": birth_chart,
                "effects": effects,
                "context": context,
                "input": user_data['query']
            }

            response = retrieval_chain.invoke(user_prompt)

            detailed_answer = response.get('answer', 'No astrological insights available at this time.').replace("**", "")

            return jsonify({
                'answer': detailed_answer,
                'birth_chart': birth_chart,
                'effects': effects
            })
        except Exception as e:
            raise CustomException(e, sys)

    return render_template('index.html')