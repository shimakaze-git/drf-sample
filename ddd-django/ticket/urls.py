from django.urls import path
# from django.contrib.auth.decorators import login_required
# from talent.views import profile, notify_agent, email, job_entry

# from django.urls import path, include
# from rest_framework import routers
# from .views import ArticleViewSet, MemberViewSet

from .views import TicketCreateView

# router = routers.DefaultRouter()
# router.register('members', MemberViewSet)
# router.register('articles', ArticleViewSet)

urlpatterns = [
    # path("", include(router.urls))
    path('', TicketCreateView.as_view())
]

# path(
#     "<pk>/profile/edit/",
#     login_required(profile.TalentProfileEdit.as_view())
# ),
