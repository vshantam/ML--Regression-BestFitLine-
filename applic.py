from statistics import mean

class regression:
	
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def slope(self,x,y):
		global m
		m=((mean(x)*mean(y))-mean(x*y))/((mean(x)**2)-(mean(y)**2))

		return m

	def cons(self,x,y):
		
		global c
		c=(mean(y)-(m*mean(x)))
		return c

	def regressionLine(self,xs,ys):
		ys=[(m*x)+c for x in xs]
		return ys
		
