from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime


operador = ''
precios_comida = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]
precios_bebida = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000]
precios_postre = [3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000]


def revisar_check():

    #Comidas
    x = 0
    for c in cuadros_meal:
        if variables_meal[x].get() == 1:
            cuadros_meal[x].config(state=NORMAL)
            if cuadros_meal[x].get() == '0':
                cuadros_meal[x].delete(0, END)
            cuadros_meal[x].focus()
        else:
            cuadros_meal[x].config(state=DISABLED)
            texto_meal[x].set('0')
        x += 1

    #Bebidas
    x = 0
    for b in cuadros_drink:
        if variables_drink[x].get() == 1:
            cuadros_drink[x].config(state=NORMAL)
            if cuadros_drink[x].get() == '0':
                cuadros_drink[x].delete(0, END)
            cuadros_drink[x].focus()
        else:
            cuadros_drink[x].config(state=DISABLED)
            texto_drink[x].set('0')
        x += 1

    #Postres
    x = 0
    for p in cuadros_dessert:
        if variables_dessert[x].get() == 1:
            cuadros_dessert[x].config(state=NORMAL)
            if cuadros_dessert[x].get() == '0':
                cuadros_dessert[x].delete(0, END)
            cuadros_dessert[x].focus()
        else:
            cuadros_dessert[x].config(state=DISABLED)
            texto_dessert[x].set('0')
        x += 1


def click_boton(boton_calculadora):
    global operador
    operador = operador + boton_calculadora
    visor_calc.delete(0, END)
    visor_calc.insert(END, operador)


def borrar_visor():
    global operador
    operador = ''
    visor_calc.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calc.delete(0, END)
    visor_calc.insert(0, resultado)
    operador = ''


def total():
    sub_total_comida = 0
    precio_comida = 0
    for cantidad in texto_meal:
        sub_total_comida = sub_total_comida + (int(cantidad.get()) * precios_comida[precio_comida])
        precio_comida += 1

    sub_total_bebida = 0
    precio_bebida = 0
    for cantidad in texto_drink:
        sub_total_bebida = sub_total_bebida + (int(cantidad.get()) * precios_bebida[precio_bebida])
        precio_bebida += 1

    sub_total_postre = 0
    precio_postre = 0
    for cantidad in texto_dessert:
        sub_total_postre = sub_total_postre + (int(cantidad.get()) * precios_postre[precio_postre])
        precio_postre += 1

    sub_total = int(sub_total_comida + sub_total_bebida + sub_total_postre)
    impuesto = int(sub_total * 0.19)
    total_cuenta = int(sub_total + impuesto)

    var_cost_meal.set(f'$ {sub_total_comida}')
    var_cost_drink.set(f'$ {sub_total_bebida}')
    var_cost_dessert.set(f'$ {sub_total_postre}')
    var_subtotal.set(f'$ {sub_total}')
    var_impuesto.set(f'$ {impuesto}')
    var_total.set(f'$ {total_cuenta}')


def recibo():
    text_bill.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    text_bill.insert(END, f'Boleta:\t{num_recibo}\t\tFecha:\t{fecha_recibo}\n')
    text_bill.insert(END, f'*' * 78 + '\n')
    text_bill.insert(END, 'Items\t\tCant.\tCosto Items\n')
    text_bill.insert(END, f'-' * 93 + '\n')

    x = 0
    for meal in texto_meal:
        if meal.get() != '0':
            text_bill.insert(END, f'{meal_list[x]}\t\t{meal.get()}\t'
                                  f'$ {int(meal.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for drink in texto_drink:
        if drink.get() != '0':
            text_bill.insert(END, f'{drink_list[x]}\t\t{drink.get()}\t'
                                  f'$ {int(drink.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for dessert in texto_dessert:
        if dessert.get() != '0':
            text_bill.insert(END, f'{dessert_list[x]}\t\t{dessert.get()}\t'
                                  f'$ {int(dessert.get()) * precios_postre[x]}\n')
        x += 1

    text_bill.insert(END, f'-' * 93 + '\n')
    text_bill.insert(END, f' Costo de la comida: \t\t\t{var_cost_meal.get()}\n')
    text_bill.insert(END, f' Costo de la bebida: \t\t\t{var_cost_drink.get()}\n')
    text_bill.insert(END, f' Costo del postre: \t\t\t{var_cost_dessert.get()}\n')
    text_bill.insert(END, f'-' * 93 + '\n')
    text_bill.insert(END, f' Sub Total: \t\t\t{var_subtotal.get()}\n')
    text_bill.insert(END, f' Impuesto: \t\t\t{var_impuesto.get()}\n')
    text_bill.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    text_bill.insert(END, f'*' * 78 + '\n')
    text_bill.insert(END, f'Muchas gracias por su visita.\n')
    text_bill.insert(END, f'\nJC Restaurant SPA')


def guardar_recibo():
    info_recibo = text_bill.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Recibo guardado.')


def resetear():
    text_bill.delete(0.1, END)
    for texto in texto_meal:
        texto.set('0')
    for texto in texto_drink:
        texto.set('0')
    for texto in texto_dessert:
        texto.set('0')

    for cuadro in cuadros_meal:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_drink:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_dessert:
        cuadro.config(state=DISABLED)

    for v in variables_meal:
        v.set(0)
    for v in variables_drink:
        v.set(0)
    for v in variables_dessert:
        v.set(0)

    var_cost_meal.set('')
    var_cost_drink.set('')
    var_cost_dessert.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


#Iniciar Tkinter
app = Tk()

#Tamaño de la ventana
app.geometry('1024x600+0+0')

#Evitar maximizar
app.resizable(False, False)

#Título de la ventana
app.title('Restaurant System App')

#Color de fondo
app.config(bg='black')

#Panel superior
top_panel = Frame(app, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

#Panel izquierdo
left_panel = Frame(app, bd=1, relief=FLAT, bg='black')
left_panel.pack(side=LEFT)

#Panel derecho
right_panel = Frame(app, bd=1, relief=FLAT, bg='black')
right_panel.pack(side=RIGHT)

#Panel costos
costos_panel = Frame(left_panel, bd=1, relief=FLAT, bg='black', padx=35, pady=10)
costos_panel.pack(side=BOTTOM)

#Panel menu
menu_panel = LabelFrame(left_panel, bd=1, relief=FLAT, bg='black', padx=172)
menu_panel.pack(side=TOP)

#Panel comidas
meal_panel = LabelFrame(left_panel, padx=10, bg='grey', text='Comidas\n',
                        font=('Montserrat', 16, 'underline'), bd=1, relief=FLAT, fg='white', labelanchor=N)
meal_panel.pack(side=LEFT)

#Panel bebidas
drink_panel = LabelFrame(left_panel, padx=10, bg='grey', text='Bebidas\n',
                         font=('Montserrat', 16, 'underline'), bd=1, relief=FLAT, fg='white', labelanchor=N)
drink_panel.pack(side=LEFT)

#Panel postres
dessert_panel = LabelFrame(left_panel, padx=10, bg='grey', text='Postres\n',
                           font=('Montserrat', 16, 'underline'), bd=1, relief=FLAT, fg='white', labelanchor=N)
dessert_panel.pack(side=LEFT)

#Panel calculadora
calc_panel = Frame(right_panel, bd=1, relief=FLAT, bg='black')
calc_panel.pack()

#Panel factura
bill_panel = Frame(right_panel, bd=1, relief=FLAT, bg='black', padx=20)
bill_panel.pack()

#Panel botones
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg='black')
buttons_panel.pack()

#Etiqueta título
label_title = Label(top_panel,
                    text='Restaurant - Sistema de facturación',
                    fg='white', font=('Montserrat', 36, 'underline'), bg='black', width=33)
label_title.grid(row=0, column=0)

#Etiqueta menú
menu_title = Label(menu_panel, text='Menú', fg='white', font=('Montserrat', 24), bg='black')
menu_title.grid(row=0, column=0)

#Listas de productos
meal_list = ['Lasagna', 'Ramen', 'Sopa', 'Pollo', 'Tacos',
             'Reineta', 'Cazuela', 'Empanada', 'Ensalada', 'Filete']

drink_list = ['Gaseosa', 'Jugo', 'Smoothie', 'Café', 'Té',
              'mineral', 'Tónica', 'Cerveza', 'Vino', 'Gin']

dessert_list = ['Flan', 'Torta', 'Kuchen', 'Tiramisú', 'Berlín',
                'Cheesecake', 'Ricota', 'Sémola', 'Panqueques', 'Compota']

#Generar items comida
cont_comidas = 0
variables_meal = []
cuadros_meal = []
texto_meal = []

for comida in meal_list:

    #Crear los Checkbutton
    variables_meal.append('')
    variables_meal[cont_comidas] = IntVar()
    comida = Checkbutton(meal_panel,
                         text=comida.title(),
                         fg='black',
                         bg='grey',
                         font=('Dosis', 12, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_meal[cont_comidas],
                         command=revisar_check)
    comida.grid(row=cont_comidas, column=0, sticky=W)

    #Crear los cuadros de entrada
    cuadros_meal.append('')
    texto_meal.append('')
    texto_meal[cont_comidas] = StringVar()
    texto_meal[cont_comidas].set('0')
    cuadros_meal[cont_comidas] = Entry(meal_panel,
                                       font=('Dosis', 12, 'bold'),
                                       bd=1,
                                       width=3,
                                       state=DISABLED,
                                       textvariable=texto_meal[cont_comidas])

    cuadros_meal[cont_comidas].grid(row=cont_comidas, column=1)
    cont_comidas += 1

#Generar items bebida
cont_bebidas = 0
variables_drink = []
cuadros_drink = []
texto_drink = []

for bebida in drink_list:
    variables_drink.append('')
    variables_drink[cont_bebidas] = IntVar()
    bebida = Checkbutton(drink_panel,
                         text=bebida.title(),
                         fg='black',
                         bg='grey',
                         font=('Dosis', 12, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_drink[cont_bebidas],
                         command=revisar_check)
    bebida.grid(row=cont_bebidas, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_drink.append('')
    texto_drink.append('')
    texto_drink[cont_bebidas] = StringVar()
    texto_drink[cont_bebidas].set('0')
    cuadros_drink[cont_bebidas] = Entry(drink_panel,
                                        font=('Dosis', 12, 'bold'),
                                        bd=1,
                                        width=3,
                                        state=DISABLED,
                                        textvariable=texto_drink[cont_bebidas])
    cuadros_drink[cont_bebidas].grid(row=cont_bebidas, column=1)
    cont_bebidas += 1

#Generar items postre
cont_postres = 0
variables_dessert = []
cuadros_dessert = []
texto_dessert = []

for postre in dessert_list:
    variables_dessert.append('')
    variables_dessert[cont_postres] = IntVar()
    postre = Checkbutton(dessert_panel,
                         text=postre.title(),
                         fg='black',
                         bg='grey',
                         font=('Dosis', 12, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_dessert[cont_postres],
                         command=revisar_check)
    postre.grid(row=cont_postres, column=0, sticky=W)

    #Crear los cuadros de entrada
    cuadros_dessert.append('')
    texto_dessert.append('')
    texto_dessert[cont_postres] = StringVar()
    texto_dessert[cont_postres].set('0')
    cuadros_dessert[cont_postres] = Entry(dessert_panel,
                                          font=('Dosis', 12, 'bold'),
                                          bd=1,
                                          width=3,
                                          state=DISABLED,
                                          textvariable=texto_dessert[cont_postres])
    cuadros_dessert[cont_postres].grid(row=cont_postres, column=1)
    cont_postres += 1

#Variables
var_cost_meal = StringVar()
var_cost_drink = StringVar()
var_cost_dessert = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

#Etiquetas y entrada de costo
label_cost_meal = Label(costos_panel,
                        text='Total Comida',
                        font=('Dosis', 12, 'bold'),
                        bg='black',
                        fg='white')
label_cost_meal.grid(row=0, column=0)
texto_cost_meal = Entry(costos_panel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_cost_meal)
texto_cost_meal.grid(row=0, column=1)

label_cost_drink = Label(costos_panel,
                         text='Total Bebida',
                         font=('Dosis', 12, 'bold'),
                         bg='black',
                         fg='white')
label_cost_drink.grid(row=1, column=0)
texto_cost_drink = Entry(costos_panel,
                         font=('Dosis', 12, 'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=var_cost_drink)
texto_cost_drink.grid(row=1, column=1)

label_cost_dessert = Label(costos_panel,
                           text='Total Postre',
                           font=('Dosis', 12, 'bold'),
                           bg='black',
                           fg='white')
label_cost_dessert.grid(row=2, column=0)
texto_cost_dessert = Entry(costos_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_cost_dessert)
texto_cost_dessert.grid(row=2, column=1)

label_subtotal = Label(costos_panel,
                       text='Subtotal',
                       font=('Dosis', 12, 'bold'),
                       bg='black',
                       fg='white')
label_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(costos_panel,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3)

label_impuesto = Label(costos_panel,
                       text='Impuesto',
                       font=('Dosis', 12, 'bold'),
                       bg='black',
                       fg='white')
label_impuesto.grid(row=1, column=2)
texto_impuesto = Entry(costos_panel,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3)

label_total = Label(costos_panel,
                    text='Total',
                    font=('Dosis', 12, 'bold'),
                    bg='black',
                    fg='white')
label_total.grid(row=2, column=2)
texto_total = Entry(costos_panel,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3)


#Botones Facturación
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []


columnas = 0
for boton in botones:
    boton = Button(buttons_panel,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='black',
                   bd=1,
                   width=9)

    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar_recibo)
botones_creados[3].config(command=resetear)

#Area de recibo
text_bill = Text(bill_panel,
                 font=('Dosis', 12, 'bold'),
                 bd=1,
                 width=52,
                 height=9)
text_bill.grid(row=0, column=0)

#Calculadora
visor_calc = Entry(calc_panel,
                   font=('Dosis', 16, 'bold'),
                   width=39,
                   bd=1)
visor_calc.grid(row=0, column=0, columnspan=4)

botones_calc = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '=', 'C', '0', '/']

botones_asignados = []

fila = 1
columna = 0
for boton in botones_calc:
    boton = Button(calc_panel,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='black',
                   bd=1,
                   width=9,)
    botones_asignados.append(boton)
    boton.grid(row=fila, column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0

botones_asignados[0].config(command=lambda: click_boton('7'))
botones_asignados[1].config(command=lambda: click_boton('8'))
botones_asignados[2].config(command=lambda: click_boton('9'))
botones_asignados[3].config(command=lambda: click_boton('+'))
botones_asignados[4].config(command=lambda: click_boton('4'))
botones_asignados[5].config(command=lambda: click_boton('5'))
botones_asignados[6].config(command=lambda: click_boton('6'))
botones_asignados[7].config(command=lambda: click_boton('-'))
botones_asignados[8].config(command=lambda: click_boton('1'))
botones_asignados[9].config(command=lambda: click_boton('2'))
botones_asignados[10].config(command=lambda: click_boton('3'))
botones_asignados[11].config(command=lambda: click_boton('*'))
botones_asignados[12].config(command=obtener_resultado)
botones_asignados[13].config(command=borrar_visor)
botones_asignados[14].config(command=lambda: click_boton('0'))
botones_asignados[15].config(command=lambda: click_boton('/'))

# Pantalla persistente
app.mainloop()
