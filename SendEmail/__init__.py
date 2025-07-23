import os
import logging
import azure.functions as func

from postmarker.core import PostmarkClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    sender_email = "applicationsdecartographieweb-webmappingapplications@ec.gc.ca"
    recipient_email = "applicationsdecartographieweb-webmappingapplications@ec.gc.ca"
    template_id = os.environ.get("POSTMARK_TEMPLATE_ID")
    postmark_token = os.environ.get("POSTMARK_API_TOKEN")

    try:
        req_body = req.get_json()
        name = req_body.get('name')
        email = req_body.get('email')
        details = req_body.get('details')

        client = PostmarkClient(server_token=postmark_token)

        client.emails.send_with_template(
            TemplateId=int(template_id),
            From=sender_email,
            To=recipient_email,
            TemplateModel={
                "name": name,
                "email": email,
                "details": details
            }
        )

        logging.info(f"Email sent.")
        return func.HttpResponse("Email sent successfully.")
    
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(f"An error occurred. Please send an email to {sender_email} for assistance.", status_code=500)