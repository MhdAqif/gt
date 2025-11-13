from django.shortcuts import render
from .forms import TranslateForm
from deep_translator import GoogleTranslator as Translator

def index(request):
  result=''
  if request.method == 'POST':
    form = TranslateForm(request.POST)
    if form.is_valid():
      text = form.cleaned_data['text']
      src_lang = form.cleaned_data['src_lang']
      dest_lang = form.cleaned_data['dest_lang']

      try:
        result = Translator(source=src_lang,target=dest_lang).translate(text)
      except Exception as e :
        result = f"Error : {str(e)}"
  else :
    form = TranslateForm()
  return render(request,'index.html',{'form':form,'result':result})



