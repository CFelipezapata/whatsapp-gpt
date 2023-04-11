from dotenv import load_dotenv
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY')

app = Flask(__name__)


def forward_to_chatgpt(message: str) -> str:
    model = "gpt-3.5-turbo"
    prompt = [{"role": "user", "content": message}]
    
    completion = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.6,
    )
    response = completion.choices[0].message.content
    print(response)
    return response


@app.route("/message", methods=['POST'])
def whatsapp_reply():

    msg = request.form.get('Body').lower()

    print("msg-->", msg)
    resp = MessagingResponse()
    reply = resp.message()

    gpt_resp = forward_to_chatgpt(msg)
    reply.body(gpt_resp)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
