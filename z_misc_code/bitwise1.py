# Soure: https://www.geeksforgeeks.org/python-bitwise-operators/

# Python program to show 
# bitwise operators 

a = 10
b = 4
	
# Print bitwise AND operation 
print("a & b =", a & b) 
	
# Print bitwise OR operation 
print("a | b =", a | b) 
	
# Print bitwise NOT operation 
print("~a =", ~a) 
	
# print bitwise XOR operation 
print("a ^ b =", a ^ b) 

# Python program to show 
# shift operators 

a = 10
b = -10

# print bitwise right shift operator 
print("a >> 1 =", a >> 1) 
print("b >> 1 =", b >> 1) 

a = 5
b = -10

# print bitwise left shift operator 
print("a << 1 =", a << 1) 
print("b << 1 =", b << 1) 


# Python program to demonstrate 
# operator overloading 

class Geek(): 
	def __init__(self, value): 
		self.value = value 
		
	def __and__(self, obj): 
		print("And operator overloaded") 
		if isinstance(obj, Geek): 
			return self.value & obj.value 
		else: 
			raise ValueError("Must be a object of class Geek") 
			
	def __or__(self, obj): 
		print("Or operator overloaded") 
		if isinstance(obj, Geek): 
			return self.value | obj.value 
		else: 
			raise ValueError("Must be a object of class Geek") 
			
	def __xor__(self, obj): 
		print("Xor operator overloaded") 
		if isinstance(obj, Geek): 
			return self.value ^ obj.value 
		else: 
			raise ValueError("Must be a object of class Geek") 
	
	def __lshift__(self, obj): 
		print("lshift operator overloaded") 
		if isinstance(obj, Geek): 
			return self.value << obj.value 
		else: 
			raise ValueError("Must be a object of class Geek") 
			
	def __rshift__(self, obj): 
		print("rshift operator overloaded") 
		if isinstance(obj, Geek): 
			return self.value & obj.value 
		else: 
			raise ValueError("Must be a object of class Geek") 
			
	def __invert__(self): 
		print("Invert operator overloaded") 
		return ~self.value 
		
		
# Driver's code 
if __name__ == "__main__": 
	a = Geek(10) 
	b = Geek(12) 
	print(a&b) 
	print(a|b) 
	print(a ^ b) 
	print(a<<b) 
	print(a>>b) 
	print(~a) 
