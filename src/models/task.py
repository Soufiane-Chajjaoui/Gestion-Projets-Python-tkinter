import time

class Task:
    STATUSES = {"to do", "in progress", "done"}

    def __init__(self, title, description, status, user,project, task_id=None):
        """
        Initializes a task.

        Args:
            task_id (int | None): Unique identifier for the task.
            title (str): The title of the task.
            description (str): The task's description.
            status (str): The task's status ('to do', 'in progress', 'done').
            user (User): The user responsible for the task.
            project (Project): The project attach for the task.
        """
        self.id = task_id if task_id else int(time.time() * 1000)  # Generate a unique ID based on timestamp
        self.title = title
        self.description = description
        self.user = user  # User ID
        self.project = project # Project ID

        if status.lower() not in self.STATUSES:
            raise ValueError(f"Invalid status. Choose from {self.STATUSES}")
        self.status = status.lower()

    def to_dict(self):
        """
        Converts the Task object into a dictionary.

        Returns:
            dict: A dictionary representation of the task.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "user": self.user,
            "project": self.project
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Task object from a dictionary.

        Args:
            data (dict): The task data as a dictionary.

        Returns:
            Task: The recreated Task object.
        """
        
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data["description"],
            status=data["status"],
            user=data["user"],
            project=data["project"]
        )
