from twilio.rest import Client
from flask import Flask, request # , redirect
# from twilio.twiml.messaging_response import MessagingResponse
import cohere
from cohere.classify import Example
from game_text import *
from random import choice

stage = a0


def send(script: str):

    "**********************************************"
    account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    "***********************************************"
    client = Client(account_sid, auth_token)

    # message =
    # add that equal to client... if this doesn't work

    "*****************************"
    client.messages.create(
        body=script,
        from_="+xxxxxxxxxxx",
        to="+xxxxxxxxxxxx"
    )


    "******************************"


def send_image(url):
    account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
    auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    client = Client(account_sid, auth_token)

    client.messages.create(
        media_url=url,
        from_="+xxxxxxxxxx",
        to="+1xxxxxxxxxx"
    )


def judge(answer: str, st: list):
    co = cohere.Client('xxxxxxxxxxxxxxxxxxxxxxxxxx')
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

    send(script=word[:-1])


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
        send_image("https://github.com/Student0544/Choose-your-Destiny---Mobile-and-ML/blob/main/Poster.png?raw=true")
        send(script=stage[0])

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

        if len(stage[1][int(code)]) == 5:
            send_image(stage[1][int(code)][4])

        send(script=stage[1][int(code)][0])

        stage = stage[1][int(code)][1]

        if stage == 1:
            send(script="Sending you back to the beginning... ")
            inventory = []
            clear_stats(character)
            stage = a0
            send_image("https://github.com/Student0544/Choose-your-Destiny---Mobile-and-ML/blob/main/Poster.png?raw=true")
            send(stage[0])

        else:
            stage = stage[1][int(code)][1]
            send(script=stage[0])

    else:
        display_stats(character)
        send(script=f"{choice(still_here)} Write 'restart' to start a new game!")


if __name__ == "__main__":
    send_image("https://github.com/Student0544/Choose-your-Destiny---Mobile-and-ML/blob/main/Poster.png?raw=true")
    send(script=stage[0])
    app.run(port=80, debug=True)
