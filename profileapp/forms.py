from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile#Profile 모델을 불러와서 form으로 사용함
        fields = ['image', 'nickname', 'message']