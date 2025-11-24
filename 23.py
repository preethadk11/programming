data={"a":12,"b":None,"c":34}
clean={k:v for k,v in data.items() if v is not None}
print(clean)