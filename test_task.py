import pytest
from requests.exceptions import HTTPError

from task import (
    get_post_by_id,
    get_posts_by_user_id,
    get_post_by_id_with_validation
)


def test_get_post_by_id_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {'id': 1}
    mocker.patch('task.http_get', return_value=mock_response)
    assert get_post_by_id(1) == {'id': 1}


def test_get_post_by_id_failure(mocker):
    mocker.patch('task.http_get', side_effect=HTTPError('HTTP Error'))
    assert get_post_by_id(1) is None


def test_get_posts_by_user_id_success(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {'id': 1}
    mocker.patch('task.http_get', return_value=mock_response)
    assert get_posts_by_user_id(1) == {'id': 1}


def test_get_posts_by_user_id_failure(mocker):
    mocker.patch('task.http_get', side_effect=HTTPError('HTTP Error'))
    assert get_posts_by_user_id(1) is None


def test_get_post_by_id_with_validation_succsee(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {'id': 1}
    mocker.patch('task.http_get', return_value=mock_response)
    assert get_post_by_id_with_validation(1) == {'id': 1}


def test_get_post_by_id_with_validation_failure(mocker):
    mocker.patch('task.http_get', side_effect=HTTPError('HTTP Error'))
    assert get_post_by_id_with_validation(1) is None


def test_get_post_by_id_with_validation_invalid_post_id():
    with pytest.raises(ValueError, match='post_id must be greater than 0'):
        get_post_by_id_with_validation(-1)
