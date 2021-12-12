# Python 3 code to demonstrate the  
# working of MD5 (byte - byte) 
  
import hashlib 
  
eg2 = b'abcdef609043'
eg2_res = hashlib.md5(eg2)
print(f"The byte equivalent of {eg2} is : {eg2_res.digest()} or {eg2_res.hexdigest()}") 

eg3 = b'pqrstuv1048970'
eg3_res = hashlib.md5(eg3)
print(f"The byte equivalent of {eg3} is : {eg3_res.digest()} or {eg3_res.hexdigest()}") 