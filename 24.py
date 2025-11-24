data=[
      {"name":"A","age":25},
      {"name":"B","age":20},
      {"name":"C","age":30}
    ]
new_data=sorted(data,key=lambda x:x.get("age"),reverse=True)
print(new_data)