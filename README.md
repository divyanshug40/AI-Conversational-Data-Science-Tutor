# Data Science Tutor - AI Chatbot 🤖

Welcome to the **Data Science AI Tutor**! 🚀

This application is your personalized, interactive AI-powered assistant designed to help you master **Data Science**. Whether you're just starting out or looking to expand your knowledge, this tutor is here to guide you through everything from **machine learning** to **data visualization** and **AI algorithms**. 🤖💡

Built using cutting-edge technologies like **Streamlit**, **Google Generative AI**, and **Langchain**, the AI tutor is capable of answering any data science-related queries in detail, with examples and clear explanations. Whether you're working on a project, need clarification on concepts, or just want to learn something new, this AI tutor will provide you with the knowledge and insights you need to succeed in the exciting world of data science! 📊📈

Dive in, ask questions, and let the AI tutor help you become a data science pro! 🌟

## Features ✨

- **Login**: Users can log in by providing a username, and their chat history is saved for future sessions.
- **Chat History**: The application saves and retrieves the chat history specific to each user.
- **Data Science Focus**: The AI tutor is specialized to provide help on topics related to **Data Science**, such as machine learning, data visualization, AI algorithms, and more.
- **Download Chat History**: Users can download their entire chat history in a text file for reference.
- **Delete Chat History**: Users can delete their chat history at any time.
- **AI Responses**: The AI will only answer questions strictly related to data science. If the question is not related, it will politely ask the user to ask a data science-related question.

## Requirements 📦

### Python Packages

The following Python libraries are required to run the application:

- `streamlit`: Web framework for creating the user interface.
- `google-generativeai`: Google Generative AI API for AI-based responses.
- `langchain`: Langchain to help manage chains of AI interactions.
- `dotenv`: To manage environment variables such as the Google API key.
- `os`: To interact with the file system.

You can install the required libraries by running:

```bash
pip install -r requirements.txt
```

### Google API Key Setup 🔑

To use the Google Generative AI service, you need to set up a **Google API key**. Follow these steps:

1. **Create a project** on the [Google Cloud Console](https://console.cloud.google.com/).
2. **Enable the Google Generative AI API** for your project.
3. **Create API credentials** and obtain your **API key**.
4. Create a `.env` file in the root directory of the project and add your API key like this:

```plaintext
google_token=YOUR_GOOGLE_API_KEY_HERE
```

## Usage 🚀

### Starting the Application

1. Ensure that you have your environment set up, including the API key as mentioned above.
2. To run the Streamlit app, use the following command:

    ```bash
    streamlit run app.py
    ```

This will start the Streamlit app, and you can access the application in your browser.

### User Flow 🧑‍💻

1. **Login**: Enter your username to start a new session. The application will load your previous chat history if available.
2. **Chat**: Ask questions related to data science in the chatbox. The AI will respond accordingly. Only data science-related questions will be answered.
3. **Manage Chat History**:
    * **Delete**: If you want to clear your chat history, click on the "Delete Chat History" button.
    * **Download**: You can download your chat history as a `.txt` file by clicking the "Download Chat History" button.

### Chat History Storage 💾

The application stores each user's chat history in a JSON file inside the `chat_history/` directory. The chat history is saved whenever a user interacts with the AI. Each entry in the history includes both the user's input and the AI's response.

If no previous chat history exists for a user, a new session is started, and the history is initialized as empty.

## Project Structure 📂

```bash
Data-Science-Tutor/
│
├── ai_tutor.py           # Main Streamlit app
├── .env                  # Environment file to store API key
├── chat_history/         # Directory where chat history JSON files are stored 
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Future Enhancements 🔮

- **User Authentication**: Implement more robust user authentication and session management.
- **Advanced AI Capabilities**: Integrate additional advanced data science tools for richer responses.
- **Data Science Resources**: Provide additional resources, such as tutorials or recommended readings, directly in the chat.

## Troubleshooting 🛠️

- If you encounter an error with the API key, make sure the `.env` file contains the correct API key, and the key is properly loaded using `dotenv`.
