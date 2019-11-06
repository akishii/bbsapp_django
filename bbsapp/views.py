from .models import BoardModel
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

#新規ユーザーをDBへ登録
def signupfn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username, '', password)
            return render(request, 'login.html')
    return render(request, 'login.html')

#ログイン認証し登録済ならトップ画面へ遷移
def loginfn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

#ログイン状態を判定し投稿内容を表示
@login_required
def listfn(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

#ログアウト処理
def logoutfn(request):
    logout(request)
    return redirect('login')

#詳細ボタン押下時にDBよりデータを取得
def detailfn(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

#いいねボタン押下時のカウント処理
def goodfn(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')

#新規投稿内容をDBへ登録しトップ画面へ遷移
class CreatePage(CreateView):    
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author')
    success_url = reverse_lazy('list')