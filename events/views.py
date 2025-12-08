from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Event
from .forms import ParticipantForm
from .utils import send_telegram
from rest_framework.generics import ListAPIView
from .serializers import EventSerializer

def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            user = form.save()

            message = (
                f"New User registered:\n"
                f"Full name: {user.full_name}\n"
                f"Email: {user.email}\n"
                f"Phone: {user.phone}"
            )
            send_telegram(message)

            send_mail(
                subject='New user created',
                message=f'Welcome {user.full_name}! You have been registered successfully!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )
            context = {
                'full_name': user.full_name,
            }
            return render(request, 'success.html', context)

    else:
        form = ParticipantForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

class ParticipantList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
