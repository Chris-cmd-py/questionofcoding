import time
import pygame
import random
#初始化
pygame.init()
#设置标题
pygame.display.set_caption('贪吃蛇')
font_style =pygame.font.Font('C:/Windows/Fonts/STFANGSO.TTF',30)
score_font =pygame.font.Font('C:/Windows/Fonts/STFANGSO.TTF',35)

white = (255,255,255)
yellow = (255,255,102)
green = (0,255,0)
blue = (50,153,213)
red = (213,50,80)
black = (0,0,0)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))

clock = pygame.time.Clock()

snake_block = 10#为何不能任意改变大小？
snake_speed = 8

def our_snake(snake_block,snake_lisk):
    for x in snake_lisk:#利用循环结构，达到绘制整条蛇长度的目的
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])
        '''pygame.draw.rect(Surface,color,Rect,width)的第一个参数是背景图案；
        第二个参数是在背景的基础上绘制图案时需要填充的颜色；
        第三个参数的形式是（（x,y）,(width,height)）表示的是所绘制矩形的区域，其中第一个元组(x, y)表示的是该矩形左上角的坐标,
        第二个元组 (width, height)表示的是矩形的宽度和高度;
        第四个参数width表示线条的粗细，单位为像素；默认值为0，表示填充矩形内部。
        '''
game_over = False

#显示文字信息
def message(msg,color):
    dis.fill('white')
    mesg = font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width / 3,dis_height /3]) 
    pygame.display.update()
    time.sleep(1)

def gameLoop():
    game_over = False
    game_close = False
    
    x1 = dis_width / 2
    y1 = dis_height /2

    x1_change = 0
    y1_change = 0  

    snake_List = []
    length_of_snake = 1

    foodx = round(random.randrange(0,dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(0,dis_height - snake_block) / 10) * 10

    while not game_over:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                game_over = True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_q:
                    game_over = True
                elif event.key == pygame.K_c:
                    message('你失败了，重新开始！','green')
                    gameLoop()
        #设置以窗口为边界，蛇走出窗口即游戏结束。
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis,'yellow',[foodx,foody,snake_block,snake_block])

        snake_Head = [x1,y1]
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]#这句话代表什么意义？
        
        our_snake(snake_block,snake_List)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0,dis_height - snake_block) / 10) * 10
            length_of_snake += 1
        
        clock.tick(snake_speed)

    message('你失败了，结束游戏！',red)
    
    pygame.quit()
    quit()

gameLoop()