# Importação de Biblioteca Tkinter
from tkinter import *
from tkinter import ttk

# Importação do Pacote Pillow
from PIL import ImageTk, Image

# Variáveis de Cores
cor1 = "#3b3b3b"
cor2 = "#1C1C1C"

# Criação de Janela
window = Tk()
window.title('')
window.geometry('910x610')
window.configure(bg=cor1)

# Frames para a Janela
frame_cima = Frame(window, width=500, height=80, bg=cor2, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)
frame_esquerda = Frame(window, width=500, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=84)
frame_direita = Frame(window, width=406, height=640, bg=cor2, pady=0, padx=3, relief='flat')
frame_direita.place(x=504, y=2)

# Estilo de Interface
style = ttk.Style(window)
style.theme_use("clam")

# Funcionalidade
unidades = {
		'Massa':[{'Quilograma':1000}, {'Grama':1}, {'Tonelada Métrica':1000000}, {'Miligrama':0.001}, {'Micrograma':0.000001}, {'Tonelada de Deslocamento':1016000}, {'Tonelada Curta':907200}, {'Stone':6350.29}, {'Libra':453.6}, {'Onça':28.35}],
		'Armazenamento de Dados':[{'Bit':0.000125},{'Kilobit':0.125},{'Kibibit':0.128},{'Megabit':125},{'Mebibit':131.072},{'Gigabit':125000},{'Gibibit':134218},{'Terabit':125000000},{'Tebibit':137400000},{'Petabit':125000000000},{'Pebibit':140700000000},{'Byte':0.001},{'Kilobyte':1000},{'Kibibyte':1024},{'Megabyte':1000000},{'MebiByte':1049000},{'Gigabyte':1000000000},{'Gibibyte':1074000000},{'Terabyte':1000000000000},{'Tebibyte':1100000000000},{'Petabype':1000000000000000},{'Pebibyte':1126000000000000}],
		'Comprimento':[{'Quilômetro':1000},{'Metro':1},{'Centímetro':0.01},{'Milímetro':0.001},{'Micrômetro':0.000001},{'Nanômetro':0.000000001},{'Milha':1609.34},{'Jarda':0.9144},{'Pé':0.3048},{'Polegada':0.0254},{'Milha Náutica':1852}],
		'Consumo de Combustível':[{'Quilômetro por Litro':1},{'Milha por Galão Americano':0.425144},{'Milhas por Galão Imperial':0.354006},{'Litro por 100 Quilômetros':100}],
		'Energia Mecânica':[{'Quilojoule':1000},{'Joule':1},{'Grama Caloria':4.184},{'Quilocaloria':4184},{'Watt-Hora':3600},{'Quilowatt-Hora':3600000},{'Elétron-Volt':1.6022*(10^(-19))},{'Unidade Térmica Britânica':1055.06},{'Therm (US)':1.055*(10^8)},{'Pré-Libra Força':1.35582}],
		'Frequência':[{'Hertz':1},{'Quilo-Hertz':1000},{'Mega-Hertz':1000000},{'Gigahertz':1000000000}],
		'Pressão':[{'Atmosfera':1},{'Bar':0.986923},{'Pascal':0.0000098682},{'Psi':0.068046},{'Torr':0.00131579}],
		'Temperatura':[{'Grau Celsius': 1},{'Grau Fahrenheit':-17.22},{'Kelvin':-272.15}],
		'Tempo':[{'Segundo':1},{'Nanosegundo':0.000000001},{'Microssegundo':0.000001},{'Milissegundo':0.001},{'Minuto':60},{'Hora':3600},{'Dia':86400},{'Semana':604800},{'Mês':2628000},{'Ano Calendário':31540000},{'Década':315400000},{'Século':3154000000}],
		'Transmissão de Dados': [{'Bit por Segundo': 1},{'Quilobit por Segundo':1000},{'Quilobyte por Segundo':8000},{'Kibibit por Segundo':1024},{'Megabit por Segundo':1000000},{'Megabyte por Segundo':8000000},{'Mebibit por Segundo': 1049000},{'Gigabit por Segundo':1000000000},{'Gigabyte por Segundo':8000000000},{'Gibibit por Segundo':1074000000},{'Terabit por Segundo':1000000000000},{'Terabyte por Segundo':8000000000000},{'Tebibit por Segundo':1100000000000}],
		'Velocidade':[{'Metro por Segundo':1},{'Milha por Hora':0.44704},{'Pés por Segundo':0.3048},{'Quilômetro por Hora':0.277778},{'Nó':0.514444}],
		'Volume':[{'Litro':1},{'Galão Americano':3.78541},{'Quarto Líquido Americano':0.946353},{'Pinta Americana':0.473176},{'Copo':0.24},{'Onça Líquida Americana':0.0295735},{'Colher de Sopa Americana':0.0147868},{'Colher de Chá Americana':0.00492892},{'Metro Cúbico':1000},{'Mililitro':0.001},{'Galão Imperial':4.54609},{'Pinto Imperial':0.568261},{'Xícara Imperial':0.284131},{'Onça Líquida Imperial':0.0284131},{'Colher de Sopa Imperial':0.0177582},{'Colher de Chá Imperial':0.00591939},{'Pé Cúbico':28.3168},{'Polegada Cúbica':0.0163871}],
		'Ângulo':[{'Grau':1},{'Grado':0.9},{'Mil Angular':0.0572958},{'Minuto de Arco':0.0166667},{'Radiano':57.2958},{'Segundo de Arco':0.000277778}],
		'Área':[{'Metro Quadrado':1},{'Quilômetro Quadrado':1000000},{'Milha Quadrada':2590000},{'Jarda Quadrada':0.836127},{'Pé Quadrado':0.092903},{'Polegada Quadrada':0.00064516},{'Hectare':10000},{'Acre':4046.86}]
	}
def mostrar_menu(i):
	unid_de = []
	unid_para = []
	unid_valor = []
	for j in unidades[i]:
		for k, v in j.items():
			unid_de.append(k)
			unid_para.append(k)
			unid_valor.append(v)
	c_de['values'] = unid_de
	c_para['values'] = unid_para
	label_unidade['text']=i
	def calcular():
		a = c_de.get()
		b = c_para.get()
		numero_para_converter = float(entrada.get())
		lista2 = unidades.get(i)
		lista3 = lista2[unid_de.index(a)]
		lista3b = lista2[unid_para.index(b)]
		lista4 = lista3.get(a)
		lista4b = lista3b.get(b)
		if(i != 'Temperatura'):
			numero = numero_para_converter*lista4/lista4b
		else:
			if(a == 'Grau Celsius' and b == 'Kelvin'):
				numero = numero_para_converter + 273.15
			if(a == 'Grau Fahrenheit' and b == 'Kelvin'):
				numero = (numero_para_converter - 32)*(5/9) + 273.15
			if(a == 'Kelvin' and b == 'Grau Celsius'):
				numero = numero_para_converter - 273.15
			if(a == 'Grau Fahrenheit' and b == 'Grau Celsius'):
				numero = (numero_para_converter - 32)*(5/9)
			if(a == 'Kelvin' and b == 'Grau Fahrenheit'):
				numero = (numero_para_converter - 273.15)*(9/5) + 32
			if(a == 'Graus Celsius' and b == 'Grau Fahrenheit'):
				numero = (numero_para_converter*(9/5)) + 32
		label_resultado['text'] = numero
	label_info = Label(frame_direita, text="Digite o Número", width=30,
	height=2, padx=3, relief='flat', pady=3, anchor='center', font=('Ivy 15 bold'), 
	bg=cor2, foreground='white')
	label_info.place(x=10, y=200)
	entrada = Entry(frame_direita, width=26, font=('Ivy 10 bold'), justify='center', relief=SOLID)
	entrada.place(x=100, y=270)
	def limpar():
		label_unidade['text']="Unidades"
		entrada.delete(0,END)
		label_resultado['text']="-------"
	button_calcular = Button(frame_direita, command=calcular, text='Calcular', width=7, height=1, padx=4,
		relief='raised', overrelief='ridge', anchor='nw', font=('Ivy 15 bold'), 
		bg='white', foreground='black')
	button_calcular.place(x=145,y=320)
	label_resultado = Label(frame_direita, text="-------", width=28, height=1, padx=0, pady=3, relief='groove', anchor='center', font=('Ivy 15 bold'), 
	bg=cor2, foreground='white')
	label_resultado.place(x=30,y=390)
	button_limpar = Button(frame_direita, command=limpar, text='Limpar', width=7, height=1, padx=4,
		relief='raised', overrelief='ridge', anchor='nw', font=('Ivy 15 bold'), 
		bg='white', foreground='black')
	button_limpar.place(x=145,y=450)


# Labels para Frame de Cima
label_nome = Label(frame_cima, text="Calculadora para Unidades de Medida", 
	height=1, padx=0, relief='flat', anchor='center', font=('Ivy 15 bold'), 
	bg=cor2, foreground='white')
label_nome.place(x=50, y=25)

# Configuração de Frame Esquerdo
img_0 = Image.open('imagens/armazenamento_de_dados.png')
img_0 = img_0.resize((25,25), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)
button_0 = Button(frame_esquerda, command=lambda:mostrar_menu('Armazenamento de Dados'), text='Armazenamento de Dados', image=img_0, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_0.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)

img_13 = Image.open('imagens/comprimento.png')
img_13 = img_13.resize((25,25), Image.ANTIALIAS)
img_13 = ImageTk.PhotoImage(img_13)
button_13 = Button(frame_esquerda, command=lambda:mostrar_menu('Comprimento'), text='Comprimento', image=img_13, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_13.grid(row=1, column=0, sticky=NSEW, pady=2, padx=2)

img_1 = Image.open('imagens/consumo_de_combustivel.png')
img_1 = img_1.resize((25,25), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)
button_1 = Button(frame_esquerda, command=lambda:mostrar_menu('Consumo de Combustível'), text='Consumo de Combustível', image=img_1, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_1.grid(row=2, column=0, sticky=NSEW, pady=2, padx=2)

img_2 = Image.open('imagens/energia_mecanica.png')
img_2 = img_2.resize((25,25), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)
button_2 = Button(frame_esquerda, command=lambda:mostrar_menu('Energia Mecânica'), text='Energia Mecânica', image=img_2, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_2.grid(row=3, column=0, sticky=NSEW, pady=2, padx=2)

img_3 = Image.open('imagens/frequencia.png')
img_3 = img_3.resize((25,25), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)
button_3 = Button(frame_esquerda, command=lambda:mostrar_menu('Frequência'), text='Frequência', image=img_3, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_3.grid(row=4, column=0, sticky=NSEW, pady=2, padx=2)

img_4 = Image.open('imagens/massa.png')
img_4 = img_4.resize((25,25), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)
button_4 = Button(frame_esquerda, command=lambda:mostrar_menu('Massa'), text='Massa', image=img_4, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_4.grid(row=5, column=0, sticky=NSEW, pady=2, padx=2)

img_5 = Image.open('imagens/pressao.png')
img_5 = img_5.resize((25,25), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)
button_5 = Button(frame_esquerda, command=lambda:mostrar_menu('Pressão'), text='Pressão', image=img_5, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_5.grid(row=6, column=0, sticky=NSEW, pady=2, padx=2)

img_6 = Image.open('imagens/temperatura.png')
img_6 = img_6.resize((25,25), Image.ANTIALIAS)
img_6 = ImageTk.PhotoImage(img_6)
button_6 = Button(frame_esquerda, command=lambda:mostrar_menu('Temperatura'), text='Temperatura', image=img_6, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_6.grid(row=7, column=0, sticky=NSEW, pady=2, padx=2)

img_7 = Image.open('imagens/tempo.png')
img_7 = img_7.resize((25,25), Image.ANTIALIAS)
img_7 = ImageTk.PhotoImage(img_7)
button_7 = Button(frame_esquerda, command=lambda:mostrar_menu('Tempo'), text='Tempo', image=img_7, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_7.grid(row=8, column=0, sticky=NSEW, pady=2, padx=2)

img_8 = Image.open('imagens/transmissao_de_dados.png')
img_8 = img_8.resize((25,25), Image.ANTIALIAS)
img_8 = ImageTk.PhotoImage(img_8)
button_8 = Button(frame_esquerda, command=lambda:mostrar_menu('Transmissão de Dados'), text='Transmissão de Dados', image=img_8, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_8.grid(row=9, column=0, sticky=NSEW, pady=2, padx=2)

img_9 = Image.open('imagens/velocidade.png')
img_9 = img_9.resize((25,25), Image.ANTIALIAS)
img_9 = ImageTk.PhotoImage(img_9)
button_9 = Button(frame_esquerda, command=lambda:mostrar_menu('Velocidade'), text='Velocidade', image=img_9, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_9.grid(row=10, column=0, sticky=NSEW, pady=2, padx=2)

img_10 = Image.open('imagens/volume.png')
img_10 = img_10.resize((25,25), Image.ANTIALIAS)
img_10 = ImageTk.PhotoImage(img_10)
button_10 = Button(frame_esquerda, command=lambda:mostrar_menu('Volume'), text='Volume', image=img_10, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_10.grid(row=11, column=0, sticky=NSEW, pady=2, padx=2)

img_11 = Image.open('imagens/area.png')
img_11 = img_11.resize((25,25), Image.ANTIALIAS)
img_11 = ImageTk.PhotoImage(img_11)
button_11 = Button(frame_esquerda, command=lambda:mostrar_menu('Área'), text='Área', image=img_11, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_11.grid(row=12, column=0, sticky=NSEW, pady=2, padx=2)

img_12 = Image.open('imagens/angulo.png')
img_12 = img_12.resize((25,25), Image.ANTIALIAS)
img_12 = ImageTk.PhotoImage(img_12)
button_12 = Button(frame_esquerda, command=lambda:mostrar_menu('Ângulo'), text='Ângulo', image=img_12, compound=LEFT, width=460, height=25, padx=10, 
	relief='flat', anchor='nw', font=('Ivy 15 bold'), overrelief='solid', 
	bg='white', foreground='black')
button_12.grid(row=13, column=0, sticky=NSEW, pady=2, padx=2)


label_unidade = Label(frame_direita, text="Unidade", width=33,
	height=3, padx=0, relief='groove', anchor='center', font=('Ivy 15 bold'), 
	bg=cor2, foreground='white')
label_unidade.place(x=0, y=0)

label_de = Label(frame_direita, text="De:",
	height=1, padx=3, relief='groove', anchor='center', font=('Ivy 10 bold'), 
	bg=cor2, foreground='white')
label_de.place(x=70, y=100)
c_de = ttk.Combobox(frame_direita, width=26, justify=('center'), font=('Ivy 10 bold'))
c_de.place(x=110, y=100)

label_para = Label(frame_direita, text="Para:",
	height=1, padx=3, relief='groove', anchor='center', font=('Ivy 10 bold'), 
	bg=cor2, foreground='white')
label_para.place(x=70, y=150)
c_para = ttk.Combobox(frame_direita, width=25, justify=('center'), font=('Ivy 10 bold'))
c_para.place(x=120, y=150)
# Execução da Interface
window.mainloop()