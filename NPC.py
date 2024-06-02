#Npc
import pygame,Img,Action,State,random,Object,Job,Setting
class NPC_data:#npc数据(方便存档)
	def __init__(self,x,y,job,img):
		self.x,self.y=x,y
		self.target_x,self.target_y=None,None
		self.state=None
		self.action=None
		self.frame=0
		self.speed=random.uniform(2.5,3.5)
		self.energy=100
		self.x_data=[]
		self.y_data=[]
		self.road=[]
		self.job=job
		self.money=10
		self.house=None#房间
		self.image=img
		self.action_time=0#当前行为持续时间
		self.old_action=None
		self.hold=None#手持
		#工坊主
		self.factory=None
		self.warehouse=None
		#工人
		self.machine=None
		for id,i in enumerate(Object.area_list):#分配房间
			if not i[0]:
				if i[1][0].type=='house' and self.house==None and id not in [0,1]:
					Object.area_list[id][0]=self
					self.house=id
					break
class NPC(pygame.sprite.Sprite):#npc精灵
	def __init__(self,x,y,job,img):
		pygame.sprite.Sprite.__init__(self)
		self.data=NPC_data(x,y,job,img)
	def update(self,screen,map,ax):
		#渲染
		if map.x:
			self.data.x_data.append(pygame.time.get_ticks() //Setting.st[1] )
			self.data.y_data.append(eval(Setting.st[2]))
		if self.data.road and len(self.data.road)>1:
			i=[]
			for a in self.data.road:
				i.append([a[0]*32+map.vx,a[1]*32+map.vy])
			pygame.draw.lines(screen,(0,8,190),False,i)
		pygame.draw.line(screen,(0,0,0),(self.data.x+map.vx,self.data.y+map.vy),(map.vx+Object.area_list[self.data.house][1][0].x*32,map.vy+Object.area_list[self.data.house][1][0].y*32),width=2)
		pygame.draw.rect(screen,(255,255,25),(map.vx+Object.area_list[self.data.house][1][0].x*32,map.vy+Object.area_list[self.data.house][1][0].y*32,5,5))
		screen.blit(self.data.image,(self.data.x+map.vx,self.data.y+map.vy))
		if not map.pause:
			#行为
			if self.data.job=='factoryowner':Job.factory_owner_action(self,map)
			if self.data.job=='worker':Job.worker_action(self,map)
			#行为状态更新
			self.data.old_action=self.data.action
			if not self.data.action and not self.data.state and random.randint(1,1000)>990:Action.random_move(self,map)
			if self.data.action!=self.data.old_action:self.data.action_time=0
			else:self.data.action_time+=1
			#状态
			State.Run_state(self,map)
			if self.data.state=='move':
				if self.data.x==self.data.target_x and self.data.y==self.data.target_y:
					self.data.road.remove([self.data.target_x//32,self.data.target_y//32])
					if self.data.road:self.data.target_x,self.data.target_y=self.data.road[0][0]*32,self.data.road[0][1]*32
				if self.data.road:self.data.x,self.data.y=State.move_state(self,self.data.x,self.data.y,self.data.target_x,self.data.target_y,self.data.speed)
				else:
					self.data.state=None