import os
import textwrap
from langchain_google_genai import ChatGoogleGenerativeAI

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Set your Google API key
GOOGLE_API_KEY = "AIzaSyBZknRAIpjSxW0VvGqQSuBLWOWWONJp1Dg"

# InitiAPI_KEY = "AIzaSyBZknRAIpjSxW0VvGqQSuBLWOWWONJp1Dg"alize the language model
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# Invoke the model with a prompt
result = llm.invoke("who is iron man")

# Convert the result to markdown and print it
op = to_markdown(result.content)
print(op)
