from utils.llm import get_llm
from langchain_core.prompts import PromptTemplate

llm = get_llm()

debug_prompt = PromptTemplate.from_template("""
You are a senior Python engineer assistant.

IMPORTANT:
Reply in the SAME language that the user used.
If the user speaks Hindi, reply in Hindi.
If the user speaks English, reply in English.
If the user mixes both, reply naturally.

Explain clearly:

1. What is the error?
2. Why is it happening?
3. How to fix it?
4. If a command is needed, suggest it clearly.

Error:
{error_message}
""")

def analyze_error(error_message):
    chain = debug_prompt | llm
    response = chain.invoke({"error_message": error_message})
    return response.content
