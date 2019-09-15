import inject

from django.urls import path

from . import views
from .views import api

from polls_app.polls.repositories import QuestionRepository, ChoiceRepository

from polls_app.polls.repositories.questions import QuestionDBRepository
from polls_app.polls.repositories.choices import ChoiceDBRepository


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),

    # ex: /polls/5/
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),
    # path('specifics/<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/results/', views.results, name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),


    # path('questions', views.IndexViewQuestion.as_view(), name='questions')
    # path('questions/', views.IndexViewQuestion.as_view())
]


urlpatterns += [
    path(
        'api/', api.json_index, name='index_api'
    ),
    path(
        'api/<int:question_id>/', api.json_detail, name='detail_api'
    ),
    path(
        'api/<int:question_id>/results/', api.json_results, name='results_api'
    ),
    path(
        'api/<int:question_id>/vote/', views.json_vote, name='vote_api'
    ),
]


def inject_config(binder):
    binder.bind(QuestionRepository, QuestionDBRepository())
    binder.bind(ChoiceRepository, ChoiceDBRepository())


inject.configure(inject_config)
