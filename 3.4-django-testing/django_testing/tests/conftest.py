import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def api_client():
    """Фикстура для клиента API"""
    return APIClient()


@pytest.fixture
def course_factory():
    """Фабрика для курсов"""
    def factory(**kwargs):
        return baker.make('Course', **kwargs)
    return factory


@pytest.fixture
def students_factory():
    """Фабрика для студентов"""
    def factory(**kwargs):
        return baker.make('Student', **kwargs)
    return factory