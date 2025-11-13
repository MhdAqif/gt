from django import forms

LANG_CHOICE = [
  ('en','English'),
  ('ml','Malayalam'),
  ('hi','Hindi'),
  ('ar','Arabic')
]

class TranslateForm(forms.Form):
  text = forms.CharField(label="Enter Text",
                          widget=forms.Textarea(attrs={'rows':4}))
  src_lang = forms.ChoiceField(label='From',choices=LANG_CHOICE)
  dest_lang = forms.ChoiceField(label='To',choices=LANG_CHOICE)