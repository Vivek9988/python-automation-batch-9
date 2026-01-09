import pytest
import app


@pytest.fixture
def sample_users():
    return [
        {"id": 1, "name": "Vivek", "email": "vivek@test.com"},
        {"id": 2, "name": "Amit", "email": "amit@test.com"},
        {"id": 3, "name": "NoEmail"},  # invalid
        {"id": 4, "email": "x@test.com"},  # invalid
    ]


@pytest.mark.parametrize("record, expected", [
    ({"id": 1, "name": "A", "email": "a@test.com"}, True),
    ({"id": 1, "name": "A"}, False),
    ({"name": "A", "email": "a@test.com"}, False),
])
def test_is_valid_record(record, expected):
    assert app.is_valid_record(record) == expected


def test_filter_valid_records(sample_users):
    valid = app.filter_valid_records(sample_users)
    assert len(valid) == 2


def test_api_success():
    url = "https://jsonplaceholder.typicode.com/users"
    data = app.fetch_users(url)
    assert isinstance(data, list)
    assert len(data) > 0


def test_api_invalid_response():
    with pytest.raises(Exception):
        app.fetch_users("https://invalid-url-123456.com")


def test_file_write(sample_users, tmp_path):
    valid = app.filter_valid_records(sample_users)

    json_file = tmp_path / "test.json"
    csv_file = tmp_path / "test.csv"

    app.save_to_json(json_file, valid)
    app.save_to_csv(csv_file, valid)

    assert json_file.exists()
    assert csv_file.exists()


@pytest.mark.xfail(reason="Feature not implemented yet")
def test_future_feature():
    assert app.some_future_function() == True
