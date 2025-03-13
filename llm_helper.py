from dotenv import load_dotenv
from groq import Groq
import re

load_dotenv()

groq = Groq()

def classify_with_llm(log_msg):
    """
    Generate a variant of the input sentence. For example,
    If input sentence is "User session timed out unexpectedly, user ID: 9250.",
    variant would be "Session timed out for user 9251"
    """
    prompt = f'''Classify the log message into one of these categories: 
    (1) Workflow Error,
    (2) Deprecation Warning.

    If you can't figure out a category, use "Unclassified".
    Put the category inside <category> </category> tags. 
    Log message: {log_msg}'''

    chat_completion = groq.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="deepseek-r1-distill-llama-70b",
        # model="llama-3.3-70b-versatile",
        temperature=0.5
    )

    content = chat_completion.choices[0].message.content
    match = re.search(r'<category>(.*)<\/category>', content, flags=re.DOTALL)
    category = "Unclassified"
    if match:
        category = match.group(1)

    return category

if __name__ == "__main__":
    print(classify_with_llm("User session timed out unexpectedly, user ID: 9250."))
    print(classify_with_llm("DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead."))
    print(classify_with_llm("Failed to connect to the database."))
    print(classify_with_llm("User 9250 logged in successfully."))