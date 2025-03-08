from django.urls import path
from .views import home, post_detail , home1 , post_detail1  # Correctly importing functions

urlpatterns = [
    path('', home, name="home"),  # Remove 'views.' since we imported them directly
    path('blog/<int:post_id>/', post_detail, name="post_detail"),  # Added a trailing slash for consistency
    path('1/', home1, name="home"),  # Remove 'views.' since we imported them directly
    path('blog1/<int:post_id>/', post_detail1, name="post_detail1"),  # Added a trailing slash for consistency
]
