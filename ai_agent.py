# Load API keys from .env when running directly or through Uvicorn.
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

#Step2: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider != "Groq":
        raise ValueError("Only the free Groq provider is enabled for this demo")
    llm=ChatGroq(model=llm_id)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []
    agent=create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )
    state={"messages": query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]

