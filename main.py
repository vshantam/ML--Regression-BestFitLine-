from lib import *
from applic import regression

def main():

	xs=[random.randint(1,100) for _ in range (1,111)]

	xs=np.array(xs,dtype=np.float64)
	
	
	ys=[random.randint(1,100) for _ in range (1,111)]

	ys=np.array(ys,dtype=np.float64)


	obj=regression(xs,ys)
	slope=obj.slope(xs,ys)

	constant=obj.cons(xs,ys)
	regressionLine=obj.regressionLine(xs,ys)
	style.use('ggplot')

	plt.scatter(xs,ys)
	
	plt.plot(xs,regressionLine,'b',label="Regression Fit LIne")

	plt.xlabel("X--> Axis")
	
	plt.ylabel("Y--> Axis")

	plt.title("Regression Fit")
	
	plt.legend(loc=1)

	plt.show()

	

if __name__=='__main__':
	try:
		main()

	except Exception as e:
	
		print("Error Occured:{}".format(str(e)))

	

