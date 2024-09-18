def calculate_todo_task_completion_percentage(todos):
    completed_tasks = sum(1 for todo in todos if todo['completed'])
    total_tasks = len(todos)
    return (completed_tasks / total_tasks) * 100