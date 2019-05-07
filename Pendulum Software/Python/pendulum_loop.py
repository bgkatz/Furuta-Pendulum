from pendulum import*
import time

ts = .005
p = pendulum('COM19', ts)

while(1):
	p.getData()
	time.sleep(ts)
	print(p.q1)