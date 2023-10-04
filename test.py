import ast, json

str = "{\"key1\": \"value1\"},"

obj = ast.literal_eval(str)

json_str = json.dumps(obj)

print(json_str)

