
# 1. use fstrings for string formatting aka no + signs 
def manual_str_formatting(name, subscribers):
	if subscribers > 100:
		print(f"wow {name}! you have {subscribers} subs")
	else:
		print(f"lol {name}")

# 2. ensuring file closes even when an exception is raised 
def manual_file_close(filename):
	# f = open(filename, "w")
	# f.write("hello!\n")
	# f.close()
	with open(filename) as f:
		f.write("hello\n")

# 3. catch actual exception, i.e. ValueError,  
def exception():
	while True:
		try:
			inp = input("Input num: ")
			break 
		# except # would mean can't use CTRL-C to exit, CTRL will display "type input error"
		except ValueError: 
			print("type input error")

# 4. mutable default arguments
# default arguments are defined when function is defined, not when it's called, use a None default 
def append(n, l=None):
	if l is None: 
		l = []
	l.append(n)
	return l 

def comprehensions():
	dict_comp = {i: i*i for i in range(10)}
	list_comp = [x*x for x in range(10)]
	set_comp = {i%3 for i in range(10)}
	gen_comp = (2*x for x in range(10))

def type_checking(): # use isinstance 
	point = (5,2)
	if isinstance(point, tuple):
		print("is tuple")

# 5. check identity, rather than equality with ==
def identity(x):
	if x is None:
		pass
	if x is True:
		pass
	if x is False:
		pass

# 6. use zip to loop over two abjects at the same time, with/without enumerate  
def zip_loop():
	a = [1,2,3]
	b = [2,3,4]
	for an, bn in zip(a,b):
		print(an,bn)
	for i, (an,bn) in enumerate(zip(a,b)):
		print(i,an,bn)

# 7. looping over dict keys is the default 
def loop_keys():
	dicti = {i: i*2 for i in range(4)}
	for key in dicti:
		print(key)
	for key, val in dicti.items(): # or to get both 
		print(key,val)

# 8. import only modules you need, i.e. from x import you

# 9. package code and install into current environment is a thing 
# from module_in_directory import foo_function 
# ...
# from mypackage.module_in_directory import foo_function 
# ...
# def main():
# 	foo_function()
# if __name__ == '__main__':
# 	main()

# 10. use pep8