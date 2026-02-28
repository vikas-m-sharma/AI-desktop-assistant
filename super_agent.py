from utils.llm import get_llm
from langchain_core.prompts import PromptTemplate
import json

llm = get_llm()
router_prompt = PromptTemplate.from_template("""
You are an intelligent intent classifier for a developer voice assistant.

Understand the user's request regardless of language (Hindi, English, Hinglish).

Classify the request into one of these intents:

- debug_error
- summarize_file
- execute_command
- open_application
- play_song
- general_question

If intent is open_application, extract app_name.
If intent is play_song, extract song_name.

Return ONLY valid JSON in this format:

{{  
  "intent": "intent_name",
  "app_name": "application_name_if_any",
  "song_name": "song_name_if_any"
}}

User Input:
{user_input}
""")

def route_intent(user_input):
    try:
        chain = router_prompt | llm
        response = chain.invoke({"user_input": user_input})

        raw_output = response.content.strip()

        # Extract JSON safely
        start = raw_output.find("{")
        end = raw_output.rfind("}") + 1

        if start == -1 or end == -1:
            return {"intent": "general_question"}

        json_str = raw_output[start:end]

        return json.loads(json_str)

    except Exception as e:
        print("Routing Error:", str(e))
        return {"intent": "general_question"}
