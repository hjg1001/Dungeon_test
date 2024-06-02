import pygame
import re,Img

# 初始化pygame
pygame.init()
# 定义普通字体和加粗字体

# 图标文件映射
icons = {
    '%M':Img.images['money'],
    '%E':Img.images['energy']
}


def render_text_with_icons(screen,text,x,y,normal_font):
    render_queue = []
    last_pos = 0
    current_color = (255, 255, 255)
    current_font = normal_font
    
    pattern = r'(%[ME])|(%N)|(%\(\d+,\d+,\d+\))'
    for match in re.finditer(pattern, text):
        start = match.start()
        if start > last_pos:
            render_queue.append(('text', text[last_pos:start], current_color, current_font))
        token = match.group()
        if token in icons:
            render_queue.append(('icon', icons[token]))
        elif token == '%C':
            current_font = normal_font
        elif token.startswith('%('):
            current_color=eval(token[1:])
        elif token == '%N':
            render_queue.append(('newline',50))
        last_pos = match.end()

    if last_pos < len(text):
        render_queue.append(('text', text[last_pos:], current_color, current_font))

    for kind, content, *params in render_queue:
        if kind == 'text':
            rendered_text = params[1].render(content, True, params[0])
            screen.blit(rendered_text, (x, y))
        elif kind == 'icon':
            screen.blit(content, (x-content.get_width(), y+5))
        elif kind == 'newline':
            y += normal_font.get_height()