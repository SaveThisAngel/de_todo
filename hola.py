import turtle
from tkinter import *
from tkinter.colorchooser import askcolor

class TurtleWindow:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=1.0, height=0.75, startx=-1, starty=1)
        self.screen.colormode(255)
        self.screen.bgcolor("#ffffff")
        self.screen.title("Paint & Draw")
        self.pen = turtle.Pen()
        self.pen.ht()
        self.pen.speed(0)
        self.pen.shape("circle")
        self.can_drag = False

    def setTkinterSource(self, tkinter_source):
        self.tkinter_source = tkinter_source #TkinterWindow instance -> to get data and form

    def onClick(self, x, y): #click the screen (wherever)
        data = self.tkinter_source.current_draw_data[:]
        form = self.tkinter_source.current_draw_form
        if data != [] and form != "":
            if form == "free draw":
                if self.can_drag:
                    self.pen.st()
                    self.pen.pencolor(data[0])
                    self.pen.pensize(int(data[1]))
                    self.pen.pu()
                    self.pen.goto(x, y)
                    self.pen.pd()

            elif form == "circle" or form == "circular eraser":
                self.pen.ht()
                if data[0].isdigit() and int(data[0]) > 0 and data[2].isdigit() \
                   and int(data[2]) > 0:
                    self.current_draw = Circle(x, y, int(data[0]), data[1], int(data[2]), data[3])
                    self.current_draw.draw(self.pen)

            elif form == "regular polygon" or form == "regular eraser":
                self.pen.ht()
                if data[0].isdigit() and int(data[0]) >= 3 and data[1].isdigit() \
                   and data[3].isdigit() and int(data[3]) > 0:
                    self.current_draw = RegularPolygon(x, y, int(data[0]), int(data[1]), data[2], int(data[3]), data[4])
                    self.current_draw.draw(self.pen)

            elif form == "rectangle":
                self.pen.ht()
                if data[0].isdigit() and int(data[0]) > 0 and data[1].isdigit() and int(data[1]) > 0\
                   and int(data[0]) != int(data[1]) and data[3].isdigit() and int(data[3]) > 0:
                    self.current_draw = Rectangle(x, y, int(data[0]), int(data[1]), data[2], int(data[3]), data[4])
                    self.current_draw.draw(self.pen)

            elif form == "trapezium":
                self.pen.ht()
                if data[0].isdigit() and int(data[0]) > 0 and data[1].isdigit() and int(data[1]) > 0 \
                   and int(data[0]) != int(data[1]) and data[2].isdigit() and int(data[2]) > 0\
                   and data[4].isdigit() and int(data[4]) > 0:
                    self.current_draw = Trapezium(x, y, int(data[0]), int(data[1]), int(data[2]), data[3], int(data[4]), data[5])
                    self.current_draw.draw(self.pen)

            elif form == "lozenge":
                self.pen.ht()
                if data[0].isdigit() and int(data[0]) > 0 and data[1].isdigit() and int(data[1]) > 0\
                   and data[3].isdigit() and int(data[3]) > 0:
                    self.current_draw = Lozenge(x, y, int(data[0]), int(data[1]), data[2], int(data[3]), data[4])
                    self.current_draw.draw(self.pen)

            elif form == "text":
                self.pen.ht()
                if data[0] != "" and data[1].isalpha() and data[2].isdigit() and int(data[2]) > 0 \
                   and data[4].lower() in ["bold", "normal", "italic"] and data[5].lower() in ["center", "left", "right"]:
                    self.current_draw = Text(x, y, data[0], data[1].lower().capitalize(), int(data[2]), data[3], data[4], data[5])
                    self.current_draw.draw(self.pen)

    def onDrag(self, x, y): #drag THE PEN (not the mouse)
        form = self.tkinter_source.current_draw_form
        if form == "free draw" and self.can_drag:
            self.pen.goto(x, y)

class TkinterWindow:
    def __init__(self):
        self.f_1 = Frame()
        self.f_1.pack()
        self.l_initial = Label(self.f_1, text="Bem-vindo ao Paint & Draw! Selecione uma opcao do menu para comecar a desenhar!",
                                fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.l_initial.pack()

        self.eraser_bg_color = "#ffffff"

        self.line_color = "#000000"
        self.bg_color = "#ffffff"
        self.font_color = "#000000"
        self.current_draw_form = ""
        self.current_draw_data = []

class MenuWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Ferramentas")
        self.menubar = Menu(master)

        self.free_draw = Menu(self.menubar, tearoff=0)
        self.free_draw.add_command(label="Desenho livre",
                                   command=self.setTkinterWindowToFreeDraw)
        self.menubar.add_cascade(label="Desenho Livre", menu=self.free_draw)

        self.circle = Menu(self.menubar, tearoff=0)
        self.circle.add_command(label="Circulo perfeito",
                                command=self.setTkinterWindowToCircle)
        self.menubar.add_cascade(label="Circulo", menu=self.circle)

        self.regular_polygon = Menu(self.menubar, tearoff=0)
        self.regular_polygon.add_command(label="Digite os dados",
                                         command=self.setTkinterWindowToRegularPolygon)
        self.menubar.add_cascade(label="Poligono regular", menu=self.regular_polygon)

        self.irregular_polygon = Menu(self.menubar, tearoff=0)
        self.irregular_polygon.add_command(label="Retangulo",
                                           command=self.setTkinterWindowToRectangle)
        self.irregular_polygon.add_command(label="Trapezio",
                                           command=self.setTkinterWindowToTrapezium)
        self.irregular_polygon.add_command(label="Losango",
                                           command=self.setTkinterWindowToLozenge)
        self.menubar.add_cascade(label="Poligono irregular", menu=self.irregular_polygon)

        self.text = Menu(self.menubar, tearoff=0)
        self.text.add_command(label="Inserir texto",
                              command=self.setTkinterWindowToText)
        self.menubar.add_cascade(label="Texto", menu=self.text)

        self.erase = Menu(self.menubar, tearoff=0)#Apagar
        self.eraser = Menu(self.menubar, tearoff=0) #borracha circular e regular
        self.eraser.add_command(label="Borracha circular", command=self.setTkinterWindowToCircularEraser)
        self.eraser.add_command(label="Borracha regular", command=self.setTkinterWindowToRegularEraser)
        self.erase.add_cascade(label="Borracha", menu=self.eraser)
        self.menubar.add_cascade(label="Apagar", menu=self.erase)
        self.erase.add_command(label="Limpar tela", command=self.setTkinterWindowToScreenCleaner)

        self.options = Menu(self.menubar, tearoff=0)
        self.options.add_command(label="Ajuda", command=self.setHelp)
        self.menubar.add_cascade(label="Opcoes", menu=self.options)

        self.f_1 = Frame(self.master)
        self.f_1.pack()

        self.master.config(menu=self.menubar)
        self.master.geometry("550x55") #resizes menu window

    def setTkinterWindow(self, tkinter_window): self.tkinter_window = tkinter_window #bottom bar

    def setTurtleWindow(self, turtle_window): self.turtle_window = turtle_window #candrag and bg_color

    def setHelp(self):
        self.l_help_title = Label(self.f_1, text="Manual do Paint & Draw", fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.l_help_title.pack(side=TOP)
        self.l_help_text = Label(self.f_1, fg="black", bg="white", font=("Raleway", 9), text=help_text.text)
        self.l_help_text.pack(side=TOP)

    def setLineBGAndCreate(self, create, line_color=True, line_thickness=True, bg_color=True):
        if line_color:
            self.tkinter_window.l_line_color = Label(self.tkinter_window.f_1, text="   Cor da linha:", font=("Raleway", 12))
            self.tkinter_window.l_line_color.pack(side=LEFT)
            self.tkinter_window.b_line_color = Button(self.tkinter_window.f_1, bg=self.tkinter_window.line_color, width=3, font=("Raleway", 12),
                                                      command=self.setLineColor)
            self.tkinter_window.b_line_color.pack(side=LEFT)
        if line_thickness:
            self.tkinter_window.l_line_thickness = Label(self.tkinter_window.f_1, text="   Espessura da linha(px):", font=("Raleway", 12))
            self.tkinter_window.l_line_thickness.pack(side=LEFT)
            self.tkinter_window.e_line_thickness = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
            self.tkinter_window.e_line_thickness.pack(side=LEFT)
        if bg_color:
            self.tkinter_window.l_bg_color = Label(self.tkinter_window.f_1, text="   Cor de fundo:", font=("Raleway", 12))
            self.tkinter_window.l_bg_color.pack(side=LEFT)
            self.tkinter_window.b_bg_color = Button(self.tkinter_window.f_1, width=3,
                                                    bg=self.tkinter_window.bg_color, font=("Raleway", 12),
                                                    command=self.setBGColor)
            self.tkinter_window.b_bg_color.pack(side=LEFT)

        self.tkinter_window.b_create = Button(self.tkinter_window.f_1, text="Criar!",
                                              font=("Raleway", 12, "bold"), width=6,
                                              fg="red", bg="yellow",
                                              command=create)
        self.tkinter_window.b_create.pack(side=LEFT)

    def setTkinterWindowToFreeDraw(self):
        #line_color, line_thickness
        self.tkinter_window.current_draw_form = "free draw"

        self.f_1.destroy()
        self.f_1 = Frame(self.master)
        self.f_1.pack()
        self.master.geometry("550x55")

        self.tkinter_window.f_1.destroy()
        self.tkinter_window.f_1 = Frame()
        self.tkinter_window.f_1.pack()

        self.tkinter_window.l_1 = Label(self.tkinter_window.f_1, text="Desenho Livre",
                                        fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.tkinter_window.l_1.pack(side=LEFT)

        self.setLineBGAndCreate(self.createFreeDraw, bg_color=False)

    def setTkinterWindowToCircle(self):
        #radius, line_color, line_thickness, bg_color
        self.tkinter_window.current_draw_form = "circle"

        self.f_1.destroy()
        self.f_1 = Frame(self.master)
        self.f_1.pack()
        self.master.geometry("550x55")

        self.tkinter_window.f_1.destroy()
        self.tkinter_window.f_1 = Frame()
        self.tkinter_window.f_1.pack()

        self.tkinter_window.l_1 = Label(self.tkinter_window.f_1, text="Circulo perfeito",
                                        fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.tkinter_window.l_1.pack(side=LEFT)

        self.tkinter_window.l_radius = Label(self.tkinter_window.f_1, text="   Raio(px):", font=("Raleway", 12))
        self.tkinter_window.l_radius.pack(side=LEFT)
        self.tkinter_window.e_radius = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_radius.pack(side=LEFT)

        self.setLineBGAndCreate(self.createCircle)

    def setTkinterWindowToRegularPolygon(self):
        #n_sides, side_size, line_color, line_thickness, bg_color
        self.tkinter_window.current_draw_form = "regular polygon"

        self.f_1.destroy()
        self.f_1 = Frame(self.master)
        self.f_1.pack()
        self.master.geometry("550x55")

        self.tkinter_window.f_1.destroy()
        self.tkinter_window.f_1 = Frame()
        self.tkinter_window.f_1.pack()

        self.tkinter_window.l_1 = Label(self.tkinter_window.f_1, text="Poligono regular",
                                        fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.tkinter_window.l_1.pack(side=LEFT)

        self.tkinter_window.l_n_sides = Label(self.tkinter_window.f_1, text="   Lados:", font=("Raleway", 12))
        self.tkinter_window.l_n_sides.pack(side=LEFT)
        self.tkinter_window.e_n_sides = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_n_sides.pack(side=LEFT)

        self.tkinter_window.l_side_size = Label(self.tkinter_window.f_1, text="   Tamanho do lado(px):", font=("Raleway", 12))
        self.tkinter_window.l_side_size.pack(side=LEFT)
        self.tkinter_window.e_side_size = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_side_size.pack(side=LEFT)

        self.setLineBGAndCreate(self.createRegularPolygon)

    def setTkinterWindowToRectangle(self):
        #side1, side2, line_color, line_thickness, bg_color
        self.tkinter_window.current_draw_form = "rectangle"

        self.f_1.destroy()
        self.f_1 = Frame(self.master)
        self.f_1.pack()
        self.master.geometry("550x55")

        self.tkinter_window.f_1.destroy()
        self.tkinter_window.f_1 = Frame()
        self.tkinter_window.f_1.pack()

        self.tkinter_window.l_1 = Label(self.tkinter_window.f_1, text="Retangulo",
                                        fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.tkinter_window.l_1.pack(side=LEFT)

        self.tkinter_window.l_side1 = Label(self.tkinter_window.f_1, text="   Altura(px):",
                                            font=("Raleway", 12))
        self.tkinter_window.l_side1.pack(side=LEFT)
        self.tkinter_window.e_side1 = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_side1.pack(side=LEFT)

        self.tkinter_window.l_side2 = Label(self.tkinter_window.f_1, text="   Comprimento(px):",
                                            font=("Raleway", 12))
        self.tkinter_window.l_side2.pack(side=LEFT)
        self.tkinter_window.e_side2 = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_side2.pack(side=LEFT)

        self.setLineBGAndCreate(self.createRectangle)

    def setTkinterWindowToTrapezium(self):
        #height, topbase, bottombase, line_color, line_thickness, bg_color
        self.tkinter_window.current_draw_form = "trapezium"

        self.f_1.destroy()
        self.f_1 = Frame(self.master)
        self.f_1.pack()
        self.master.geometry("550x55")

        self.tkinter_window.f_1.destroy()
        self.tkinter_window.f_1 = Frame()
        self.tkinter_window.f_1.pack()

        self.tkinter_window.l_1 = Label(self.tkinter_window.f_1, text="Trapezio",
                                        fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.tkinter_window.l_1.pack(side=LEFT)

        self.tkinter_window.l_top_base = Label(self.tkinter_window.f_1, text="   Base superior(px):",
                                               font=("Raleway", 12))
        self.tkinter_window.l_top_base.pack(side=LEFT)
        self.tkinter_window.e_top_base = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_top_base.pack(side=LEFT)

        self.tkinter_window.l_bottom_base = Label(self.tkinter_window.f_1, text="   Base inferior(px):",
                                                  font=("Raleway", 12))
        self.tkinter_window.l_bottom_base.pack(side=LEFT)
        self.tkinter_window.e_bottom_base = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_bottom_base.pack(side=LEFT)

        self.tkinter_window.l_height = Label(self.tkinter_window.f_1, text="   Altura(px):",
                                                  font=("Raleway", 12))
        self.tkinter_window.l_height.pack(side=LEFT)
        self.tkinter_window.e_height = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_height.pack(side=LEFT)

        self.setLineBGAndCreate(self.createTrapezium)

    def setTkinterWindowToLozenge(self):
        #height, width, line_color, line_thickness, bg_color
        self.tkinter_window.current_draw_form = "lozenge"

        self.f_1.destroy()
        self.f_1 = Frame(self.master)
        self.f_1.pack()
        self.master.geometry("550x55")

        self.tkinter_window.f_1.destroy()
        self.tkinter_window.f_1 = Frame()
        self.tkinter_window.f_1.pack()

        self.tkinter_window.l_1 = Label(self.tkinter_window.f_1, text="Losango",
                                        fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.tkinter_window.l_1.pack(side=LEFT)

        self.tkinter_window.l_height = Label(self.tkinter_window.f_1, text="   Altura(px):", font=("Raleway", 12))
        self.tkinter_window.l_height.pack(side=LEFT)
        self.tkinter_window.e_height = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_height.pack(side=LEFT)

        self.tkinter_window.l_width = Label(self.tkinter_window.f_1, text="   Largura(px):", font=("Raleway", 12))
        self.tkinter_window.l_width.pack(side=LEFT)
        self.tkinter_window.e_width = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_width.pack(side=LEFT)

        self.setLineBGAndCreate(self.createLozenge)

    def setTkinterWindowToText(self):
        #text, font_family, font_size, font_color, font_type, align
        self.tkinter_window.current_draw_form = "text"

        self.f_1.destroy()
        self.f_1 = Frame(self.master)
        self.f_1.pack()
        self.master.geometry("550x55")

        self.tkinter_window.f_1.destroy()
        self.tkinter_window.f_1 = Frame()
        self.tkinter_window.f_1.pack()

        self.tkinter_window.l_1 = Label(self.tkinter_window.f_1, text="Texto",
                                        fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.tkinter_window.l_1.pack(side=LEFT)

        self.tkinter_window.l_text = Label(self.tkinter_window.f_1, text="   Texto:", font=("Raleway", 12))
        self.tkinter_window.l_text.pack(side=LEFT)
        self.tkinter_window.e_text = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=30)
        self.tkinter_window.e_text.pack(side=LEFT)

        self.tkinter_window.l_font_family = Label(self.tkinter_window.f_1, text="   Fonte:", font=("Raleway", 12))
        self.tkinter_window.l_font_family.pack(side=LEFT)
        self.tkinter_window.e_font_family = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=15)
        self.tkinter_window.e_font_family.pack(side=LEFT)

        self.tkinter_window.l_font_size = Label(self.tkinter_window.f_1, text="   Tamanho da fonte(px):", font=("Raleway", 12))
        self.tkinter_window.l_font_size.pack(side=LEFT)
        self.tkinter_window.e_font_size = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=3)
        self.tkinter_window.e_font_size.pack(side=LEFT)

        self.tkinter_window.l_font_color = Label(self.tkinter_window.f_1, text="   Cor da fonte:", font=("Raleway", 12))
        self.tkinter_window.l_font_color.pack(side=LEFT)
        self.tkinter_window.b_font_color = Button(self.tkinter_window.f_1, width=3, height=1,
                                                  bg=self.tkinter_window.font_color, command=self.setFontColor)
        self.tkinter_window.b_font_color.pack(side=LEFT)

        self.tkinter_window.l_font_type = Label(self.tkinter_window.f_1, text="   Tipo da fonte:", font=("Raleway", 12))
        self.tkinter_window.l_font_type.pack(side=LEFT)
        self.tkinter_window.e_font_type = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=7)
        self.tkinter_window.e_font_type.pack(side=LEFT)

        self.tkinter_window.l_align = Label(self.tkinter_window.f_1, text="   Alinhamento:", font=("Raleway", 12))
        self.tkinter_window.l_align.pack(side=LEFT)
        self.tkinter_window.e_align = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=7)
        self.tkinter_window.e_align.pack(side=LEFT)

        self.tkinter_window.b_create = Button(self.tkinter_window.f_1, text="Criar!",
                                              font=("Raleway", 12, "bold"), width=6,
                                              fg="red", bg="yellow", command=self.createText)
        self.tkinter_window.b_create.pack(side=LEFT)

    def setTkinterWindowToCircularEraser(self):
        self.tkinter_window.current_draw_form = "circular eraser"

        self.f_1.destroy()
        self.f_1 = Frame(self.master)
        self.f_1.pack()
        self.master.geometry("550x55")

        self.tkinter_window.f_1.destroy()
        self.tkinter_window.f_1 = Frame()
        self.tkinter_window.f_1.pack()

        #RGB to hex
        self.tkinter_window.eraser_bg_color = "#"
        for c in self.turtle_window.screen.bgcolor():
            self.tkinter_window.eraser_bg_color += hex(int(c))[2:]

        self.tkinter_window.l_1 = Label(self.tkinter_window.f_1, text="Borracha circular",
                                        fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.tkinter_window.l_1.pack(side=LEFT)

        self.tkinter_window.l_radius = Label(self.tkinter_window.f_1, text="   Raio(px):", font=("Raleway", 12))
        self.tkinter_window.l_radius.pack(side=LEFT)
        self.tkinter_window.e_radius = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_radius.pack(side=LEFT)

        self.tkinter_window.l_bg_color = Label(self.tkinter_window.f_1, text="   Cor de fundo:", font=("Raleway", 12))
        self.tkinter_window.l_bg_color.pack(side=LEFT)
        self.tkinter_window.b_eraser_bg_color = Button(self.tkinter_window.f_1, width=3,
                                                bg=self.tkinter_window.eraser_bg_color, font=("Raleway", 12),
                                                command=self.setEraserBGColor)
        self.tkinter_window.b_eraser_bg_color.pack(side=LEFT)

        self.tkinter_window.b_create = Button(self.tkinter_window.f_1, text="Criar!",
                                              font=("Raleway", 12, "bold"), width=6,
                                              fg="red", bg="yellow", command=self.createCircle)
        self.tkinter_window.b_create.pack(side=LEFT)

    def setTkinterWindowToRegularEraser(self):
        self.tkinter_window.current_draw_form = "regular eraser"

        self.f_1.destroy()
        self.f_1 = Frame(self.master)
        self.f_1.pack()
        self.master.geometry("550x55")

        self.tkinter_window.f_1.destroy()
        self.tkinter_window.f_1 = Frame()
        self.tkinter_window.f_1.pack()

        self.tkinter_window.l_1 = Label(self.tkinter_window.f_1, text="Borracha regular",
                                        fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.tkinter_window.l_1.pack(side=LEFT)

        self.tkinter_window.eraser_bg_color = "#"
        for c in self.turtle_window.screen.bgcolor():
            self.tkinter_window.eraser_bg_color += hex(int(c))[2:]

        self.tkinter_window.l_n_sides = Label(self.tkinter_window.f_1, text="   Lados:", font=("Raleway", 12))
        self.tkinter_window.l_n_sides.pack(side=LEFT)
        self.tkinter_window.e_n_sides = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_n_sides.pack(side=LEFT)

        self.tkinter_window.l_side_size = Label(self.tkinter_window.f_1, text="   Tamanho do lado(px):", font=("Raleway", 12))
        self.tkinter_window.l_side_size.pack(side=LEFT)
        self.tkinter_window.e_side_size = Entry(self.tkinter_window.f_1, font=("Raleway", 12), width=4)
        self.tkinter_window.e_side_size.pack(side=LEFT)

        self.tkinter_window.l_bg_color = Label(self.tkinter_window.f_1, text="   Cor de fundo:", font=("Raleway", 12))
        self.tkinter_window.l_bg_color.pack(side=LEFT)

        self.tkinter_window.b_eraser_bg_color = Button(self.tkinter_window.f_1, width=3,
                                                bg=self.tkinter_window.eraser_bg_color, font=("Raleway", 12),
                                                command=self.setEraserBGColor)
        self.tkinter_window.b_eraser_bg_color.pack(side=LEFT)

        self.tkinter_window.b_create = Button(self.tkinter_window.f_1, text="Criar!",
                                              font=("Raleway", 12, "bold"), width=6,
                                              fg="red", bg="yellow", command=self.createRegularPolygon)
        self.tkinter_window.b_create.pack(side=LEFT)

    def setTkinterWindowToScreenCleaner(self):
        self.f_1.destroy()
        self.f_1 = Frame(self.master)
        self.f_1.pack()
        self.master.geometry("550x55")

        self.tkinter_window.f_1.destroy()
        self.tkinter_window.f_1 = Frame()
        self.tkinter_window.f_1.pack()

        self.tkinter_window.bg_color = "#"
        for c in self.turtle_window.screen.bgcolor():
            self.tkinter_window.bg_color += hex(int(c))[2:]

        self.tkinter_window.l_1 = Label(self.tkinter_window.f_1, text="Limpar tela",
                                        fg="cyan", bg="navy", font=("Raleway", 12, "bold"))
        self.tkinter_window.l_1.pack(side=LEFT)

        self.tkinter_window.l_bg_color = Label(self.tkinter_window.f_1, text="   Nova cor de fundo:", font=("Raleway", 12))
        self.tkinter_window.l_bg_color.pack(side=LEFT)

        self.tkinter_window.b_bg_color = Button(self.tkinter_window.f_1, width=3,
                                                bg=self.tkinter_window.bg_color, font=("Raleway", 12), command=self.setBGColor)
        self.tkinter_window.b_bg_color.pack(side=LEFT)

        self.tkinter_window.b_clear = Button(self.tkinter_window.f_1, text="Limpar!",
                                              font=("Raleway", 12, "bold"), width=6,
                                              fg="red", bg="yellow", command=self.clearTurtleScreen)
        self.tkinter_window.b_clear.pack(side=LEFT)

    ###########functions to the form settings

    def setLineColor(self):
        line_color = askcolor(color=self.tkinter_window.line_color, title="Cor da linha")
        if None not in line_color:
            self.tkinter_window.line_color = line_color[1]
            self.tkinter_window.b_line_color["bg"] = line_color[1]

    def setBGColor(self):
        bg_color = askcolor(color=self.tkinter_window.bg_color, title="Cor de fundo")
        if None not in bg_color:
            self.tkinter_window.bg_color = bg_color[1]
            self.tkinter_window.b_bg_color["bg"] = bg_color[1]

    def setFontColor(self):
        font_color = askcolor(color=self.tkinter_window.font_color, title="Cor da fonte")
        if None not in font_color:
            self.tkinter_window.font_color = font_color[1]
            self.tkinter_window.b_font_color["bg"] = font_color[1]

    def setEraserBGColor(self):
        bg_color = askcolor(color=self.tkinter_window.eraser_bg_color, title="Cor de fundo")
        if None not in bg_color:
            self.tkinter_window.eraser_bg_color = bg_color[1]
            self.tkinter_window.b_eraser_bg_color["bg"] = bg_color[1]

    #forms creation/update

    def createFreeDraw(self):
        self.tkinter_window.current_draw_data = [self.tkinter_window.line_color, self.tkinter_window.e_line_thickness.get()]
        if self.tkinter_window.current_draw_data[1].isdigit() and int(self.tkinter_window.current_draw_data[1]) > 0:
            self.turtle_window.pen.pencolor(self.tkinter_window.current_draw_data[0])
            self.turtle_window.pen.pensize(int(self.tkinter_window.current_draw_data[1]))
            self.turtle_window.pen.st()
            self.turtle_window.pen.pd()
            self.turtle_window.can_drag = True
        else:
            self.turtle_window.pen.ht()
            self.turtle_window.can_drag = False
        print(self.tkinter_window.current_draw_data)

    def createRegularPolygon(self):
        if self.tkinter_window.current_draw_form == "regular polygon":
            self.tkinter_window.current_draw_data = [self.tkinter_window.e_n_sides.get(), self.tkinter_window.e_side_size.get(),
                                                     self.tkinter_window.line_color, self.tkinter_window.e_line_thickness.get(),
                                                     self.tkinter_window.bg_color]
        elif self.tkinter_window.current_draw_form == "regular eraser":
            self.tkinter_window.current_draw_data = [self.tkinter_window.e_n_sides.get(), self.tkinter_window.e_side_size.get(),
                                                     self.tkinter_window.eraser_bg_color, "1", self.tkinter_window.eraser_bg_color]
        print(self.tkinter_window.current_draw_data)

    def createCircle(self):
        if self.tkinter_window.current_draw_form == "circle":
            self.tkinter_window.current_draw_data = [self.tkinter_window.e_radius.get(), self.tkinter_window.line_color,
                                                     self.tkinter_window.e_line_thickness.get(), self.tkinter_window.bg_color]
        elif self.tkinter_window.current_draw_form == "circular eraser":
            self.tkinter_window.current_draw_data = [self.tkinter_window.e_radius.get(), self.tkinter_window.eraser_bg_color,
                                                     "1", self.tkinter_window.eraser_bg_color]
        print(self.tkinter_window.current_draw_data)

    def createRectangle(self):
        self.tkinter_window.current_draw_data = [self.tkinter_window.e_side1.get(), self.tkinter_window.e_side2.get(),
                                                 self.tkinter_window.line_color, self.tkinter_window.e_line_thickness.get(),
                                                 self.tkinter_window.bg_color]
        print(self.tkinter_window.current_draw_data)

    def createTrapezium(self):
        self.tkinter_window.current_draw_data = [self.tkinter_window.e_top_base.get(), self.tkinter_window.e_bottom_base.get(),
                                                 self.tkinter_window.e_height.get(), self.tkinter_window.line_color,
                                                 self.tkinter_window.e_line_thickness.get(), self.tkinter_window.bg_color]
        print(self.tkinter_window.current_draw_data)

    def createLozenge(self):
        self.tkinter_window.current_draw_data = [self.tkinter_window.e_height.get(), self.tkinter_window.e_width.get(),
                                                 self.tkinter_window.line_color, self.tkinter_window.e_line_thickness.get(),
                                                 self.tkinter_window.bg_color]
        print(self.tkinter_window.current_draw_data)

    def createText(self):
        self.tkinter_window.current_draw_data = [self.tkinter_window.e_text.get(), self.tkinter_window.e_font_family.get(),
                                                 self.tkinter_window.e_font_size.get(), self.tkinter_window.font_color,
                                                 self.tkinter_window.e_font_type.get(), self.tkinter_window.e_align.get()]
        print(self.tkinter_window.current_draw_data)

    def clearTurtleScreen(self):
        self.turtle_window.screen.reset()
        self.turtle_window.pen.ht()
        self.turtle_window.pen.speed(0)
        self.turtle_window.screen.bgcolor(self.tkinter_window.bg_color)


turtleWindow = TurtleWindow()
tkinterWindow = TkinterWindow()
menuWindow = MenuWindow(Tk())

menuWindow.setTkinterWindow(tkinterWindow)
menuWindow.setTurtleWindow(turtleWindow)
turtleWindow.setTkinterSource(tkinterWindow)

turtleWindow.screen.onclick(turtleWindow.onClick)
turtleWindow.pen.ondrag(turtleWindow.onDrag)

mainloop()
turtle.done()