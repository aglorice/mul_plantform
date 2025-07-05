#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # 设置Django的设置模块
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_platform.settings')
    try:
        # 尝试导入Django的管理命令
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # 如果导入失败，抛出异常
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 执行Django的管理命令
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
