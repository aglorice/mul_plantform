from rest_framework import serializers
from .models import Software, SoftwareVersion, TestData, TestCase, TestRun


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'


class SoftwareVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareVersion
        fields = '__all__'


class TestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestData
        fields = '__all__'


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'


class TestRunSerializer(serializers.ModelSerializer):
    test_case = TestCaseSerializer(read_only=True)

    class Meta:
        model = TestRun
        fields = '__all__'


class TestRunUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRun
        fields = ['status', 'output']
