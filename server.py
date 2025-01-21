import os
from fastapi import FastAPI, Request, HTTPException
from groq import Groq
from pydantic import BaseModel
import urllib.parse  # Add this import for URL encoding

# Load the GROQ API key from environment variable
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# FastAPI app
app = FastAPI()

# List of unwanted keywords
unwanted_keywords = ["ass", "bitch", "fuck", "generate", "Java", "Python Code", "Javascript", "code"]

# Define a function to check for unwanted keywords
def contains_unwanted_keywords(text: str) -> bool:
    return any(keyword in text.lower() for keyword in unwanted_keywords)

class WebhookRequest(BaseModel):
    queryResult: dict

@app.post("/dialogflow-webhook")
async def dialogflow_webhook(request: WebhookRequest):
    query_result = request.queryResult
    user_message = query_result.get("queryText", "")
    intent_name = query_result.get("intent", {}).get("displayName", "")
    parameters = query_result.get("parameters", {})
    product_name = parameters.get("product", "")

    # Check if the message contains any unwanted keywords
    if contains_unwanted_keywords(user_message):
        return {
            "fulfillmentText": "I am a hear to help you. I can't provide information about that."
        }
    
    # If no unwanted keywords, send the message to Groq API
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_message}
        ],
        model="llama3-8b-8192"
    )

    groq_response = chat_completion.choices[0].message.content

    # For product search intent, include Google search link
    if intent_name == "e.Product_search" and product_name:
        encoded_product_name = urllib.parse.quote(product_name)
        google_search_url = f"https://www.google.com/search?q={encoded_product_name}"

        return {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [groq_response]
                    }
                },
                {
                    {
                        "richContent": [
                            [
                                {
                                    "type": "info",
                                    "title": f"Search results for '{product_name}'",
                                    "subtitle": "You can check more details from the link below."
                                },
                                {
                                    "type": "chips",
                                    "options": [
                                        {
                                            "link": google_search_url,
                                            "text": "Click here"
                                        }
                                    ]
                                }
                            ]
                        ]
                    }
                }
            ]
        }

    # For other intents, return simple text response
    return {
        "fulfillmentText": groq_response
    }
