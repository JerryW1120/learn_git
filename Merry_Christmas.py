import turtle as t
from turtle import *
import random
import time
import pygame


n = 100.0

speed("fastest")  # 定义速度
screensize(bg='black')  # 定义背景颜色，可以自己换颜色
left(90)
forward(3*n)
color("orange", "yellow")  # 定义最上端星星的颜色，外圈是orange，内部是yellow
begin_fill()
left(126)

for i in range(5):  # 画五角星
    forward(n/5)
    right(144)  # 五角星的角度
    forward(n/5)
    left(72)  # 继续换角度
end_fill()
right(126)


def drawlight():  # 定义画彩灯的方法
    if random.randint(0, 30) == 0:  # 如果觉得彩灯太多，可以把取值范围加大一些，对应的灯就会少一些
        color('tomato')  # 定义第一种颜色
        circle(6)  # 定义彩灯大小
    elif random.randint(0, 30) == 1:
        color('orange')  # 定义第二种颜色
        circle(3)  # 定义彩灯大小
    else:
        color('dark green')  # 其余的随机数情况下画空的树枝


color("dark green")  # 定义树枝的颜色
backward(n*4.8)


def tree(d, s):  # 开始画树
    if d <= 0:
        return
    forward(s)
    tree(d-1, s*.8)
    right(120)
    tree(d-3, s*.5)
    drawlight()  # 同时调用小彩灯的方法
    right(120)
    tree(d-3, s*.5)
    right(120)
    backward(s)


tree(15, n)
backward(n/2)

for i in range(200):  # 循环画最底端的小装饰
    a = 200 - 400 * random.random()
    b = 10 - 20 * random.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if random.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)

t.color("dark red", "red")  # 定义字体颜色
t.write("Merry Christmas", align="center", font=(
    "Comic Sans MS", 40, "bold"))  # 定义文字、位置、字体、大小


def drawsnow():  # 定义画雪花的方法
    t.ht()  # 隐藏笔头，ht=hideturtle
    t.pensize(2)  # 定义笔头大小
    for i in range(200):  # 画多少雪花
        t.pencolor("white")  # 定义画笔颜色为白色，其实就是雪花为白色
        t.pu()  # 提笔，pu=penup
        t.setx(random.randint(-350, 350))  # 定义x坐标，随机从-350到350之间选择
        t.sety(random.randint(-100, 350))  # 定义y坐标，注意雪花一般在地上不会落下，所以不会从太小的纵座轴开始
        t.pd()  # 落笔，pd=pendown
        dens = 6  # 雪花瓣数设为6
        snowsize = random.randint(1, 10)  # 定义雪花大小
        for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            # t.forward(int(snowsize))  #int（）取整数
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
            t.right(int(360/dens))  # 转动角度


# 初始化 pygame
pygame.init()
# 设置屏幕宽高，根据背景图调整
bg_img = "bg.png"
bg_size = (609, 601)
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("雪夜圣诞树")
bg = pygame.image.load(bg_img)
# 雪花列表
snow_list = []
for i in range(150):
    x_site = random.randrange(0, bg_size[0])   # 雪花圆心位置
    y_site = random.randrange(0, bg_size[1])   # 雪花圆心位置
    X_shift = random.randint(-1, 1)         # x 轴偏移量
    radius = random.randint(4, 6)           # 半径和 y 周下降量
    snow_list.append([x_site, y_site, X_shift, radius])
# 创建时钟对象
clock = pygame.time.Clock()
# 添加音乐
track = pygame.mixer.music.load('my.mp3')  # 加载音乐文件
pygame.mixer.music.play()  # 播放音乐流
pygame.mixer.music.fadeout(600000)  # 设置音乐结束时间
done = False
while not done:
    # 消息事件循环，判断退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(bg, (0, 0))
    # 雪花列表循环
    for i in range(len(snow_list)):
        # 绘制雪花，颜色、位置、大小
        pygame.draw.circle(screen, (255, 255, 255),
                           snow_list[i][:2], snow_list[i][3] - 3)
        # 移动雪花位置（下一次循环起效）
        snow_list[i][0] += snow_list[i][2]
        snow_list[i][1] += snow_list[i][3]
        # 如果雪花落出屏幕，重设位置
        if snow_list[i][1] > bg_size[1]:
            snow_list[i][1] = random.randrange(-50, -10)
            snow_list[i][0] = random.randrange(0, bg_size[0])
    # 刷新屏幕
    pygame.display.flip()
    clock.tick(30)
# 退出
pygame.quit()

# drawsnow()#调用画雪花的方法
t.done()  # 完成,否则会直接关闭
