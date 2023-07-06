import os
import logging
import azure.functions as func

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Content


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    sender_email = "applicationsdecartographieweb-webmappingapplications@ec.gc.ca"
    recipient_email = "applicationsdecartographieweb-webmappingapplications@ec.gc.ca"
    subject = "New RAMP Contact Form Submission"

    req_body = req.get_json()
    name = req_body.get('name')
    email = req_body.get('email')
    details = req_body.get('details')

    title = "<h1 style='text-align: center;'>Respectful contact has been made 🚀</h1>"
    content = f"<strong>Name:</strong> {name}<br><br><strong>Email:</strong> {email}<br><br><strong>Details:</strong> {details}"
    message = f"{title}<br>{content}"
    
    mail = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject=subject,
        html_content= Content("text/html", message))

    try:
        sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        response = sg.send(mail)
        logging.info(f"Email sent. Status Code: {response.status_code}")
        return func.HttpResponse("Email sent successfully.")
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)