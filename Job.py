import Action,Object,random
def factory_owner_action(self,map):#工坊主
	#非周五 5:00-13:00 工作
	if not map.week==5 and 13>=map.hour>=5:#工作期间
		pass
	if (self.data.energy<=40 or map.hour>=23) and not self.data.action:
		Action.go_sleep(self,map)
def worker_action(self,map):#工人
	#非周五 5:00-20:00工作
	if not map.week==5 and 20>=map.hour>=5 and not self.data.action:
		x,y,self.data.machine=Action.search(self,map,Object.area_list_public,self.data.factory,'machine',True)
		if not map.data[self.data.machine.y][self.data.machine.x].locking:
			Action.move(self,x,y-1,map)
			map.data[self.data.machine.y][self.data.machine.x].locking=True
			self.data.action='work'
	elif (map.week==5 or not(20>=map.hour>=5)) and self.data.action=='work':
		self.data.action,self.data.state=None,None
		map.data[self.data.machine.y][self.data.machine.x].locking=False
	if (self.data.energy<=40 or map.hour>=23) and not self.data.action:
		Action.go_sleep(self,map)