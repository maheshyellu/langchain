#### Google Gemini Model integration

import os
from dotenv import load_dotenv
load_dotenv()

os.environ[ "GOOGLE_API_KEY" ] = os.getenv( "GOOGLE_API_KEY" )
os.environ[ "GROQ_API_KEY" ] = os.getenv( "GROQ_API_KEY" )

from langchain.chat_models import init_chat_model

os.environ[ "GOOGLE_API_KEY" ] = os.getenv( "GOOGLE_API_KEY" )
model = init_chat_model( "google_genai:gemini-2.5-flash-lite" )
response = model.invoke( "Why do parrots talk?" )
print( response.content )


# Chatgoogle
from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI( model = "gemini-2.5-flash-lite" )
response = model.invoke( "Why do parrots talk?" )
print( response.content )


#### GROQ MODEL INTEGRATION

from langchain.chat_models import init_chat_model
os.environ[ "GROQ_API_KEY" ] = os.getenv( "GROQ_API_KEY" )
model = init_chat_model( "groq:qwen/qwen3-32b")
response = model.invoke( "Why do parrots talk?" )
print( response.content )


# ChatGroq

from langchain_groq import ChatGroq
model = ChatGroq( model = "qwen/qwen3-32b" )
response = model.invoke( "Why do parrots talk?" )
print( response.content )
