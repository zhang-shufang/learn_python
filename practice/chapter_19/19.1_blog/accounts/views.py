from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空表单
        form = UserCreationForm()
    else:
        # 处理填充的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 注册完成后自动登录并跳转到主页
            login(request, new_user)
            return redirect('blog_apps:blogs')

    # 显示空表单活指出表单无效
    context = {'form': form}
    return render(request, 'registration/register.html', context)