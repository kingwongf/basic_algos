# Python Interview questions

1. ## What's a decorator? 
	a synthetic sugar that accepts a function w/o medifiying its behaviour 

2. ## What're @property, getters, setters and deletar?
	- @getter: methods helps to access the private attributes from a class
	- @setter: methods helps to set the value to private
	- @property: e.g. self.__a = a in __init__, private variable or property, tunring the function into a "getter" method
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





3. ## What's a context manager?
	To allocate and release resources precisely, e.g. `with`, make sure file is closed. 


4. ## What's a generator?
	yield in function


5. ## What's a descriptor?
	built-in descriptors include python function, properties, static methods, class methods

	if any of `__get__()`, `__set__()`, and `__delete__()` methods are defined for an object, it's a descriptor.

	https://docs.python.org/3/howto/descriptor.html


	You can build a descriptor using property() as show aboved. 

	### Functions and methods
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
	### Static Methods and Class 
	Review this
	[Python HOWTO](https://docs.python.org/3/howto/descriptor.html#static-methods-and-class-methods "Descriptor")
	Non-data descriptors provide a simple mechanism for variations on the usual patterns of binding functions into methods.

	To recap, functions have a `__get__()` method so that they can be converted to a method when accessed as attributes. The non-data descriptor transforms an `obj.f(*args)` call into `f(obj, *args)`. Calling `klass.f(*args)` becomes `f(*args)`.

	static method returns the same/ underlying function
	class method has a class, not instance as the first argument, result same as `type(self).__<some method>__`. But the @classmethod calls on the class object alone, not self, the instance. Review this,
	[When should I use @classmethod and when def method(self)?](https://stackoverflow.com/questions/10586787/when-should-i-use-classmethod-and-when-def-methodself)



6. ## What's a staticmethod?
	A function within a class that is a pure function, accepts only arguments, not the its class instance at the first term. e.g.
	```
	class a(object):
	    def __init__(self,var):
	        self.var = var
	    @staticmethod
	    def sth_static(a,b):
	        print(a+b)
	    def sth_norma(self,a,b):
	        print(a+b)
	x = a(4)
	print(x.sth_norma)
	<bound method a.sth_norma of <__main__.a object at 0x103f628d0>>
	print(x.sth_static)
	<function a.sth_static at 0x1059d2680>
	```


7. ## What's an abstract base class?
	Review this [ABC](https://pymotw.com/2/abc/#:~:text=Abstract%20base%20classes%20are%20a,for%20a%20set%20of%20subclasses.)
	An abstract base class is a blueprint for other subclasses you later going to write. e.g.
	```
	import abc

	class PluginBase(object):
	    __metaclass__ = abc.ABCMeta

	    @abc.abstractmethod
	    def load(self, input):
		"""Retrieve data from the input source and return an object."""
		return

	    @abc.abstractmethod
	    def save(self, output, data):
		"""Save the data object to the output."""
		return
	```

	Later we can import this base.py and define the actual methods through subclassing
	```
	import abc
	from abc_base import PluginBase

	class SubclassImplementation(PluginBase):
	    
	    def load(self, input):
	        return input.read()
	    
	    def save(self, output, data):
	        return output.write(data)
	if __name__ == '__main__':
	    print 'Subclass:', issubclass(SubclassImplementation, PluginBase)
	    print 'Instance:', isinstance(SubclassImplementation(), PluginBase)
	```

	Useful abc in standard library,
	The collections module defines several abstract base classes related to container (and containable) types.

	General container classes:
		- Container
		- Sized

	Iterator and Sequence classes:
		- Iterable
		- Iterator
		- Sequence
		- MutableSequence

	Unique values:
		- Hashable
		- Set
		- MutableSet

	Mappings:
		- Mapping
		- MutableMapping
		- MappingView
		- KeysView
		- ItemsView
		- ValuesView

	Miscelaneous:
		- Callable


8. ## What's a classmethod?
	@classmethod takes the class (not the instance) as the first argument.


9. ## What're polymorphism and method overriding?
	Polymorphism means the ability to take different form.
	e.g. len() is a polymorphic function as it takes, list, string, dict
	Method overriding is when the subclasses methods overriding the parent class's methods, while retaining methods that are not mentioned in the subclasses.
	```
	from math import pi
	class Shape:
	    def __init__(self, name):
	        self.name = name

	    def area(self):
	        pass

	    def fact(self):
	        return "I am a two-dimensional shape."

	    def __str__(self):
	        return self.name


	class Square(Shape):
	    def __init__(self, length):
	        super().__init__("Square")
	        self.length = length

	    def area(self):
	        return self.length**2

	    def fact(self):
	        return "Squares have each angle equal to 90 degrees."


	class Circle(Shape):
	    def __init__(self, radius):
	        super().__init__("Circle")
	        self.radius = radius

	    def area(self):
	        return pi*self.radius**2
	```

	This outputs the following,
	```
	Circle
	I am a two-dimensional shape.
	Squares have each angle equal to 90 degrees.
	153.93804002589985
	```

	`area()` has been overrided but `__str__` is retained from parent. Remember to inherit parent class's attributes,
	
	```
	super().__init__("Square")
	```


10. ## Why not put mutable in args?
	Because it will be kept as the same reference.
	```
	def sth_f(a, b=[]):
	    b.append(a)
	    return b
	def sth_g(a):
	    b = []
	    b.append(a)
	    return b
	print(sth_f(5))
	print(sth_f(6))
	print(sth_g(5))
	print(sth_g(6))
	```

	Gives
	```
	[5]
	[5, 6]
	[5]
	[6]
	```


11. ### What are `*args` and `**kwargs`?
	non-keyword and kewyword argumnets. e.g. iterable and a dict.


12. ### What's lambda?
	inline function

13. ### What're properties, attributes and methods?
	properties are any function that is `get`, `set` or `fdel`.
	class attributes are share across instance while instance attributes are instance specific.

14. ### What's dir? 
	returns the local namespace of obj, when dir(obj)
15. ### What's name mangling? 
	if you set `self.__c__`, it will change to `self._<class_name>.__c`, even if you reference sth to `self._<class_name>.__c` before, it will change to that variable assigned


16. ### Write a context_manager that redirects stdout and stderr

17. ### When to use multithreading and multiprocessing?

18. ### Write a a decorator that catches exception to stdout
	```
	def exception_exec(func):
	    def inner_func(*args, **kwargs)
                try:
		    func(*args, **kwargs)
		except as e:
	            sys.stdout = e
	    return inner_func
	```


19. ### How many classes I need to price a swap, a bond, a future? 
	With polymorphism and inheritance, you can first create a parent class with fixed and floating legs methods, the child classes that inherit the methods to price different products. 

20. ### Write a map() function without increasing memory complexity.
	```
	def usr_map(fun, iterables): 
	    return [func(x) for x in iterables]
	```
	   
	
21. ### What's GIL and how it affects the code?
    GIL, global interpretor lock allows single thread exceution one at a time.

22. ### How GIL transform the code to machine language?
    Python virture machines translates the source code (.py) into byte code (.pyc), which is an intermediate for CPython (virtual machine) to interpret. The CPython sits within the GIL, intepreting the bytecode. 

23. ### Difference between methods and functions?
	methods' first argument is the obj instance e.g. self where function is defined as def/ lambda

24. ### What is an instance?

	e.g. x = some_class('x_instance'), x here is an instance object of the a class, which is different from the class "some_class" itself. Mainly when you call
	```
	some_class.some_method 
	```
	gives the function, while when you call
	```
	some_class().some_method 
	```
	gives the bound method 

25. ### Explain Exceptions catching

26. ### What is bound method?
	a method that depends on the instance as the first argument.

27. ### Garbage collecter and reference count in Python?

28. ## What does `(False, 0, [])` give?
	 a tuple of Falses is True.
29. List comprehension with if and else?
    `[f(x) if condition(x) else g(x) for x in sequence]`



