from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from user.views import custom_user_views, register_views

urlpatterns = [
    path("", custom_user_views.CustomUserList.as_view()),
    path("<int:pk>", custom_user_views.CustomUserDetail.as_view()),
    path("logout", register_views.CustomLogoutView.as_view(), name="logout"),
    path(
        "api/token",
        register_views.CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
