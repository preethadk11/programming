scores=[72,85,90,60,45,99,38]
result=[]
for x in scores:
   status="Pass" if x>50 else "Fail"
   result.append({"Score":x,"Status":status})
print(result)
   
