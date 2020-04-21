# Standard packages
import random
import os

# 3rd Party packages
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()

# Roast list 
roast_list = [
    "Bro you're built like KFC cheeto sandwich",
    "I think I saw you in Free Willy. Your method acting as a whale was amazing.",
    "If laughter is the best medicine, your face must be curing the world",
    "You're so fat you're growing every day like a Katamari ball",
    "You're wrists are so small you have to go to Baby Gap for gloves"
]

twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_from = os.getenv("TWILIO_PHONE_NUM_FROM")
twilio_phone_to = os.getenv("TWILIO_PHONE_NUM_TO")

client = Client(twilio_sid, twilio_auth)

# Create random index value to randomly select roast statement from list of jokes
random_idx = random.randint(0, len(roast_list)-1)
random_roast = roast_list[random_idx] + " - With ❤️ from Roastbot"

message = client.messages.create(
    body=random_roast,
    from_=twilio_phone_from,
    to=twilio_phone_to
)

print(message.body)