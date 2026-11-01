marks = {
    "Math": 85,
    "Python": 92,
    "English": 67,
    "DSA": 38,
    "DBMS": 76
}

print(marks)
marks["DBMS"] = 89
print(marks["DBMS"])


for key,value in marks.items():
    print(key, " = " , value)

result = {key: value for  key , value in  marks.items() if value >= 70}
# {key: value for key, value in dictionary.items() if condition}


#print(result)