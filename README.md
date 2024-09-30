# AstroGen AI App

AstroGen AI is an astrological web application that generates personalized astrological insights based on a user's birth details and queries. Utilizing advanced AI models, including FAISS vector storage and Langchain, the app provides meaningful insights by integrating traditional astrological principles with modern machine learning technology.

## Features

- **Personalized Birth Charts**: Generate birth charts based on user data (name, date of birth, time of birth, place of birth, gender).
- **Astrological Document Retrieval**: Retrieve relevant astrological insights using a document retrieval chain powered by FAISS and Langchain.
- **Detailed Insights**: Display birth chart details, planetary effects, and interpretations derived from querying large language models (LLMs).
- **User-Friendly Interface**: Built using a Flask backend, with an intuitive HTML/CSS frontend for smooth user interaction.

## Demo

**App in Action**  
![GIF](https://github.com/user-attachments/assets/18a38bb1-00ca-43a2-bb1b-ebf7ab56f964)

## Screenshots

### 1. Home Page
Welcome page guiding users to the astrological insights section.  
![Home Page](https://github.com/user-attachments/assets/d5e296ef-b26a-47e7-931c-494c55406e8c)

### 2. Astrological Insights - User Form
Form where users input their birth details and astrological queries.  
![Astrological Insights - Form](https://github.com/user-attachments/assets/a48f45b8-961c-4bb2-b924-24d5f58831d4)

### 3. Astrological Insights - Birth Chart and Planetary Effects
Displays the generated birth chart and associated planetary effects.  
![Astrological Insights - Birth Chart and Planetary Effects](https://github.com/user-attachments/assets/35953948-4d68-485b-be1e-cc397453767f)

### 4. Astrological Insights - Answer
Personalized astrological insights and answers to the user’s query.  
![Astrological Insights - Answer](https://github.com/user-attachments/assets/9f358aa3-0c61-4684-9e6c-3339190769f7)

## Project Structure

The project is organized as follows:

### 1. **app.py**
Core application file. It defines the Flask web framework, manages the routing, and handles API requests. This file is responsible for handling the input data (birth details and queries), retrieving insights, and returning results.

### 2. **birth_chart.py**
This module calculates the birth chart by assigning planets to astrological houses based on birth data. It contains classes like `Planet`, `House`, and `BirthChart` to structure the astrological data and compute planetary effects.

### 3. **embedding.py**
Handles pre-calculated vector embeddings of astrological documents and literature. These embeddings allow the app to retrieve relevant information when generating insights based on the user’s query.

### 4. **Templates (HTML Files)**
- **home.html**: Displays the welcome page, introducing users to the app.
- **index.html**: Main form page where users input their birth details and query. It also displays results, including the birth chart, planetary effects, and generated insights.

### 5. **styles.css**
Custom styles used to make the web application visually appealing, ensuring a modern and clean user interface.

## Technologies Used

### 1. **Flask**
   - Flask serves as the web framework, allowing for routing, handling form submissions, and rendering HTML templates.

### 2. **FAISS (Facebook AI Similarity Search)**
   - FAISS is used for storing and retrieving astrological document embeddings. It allows the app to query large amounts of data efficiently when generating astrological insights.

### 3. **Langchain**
   - Langchain creates a retrieval chain that processes user queries and integrates them with astrological documents stored in the FAISS vector store to provide relevant insights from large language models.

### 4. **HTML/CSS**
   - The frontend of the app is built with HTML and CSS for a responsive, easy-to-navigate interface. Bootstrap 5 is used for additional styling and layout features.

### 5. **Bootstrap 5**
   - Provides responsive design components, ensuring a seamless user experience across different devices.

### 6. **JavaScript/jQuery**
   - JavaScript and jQuery handle form submission asynchronously, allowing dynamic content updates and improved user experience by showing insights without page reloads.

### 7. **Python**
   - Python is the primary language used for the backend logic, including birth chart generation and the integration of FAISS and Langchain.

## How It Works

1. **Birth Chart Generation**  
   The app generates a birth chart based on user input (date, time, and place of birth). Using astrological principles, it calculates planetary positions and their effects on different aspects of life.

2. **Document Retrieval with FAISS**  
   Pre-embedded astrological documents are stored in a FAISS vector store. When a user submits an astrological query, the vector store retrieves the most relevant documents.

3. **Langchain and LLM Insights**  
   The Langchain library processes user queries. It retrieves the necessary astrological knowledge from the FAISS store, integrates it with the user’s birth chart, and queries a large language model (LLM) to generate personalized insights.

## Acknowledgments

- **Pt. Radhakrishna Shrimali’s Lal Kitab**: A traditional source of astrological knowledge used for creating the astrological knowledge base embedded in the app.

## About Me

Hello, I'm Akhilesh Thapliyal!

## Contact

- **Email:** akhilesh.thedev@gmail.com
- **LinkedIn:** www.linkedin.com/in/akhilesh-thapliyal
- **GitHub:** https://github.com/The-Akhilesh-Thapliyal
