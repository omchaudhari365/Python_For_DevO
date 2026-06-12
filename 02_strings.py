#concat
a = "hellow"
b = "BRO"
r = a  +" "+ b
print(r)

#len
print("length of string is",len(a))

#lower&Upper
upper = a.upper()
lower = b.lower()
print(upper,lower)


#replace
text = "python for cloud"
new_text = text.replace("cloud","DevOps")
print("modified text: ",new_text)

#split
cloud = "Aws and Gcp are cloud platforms"
words = cloud.split()
print("words: ",words)

#strip
p = "some space around"
stripd_text = p.strip()
print("striped text: ",stripd_text)

#substring
q = "python for DevOps"
substring = "DevOps"
if substring in q :
    print(substring," found in q")
