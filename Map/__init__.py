#Map
from .generate import  *
import pygame,Setting,astar
class Map:
	def __init__(self,screen,font):
		g=generate(screen,font)
		self.data=g[0]
		self.data2=g[2]
		self.surface=g[1]
		self.vx,self.vy,self.m_u,self.m_d,self.m_l,self.m_r=0,0,False,False,False,False
		self.npcs=pygame.sprite.Group()
		self.items=pygame.sprite.Group()
		self.pause=False
		self.astar=astar.Astar(g[2])
		self.area=g[3]
		self.time=0#时间 刻(//60//24=1小时)
		self.date=1#日期(1-30) 天
		self.week=1#星期
		self.hour=self.time//24//60
		self.x=False
		self.month=0#月数 不循环
	def control(self,event):
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_UP:
				self.m_u=True
			if event.key==pygame.K_DOWN:
				self.m_d=True
			if event.key==pygame.K_LEFT:
				self.m_l=True
			if event.key==pygame.K_RIGHT:
				self.m_r=True
			if event.key==pygame.K_c and not self.pause:
				self.pause=True
			elif self.pause and event.key==pygame.K_c:
				self.pause=False
		#松开按键
		if event.type == pygame.KEYUP:
			if event.key==pygame.K_UP:
				self.m_u=False
			if event.key==pygame.K_DOWN:
				self.m_d=False
			if event.key==pygame.K_LEFT:
				self.m_l=False
			if event.key==pygame.K_RIGHT:
				self.m_r=False
	def key_act(self):
		if self.m_u and self.vy<30:
			self.vy+=10
		if self.m_d and -self.vy+Setting.screen_size[1]<Setting.map_size[1]+30:
			self.vy-=10
		if self.m_l and self.vx<30:
			self.vx+=10
		if self.m_r and -self.vx+Setting.screen_size[0]<Setting.map_size[0]+30:
			self.vx-=10