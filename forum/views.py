from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from forum.models import Post, Comment


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = "login"

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    login_url = "login"


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name_suffix = "_update"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")
    login_url = "login"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    login_url = "login"

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={
                "pk": self.object.pk,
            },
        )

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super(PostCreateView, self).form_valid(form)
