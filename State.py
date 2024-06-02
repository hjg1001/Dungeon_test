#State
import math,Object,random,Text
def move_state(self,x, y, target_x, target_y, speed):
    dx = target_x - x
    dy = target_y - y
    distance = math.sqrt(dx**2 + dy**2)
    if distance <= speed:
        new_x = target_x
        new_y = target_y
    else:
        ratio = speed / distance
        new_x = x + dx * ratio
        new_y = y + dy * ratio
    return new_x, new_y
def Run_state(self,map):#状态变化
	if self.data.road==None:self.data.road=[]
	if self.data.energy>30 and self.data.state!='sleep':self.data.energy-=0.005
	sleep(self)
	work(self,map)
def work(self,map):
	if self.data.action=='work'and not self.data.state:
		R=map.data[self.data.machine.y][self.data.machine.x].work()
		self.data.energy-=0.03
		if R:#产品以完成，返回产品
			for i in list(map.items):
				if i.type=='box':
					i.item_list.append(R)
def sleep(self):
	if self.data.action=='sleep' and not self.data.state:
		self.data.state='sleep'
	if self.data.state=='sleep':
		self.data.energy+=0.02
		if self.data.energy>=90:
			self.data.action,self.data.state=None,None