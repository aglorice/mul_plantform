from django.contrib import admin
from .models import Software, SoftwareVersion, TestData, TestCase, TestRun

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(SoftwareVersion)
class SoftwareVersionAdmin(admin.ModelAdmin):
    list_display = ('software', 'version', 'uploaded_at')
    list_filter = ('software',)

@admin.register(TestData)
class TestDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at')
    search_fields = ('name',)

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'software_version', 'created_at')
    list_filter = ('software_version__software',)
    search_fields = ('name', 'description')

@admin.register(TestRun)
class TestRunAdmin(admin.ModelAdmin):
    list_display = ('test_case', 'status', 'started_at', 'completed_at')
    list_filter = ('status', 'test_case__software_version__software')
    readonly_fields = ('started_at', 'completed_at', 'output')
    search_fields = ('test_case__name',)
