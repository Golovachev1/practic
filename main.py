import pygame, sys
from pygame.locals import *
from tkinter import *
import matplotlib.pyplot as plt
import random, time
from train import Train
from background import Background
from relsi import Relsi
from train_station import Train_station
from road import Road

DISPLAYSURF = pygame.display.set_mode((1000,700))
DISPLAYSURF.fill((181, 247, 91))
pygame.display.set_caption("Train")

train = Train()

back_ground = Background()

relsi = Relsi()

train_station = Train_station()

counter = 0
running = True

a = Road('№ 7015А', 'Barnaul', 'Rubcovsk', 5, [18.18, 18.49, 19.26, 19.52, 20.15, 20.34, 20.5, 21.0, 21.16, 21.3, 21.57, 22.57], [16.0, 17.37, 18.2, 18.52, 19.31, 19.54, 20.17, 20.36, 20.52, 21.02, 21.18, 21.32])
b = Road('№ 602*Н', 'Barnaul', 'Biysk', 5, [5.14, 5.37, 6.02, 6.25, 6.43, 6.59, 7.4, 8.4], [2.0, 3.58, 5.19, 5.40, 6.12, 6.27, 6.45, 7.01])
c = Road('№ 7013М', 'Barnaul', 'Kulunda', 5, [17.07, 17.47, 18.37, 19.01, 19.36, 21.07, 22.07], [14.0, 15.35, 17.09, 17.49, 18.39, 19.07, 19.41])
d = Road('№ 078*Ы', 'Barnaul', 'Karasuk', 5, [14.16, 16.0, 16.53, 17.47, 18.21, 18.43, 19.42, 20.42], [12.0, 13.58, 14.18, 16.02, 16.55, 17.48, 18.22, 18.44])
e = Road('№ 602Н', 'Barnaul', 'Tomsk', 5, [2.26, 3.08, 4.01, 4.3, 4.53, 5.4, 9.02, 9.46, 11.45, 12.45], [0.0, 1.01, 2.31, 3.35, 4.03, 4.32, 4.55, 6.35, 9.04, 9.48])

z1 = random.randint(0, 15)
z2 = random.randint(0, 15)
z3 = 0
z4 = random.randint(0, 15)
z5 = random.randint(0, 15)
ot1 = random.randint(0, 60)
ot2 = random.randint(0, 60)
ot3 = 0
ot4 = random.randint(0, 60)
ot5 = random.randint(0, 60)

def first():
    x = ['Барнаул', 'Калманка', 'Топчиха', 'Алейская', 'Язевка-Сибирская', 'Шипуново', 'Хлопуново', 'Поспелиха', 'За Урожай', 'Озимая', 'Мамонтово', 'Рубцовск']
    y = [a.time_prib[0], a.time_prib[1], a.time_prib[2], a.time_prib[3], a.time_prib[4], a.time_prib[5], a.time_prib[6], a.time_prib[7], a.time_prib[8], a.time_prib[9], a.time_prib[10], a.time_prib[11]]
    y1 = [a.time_otpr[0], a.time_otpr[1], a.time_otpr[2], a.time_otpr[3], a.time_otpr[4], a.time_otpr[5], a.time_otpr[6], a.time_otpr[7], a.time_otpr[8], a.time_otpr[9], a.time_otpr[10], a.time_otpr[11]]
    plt.plot(x, y, label='Прибытие')
    plt.plot(x, y1, label='Отправление')
    plt.figtext(0.02, 0.04, f"Средняя задержка на станциях составляет {z1} мин.", fontsize = 10)
    plt.figtext(0.02, 0.01, f"Общее время нарушения движения вследствие аварии составляет {ot1} мин.", fontsize = 10)
    plt.xlabel('Название станции')
    plt.ylabel('Время')
    plt.title(f'График движения поезда {a.number} {a.start}-{a.end}')
    plt.legend()
    plt.show()

def second():
    x = ['Барнаул', 'Овчинниково', 'Гордеево', 'Большая Речка', 'Загайново', 'Буланиха', 'Зональный', 'Бийск']
    y = [b.time_prib[0], b.time_prib[1], b.time_prib[2], b.time_prib[3], b.time_prib[4], b.time_prib[5], b.time_prib[6], b.time_prib[7]]
    y1 = [b.time_otpr[0], b.time_otpr[1], b.time_otpr[2], b.time_otpr[3], b.time_otpr[4], b.time_otpr[5], b.time_otpr[6], b.time_otpr[7]]
    plt.plot(x, y, label='Прибытие')
    plt.plot(x, y1, label='Отправление')
    plt.figtext(0.02, 0.04, f"Средняя задержка на станциях составляет {z2} мин.", fontsize = 10)
    plt.figtext(0.02, 0.01, f"Общее время нарушения движения вследствие аварии составляет {ot2} мин.", fontsize = 10)
    plt.xlabel('Название станции')
    plt.ylabel('Время')
    plt.title(f'График движения поезда {b.number}  {b.start}-{b.end}')
    plt.legend()
    plt.show()

def third():
    x = ['Барнаул', 'Ребриха', 'Корчино', 'Гилёвка', 'Леньки', 'Новоблаговещенка', 'Кулунда']
    y = [c.time_prib[0], c.time_prib[1], c.time_prib[2], c.time_prib[3], c.time_prib[4], c.time_prib[5], c.time_prib[6]]
    y1 = [c.time_otpr[0], c.time_otpr[1], c.time_otpr[2], c.time_otpr[3], c.time_otpr[4], c.time_otpr[5], c.time_otpr[6]]
    plt.plot(x, y, label='Прибытие')
    plt.plot(x, y1, label='Отправление')
    plt.figtext(0.02, 0.04, f"Средняя задержка на станциях составляет {z3} мин.", fontsize = 10)
    plt.figtext(0.02, 0.01, f"Общее время нарушения движения вследствие аварии составляет {ot3} мин.", fontsize = 10)
    plt.xlabel('Название станции')
    plt.ylabel('Время')
    plt.title(f'График движения поезда {c.number}  {c.start}-{c.end}')
    plt.legend()
    plt.show()

def fourth():
    x = ['Барнаул', 'Алтайская', 'Сузун', 'Камень-На-Оби', 'Панкрушиха', 'Хабары', 'Краснозерское', 'Карасук']
    y = [d.time_prib[0], d.time_prib[1], d.time_prib[2], d.time_prib[3], d.time_prib[4], d.time_prib[5], d.time_prib[6], d.time_prib[7]]
    y1 = [d.time_otpr[0], d.time_otpr[1], d.time_otpr[2], d.time_otpr[3], d.time_otpr[4], d.time_otpr[5], d.time_otpr[6], d.time_otpr[7]]
    plt.plot(x, y, label='Прибытие')
    plt.plot(x, y1, label='Отправление')
    plt.figtext(0.02, 0.04, f"Средняя задержка на станциях составляет {z4} мин.", fontsize = 10)
    plt.figtext(0.02, 0.01, f"Общее время нарушения движения вследствие аварии составляет {ot4} мин.", fontsize = 10)
    plt.xlabel('Название станции')
    plt.ylabel('Время')
    plt.title(f'График движения поезда {d.number}  {d.start}-{d.end}')
    plt.legend()
    plt.show()

def fifth():
    x = ['Барнаул', 'Усть-Тальменская', 'Черепаново', 'Линево', 'Искитим', 'Бердск', 'Новосибирск-Главный', 'Юрга', 'Юшкино', 'Томск']
    y = [e.time_prib[0], e.time_prib[1], e.time_prib[2], e.time_prib[3], e.time_prib[4], e.time_prib[5], e.time_prib[6], e.time_prib[7], e.time_prib[8], e.time_prib[9]]
    y1 = [e.time_otpr[0], e.time_otpr[1], e.time_otpr[2], e.time_otpr[3], e.time_otpr[4], e.time_otpr[5], e.time_otpr[6], e.time_otpr[7], e.time_otpr[8], e.time_otpr[9]]
    plt.plot(x, y, label='Прибытие')
    plt.plot(x, y1, label='Отправление')
    plt.figtext(0.02, 0.04, f"Средняя задержка на станциях составляет {z5} мин.", fontsize = 10)
    plt.figtext(0.02, 0.01, f"Общее время нарушения движения вследствие аварии составляет {ot5} мин.", fontsize = 10)
    plt.xlabel('Название станции')
    plt.ylabel('Время')
    plt.title(f'График движения поезда {e.number} {e.start}-{e.end}')
    plt.legend()
    plt.show()

def counter_label():
	def count():
		if running:
			global counter
			#label.after(1000, count)
			counter += 1
	count()

while True:
    counter_label() 
    for event in pygame.event.get():
        #print(counter)  
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    back_ground.update()
    back_ground.render()

    relsi.update()
    relsi.render()

    train_station.update()
    train_station.render()

    train.update()
    train.render()
    if counter < 170:
            back_ground.movingUpSpeed = 0
            relsi.movingUpSpeed = 0
            train_station.movingUpSpeed = 0
    elif counter > 570 and counter < 770:
            back_ground.movingUpSpeed = 0
            relsi.movingUpSpeed = 0
            train_station.movingUpSpeed = 0
    elif counter > 1090 and counter < 1280:
            back_ground.movingUpSpeed = 0
            relsi.movingUpSpeed = 0
            train_station.movingUpSpeed = 0
    elif counter > 1560 and counter < 1770:
            back_ground.movingUpSpeed = 0
            relsi.movingUpSpeed = 0
            train_station.movingUpSpeed = 0
    elif counter > 2050 and counter < 2270:
            back_ground.movingUpSpeed = 0
            relsi.movingUpSpeed = 0
            train_station.movingUpSpeed = 0
    elif counter > 2550 and counter < 2770:
            back_ground.movingUpSpeed = 0
            relsi.movingUpSpeed = 0
            train_station.movingUpSpeed = 0
    elif counter > 3050:
            back_ground.movingUpSpeed = 0
            relsi.movingUpSpeed = 0
            train_station.movingUpSpeed = 0
            window = Tk()
            window.geometry("500x500")
            plot_button = Button(master = window, 
                     command = first,
                     height = 2, 
                     width = 10,
                     text = f"{a.number}")

            plot_button2 = Button(master = window, 
                     command = second,
                     height = 2, 
                     width = 10,
                     text = f"{b.number}")

            plot_button3 = Button(master = window, 
                     command = third,
                     height = 2, 
                     width = 10,
                     text = f"{c.number}")

            plot_button4 = Button(master = window, 
                     command = fourth,
                     height = 2, 
                     width = 10,
                     text = f"{d.number}")

            plot_button5 = Button(master = window, 
                     command = fifth,
                     height = 2, 
                     width = 10,
                     text = f"{e.number}")

            plot_button.pack()
            plot_button2.pack()
            plot_button3.pack()
            plot_button4.pack()
            plot_button5.pack()
            window.title('Show statistic')
            window.mainloop()
            break
    else:
            back_ground.movingUpSpeed = 5
            relsi.movingUpSpeed = 5
            train_station.movingUpSpeed = 5

    pygame.display.update()
