from portfolio_mvc.celery import app
from django.core.mail import send_mail
from django.conf import settings
from portfolio_mvc.celery import celery_log


@app.task(bind=True)
def send_email_delayed(sender_email: str, message_text: str, sender_name: str, email_class: str, recipient_email=None):
    """
    Sends emails using django send_email via a celery task
    :param sender_email:
    :param message_text: Message body to be sent
    :param sender_name: Name of the sender
    :param email_class: Type of email template to use
    :param recipient_email: Email recipient list
    :return:
    """
    if email_class == 'Contact':
        title = 'Portfolio Website Contact Notification'
        message = f"Hey David, \n\nI am {sender_name} and I sent this message via your website.\n{message_text}" \
                  f"\n\nYou can contact me via my email address {sender_email}"
    else:
        title = "Generic Email"
        message = message_text

    response = send_mail(title, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_CONTACT_EMAIL])
    if response == 1:
        celery_log.info('Email sent successfully')
    else:
        celery_log.error('An error occurred while sending this email')
