from twilio.rest import Client

# Set up your Twilio client (replace "account_sid" and "auth_token" with your actual credentials)
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
a= '+91_yournumber'
# Send a WhatsApp message (replace "to_number" and "from_number" with actual phone numbers)
message = client.messages.create(
    body="gud ",
    from_=a,
    to="+91_frnd_number"
)

print("Message sent!")
