# from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Product
# from django.views import View
# from django.http import HttpResponseRedirect
# from django.urls import reverse
#
#
# class AddLike(LoginRequiredMixin, View):
#
#     def post(self, request, pk, *args, **kwargs):
#         post = Product.objects.get(pk=pk)
#
#         is_dislike = False
#
#         for dislike in post.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break
#
#
#         if is_dislike:
#             post.dislikes.remove(request.user)
#
#         is_like = False
#
#         for like in post.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break
#
#         if not is_like:
#             post.likes.add(request.user)
#
#         if is_like:
#             post.likes.remove(request.user)
#
#         return HttpResponseRedirect(reverse('product', args=[str(pk)]))
#
#
#
# class AddDislike(LoginRequiredMixin, View):
#
#     def post(self, request, pk, *args, **kwargs):
#         post = Product.objects.get(pk=pk)
#
#         is_like = False
#
#         for like in post.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break
#
#         if is_like:
#             post.likes.remove(request.user)
#
#
#
#         is_dislike = False
#
#         for dislike in post.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 break
#
#         if not is_dislike:
#             post.dislikes.add(request.user)
#
#         if is_dislike:
#             post.dislikes.remove(request.user)
#
#         return HttpResponseRedirect(reverse('product', args=[str(pk)]))