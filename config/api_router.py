from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from covidtracker.tracker.api.views import CaseViewSet, LocationViewSet, TimeLineViewSet
from covidtracker.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register(r"locations", LocationViewSet)
router.register(r"timelines", TimeLineViewSet)
router.register(r"cases", CaseViewSet)


app_name = "api"
urlpatterns = router.urls
