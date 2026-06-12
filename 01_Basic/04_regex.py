import re
text = "my age is 19"

# Find numbers
num = re.findall(r"\d+", text)
print(num)

# Search for a word
result = re.search("python", text)
if result:
    print("found")
else:
    print("not found")

# Replace 19 with nineteen
neww = re.sub(r"\d+", "nineteen", text)
print(neww)

# Split text
fruits = "apple,banana,orange,grape"
split_result = re.split(",", fruits)
print("Split result:", split_result)