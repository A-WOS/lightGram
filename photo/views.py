from urllib.parse import urlparse

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from photo.models import Photo


#
class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'


class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_update'

    # success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PhotoUpdate, self).dispatch(request, *args, **kwargs)


class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'

    # success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PhotoDelete, self).dispatch(request, *args, **kwargs)


class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'


class PhotoLike(View):
    def get(self, request, *args, **kwargs):
        # 로그인 확인
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user

                # user가 이미 좋아요 한 사람 중에 있으면 클릭했을 때 지워지도록 하고
                if user in photo.like.all():
                    photo.like.remove(user)
                # 그렇지 않으면 더하게 함.
                else:
                    photo.like.add(user)

            # referer_url을 통해서 url을 parse하여
            # 만약에 메인페이지에서 좋아요를 누르면 그 메인페이지에 있도록 하고
            # 상세페이지에서 좋아요를 누르면 그 상세페이지로 redirect하게 함.
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class PhotoFavorite(View):
    def get(self, request, *args, **kwargs):
        # 로그인 확인
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.favorite.all():
                    photo.favorite.remove(user)
                else:
                    photo.favorite.add(user)
            return HttpResponseRedirect('/')


class PhotoLikeList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(PhotoLikeList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # 내가 좋아요한 글을 보여줌
        user = self.request.user
        queryset = user.like_post.all()
        return queryset


class PhotoFavoriteList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(PhotoFavoriteList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # 내가 좋아요한 글을 보여줌
        user = self.request.user
        queryset = user.favorite_post.all()
        return queryset
