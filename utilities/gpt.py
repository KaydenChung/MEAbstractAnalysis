# Imports
from g4f.client import Client
from g4f.Provider import You

# Asyncio Fix
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Format Text
def formatText(text):
    cleanedText = text.replace("*", "").lower()
    return cleanedText
    
# Get AI Response
def askGPT(abstract):
    client = Client()
    prompt = f"""Given this abstract for a research paper, would this article be suitable 
                for biotechnological ecosystem service replacement research: {abstract}. 
                Only reply with \"Yes\", \"Maybe\", or \"No\". After replying with a yes/maybe/no,
                provide a brief analysis of the abstract on a newline with no special formatting."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        provider=You, 
        messages=[{"role": "user", "content": prompt}],
    )
    return formatText(response.choices[0].message.content)
