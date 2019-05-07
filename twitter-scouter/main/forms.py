from django import forms

PAGINATE_CHOICES = (
  ('', '-'*10),
)

for i in range(10,100,10):
  PAGINATE_CHOICES += ((i, str(i)),)


class Paginate(forms.Form):
  paginate_by = forms.ChoiceField(
    label='表示数',
    widget=forms.Select(attrs={'onchange': 'submit(this.form);','id':'selectPaginateBy'}),
    choices=PAGINATE_CHOICES
  )
