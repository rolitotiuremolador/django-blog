from django import forms

class ContactForm(forms.Form):
  full_name = forms.CharField()
  email = forms.EmailField()
  content = forms.CharField(widget=forms.Textarea)
  
  def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get('email')
    print(email)
    if email.endswith(".edu"):
      raise forms.ValidationError("This is not a valid email, donot use .edu")
    return email

class HomeForm(forms.Form):
  firstname = forms.CharField(max_length=100)
  lastname = forms.CharField(max_length= 100)
  address = forms.CharField(widget=forms.Textarea)