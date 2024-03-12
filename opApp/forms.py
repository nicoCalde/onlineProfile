from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='',max_length=50,widget= forms.TextInput(attrs={'id':"contactName",'placeholder':"Nombre"}))
    email = forms.EmailField(label='',max_length=50,widget= forms.TextInput(attrs={'id':"contactEmail",'placeholder':"Email"}))
    subject = forms.CharField(label='',max_length=80,widget= forms.TextInput(attrs={'id':"contactSubject",'placeholder':"Asunto"}))
    message = forms.CharField(label='',max_length=500,widget= forms.Textarea(attrs={'id':"contactMessage",'placeholder':"Menssage",'rows':'10'}))