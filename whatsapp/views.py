from twilio.rest import Client
from notifications.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
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

        Perfil.objects.get(nome_completo = nome_completo)

        message = client.messages.create(
            from_='whatsapp:+14155238886',

            body="""Your *{}* order of _{}_ 
                has shipped and should be delivered
                on *_{}_*. Details: ~{}~""".format(
                nome_completo, nome_completo, nome_completo,
                nome_completo),
                
            to='whatsapp:+{}'.format(user_whatsapp_number)
        )

        print(user_whatsapp_number)
        print(message.sid)
        return HttpResponse('Great! Expect a message...')

    return render(request, 'phone.html')