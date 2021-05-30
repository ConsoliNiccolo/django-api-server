from django.urls import include, path
from .views import TokenCreate, TokenList, TokenDetail, TokenUpdate, TokenDelete


urlpatterns = [
	path('create/', TokenCreate.as_view(), name='create-token'),
    path('', TokenList.as_view()),
    path('<int:pk>/', TokenDetail.as_view(), name='retrieve-token'),
    path('update/<int:pk>/', TokenUpdate.as_view(), name='update-token'),
    # path('delete/<int:pk>/', TokenDelete.as_view(), name='delete-token')
]