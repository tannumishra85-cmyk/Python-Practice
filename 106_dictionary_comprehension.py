marks = {
    "Math": 85,
    "Python": 92,
    "English": 67,
    "DSA": 38,
    "DBMS": 76
}


result = {key: value for  key , value in  marks.items() if value >= 70}
# {key: value for key, value in dictionary.items() if condition}


print(result)