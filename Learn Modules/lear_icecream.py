import os
import sys
from icecream import ic

os.system("cls")


def add(x, y):
    return x + y


# print(add(x=1, y=30))
# print(add(x=10, y=-1))
# print(add(x=20, y=0))
# print(add(x=30, y=6))
# print(add(x=40, y=30))
# print(add(x=50, y=5))

ic(add(x=1, y=30))
ic(add(x=10, y=-1))
ic(add(x=20, y=0))
ic(add(x=30, y=6))
ic(add(x=40, y=30))
ic(add(x=50, y=5))

print()
result = ic(add(x=50, y=5))
print(result)


data = {
    "data": [1, 2, 3, 4, 5],
    "labels": ["a", "b", "c", "d", "e"],
}

print()
print(data["data"][2])
print()
ic(data["data"][2])
print()

more_data = {
    "users": [
        {
            "id": 1,
            "name": "Alice",
            "posts": [
                {"title": "Hello World", "content": "Why I love Python"},
            ],
        }
    ],
}


print(more_data)
print()
ic(more_data)
print()
