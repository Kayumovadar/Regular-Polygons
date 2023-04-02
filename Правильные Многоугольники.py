import random
import turtle


#настраиваем перо
t = turtle.Pen()#создаем перо
t.shape("turtle")# стрелка меняется на черепаху
t.up()#поднимаем ручку, чтобы черепаха не оставляла след
t.goto(0, -200)# задаем координаты
t.down()#опускаем ручку
t.pensize(3)#создаем ширину пера

#настраиваем окно
window = turtle.Screen()#создаем окно
window.screensize(400, 400, "lightblue")# размер и цвет окна
window.title("Изучаем многоугольники")# название окна

#реализуем список цветов
colour = ["steelblue3", "steelblue4", "skyblue4", "ivory4", "light pink", "medium purple", "dark salmon"]

def draw(side):
    t.begin_fill()#начинаем заливку
    for i in range(side):
        t.forward(200)# идем прямо на 200 пикселей
        t.left(180 - ((side - 2) * 180/side))# делаем поворот в зависимости от кол-во сторон
    t.end_fill()#заканчиваем заливку

window_in = turtle.textinput("Многоугольники", "Введите количество углов")# окно ввода углов

#выбираем рандомно цвет многоугольника
t.fillcolor(random.choice(colour))# присваиваем перу цвет
draw(int(window_in))#вызыываем draw, передаем углы
turtle.mainloop()#запаковываем
