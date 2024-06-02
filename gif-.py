import pygame
import os
#素材处理
images = {}
pygame.init()
pygame.display.set_caption('g')
screen=pygame.display.set_mode((18,18))
for num,file_name in enumerate(os.listdir(os.path.abspath('Img_'))):
    if file_name.endswith('.png'):
        name = os.path.splitext(file_name)[0]
        image=pygame.image.load(os.path.abspath('Img_')+'/'+file_name).convert_alpha()
        images[name] = image
num+=1
width,height=32,32#个体图片宽长
new=pygame.Surface((width*num,height)).convert_alpha()
new.fill((255,0,0))
x=0
for i in images:
	new.blit(images[i],(x,0))
	x+=width
new=pygame.transform.scale(new,(int(num*32),32))
pygame.image.save(new,'new.png')