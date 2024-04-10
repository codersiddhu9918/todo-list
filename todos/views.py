from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
# from .models import Todo, user_login
from django.views.generic.list import ListView
from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class customLogin(LoginView):
    template_name = 'todos/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
# def todo_list(request):
#     x = {'item': Todo.objects.all()}
#     return render(request, 'todos/todo_list.html', x)
# def insert_todo_items(request:HttpRequest):
#     todo = Todo(content = request.POST['content'])
#     todo.save()
#     return redirect('main')
# def delete_todo_items(request,todo_id):
#     todoid = Todo.objects.get(id=todo_id)
#     todoid.delete()
#     return redirect('main')

# def us_login(request):
#     if request.method=="POST":
#         user = request.POST['user']
#         upass = request.POST['upass']
#         print(user,upass)
#         res = user_login.objects.filter(user=user,upass=upass)
#         print(res)
#
#         if len(res) == 1:
#             request.session['user'] = res[0].user
#             return redirect('main')
#         else:
#             return render(request, 'todos/login.html', {'error': 'Username or Password Incorrect!!!'})
#
# def ulogin(request):
#     return render(request,'todos/login.html')


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todos/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name = 'todos/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage,self).get(*args,**kwargs)





