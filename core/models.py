from django.db import models


# Create your models here.

class Software(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="软件名称")
    description = models.TextField(blank=True, null=True, verbose_name="描述")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "被测软件"
        verbose_name_plural = verbose_name


class SoftwareVersion(models.Model):
    software = models.ForeignKey(Software, on_delete=models.CASCADE, related_name='versions', verbose_name="所属软件")
    version = models.CharField(max_length=50, verbose_name="版本号")
    file = models.FileField(upload_to='software/', verbose_name="程序文件")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")

    def __str__(self):
        return f"{self.software.name} - {self.version}"

    class Meta:
        verbose_name = "软件版本"
        verbose_name_plural = verbose_name
        unique_together = ('software', 'version')


class TestData(models.Model):
    name = models.CharField(max_length=100, verbose_name="数据名称")
    description = models.TextField(blank=True, null=True, verbose_name="描述")
    file = models.FileField(upload_to='testdata/', verbose_name="数据文件")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "测试数据"
        verbose_name_plural = verbose_name


class TestCase(models.Model):
    name = models.CharField(max_length=200, verbose_name="用例名称")
    description = models.TextField(blank=True, null=True, verbose_name="用例描述")
    software_version = models.ForeignKey(SoftwareVersion, on_delete=models.PROTECT, verbose_name="被测软件版本")
    test_data = models.ManyToManyField(TestData, blank=True, verbose_name="关联测试数据")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "测试用例"
        verbose_name_plural = verbose_name


class TestRun(models.Model):
    STATUS_CHOICES = [
        ('PENDING', '待执行'),
        ('RUNNING', '执行中'),
        ('PASSED', '通过'),
        ('FAILED', '失败'),
        ('ERROR', '错误'),
    ]

    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE, related_name='runs', verbose_name="测试用例")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING', verbose_name="执行状态")
    output = models.TextField(blank=True, null=True, verbose_name="执行输出")
    started_at = models.DateTimeField(null=True, blank=True, verbose_name="开始时间")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="完成时间")

    def __str__(self):
        return f"{self.test_case.name} - {self.get_status_display()}"

    class Meta:
        verbose_name = "测试执行记录"
        verbose_name_plural = verbose_name
