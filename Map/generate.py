from PIL import Image
import pygame,Img,random,Setting,Object
from os import path
def generate(screen,font):
	#地块标准32*32
	#二维数组[y[x],y[x]]
	m=Image.open(path.dirname(path.abspath(__file__))+'/map.png')
	m2=Image.open(path.dirname(path.abspath(__file__))+'/map2.png')
	data=[]
	data2=[]
	data3=[]
	map=pygame.Surface((32*m.size[0],32*m.size[1]))
	Setting.map_size=(m.size[0]*32,m.size[1]*32)
	for y in range(m.size[1]):
		data.append([])#地块地图
		data2.append([])#碰撞箱地图
		data3.append([])#区域地图
		#透明度为通畅度 0~100不通畅 100~255通畅
		for x in range(m.size[0]):
			key=m.getpixel((x,y))
			key2=m2.getpixel((x,y))
			#id为相对于整个列表的id
			#私人区域生成(255,type,id,255)
			if key2[0]==255:#私人区域(住宅等)
				if key2[1]==0:#住宅
					type='house'
				while True:
					if len(Object.area_list)<key2[2]+1:
						Object.area_list.append([None,[]])
					else:break
				a=Object.Area(type,key2[2],x,y,False)
				Object.area_list[key2[2]][1].append(a)
				data3[y].append(a)
			else:#公享区域生成(0,type,id,255)
				if key2[1]==0:type='factory'#工坊
				elif key2[1]==1:type='warehouse'#工坊仓库
				elif key2[1]==2:type='bar'#酒吧
				elif key2[1]==3:type='kitchen'#厨房
				elif key2[1]==4:type='store'#商店
				elif key2[1]==5:type='exit'#出口
				else:type=None#空地
				if type:
					while True:
						if len(Object.area_list_public)<key2[2]+1:
							Object.area_list_public.append([None,[]])
						else:break
					a=Object.Area(type,key2[2],x,y,True)
					Object.area_list_public[key2[2]][1].append(a)
					data3[y].append(a)
				else:data3[y].append(Object.Area(None,None,x,y,True))#空地
			#地块与碰撞箱生成
			if key[:3]==(26,0,0):
				data[y].append(Object.Shelve())#7 货架(26,0,0)
				data2[y].append(None)
			elif key==(255,0,25,255):
				data[y].append(Object.Door())#4 门 (255,0,25,0)
				data2[y].append(0)
			elif key==(0,5,0,255):#5 床 (0,5,0,255)
				data[y].append(5)
				data2[y].append(0)
			elif key==(0,255,0,255):# 2 墙 (0,255,0,255)
				data[y].append(2)
				data2[y].append(None)
			elif key==(27,0,0,255):# 6 椅子 (27,0,0)
				data[y].append(6)
				data2[y].append(0)
			elif key==(28,0,0,255):# 8 桌子 (28,0,0)
				data[y].append(8)
				data2[y].append(None)
			elif key==(29,0,0,255):# 9 告示牌 (29,0,0)
				data[y].append(9)
				data2[y].append(None)
			elif key==(30,0,0,255):# 10 工厂机器 (30,0,0)
				data[y].append(Object.Machine())
				data2[y].append(None)
			else:
				data[y].append(0)#0 地板 (255,255,255,255)或(留空)
				data2[y].append(0)
		screen.fill((0,0,0))
		text=str(x*y)+'/'+str(m.size[0]*m.size[1])
		screen.blit(font.render('Loading:',False,(255,250,255)),(screen.get_width()//2-80,screen.get_height()//2))
		screen.blit(font.render(text,False,(210,200,190)),(screen.get_width()//2-len(text)*10,screen.get_height()//2+50))
		pygame.display.update()
	map=pygame.image.load('map/map0.png').convert()
	pygame.image.save(map,'b.png')
	return data,map,data2,data3