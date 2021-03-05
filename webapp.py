import random
import string
from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    length = request.args['length'] 
    amount = request.args['amount'] 
    color = request.args['color'] 
    pet = request.args['pet']
    symbol = request.args['symbol'] 
    number = request.args['number'] 
    #if int(length) <= 5:
    #    reply = "Your password must have more than 5 characters."
    #elif int(amount) <= 0:
    #    reply = "Generate at least 1 password."
    #else:
    #    reply = "Passwords:"
    reply = symbol
    replyTwo = ""
    keyWord = color
    keyWordTwo = pet
    if len(keyWord) + len(keyWordTwo) <= int(length):
        keyWord = keyWord[0]
        keyWordTwo = keyWordTwo[0]
    for x in range(1, int(amount)):
        for y in range(1, int(length)):
            if symbol != "yes" and number != "yes":
                replyTwo = replyTwo + random.choice(string.digits + string.punctuation)
            elif symbol != "yes":
                replyTwo = replyTwo + random.choice(string.punctuation)
            elif number != "yes":
                replyTwo = replyTwo + random.choice(string.ascii_digits)
            replyTwo = replyTwo + " - "
    return render_template('response.html', response = reply, responseTwo = replyTwo)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
