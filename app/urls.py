from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'demandes-vidage', DemandeVidageViewSet)
router.register(r'demandes-lavage', DemandeLavageViewSet)
router.register(r'demandes-puisage', DemandePuisageViewSet)

urlpatterns = router.urls
