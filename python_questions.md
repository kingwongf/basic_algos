Python Interview questions

1. What's a decorator? 
	a synthetic sugar that accepts a function w/o medifiying its behaviour 

2. What're @property, getters, setters and deletar?
	@<method>.getter: methods helps to access the private attributes from a class
	@<method>.setter: methods helps to set the value to private
	@property: e.g. self.__a = a in __init__, private variable or property, tunring the function into a "getter" method
			  basically __init__ initialise the attributes or properties of a class
	instead of using 
	```
	def get_<method>: 
		return self.__a
	```
	we define 
	```
	@property
	def a(self):
		''' get a '''
	    return self.__a
	```
	this turns method a() into a "getter" and set docstring to 'get a'. You can also use 'setter' if you add a setter after the function.
	```
	@a.setter
	def a(self,val):
		self.__a = val
	```
	you can also use property() instead of @property
	```
	class C(object):
	    def getx(self): return self.__x
	    def setx(self, value): self.__x = value
	    def delx(self): del self.__x
	    x = property(getx, setx, delx, "I'm the 'x' property.")
	```





3. What's a context manager?
	allocate and release resources precisely, e.g. `with`, make sure file is closed. 


4. What's a generator?
	yield in function


5. What's a descriptor?
	built-in descriptors include python function, properties, static methods, class methods

	if any of `__get__()`, `__set__()`, and `__delete__()` methods are defined for an object, it's a descriptor.

	https://docs.python.org/3/howto/descriptor.html


	You can build a descriptor using property() as show aboved. 

	## Functions and methods
	All functions are non-data descriptors which return bound methods( methods that are dependent on the instance of the class as the first argument) when they are inovke from an object. 

	```
	>>> class D(object):
	...     def f(self, x):
	...         return x
	...
	>>> d = D()
	# Access through the class dictionary does not invoke __get__.
	# It just returns the underlying function object.
	>>> D.__dict__['f']
	<function D.f at 0x00C45070>
	# Dotted access from a class calls __get__() which just returns
	# the underlying function unchanged.
	>>> D.f
	<function D.f at 0x00C45070>
	# The function has a __qualname__ attribute to support introspection
	>>> D.f.__qualname__
	'D.f'
	# Dotted access from an instance calls __get__() which returns the
	# function wrapped in a bound method object
	>>> d.f
	<bound method D.f of <__main__.D object at 0x00B18C90>>
	```
	## Static Methods and Class methods
	static method just returns the same/ underlying function
	class method has a class(not instance) as the first argument, so sth with it



6. What's a staticmethod?

7. What's a abstract base class?

8. What's a classmethod?

9. What's polymorphism?

10. Why not put mutable in args?

11. What are args and kwargs?

12. What's lambda?
	inline function

13. What're properties, attributes and methods?

14. What's dir? returns all properties and methods of the object?

15. What's name mangling? 
	if you set `self.__c__`, it will change to `self._<class_name>.__c`, even if you reference sth to `self._<class_name>.__c` before, it will change to that variable assigned


16. Write a context_manager that redirects stdout and stderr

17. When to use multithreading and multiprocessing?

18. Write a a decorator that catches exception to stdout

19. How many classes I need to price a swap, a bond, a future? 
	With polymorphism and inheritance, you can first create a parent class with fixed and floating legs methods, the child classes that inherit the methods to price different products. 

20. Write a map() function without increasing memory complexity.

21. What's GIL and how it affects the code?

22. How GIL transform the code to machine language?

23. Difference between methods and functions?
	methods' first argument is the obj instance e.g. self where function is defined as def/ lambda

24. What is an instance?

	e.g. x = some_class('x_instance'), x here is an instance object of the a class, which is different from the class "some_class" itself. Mainly when you call
	```
	some_class.some_method 
	```
	gives the function, while when you call
	```
	some_class().some_method 
	```
	gives the bound method 



