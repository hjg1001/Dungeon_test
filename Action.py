#Action
import random,pygame,Img,Object
def move(self,target_x, target_y,map):#目标坐标为格点
	 if map.data2[target_y][target_x]!=None:
	 	self.data.road=map.astar.run((int(self.data.x//32),int(self.data.y//32)),(target_x,target_y))
	 if self.data.road:
	  self.data.target_x,self.data.target_y=self.data.road[0][0]*32,self.data.road[0][1]*32
	  self.data.state='move'
def random_move(self,map):
	x,y=random.randint(-5,5),random.randint(-5,5)
	if self.data.y//32+y<=len(map.data) and self.data.y//32+y>=0 and self.data.x//32+x<=len(map.data[self.data.y//32]) and self.data.x//32+x>=0:
		if map.area[self.data.y//32+y][self.data.x//32+x].public and map.data2[self.data.y//32+y][self.data.x//32+x]!=None:
			move(self,self.data.x//32+x,self.data.y//32+y,map)
def area_random_move(self,map,list,id):
	obj=random.choice(list[id][1])
	move(self,obj.x,obj.y,map)
def go_sleep(self,map):
	if self.data.house!=None:
				x,y=search(self,map,Object.area_list,self.data.house,5,False)
				move(self,x,y,map)
				self.data.action='sleep'
def search(self,map,list,id,content,S):#返回坐标 S-是否检查是否锁定
	for i in list[id][1]:
			if type(map.data[i.y][i.x])==int and map.data[i.y][i.x]==content:
				return i.x,i.y
			elif type(map.data[i.y][i.x])!=int and map.data[i.y][i.x].type==content:
				if S and not map.data[i.y][i.x].locking:
					return i.x,i.y,i
def go_check_order(self,map):
	self.data.action='check_order'
	x,y,obj=search(self,map,Object.area_list_public,self.data.factory,'OrderBoard',False)
	move(self,x,y+1,map)
	self.data.order=map.data[y][x]