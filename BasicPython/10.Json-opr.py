import json

print("-----------------------------------CODE BEGINS ---------------------------------------")

## Code Here...
student = { "id": 1, "grade":"primary", "name": "neeraj"}
print(type(student),student)
studentJson = json.dumps(student)
print(type(studentJson),studentJson)

print("-----------------------------------CODE ENDS ---------------------------------------")