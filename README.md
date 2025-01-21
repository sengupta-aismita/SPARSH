# SPARSH - Intelligent chatbot for multiple industries

Try Our CHATBOT - https://nishanroy561.github.io/SPARSH-URL/
## Overview

This repository contains SPARSH, an advanced NLP-based chatbot designed to cater to four major industries:

- **Healthcare**
- **E-commerce**
- **Telecommunication**
- **Banking**

SPARSH handles user queries with ease, leveraging FastAPI for server-side functionality. It integrates with Dialogflow and external APIs to deliver intelligent and contextual responses.

## Features

- **Multi-Industry Support**: Customized responses and workflows for each industry.
- **Intent Matching**:
  - **Dialogflow ES** for predefined intents and parameter extraction.
  - **Grok API** for managing fallback intents and additional queries.
- **Dynamic Responses**: Supports real-time responses, including Google Search links for user queries.
- **User Interface**:
  - Built with **HTML** and **CSS** to ensure a clean and intuitive user experience.
- **Secure Configuration**: Environment variables ensure secure management of API keys and sensitive information.
- **Structured Design**: Organized project folders for scalability and maintainability.

## Technology Stack

- **Backend**: FastAPI and Dialogflow ES
- **Fallback Intents**: Grok API
- **Frontend**: HTML, CSS

## Project Structure

```
SPARSH/
├── index.html            # Web interface (optional usage for displaying chatbot UI)
├── server.py             # FastAPI server for handling webhooks
├── .env                  # Environment variables (e.g., API keys)
├── ngrok.exe             # Converts http to https
└── intents/              # Directory for storing intent-specific logic or data
    ├── e.Product_search.py  # Logic for handling the `e.Product_search` intent
    └── ...                 # Add other intent handlers here
```

## Installation and Setup

### Prerequisites

1. Python 3.9+
2. Virtual environment (optional but recommended)
3. Dialogflow project setup

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sengupta-aismita/SPARSH
   cd SPARSH
   ```

2. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add:

   ```
   GROQ_API_KEY=your_groq_api_key
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Server**:

   ```bash
   uvicorn server:app --reload
   ```

5. **Integrate with Dialogflow**:
   - Go to Dialogflow Console.
   - Set the webhook URL in the fulfillment section to:
     ```
     https://your-server-url.com/dialogflow-webhook
     ```

## Environment Variables

| Variable       | Description                   |
| -------------- | ----------------------------- |
| `GROQ_API_KEY` | API key for Groq integration. |

## Dependencies

- **FastAPI**: For building the webhook server.
- **Groq**: For AI-powered responses.
- **Pydantic**: For request validation.
- **Uvicorn**: ASGI server for FastAPI.

Install them with:

```bash
pip install -r requirements.txt
```

## Usage

- The chatbot provides industry-specific answers to user queries.
- For undefined intents, the Grok API ensures intelligent fallback responses.
- Access the chatbot through the web interface (HTML and CSS-based UI).

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

## License

## SPARSH is open-source software licensed under the [MIT License](LICENSE).

### Notes:

- The Grok API integration ensures the chatbot remains versatile and accurate for unexpected queries.
- The project is a work in progress; future updates will include additional industries and improved UI elements.
