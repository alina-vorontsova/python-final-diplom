from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from .models import User 


def send_registration_confirmation(user_id: int, **kwargs):
    """Отправить эл. письмо с подтверждением регистрации.

    
    Ключевые аргументы:
    user_id -- ID пользователя в базе данных.
    """
    user = User.objects.get(id=user_id)
    subject = 'Email Confirmation'
    to = [user.email,]
    body = f"Your registration was successful. Your username: {user.username}, your password: {user.password}"
    message = EmailMultiAlternatives(subject=subject, body=body, from_email=settings.EMAIL_HOST_USER, to=to)
    message.send()


def send_order_confirmation(user_id: int, **kwargs):
    """Отправить эл. письмо с подтверждением заказа.
    
    Ключевые аргументы: 
    user_id -- ID пользователя в базе данных.
    """
    user = User.objects.get(id=user_id)
    subject = 'Order Confirmation'
    to = [user.email,]
    body = f"Seems like you have ordered something..."
    message = EmailMultiAlternatives(subject=subject, body=body, from_email=settings.EMAIL_HOST_USER, to=to)
    message.send()