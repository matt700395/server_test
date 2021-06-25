from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorator import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    #success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form): #받은 form이 여기 form에 들어가 있음
        temp_profile = form.save(commit = False) #commit(db에 저장)하지 않고 form에서 받아온 데이터를 임시로 temp_profile에 저장함
        temp_profile.user = self.request.user #temp_profile의 user를 request를 보낸 유저 자신으로 정함
        temp_profile.save() #db에 저장
        return super().form_valid(form) #form_valid 함수 를 다시 넘겨줌

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})#각 사용자의 detail페이지로 돌아감 pk때문에 이렇게 처리해야함

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    #success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})