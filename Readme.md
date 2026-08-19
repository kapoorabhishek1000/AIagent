# Project Setup Guide

## Run the Demo on Another Computer

### Requirements

- Python 3.10 or newer
- A free Groq API key from [console.groq.com](https://console.groq.com/)

Create a `.env` file in the project root:

```dotenv
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

`TAVILY_API_KEY` is only needed when web search is enabled. Never commit `.env` or share its contents.

### Install

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
py -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Start the Application

Open two terminals in the project directory. Activate the virtual environment in both.

Terminal 1, start the backend:

```bash
python backend.py
```

Terminal 2, start the frontend:

```bash
streamlit run frontend.py
```

Open the URL shown by Streamlit, usually [http://localhost:8501](http://localhost:8501). The API documentation is available at [http://127.0.0.1:9999/docs](http://127.0.0.1:9999/docs).

Select the Groq provider model `openai/gpt-oss-120b` in the UI for the demo.

## Deploy as a Website

### Free Render Deployment

The repository includes `render.yaml`, which defines a free FastAPI service and a free Streamlit service. Render's free services may sleep when unused, so the first request after inactivity can take a little longer.

1. Push this project to a GitHub repository. Make sure `.env` is not committed.
2. Create a free account at [render.com](https://render.com/).
3. Choose **New > Blueprint** and connect the GitHub repository.
4. Render reads `render.yaml` and creates the API and UI services.
5. In the API service environment settings, add `GROQ_API_KEY` and, if search is needed, `TAVILY_API_KEY`.
6. Copy the API service URL, such as `https://ai-agent-chatbot-api.onrender.com`.
7. In the UI service environment settings, set `BACKEND_URL` to that API URL without `/chat` at the end.
8. Redeploy the UI service, then open its Render URL.

Test the API at `https://your-api-url.onrender.com/health`. It should return `{"status":"ok"}`.

The project runs as two services:

- Deploy `backend.py` as a Python web service with start command `python backend.py`.
- Deploy `frontend.py` as a Streamlit service with start command `streamlit run frontend.py`.

Set these variables in the backend service:

```dotenv
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
BACKEND_HOST=0.0.0.0
BACKEND_PORT=9999
```

Set this variable in the frontend service, using the public backend URL supplied by your host:

```dotenv
BACKEND_URL=https://your-backend.example.com
```

Do not commit `.env` or API keys. The frontend must be able to reach the deployed backend URL, and the backend must be running before users submit questions.

This guide provides step-by-step instructions to set up your project environment, including setting up a Python virtual environment using Pipenv, pip, or conda.

## Table of Contents

1. [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)
   - [Using Pipenv](#using-pipenv)
   - [Using pip and venv](#using-pip-and-venv)
   - [Using Conda](#using-conda)
2. [Running the application](#project-phases-and-python-commands)


## Setting Up a Python Virtual Environment

### Using Pipenv
1. **Install Pipenv (if not already installed):**  
```
pip install pipenv
```

2. **Install Dependencies with Pipenv:** 

```
pipenv install
```

3. **Activate the Virtual Environment:** 

```
pipenv shell
```

---

### Using `pip` and `venv`
#### Create a Virtual Environment:
```
python -m venv venv
```

#### Activate the Virtual Environment:
**macOS/Linux:**
```
source venv/bin/activate
```

**Windows:**
```
venv\Scripts\activate
```

#### Install Dependencies:
```
pip install -r requirements.txt
```

---

### Using Conda
#### Create a Conda Environment:
```
conda create --name myenv python=3.11
```

#### Activate the Conda Environment:
```
conda activate myenv
```

#### Install Dependencies:
```
pip install -r requirements.txt
```


# Project Phases and Python Commands

## Phase 1: Create AI Agent
```
python ai_agent.py
```

## Phase 2: Setup Backend with FastAPI
```
python backend.py
```

## Phase 3: Setup Frontend with Streamlit
```
python frontend.py
```

## IMPORTANT
### Make sure backend python script is running in a separate terminal



