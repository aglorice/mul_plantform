from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from .models import TestRun
from .serializers import TestRunSerializer, TestRunUpdateSerializer


# Create your views here.

@api_view(['GET'])
def get_next_task(request):
    """
    获取下一个待执行的任务，并将其状态更新为"执行中"。
    """
    next_run = TestRun.objects.filter(status='PENDING').order_by('id').first()
    if next_run:
        next_run.status = 'RUNNING'
        next_run.started_at = timezone.now()
        next_run.save()
        serializer = TestRunSerializer(next_run)
        return Response(serializer.data)
    else:
        return Response({'detail': 'No pending tasks available.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update_task_status(request, pk):
    """
    更新指定任务的状态和输出。
    """
    try:
        test_run = TestRun.objects.get(pk=pk)
    except TestRun.DoesNotExist:
        return Response({'detail': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TestRunUpdateSerializer(test_run, data=request.data, partial=True)
    if serializer.is_valid():
        # 在保存前，额外设置完成时间
        if 'status' in serializer.validated_data and serializer.validated_data['status'] in ['PASSED', 'FAILED',
                                                                                             'ERROR']:
            serializer.instance.completed_at = timezone.now()
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
