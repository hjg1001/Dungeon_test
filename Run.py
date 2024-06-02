def main():
	ax=None
	if Setting.st[0]:fig, ax = plt.subplots()
	map.X=False
	running=True
	surf=None
	week=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
	while running:
		#操作
		if map.x:map.x=False
		for event in pygame.event.get():
			map.control(event)
			if event.type==pygame.QUIT:
				running=False
				if Setting.st[0]and surf:pygame.image.save(surf,'a.png')
		map.key_act()
		if not map.pause:
			map.hour=map.time//24//60
			if map.time//60//24<=24:map.time+=6
			else:
				map.date+=1
				map.time=0
				if map.week<7:
					map.week+=1
				else:
					map.week=1
			if Setting.st[0] and pygame.time.get_ticks()%Setting.st[1]==0 :
				map.x=True
				ax.clear()
			if map.date==30:
				map.date=0
				map.month+=1
		screen.fill((0,0,0))
		screen.blit(map.surface,(map.vx,map.vy))
		#更新NPC
		map.npcs.update(screen,map,ax)
		#更新物品
		map.items.update(screen,map)
		#文字
		clock.tick(Setting.fps)
		fps=int(clock.get_fps())
		for i in map.npcs.sprites():
			Text_render.render_text_with_icons(screen,f'行为:{i.data.action}%N状态:{i.data.state}%N%M%(255,255,0)金钱:{i.data.money}%N%E%(69,226,232)能量:{int(i.data.energy)}',i.data.x-20+map.vx,i.data.y-80+map.vy,font2)
		Text_render.render_text_with_icons(screen,f'FPS:{fps}%N{week[map.week-1]} {map.time//24//60}:00%N{map.month*30+map.date}天',0,0,font)
	#统计图
		# 将Matplotlib图形渲染到Pygame窗口
		if map.pause and not map.X and Setting.st[0]:
			ax.clear()
			for self in map.npcs:
				ax.plot(self.data.x_data,self.data.y_data,label=str(self.data.house))
			ax.legend()
			canvas = FigureCanvas(fig)
			canvas.draw()
			renderer = canvas.get_renderer()
			raw_data = renderer.tostring_rgb()
			size = canvas.get_width_height()
			surf = pygame.image.fromstring(raw_data, size, "RGB").convert()
			surf.set_alpha(180)
			screen.blit(surf, (0, 0))
			map.X=True
		elif not map.pause and Setting.st[0]:
			map.X=False
		elif Setting.st[0]:
			screen.blit(surf,(0,0))
		#刷新屏幕
		pygame.display.flip()

if __name__ == "__main__":
	import pygame,Setting,Text_render
	if Setting.st[0]:
		import matplotlib.pyplot as plt
		from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	pygame.init()
	font=pygame.font.Font('NotoSerifCJK-Regular.ttc',30)
	font3=pygame.font.Font('NotoSerifCJK-Regular.ttc',8)
	font2=pygame.font.Font('NotoSerifCJK-Regular.ttc',15)
	screen=pygame.display.set_mode(Setting.screen_size)
	clock=pygame.time.Clock()
	import Map,NPC,Img,Object
	map=Map.Map(screen,font)
	map.time=6900
	#地牢部署
	map.items.add(Object.Box(11*32,20*32))
	N1=NPC.NPC(150,100,'factoryowner',Img.images['factoryowner'])
	N1.data.house=16
	N1.data.factory=0
	N1.data.warehouse=1
	map.npcs.add(N1)
	for _ in range(5):
		N2=NPC.NPC(150,90,'worker',Img.images['civilian'])
		N2.data.factory=0
		map.npcs.add(N2)
	main()