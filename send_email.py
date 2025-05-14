from app import app, mail
from flask_mail import Message

with app.app_context():
    msg = Message(
        subject="Test Email",
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[app.config['ADMINS'][0]],
        body="This is a test email sent from the terminal."
    )
    mail.send(msg)
    print("Test email sent!")