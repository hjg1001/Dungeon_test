import random,Img,pygame,Text
class Bed:
	def __init__(self,owner):
		self.type='bed'
		self.owner=owner
		self.sleeper=None
class Door:
	def __init__(self):
		self.type='door'
		self.lock=False
		self.open=False
area_list=[]#区域格式[所有者,[区块,区块,区块,区块……]]
area_list_public=[]
class Area:
	def __init__(self,ype,id,x,y,p):#区块(构成区域)
		self.type=ype#区域类型
		self.owner=None#所有者
		self.x,self.y=x,y
		self.public=p#是否公开
		self.id=id#区域在列表中的序列号
class Shelve:
	def __init__(self):
		self.type='Shelve'
		self.goods=[]#容量10
class Food:
	def __init__(self):
		self.type='food'
class Machine:
	def __init__(self):
		self.type='machine'
		self.locking=False
		self.product=[]#产品[产品,当前进度,总进度]
	def work(self):
		if self.product:
			self.product[1]+=0.8
			if self.product[1]>=self.product[2]:
				P=self.product[0]
				self.product=[]
				return P
			return None
		else:
			P=random.choice(Text.items)
			self.product=[P,0,P[1]*5]
			return None
class Box(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.x,self.y=x,y
		self.locking=False#被锁定
		self.item_list=[]
		self.type='box'
	def update(self,screen,map):
		screen.blit(Img.images['box'],(self.x+map.vx,self.y+map.vy))