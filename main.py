import requests
from api_clients import get_users, get_todos
from user_filters import filter_users_by_location
from todo_calculator import calculate_todo_task_completion_percentage

def main():
    # Retrieve users from API
    users = get_users()

    # Filter users who belong to FanCode City
    fan_code_city_users = filter_users_by_location(users)

    # Iterate over filtered users
    for user in fan_code_city_users:
        # Retrieve todo tasks for user
        todos = get_todos(user['id'])

        # Calculate completion percentage
        completion_percentage = calculate_todo_task_completion_percentage(todos)

        # Verify completion percentage
        if completion_percentage > 50:
            print(f"User {user['name']} has completed {completion_percentage:.2f}% of their todo tasks.")
        else:
            print(f"User {user['name']} has not completed more than 50% of their todo tasks.")

if __name__ == '__main__':
    main()