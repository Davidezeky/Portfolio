from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

def enviar_correo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        subject = f'Nuevo mensaje de {name} ({phone})'
        body = f'Mensaje:\n{message}\n\nDe: {name}\nCorreo: {email}'
        
        send_mail(
            subject,
            body,
            'davidezequielromerovasquez@gmail.com',  # Desde
            ['destinatario@example.com'],  # A (cambia por la dirección de destino)
            fail_silently=False,
        )
        return HttpResponse("Correo enviado.")
    
    return HttpResponse("Método no permitido.", status=405)
