name = "Om"
age = 18
height = 5.8
is_student = True

def greet(user):
    return f"Hello, {user}!"

print(greet(name))

next_age = age + 1
print("Next Age:", next_age)

if age >= 18:
    print("Adult")
else:
    print("Minor")

skills = ["Python", "AWS", "DevOps"]
skills.append("Linux")

print("\nSkills:")
for skill in skills:
    print(skill)

server = {
    "name": "web-server",
    "ip": "192.168.1.10",
    "status": "running"
}

print("\nServer Info:")
for key, value in server.items():
    print(f"{key}: {value}")

ports = {80, 443, 22, 80}
print("\nUnique Ports:", ports)

message = f"{name} is learning Python for DevOps."
print(message.upper())

cpu_usage = 75.5
memory_usage = 60

if cpu_usage > 70 and memory_usage > 50:
    print("High resource usage detected!")

import math

print("Square Root of 64:", math.sqrt(64))
