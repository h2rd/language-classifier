class SlowFunctor(object):
	def __init__(self,func):
		self.func = func
	def __add__(self,val):                  # сложение функтора с чем-то
		if isinstance(val,SlowFunctor): # если это функтор
			new_func = lambda *dt,**mp : self(*dt,**mp) + val(*dt,**mp)
		else:                           # если что-то другое
			new_func = lambda *dt,**mp : self(*dt,**mp) + val
		return SlowFunctor( new_func )
	def __call__(self,*dt):
		return self.func(*dt)

import math
def test1(x):
    return x + 1
def test2(x):
    return math.sin(x)

func = SlowFunctor(test1)                # создаем функтор
func = func + SlowFunctor(test2)         # этот функтор можно складывать с функторами
func = (lambda x : x + 2)(func)          # и числами, передавать в качестве параметра в функции
                                         # как будто это число

def func2(x):                            # Эквивалентная функция
    return test1(x) + test2(x) + 2

print func(math.pi)                      # печатает 3.14159265359
print func(math.pi) - func2(math.pi)     # печатает 0.0
