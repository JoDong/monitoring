from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from domain.forms import UrlForm
from domain.models import UrlModel
from statuslog.models import StatusLog


# 메인 페이지 (조회) - 조회
@login_required
def home(request):
    all_urls = UrlModel.objects.all().order_by('-created_at')
    status_log = StatusLog.objects.all().order_by('-created_at')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_urls, 5)
    urls = paginator.get_page(page)
    return render(request, 'domain/home.html', {'urls': urls, 'status_log': status_log})


# 디테일 페이지
@login_required
def detail(request, pk):
    urls = get_object_or_404(UrlModel, pk=pk)
    all_status_log = StatusLog.objects.filter(url=urls.pk).order_by('-created_at')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_status_log, 30)
    status_log = paginator.get_page(page)

    return render(request, 'domain/detail.html', {'urls': urls, 'status_log': status_log})


# 생성
@login_required
def url_create(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.save()

            return redirect('/')

        else:
            return render(request, 'domain/url_create.html', {'form': form})
    else:
        return render(request, 'domain/url_create.html', {'form': UrlForm()})


# 수정
@login_required
def url_update(request, pk):
    url = get_object_or_404(UrlModel, pk=pk)
    if request.method == 'POST':
        form = UrlForm(request.POST, instance=url)
        if form.is_valid():
            url = form.save(commit=False)
            url.save()
            return HttpResponseRedirect("/detail/{id}".format(id=url.pk))
        else:
            return redirect('home')
    else:
        form = UrlForm(instance=url)
    return render(request, 'domain/url_update.html', {'form': form, 'url': url})


# 삭제
@login_required
def url_delete(request, pk):
    url = get_object_or_404(UrlModel, pk=pk)
    url.delete()
    return redirect('home')


#  chart
def url_charts(request, pk):
    pass
