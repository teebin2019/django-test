from django.urls import path
from .views import home, post_detail   # Correctly importing functions

urlpatterns = [
    path('', home, name="home"),  # Remove 'views.' since we imported them directly
    path('blog/<int:post_id>/', post_detail, name="post_detail"),  # Added a trailing slash for consistency
]
