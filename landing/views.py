from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
import telegram
import asyncio

async def send_telegram_message(message):
    bot_token = '6482751257:AAFiPvJ53qamu7EpmaT9PKa7OL90EWEFfk4'
    chat_ids = ['1182532876']# '905712628']
    bot = telegram.Bot(token=bot_token)

    for chat_id in chat_ids:
        await bot.send_message(chat_id=chat_id, text=message)


def landing(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = message = f"New contact form submission:\nName: {form.cleaned_data['name']}\nAge: {form.cleaned_data['age']}\nCity: {form.cleaned_data['city']}\nPhone: {form.cleaned_data['phone']}\n"
            asyncio.run(send_telegram_message(message))
            # Add code here to send a Telegram message
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'landing/index.html', {'form': form})

def success_page(request):
    return render(request, 'landing/success.html')
