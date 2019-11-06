from pendulum import*
import time

ts = .0025
p = pendulum('COM26', ts)
p.enable()
while(1):
	start = time.time()
	p.getData()
	time.sleep(ts)
	dt = time.time()-start
	#print(dt, p.q1_control)
	#print(p.qd0, p.q1_control)