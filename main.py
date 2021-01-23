#импорт библиотек (КОММЕНТАРИЙ)
from tkinter import *
from tkinter import messagebox

#настройка окон с вопросами и ответами (КОММЕНТАРИЙ)
level1 = Tk()
level2 = Tk()
level3 = Tk()
level4 = Tk()

k1 = False
k2 = False
k3 = False
k4 = False

level1.title("Викторина")
level1.geometry("900x900")



def level_error_button(): #неправильный ответ (КОММЕНТАРИЙ)
    messagebox.showerror('Неправильно','Ответ неверен! Попробуй ещё раз!')

def level_click_button(): #правильный ответ на первый вопрос (КОММЕНТАРИЙ)
    messagebox.showinfo("Правильно!", "Вы ответили верно!")
    level2.title("Викторина")
    level2.geometry("900x900")
    level_2()
    level1.quit()

def level_click_button2(): #правильный ответ на второй вопрос (КОММЕНТАРИЙ)
    messagebox.showinfo("Правильно!", "Вы ответили верно!")
    level3.title('Викторина')
    level3.geometry('900x900')
    level_3()
    level2.quit()

def level_click_button3(): #правильный ответ на третий вопрос (КОММЕНТАРИЙ)
    messagebox.showinfo("Правильно!", "Вы ответили верно!")
    level4.title('Викторина')
    level4.geometry('900x900')
    level_4()
    level3.quit()

def level_click_button4(): #правильный ответ на четвёртый вопрос (КОММЕНТАРИЙ)
    messagebox.showinfo("Правильно!", "Вы ответили верно!")
    level1.title('Викторина')
    level1.geometry('900x900')
    level_1()
    level4.quit()




def level_1(): #Метод обработки первого вопроса (КОММЕНТАРИЙ)
 
    question = Label(level1,text = "Какая бывает лопата?",font = "Jokerman 20") #Текст вопроса плюс шрифт текста
    btn1 = Button(level1,text = "Совковая",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_click_button) #Далее создаем кнопки с ответами
    btn2 = Button(level1,text = "Граблевая",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)
    btn3 = Button(level1,text = "Тяпковая",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)
    btn4 = Button(level1,text = "Мотыжная",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)
 

    question.pack() #создаём видимые объекты (КОММЕНТАРИЙ)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
 
def level_2(): #Метод обработки второго вопроса (КОММЕНТАРИЙ)
 
    question = Label(level2,text = "Кто такой ара?",font = "Jokerman 20")
    btn1 = Button(level2,text = "Дельфин",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)
    btn2 = Button(level2,text = "Медьведь",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)
    btn3 = Button(level2,text = "Попугай",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_click_button2)
    btn4 = Button(level2,text = "Крокодил",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)


    question.pack() #создаём видимые объекты (КОММЕНТАРИЙ)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()

def level_3(): #Метод обработки третьего вопроса (КОММЕНТАРИЙ)
 
    question = Label(level3,text = "Сколько зубов у человека?",font = "Jokerman 20")
    btn1 = Button(level3,text = "27",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)
    btn2 = Button(level3,text = "49",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)
    btn3 = Button(level3,text = "36",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)
    btn4 = Button(level3,text = "32",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_click_button3)


    question.pack() #создаём видимые объекты (КОММЕНТАРИЙ)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()

def level_4(): #Метод обработки четвёртого вопроса (КОММЕНТАРИЙ)
 
    question = Label(level4,text = "Что является сумой всех сторон?",font = "Jokerman 20")
    btn1 = Button(level4,text = "Площадь",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)
    btn2 = Button(level4,text = "Периметр",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_click_button4)
    btn3 = Button(level4,text = "Радиус",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)
    btn4 = Button(level4,text = "Диаметр",font = "Jokerman 20",background = "#1E90FF",foreground = "#FFFFFF",width= "200",command = level_error_button)


    question.pack() #создаём видимые объекты
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()

#запуск всех окон (КОММЕНТАРИЙ)
level_1()
level1.mainloop()
level2.mainloop()
level3.mainloop()
level4.mainloop()
