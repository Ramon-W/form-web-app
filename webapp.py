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
    replyTwo = ""
    if length != "" and amount != "":
        if int(length) <= 5:
            reply = "Your password must have more than 5 characters."
        elif int(amount) <= 0:
            reply = "Generate at least 1 password."
        else:
            reply = "Passwords:"
        keyWord = color
        keyWordTwo = pet
        if reply == "Passwords:":
            for x in range(1, int(amount)):
                keyWord = color
                keyWordTwo = pet
                while len(keyWord) + len(keyWordTwo) >= int(length):
                    rand = random.randrange(0, 2)
                    if rand == 0:
                        rand = random.randrange(0, len(keyWord))
                        keyWord = keyWord[0:rand]
                    else:
                        rand = random.randrange(0, len(keyWordTwo))
                        keyWordTwo = keyWordTwo[0:rand]
                randB = random.randrange(0, 2)
                if randB == 0:
                    replyTwo = replyTwo + keyWord + keyWordTwo
                else:
                    replyTwo = replyTwo + keyWordTwo + keyWord
                for y in range(1, int(length) - len(keyWord) - len(keyWordTwo)):
                    if symbol == "true" and number == "true":
                        replyTwo = replyTwo + random.choice(string.digits + string.punctuation)
                    elif symbol == "true":
                        replyTwo = replyTwo + random.choice(string.punctuation)
                    elif number == "true":
                        replyTwo = replyTwo + random.choice(string.digits)
                replyTwo = replyTwo + " _______ "
        else:
            replyTwo = ""
    elif length == "" and amount == "":
        reply = "Please specify a length and amount."
    elif length == "":
        reply = "Please specify a length."
    else:
        reply = "Please specify an amount."
    return render_template('response.html', response = reply, responseTwo = replyTwo)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
