from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from forum.models import Comment, Post


@method_decorator(login_required, name="dispatch")
class PostListView(ListView):
    model = Post
    template_name = "forum:post_list"

    def get_queryset(self):
        published_qs = Post.objects.filter(status="published")
        curr_user_qs = Post.objects.filter(author=self.request.user.id)
        return published_qs.union(curr_user_qs).order_by("-created_at")


@method_decorator(login_required, name="dispatch")
class PostDetailView(DetailView):
    model = Post


@method_decorator(login_required, name="dispatch")
class PostUpdateView(UpdateView):
    model = Post
    fields = [
        "title",
        "content",
        "status",
    ]
    template_name_suffix = "_update"

    def get_success_url(self):
        return reverse_lazy(
            "forum:post_detail",
            kwargs={
                "slug": self.object.slug,
            },
        )


@method_decorator(login_required, name="dispatch")
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("forum:post_list")


@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    fields = [
        "title",
        "content",
        "status",
    ]

    def get_success_url(self):
        return reverse_lazy(
            "forum:post_detail",
            kwargs={"slug": self.object.slug},
        )

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super(PostCreateView, self).form_valid(form)


@method_decorator(login_required, name="dispatch")
class CommentCreateView(CreateView):
    model = Comment
    fields = ["content"]

    def get_success_url(self):
        return reverse_lazy(
            "forum:post_detail",
            kwargs={
                "slug": self.request.GET.get("slug"),
            },
        )

    def form_valid(self, form):
        post = Post.objects.get(slug=self.request.GET.get("slug"))
        author = self.request.user
        form.instance.author = author
        form.instance.post = post
        return super(CommentCreateView, self).form_valid(form)
