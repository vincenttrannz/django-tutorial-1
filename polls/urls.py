from django.urls import path

from .views import IndexView, DetailView, ResultsView, vote

# This app_name to declare which app we want to declare to access the obeject in frontend for URL
app_name = 'polls'

# urlpatterns = [
#     # Poll page "/polls"
#     path('', index, name='index'),
#     # Question detail page "/polls"
#     # the 'name' value as called by the {% url %} template tag
#     path('<int:question_id>/', detail, name='detail'),
#     # /polls/5/results/
#     path('<int:question_id>/results/', results, name='results'),
#     # /polls/5/vote/
#     path('<int:question_id>/vote/', vote, name='vote'),
# ]

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]