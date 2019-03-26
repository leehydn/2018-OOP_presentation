import math

def prob1(y0, t0, gap, num):
	def dydt(y, t):
		return (y-1) * (y-1) * (y-4) * (y-4) * (y-6) * (y-7)
		
	y = y0; t = t0;
	
	for i in range(num):
		y += dydt(y, t) * gap;
		t += gap;
		print("#{} t_{} = {}, y({}) = {}".format(i+1, i+1, t, gap*(i+1), round(y, 3)))
		
	
#prob1(0.8, 0, 0.001, 10000)

def prob4(x0, y0, t0, time_gap, num):
    def dxdt(x, y, t):
        return 25 - x ** 2 - y ** 2

    def dydt(x, y, t):
        return 9 * y ** 2 - 16 * x ** 2
     
    x = x0; y = y0; t = t0;
    
    for i in range(num):
        x += dxdt(x, y, t) * time_gap
        y += dydt(x, y, t) * time_gap
        t += time_gap
        
        print("#{} t={}, x({}) = {}, y({}) = {}".format(i+1, time_gap * (i+1), time_gap * (i+1), x, time_gap * (i+1), y))
        

prob4(7, 0, 0, 0.001, 100000)