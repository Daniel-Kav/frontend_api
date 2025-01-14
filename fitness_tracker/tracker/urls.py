from django.urls import path,include
from .views import index
from rest_framework.routers import DefaultRouter
from tracker import views



router = DefaultRouter()
router.register(r'user_profiles', views.UserProfileViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'meals', views.MealViewSet)
router.register(r'goals', views.GoalViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]


