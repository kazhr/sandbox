import datetime
from django.shortcuts import get_object_or_404
from django.views import generic
from django.shortcuts import redirect

from .models import TodoList


class TodoListListView(generic.ListView):

    model = TodoList


class TodoListDetailView(generic.DetailView):

    model = TodoList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 事前処理
        todo_list = TodoList.objects.get(pk=self.kwargs["pk"])
        if not todo_list.updated == datetime.date.today():
            # 最終更新日が今日でなければ完了マークリセット
            todo_list.reset()

        return context


def reset(request, pk):
    """
    強制リセット
    """
    todo_list = TodoList.objects.get(pk=pk)
    todo_list.reset()
    return redirect("todo:detail", pk)


def checked(request, pk):
    """
    checkが押されたtaskに完了マークをつける
    """
    todo_list = TodoList.objects.get(pk=pk)

    task_pk = [int(k) for k, v in request.POST.items() if v == "Check"][0]
    task = get_object_or_404(todo_list.tasks, pk=task_pk)
    task.checked()

    todo_list.touch()
    return redirect("todo:detail", pk)
