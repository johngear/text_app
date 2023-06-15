import os
import openai

from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, OPENAI_API_KEY, OPENAI_ORG_KEY



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
        openai.organization = OPENAI_ORG_KEY #this is identical to other organization keys. this is fine to share
        openai.api_key = OPENAI_API_KEY
        
    print("done!!!!")
    #I STG if twilio website doesn't just send me a damn verificaiton email 


    # client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #                             body=get_message(),
    #                             from_='+15017122661',
    #                             to='+15558675310'
    #                         )

    # print(message.sid)


def get_message():

    COMPLETIONS_MODEL = "text-davinci-003"

    
    openai.Model.list()

    COMPLETIONS_API_PARAMS = {
        # We use temperature of 0.0 because it gives the most predictable, factual answer.
        "temperature": .9,
        "max_tokens": 500,
        "model": COMPLETIONS_MODEL,
    }


    hmmm= "I want you to write an encouraging text message to yourself, encouraging hard work, but in a slightly mean way. These are some examples: \n\n1: Go get some money today you broke bitch. Wake up and grind! \n2: Who's hungry? It's time to eat some glass and work your ass off. \n3: Seize the day. Work hard. Take the step into the unknown.\n4:"

    response = openai.Completion.create(
                prompt=hmmm,
                **COMPLETIONS_API_PARAMS
            )

    return response["choices"][0]["text"].strip(" \n")

if __name__ == "__main__":
    main()
