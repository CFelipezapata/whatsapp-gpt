from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json
 
app = Flask(__name__)
 
 
@app.route("/message", methods=['POST'])
def wa_sms_reply():
        
    msg = request.form.get('Body').lower()
 
    print("msg-->",msg)
    resp = MessagingResponse()
    reply=resp.message()
    
    if msg == "hi":
       reply.body("hello!")
 
 
    return str(resp)
 
if __name__ == "__main__":	
    app.run(debug=True)