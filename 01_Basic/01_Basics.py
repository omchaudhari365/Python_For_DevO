import math

#Data type & Variables
name = "Om"
age = 18
height = 5.8
is_student = True

#Fun^tn
def greet(user):
    return f"Hello, {user}!"

print(greet(name))

#operator
next_age = age + 1
print("Next Age:", next_age)

#condn
if age >= 18:
    print("Adult")
else:
    print("Minor")

#list & tuple
skills = ["Python", "AWS", "DevOps"]
skills.append("Linux")
futureskills=("GCP","Terraform")


#loop
print("\nSkills:")
for skill in skills:
    print(skill)

print("\nFuture Skills:")
for skill in futureskills:
  print(skill)


#Dict
server = {
    "name": "web-server",
    "ip": "192.168.1.10",
    "status": "running"
}
print("\nServer Info:",server)
    
#set
ports = {80, 443, 22, 80}
print("\nUnique Ports:", ports)


#string opertn
message = f"{name} is learning Python for DevOps."
print(message.upper())

cpu_usage = 75.5
memory_usage = 60
if cpu_usage > 70 and memory_usage > 50:
    print("High resource usage detected!")

#module
print("Square Root of 64:", math.sqrt(64))
