from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from learningpage.models import learningpost

urlpatterns = [
                url(r'^$', ListView.as_view(queryset=learningpost.objects.all().order_by("-date")[:25],
                                            template_name="learningpage/learningpage.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = learningpost,
                                                         template_name = "learningpage/learningpost.html")),

              ]