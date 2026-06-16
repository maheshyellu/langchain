#### Langchain Version V1

import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_groq import ChatGroq
load_dotenv()

@tool
def get_weather( city: str ) -> str:
    """Get the weather for a city."""
    return f"The weather in {city} is sunny."

# Create Groq model
groq_model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key= os.getenv( "GROQ_API_KEY" )
)

# Create agent
agent = create_agent(
    model = groq_model,
    tools = [ get_weather ],
    system_prompt = "You are a helpful assistant."
)

# Run the agent
result = agent.invoke({
    "messages" : [{
        "role" : "user",
        "content" : "What is the weather like in New York?"
    }]
})

print( result )