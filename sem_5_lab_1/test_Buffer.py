import pytest
from Buffer import Buffer

max_buf_file_size = 10
item = "123"


@pytest.fixture
def buf():
    return Buffer(max_buf_file_size)


def test_can_push_and_pop_item(buf):
    buf.push(item)
    assert item in buf.info
    buf.pop()
    assert item not in buf.info


def test_cannot_push_more_to_buffer(buf):
    for _ in range(max_buf_file_size):
        buf.push(item)
    with pytest.raises(OverflowError):
        buf.push(item)


def test_cannot_pop_more_from_buffer(buf):
    buf.push(item)
    buf.pop()
    with pytest.raises(IndexError):
        buf.pop()

