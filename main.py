from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables
load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

# Read essay
with open("essay.txt", "r", encoding="utf-8") as file:
    essay = file.read()

print("=" * 60)
print("ORIGINAL ESSAY")
print("=" * 60)
print(essay)

# Correct the essay
response = client.responses.create(
    model=deployment_name,
    input=f"""
Correct the following essay.

Fix grammar, spelling, punctuation, and sentence structure.
Do not change the meaning.
Return only the corrected essay.

Essay:
{essay}
"""
)

corrected = response.output_text

print("\n")
print("=" * 60)
print("CORRECTED ESSAY")
print("=" * 60)
print(corrected)

# Translate to French
response = client.responses.create(
    model=deployment_name,
    input=f"""
Translate the following essay into French.

Return only the translated essay.

Essay:
{corrected}
"""
)

translated = response.output_text

print("\n")
print("=" * 60)
print("FRENCH TRANSLATION")
print("=" * 60)
print(translated)