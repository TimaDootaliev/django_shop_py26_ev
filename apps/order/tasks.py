from django.core.mail import send_mail


def send_confirmation_mail(instance):
    message = f"""
    Здравствуйте, {instance.user.username}!
    Подтвердите заказ на адрес {instance.address}!

    http://localhost:8000/order/{instance.pk}/confirm/

    Если это были не Вы, игнорируйте это сообщение
    """
    send_mail(
        subject='Подтверждение заказа',
        message=message,
        from_email='test@test.com',
        recipient_list=[instance.user.email],
        fail_silently=False
    )