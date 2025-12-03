# LLM Demo Collection

This repository contains a collection of Python scripts and notebooks demonstrating how to integrate with various Large Language Models (LLMs) including Google Gemini, OpenAI, and local models via Ollama. It also includes examples using the LangChain framework and a Streamlit application.

## Prerequisites

- Python 3.x
- API Keys for the respective services (OpenAI, Google AI Studio)

## Installation

1.  Clone the repository.
2.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Create a `.env` file in the root directory and add your API keys:

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Demos

### Google Gemini
-   [gemini-2.5-pro-demo.py](gemini-2.5-pro-demo.py): A basic script demonstrating how to use the Google Gemini 2.5 Pro model.
-   [gemini-2.5-pro-demo.ipynb](gemini-2.5-pro-demo.ipynb): A Jupyter notebook version of the Gemini demo.
-   [gemini-2.5-pro-langchain-demo.py](gemini-2.5-pro-langchain-demo.py): Demonstrates using Gemini 2.5 Pro with LangChain.

### OpenAI
-   [openai_demo.py](openai_demo.py): Basic usage of the OpenAI API.
-   [openai_langchain_demo.py](openai_langchain_demo.py): Using OpenAI models with LangChain.
-   [openai_langchain_prompt_template.py](openai_langchain_prompt_template.py): Examples of using Prompt Templates with OpenAI and LangChain.

### Local Models (Ollama)
-   [ollama-llama3.2-demo.py](ollama-llama3.2-demo.py): Demonstrates how to run Llama 3.2 locally using Ollama.

### Chatbots & Templates
-   [chatbot-v1-prompt-template.py](chatbot-v1-prompt-template.py): A V1 chatbot implementation using prompt templates.
-   [chatbot-v2-chat-template.py](chatbot-v2-chat-template.py): A V2 chatbot implementation using chat templates.
-   [prompt_template.py](prompt_template.py): General examples of prompt template usage.

### Web Application
-   [streamlit-demo-001.py](streamlit-demo-001.py): A simple web interface built with Streamlit to interact with the models. Run it with:

    ```bash
    streamlit run streamlit-demo-001.py
    ```

## License

MIT
