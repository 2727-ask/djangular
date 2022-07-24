from django.core.mail import send_mail


def send_my_email():
    send_mail(
        'Email Rocks',
        'Ashutosh Kumbhar SDE',
        'ashutoshkumbhar27@gmail.com',
        ['4ksatisfaction@gmail.com']
    )
