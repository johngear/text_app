import os
import openai

from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, OPENAI_API_KEY, OPENAI_ORG_KEY, MY_TWILIO_NUMBER, MY_PRIVATE_NUMBER



def main():
    try: 
        #see if we have OS variables for what we need
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        openai.organization = os.environ['OPENAI_ORG_KEY'] #this is identical to other organization keys. this is fine to share
        openai.api_key = os.environ['OPENAI_API_KEY']

    except KeyError:
        #if we don't, load them from a config file, which is gitignored
        account_sid = TWILIO_ACCOUNT_SID
        auth_token = TWILIO_AUTH_TOKEN
        openai.organization = OPENAI_ORG_KEY 
        openai.api_key = OPENAI_API_KEY
        
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body=get_message(),
                                from_=MY_TWILIO_NUMBER,
                                to=MY_PRIVATE_NUMBER
                            )

    # print(message.sid)


def get_message():

    COMPLETIONS_MODEL = "text-davinci-003"
    openai.Model.list()

    COMPLETIONS_API_PARAMS = {.
        "temperature": .9,
        "max_tokens": 500,
        "model": COMPLETIONS_MODEL,
    }

    hmmm= "I want you to write a message that is to be sent via text, encouraging hard work and calling them broke. Emphasize that they have no money or girls. Here are 4 examples: \n\n1: Go get some money today you broke bitch. Grind like the rent's due! \n2: Who's hungry? It's time to eat some glass and work your ass off. \n3: You broke as shit and need to change that LMAO \n4:"

    response = openai.Completion.create(
                prompt=hmmm,
                **COMPLETIONS_API_PARAMS
            )

    return response["choices"][0]["text"].strip(" \n")

if __name__ == "__main__":
    main()