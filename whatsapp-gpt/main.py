from dotenv import load_dotenv
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY')
 
app = Flask(__name__)
 
def forward_to_chatgpt(prompt: str) -> str:
    model_engine = "gpt-3.5-turbo"
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.6,
    )
    response = completion.choices[0].text
    return response

@app.route("/message", methods=['POST'])
def whatsapp_reply():
        
    msg = request.form.get('Body').lower()
 
    print("msg-->", msg)
    resp = MessagingResponse()
    reply=resp.message()
    
    gpt_resp = forward_to_chatgpt(msg)
    reply.body(gpt_resp) 
 
    return str(resp)
 
if __name__ == "__main__":	
    app.run(debug=True)