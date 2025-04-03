import reminder as app

from reminder import Task
import pytest

@pytest.mark.parametrize("test_input, expected",
                         [("buy bread", Task(name="buy bread")),
                          ("buy banana", None),
                         ])
def test_find_task(test_input, expected):
    task_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task(test_input,task_list) == expected

# def test_find_task_none():
#     task_list = [Task(name="pay rent"), Task(name="buy bread")]
#     assert app._find_task("buy banana",task_list) is None