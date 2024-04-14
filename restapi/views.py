from rest_framework import viewsets, response, status
from .models import Pereval
from .serializers import PerevalSerializer


# вьюсет для отправки пользователем данных о перевале
class SubmitData(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields = ["user__email"]

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

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        # если запись уже не новая
        if pereval.status != 'new':
            return response.Response({
                'state': 0,
                'message': 'Запись уже ушла на модерацию',
            })
        # если прошла проверку на новизну, то обновляем
        serializer = PerevalSerializer(pereval, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
               'state': 1,
               'message': 'Запись успешно обновлена',
            })
        else:
            return response.Response({
                'state': 0,
                'message': serializer.errors,
            })
