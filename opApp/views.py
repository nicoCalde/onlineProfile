from django.shortcuts import render, redirect
from opApp.models import *
from opApp.forms import *
from django.http import JsonResponse
from django.core.mail import send_mail
import openai
from openai import OpenAI
from dotenv import load_dotenv
import os
from django.urls import reverse

load_dotenv()

client = OpenAI(
    api_key= os.getenv('OPENAI_API_KEY'),
)

# Create your views here.
def index(request):
    skills = IndexSkillSet.objects.all().order_by('id')
    return render(request,'opApp/public/views/index.html',{'skills':skills})

def skills(request):
    skills = Skills.objects.all().order_by('id')
    return render(request,'opApp/public/views/skills.html',{'skills':skills})

def works(request):
    works = Works.objects.all()
    return render(request,'opApp/public/views/works.html',{'works':works})

def get_works(request):
    works = Works.objects.all().values('title', 'modal_description', 'modal_image', 'skills', 'link')
    return JsonResponse({'works': list(works)})

def education(request):
    education = Education.objects.all().order_by('-id')       
    return render(request,'opApp/public/views/education.html',{'education':education})

def about(request):
    about = About.objects.all()
    return render(request,'opApp/public/views/about.html',{'about':about})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_message = f'''
                Name: {name}

                From: {email}

                Message: {message}
            '''

            send_mail(subject,email_message,'calde_kpo@hotmail.com', ['calde_kpo@hotmail.com'], fail_silently=False)

            return redirect('opApp:index') 
    else:
        form = ContactForm()
    return render(request, 'opApp/public/views/contact.html', {'form': form})

def ask_openai(message, context_file): 
    try:
        with open(context_file, 'r') as file:
            context = file.read()
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": message},
            ],
            max_tokens=50,
        )

        answer = response.choices[0].message.content.strip()
        return answer
    except openai.RateLimitError:
        contact_url = reverse('opApp:contact')
        answer = f"Rate limit exceeded. Please try again later or <a href='{contact_url}' class='contact-link'>contact</a> us for assistance."
        return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        context_file = os.path.abspath('opApp/static/opApp/img/resources/data.txt')
        response = ask_openai(message, context_file)
        return JsonResponse({'message': message, 'response': response})
    else:
        return JsonResponse({'error': 'Invalid request method'})