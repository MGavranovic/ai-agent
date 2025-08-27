import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

script_args = sys.argv
if len(script_args) < 2:
    print("Prompt hasn't been provided as an arg for python3 command")
    print("Please make sure to use python3 main.py [prompt]")
    sys.exit(1)

prompt_arg = script_args[1]
messages = [types.Content(role="user", parts=[types.Part(text=prompt_arg)])]
try:
    api_response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages,config=types.GenerateContentConfig(system_instruction=system_prompt))
    api_response_text = api_response.text

    if "--verbose" in script_args:
        print(f"User prompt: {prompt_arg}")
        print(f"Prompt tokens: {api_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {api_response.usage_metadata.candidates_token_count}")
        print(api_response_text)
    else:
        print(api_response_text)
except ServerError:
    print("The Gemini API is temporarily unavailable. Please try again later.")