from rest_framework import viewsets, response, status
from .models import Pereval
from .serializers import PerevalSerializer


# вьюсет для отправки пользователем данных о перевале
class SubmitData(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    # перепилим функцию create, чтобы ответ был таким, какой нам нужен
    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
                'status': status.HTTP_200_OK,
                'message': 'Отправка успешна',
                'id': serializer.data['id'],
            })
        if status.HTTP_400_BAD_REQUEST:
            return response.Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad Request',
                'id': None,
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return response.Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Ошибка подключения к базе данных',
                'id': None,
            })
