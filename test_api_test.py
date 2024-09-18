import pytest
from main import main, get_users, get_todos

def test_all_fancode_users_have_more_than_half_tasks_completed(capsys):
    # Test case 1: All users have more than half tasks completed
    main()
    captured = capsys.readouterr()
    output = captured.out
    assert all("has completed" in line and "more than 50%" not in line for line in output.splitlines())



def test_one_fancode_user_with_half_tasks_completed(capsys):
    # Test case 3: One user from FanCode City has exactly half tasks completed
    users = get_users()
    fan_code_users = [user for user in users if user['address']['geo']['lat'] == 0 and user['address']['geo']['lng'] == 50]
    if fan_code_users:
        user_id = fan_code_users[0]['id']
        todos = get_todos(user_id)
        completed_todos = [todo for todo in todos if todo['completed']]
        if len(completed_todos) == len(todos) / 2:
            main()
            captured = capsys.readouterr()
            output = captured.out
            assert "has not completed more than 50% of their todo tasks." in output

def test_one_fancode_user_with_all_tasks_completed(capsys):
    # Test case 4: One user from FanCode City has all tasks completed
    users = get_users()
    fan_code_users = [user for user in users if user['address']['geo']['lat'] == 0 and user['address']['geo']['lng'] == 50]
    if fan_code_users:
        user_id = fan_code_users[0]['id']
        todos = get_todos(user_id)
        completed_todos = [todo for todo in todos if todo['completed']]
        if len(completed_todos) == len(todos):
            main()
            captured = capsys.readouterr()
            output = captured.out
            assert "has completed 100.00% of their todo tasks." in output

def test_multiple_fancode_users_with_more_than_half_tasks_completed(capsys):
    # Test case 5: Multiple users from FanCode City have more than half tasks completed
    users = get_users()
    fan_code_users = [user for user in users if user['address']['geo']['lat'] == 0 and user['address']['geo']['lng'] == 50]
    if len(fan_code_users) > 1:
        for user in fan_code_users:
            user_id = user['id']
            todos = get_todos(user_id)
            completed_todos = [todo for todo in todos if todo['completed']]
            if len(completed_todos) > len(todos) / 2:
                main()
                captured = capsys.readouterr()
                output = captured.out
                assert all("has completed" in line and "more than 50%" not in line for line in output.splitlines())

def test_api_errors(capsys):
    # Test case 6: API errors occur while retrieving users or todos
    try:
        get_users()
        get_todos(1)
    except Exception as e:
        main()
        captured = capsys.readouterr()
        output = captured.out
        assert "Error occurred while retrieving users or todos" in output