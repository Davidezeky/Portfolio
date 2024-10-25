from django.core.mail import send_mail
from django.shortcuts import render, redirect

def enviar_correo(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Aquí puedes personalizar el asunto y el contenido del correo
        asunto = f"Nuevo mensaje de {name}"
        contenido = f"Nombre: {name}\nCorreo: {email}\nTeléfono: {phone}\nMensaje: {message}"

        send_mail(
            asunto,
            contenido,
            'davidezequielromerovasquez@gmail.com',  # Desde
            ['destinatario@example.com'],  # A
            fail_silently=False,
        )
        # Redirigir o renderizar una respuesta
        return render(request, 'success.html')  # Asegúrate de crear esta plantilla

    return render(request, 'contact_form.html')  # Si no es POST, muestra el formulario
