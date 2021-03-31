from twilio.rest import Client
from e_commerce.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from django.http import HttpResponse
from django.shortcuts import render
from user.models import Perfil

order_details = {
    'amount': '5kg',
    'item': 'Tomatoes',
    'date_of_delivery': '03/04/2021',
    'address': 'No 1, Ciroma Chukwuma Adekunle Street, Ikeja, Lagos'
}

def send_notification(request):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    if request.method == 'POST':
        user_whatsapp_number = request.POST['user_number']

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Your {} order of {} has shipped and should be delivered on {}. Details: {}'.format(
                order_details['amount'], order_details['item'], order_details['date_of_delivery'],
                order_details['address']),
            to='whatsapp:+{}'.format(user_whatsapp_number)
        )

        print(user_whatsapp_number)
        print(message.sid)
        return render(request, 'phone.html')

    return render(request, 'phone.html')