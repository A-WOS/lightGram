# from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            user_instance = signup_form.save(commit=False)
            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.save()
            return redirect(request, 'accounts/signup_complete.html', {'username': user_instance.username})

        else:
            signup_form = SignUpForm()

        return render(request, 'accounts/signup.html', {'form': signup_form.as_p})


    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     password2 = request.POST.get('password2')
    #     print(username, password, password2)
    #
    #     # 회원 객체 생성하기
    #     user = User()
    #     user.username = username
    #     user.password = password
    #     user.set_password(password)
    #     user.save()
    #     return render(request, 'accounts/signup_complete.html')
    # else:
    #     context_values = {'form':'this is form'}
    #     return render(request, 'accounts/signup.html', context_values)
