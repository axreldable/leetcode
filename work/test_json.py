import json


class User:
    def __init__(self, name, age, optional_field=None):
        self.name = name
        self.age = age
        self.optional_field = optional_field

    def __str__(self):
        return f"{self.name} - {self.age} - {self.optional_field}"


if __name__ == "__main__":
    # Create a Class object from the json string:
    js = '{"name":"John", "age":30, "optional_field":"123"}'
    js = '{"name":"John", "age":30}'

    d = json.loads(js)

    u = User(**d)
    print(u)
