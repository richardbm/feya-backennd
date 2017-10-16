from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(template, email_destinity, subject, data={}):
    if 'msg' not in data.keys():
        data['msg'] = subject
    if True:
        data["url"] = settings.URL
        from_email = settings.EMAIL_HOST_USER
        text_content = render_to_string(template, data)
        html_content = render_to_string(template, data)

        to = email_destinity
        send = EmailMultiAlternatives(subject, text_content, from_email, [to])
        send.attach_alternative(html_content, "text/html")
        send.send()