from twilio.rest import Client
from flask import Flask, request # , redirect
# from twilio.twiml.messaging_response import MessagingResponse
import cohere
from cohere.classify import Example
from game_text import *
from random import choice

stage = a0


def send(script: str, s: tuple):

    "**********************************************"
    # account_sid = "AC17fbb6fe6a08882d01aa028302fe614e"
    # auth_token = "7ab5a0fb5c2843b4badb01e6724f51a7"
    account_sid = "ACce8cd2852068bbb3ab8daa99ef2efb09"
    auth_token = "8daeba5da3b59d808690b9b0905cf312"
    "***********************************************"
    client = Client(account_sid, auth_token)

    # message =
    # add that equal to client... if this doesn't work

    "*****************************"
    if len(s) == 3:
        client.messages.create(
            body=script,
            from_="+17792090819",
            to="+15147958168"
        )
    
    elif len(s) == 4:
        client.messages.create(
            media_url=s[3],
            body=script,
            from_="+17792090819",
            to="+15147958168"
        )
    "******************************"

def judge(answer: str, st: list):
    co = cohere.Client('Bl6g74gBTNtvElVSo3387cHcCIEGWs7N26k35UHN')
    response = co.classify(
        model='large',
        inputs=[str(answer) + "."],
        examples=st[2])

    if response.classifications[0].confidence >= 0.70:
        result = response.classifications[0].prediction

    else:
        result = max(list(st[1].keys()))

    return result


def add_points(stats: dict, characters: list):
    for item in characters:
        stats[item] += 1


def display_stats(stats: dict):
    word = "Here's how much you displayed certain characteristics during this adventure: "
    for k in stats:
        word += f"{k}: {stats[k]}   "

    send(script=word[:-1], s=stage)


def clear_stats(stats: dict):
    for k in stats:
        stats[k] = 0


# send(script=stage[0])

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    global stage
    global inventory
    global character

    body = request.values.get('Body', None)

    if stage is None and body.lower() == "restart":
        stage = a0
        inventory = []
        clear_stats(character)
        send(script=stage[0], s=stage)

    # elif stage == 1:
    #     send(script="Sending you back to the beginning... ")
    #     stage = a0
    #     send(stage[0])
    #     inventory = []
    #     clear_stats(character)

    elif stage is not None:
        code = judge(body, stage)

        effects = stage[1][int(code)]

        if effects[2]:
            add_points(character, effects[2])

        if effects[3]:
            inventory.append(effects[3][0])

        send(script=stage[1][int(code)][0], s=stage)

        stage = stage[1][int(code)][1]

        if stage == 1:
            send(script="Sending you back to the beginning... ", s=stage)
            inventory = []
            clear_stats(character)
            stage = a0
            send(stage[0], s=stage)

        else:
            stage = stage[1][int(code)][1]
            send(script=stage[0], s=stage)

    else:
        display_stats(character)
        send(script=f"{choice(still_here)} Write 'restart' to start a new game!", s=stage)


if __name__ == "__main__":
    send(script=stage[0], s=stage)
    app.run(port=80, debug=True)
