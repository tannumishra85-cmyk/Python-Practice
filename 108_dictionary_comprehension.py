marks = {
    "Math": 85,
    "Python": 92,
    "English": 37,
    "DSA": 45,
    "DBMS": 28
}

result = {key: "pass" if value >= 40 else "Fail"
          for key, value in marks.items()}

print(result)