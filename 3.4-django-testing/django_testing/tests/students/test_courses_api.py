import pytest
from django.urls import reverse

from students.models import Course


@pytest.mark.django_db
def test_get_course(api_client, course_factory):
    course = course_factory(_quantity=1)
    url = reverse('courses-detail', args=(course[0].id,))
    resp = api_client.get(url)
    resp_json = resp.json()

    assert resp.status_code == 200
    assert course[0].id == resp_json.get('id')
    assert course[0].name == resp_json.get('name')


@pytest.mark.django_db
def test_get_courses(api_client, course_factory):
    course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = api_client.get(url)

    assert resp.status_code == 200
    assert len(resp.data) == 3


@pytest.mark.django_db
def test_filters_courses_id(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = api_client.get(url, data={'id': courses[0].id})
    resp_json = resp.json()

    assert resp.status_code == 200
    assert courses[0].id == resp_json[0].get('id')


@pytest.mark.django_db
def test_filters_courses_name(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = api_client.get(url, data={'name': courses[0].name})
    resp_json = resp.json()

    print(resp_json)

    assert resp.status_code == 200
    assert courses[0].name == resp_json[0].get('name')


@pytest.mark.django_db
def test_create_course(api_client):
    data = {
        'name': 'Python'
    }
    url = reverse('courses-list')
    resp = api_client.post(url, data=data)

    assert resp.status_code == 201
    assert resp.data['name'] == 'Python'


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    data = {
        'name': 'Python'
    }
    courses = course_factory(_quantity=1)
    url = reverse('courses-detail', args=(courses[0].id,))
    resp = api_client.patch(url, data=data)

    assert resp.status_code == 200
    assert resp.data['name'] == 'Python'


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    courses = course_factory(_quantity=3)
    counts_objects = Course.objects.count()

    url = reverse('courses-detail', args=(courses[0].id,))
    resp = api_client.delete(url)

    assert resp.status_code == 204
    assert counts_objects - 1 == Course.objects.count()

