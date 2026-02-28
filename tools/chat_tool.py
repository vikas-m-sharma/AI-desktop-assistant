from utils.llm import get_llm
from langchain_core.prompts import PromptTemplate

llm = get_llm()

chat_prompt = PromptTemplate.from_template("""
You are a helpful AI assistant talking to a user.

IMPORTANT:
- Respond naturally.
- If the user is emotional, respond empathetically.
- If the user is stressed, calm them.
- If the user is confused, guide them.
- Always address the user as "Sir".
- Reply in the same language the user uses.

User:
{user_input}
""")

def chat_response(user_input):
    chain = chat_prompt | llm
    response = chain.invoke({"user_input": user_input})
    return response.content
