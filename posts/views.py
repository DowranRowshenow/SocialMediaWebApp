# type: ignore
from django.views.generic import (
    View,
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages


from main.views import context
from .models import Post, PostComment
from .forms import CreatePostForm, EditPostForm, CommentForm


class PostsView(ListView):
    template_name = "posts/posts.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        return context(self, super().get_context_data(**kwargs))


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        return context(self, super().get_context_data(**kwargs))


class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "posts/create_post.html"

    def form_valid(self, form):
        form.init(self.request.user)
        try:
            self.object = form.save()
        except Exception:
            return super().form_invalid(form)
        return HttpResponseRedirect(reverse("posts"))


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "posts/edit_post.html"

    def form_valid(self, form):
        form.init(self.object)
        try:
            self.object = form.save()
        except Exception:
            return super().form_invalid(form)
        return HttpResponseRedirect(reverse("posts"))


class LikePostView(View):

    def get(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()
        post.add_liked_user(self.request.user)
        return redirect(self.request.META.get("HTTP_REFERER"))


class DislikePostView(View):

    def get(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()
        post.add_disliked_user(self.request.user)
        return redirect(self.request.META.get("HTTP_REFERER"))


class DeletePostView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse("posts")


class CommentPostView(CreateView):
    form_class = CommentForm
    template_name = "posts/post_detail.html"

    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs["post_id"])
        try:
            # Get the room token from form data
            content = form.cleaned_data.get("content")

            # Create the message
            comment = PostComment.objects.create(
                user=self.request.user, content=content
            )
            post.comments.add(comment)

            return redirect(self.request.META.get("HTTP_REFERER"))
        except post.DoesNotExist:
            messages.error(self.request, "Room not found")
            return redirect(self.request.META.get("HTTP_REFERER"))
        except Exception as e:
            messages.error(self.request, f"Error sending message: {str(e)}")
            return redirect(self.request.META.get("HTTP_REFERER"))
