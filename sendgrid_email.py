import sendgrid
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=<key>)
from_email = Email("example_from@me.be")
to_email = Email("example_to@me.be")
subject = ""
content = ""
content = Content("text/plain", content)
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
