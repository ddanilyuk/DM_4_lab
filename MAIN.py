from tkinter import *
import random
import networkx as nx
import pylab as pl


# БРОВЧЕНКО
class Lab4:

    def create_tabl_random(self, n):
        self.tabl = []
        for i in range(n):
            self.tabl.append([])
            for j in range(n):
                self.tabl[i].append(random.randint(0, 1))
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.tabl[i][j] = 0
                else:
                    self.tabl[i][j] = self.tabl[j][i]
        return self.tabl

    def student(self, nzk=8208):
        self.slave = Toplevel(self.root)
        self.slave.title('Student')
        self.slave.focus_set()
        self.slave.minsize(300, 100)
        self.slave.maxsize(300, 100)
        self.slave['bg'] = 'seashell'
        self.slave.wm_geometry("+600+250")
        Label(self.slave, text='Данилюк Денис\n'
                               'група ІВ-82\n'
                               'варіант {}'.format(divmod(nzk, 6)[1] + 1),
              justify=LEFT, font="Arial 17 bold", bg='seashell').pack(fill='both')

    def getMatrix(self):
        self.slave = Toplevel(self.root)
        self.slave.title('Student')
        self.slave.focus_set()
        self.slave.minsize(300, 100)
        self.slave.maxsize(300, 100)
        self.slave['bg'] = 'seashell'
        self.slave.wm_geometry("+600+250")
        a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def GraphColoring(self, matrix, nodes):

        ####################

        ####################
        """
        def SortEdges():
            sort_list = {}
            for key in Edges:
                sort_list[key] = len(Edges[key])
            sort2 = sorted(sort_list.items(), key=lambda x: x[1], reverse=True)

            return sort2

        def colorize():
            for key in range(4):
                w = {'red'}
                # print(key)

                for i in range(key+1):
                    if matrix
                    w.add(colors[i])
                print(w)
                some_i = 0
                curcol = colors[some_i]
                # curcol = 0
                while True:
                    some_i += 1

                    # curcol += 1
                    # print(curcol)
                    print("before break")

                    if colors[some_i] not in w:
                        print("break")
                        break
                print(curcol)

                print(curcol)
                print("===")
                result[key + 1] = colors[some_i-1]
            return result
        """
        n = nodes
        a = matrix
        colors = ['red', 'blue', 'yellow', 'green', 'orange', 'springgreen', 'lime', 'olive', 'indigo', 'fuchsia']

        colarr = [0 for i in range(n)]
        print(a)

        def colorize(i):
            if i == n:
                print("stop")
            else:
                # Функція вибору фарби для розфарбування вершини з номером
                w = {0}
                print(i)
                for j in range(i):
                    if int(a[j][i]) > 0:
                        w.add(colarr[j])
                print(w)

                curcol = 0
                while True:
                    curcol += 1
                    if curcol not in w:
                        break
                colarr[i] = curcol
                return colorize(i + 1)

        colorize(0)
        color_dict = {a + 1: colors[colarr[a] - 1] for a in range(n)}
        return color_dict

    def main_window(self):
        self.root = Tk()
        self.root.minsize(700, 300)
        self.root.maxsize(700, 300)
        self.root.title('Завдання (лабораторна №4)')

        def but_bind():
            if len(self.e.get()) == 0:
                Label(self.root, text='*задайте спершу кількість вершин графа', fg='red', font='Arial 12', ) \
                    .grid(column=1, row=4, columnspan=2)
            else:
                self.window2()

        def but_bind_2():
            n = 10
            colarr = [0 for i in range(n)]
            #     1  2  3  4  5  6  7  8  9  10
            a = [[0, 0, 1, 0, 0, 1, 1, 0, 0, 0],  # 1
                 [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],  # 2
                 [1, 1, 0, 1, 0, 0, 0, 0, 1, 0],  # 3
                 [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],  # 4
                 [0, 0, 0, 1, 0, 0, 0, 0, 1, 1],  # 5
                 [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 6
                 [1, 1, 0, 0, 0, 1, 0, 1, 0, 0],  # 7
                 [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],  # 8
                 [0, 0, 1, 1, 1, 0, 0, 1, 0, 1],  # 9
                 [0, 0, 0, 0, 1, 0, 0, 0, 1, 0]]  # 10


            def colorize(i):
                if i == n:
                    print("stop")
                else:
                    # Функція вибору фарби для розфарбування вершини з номером
                    w = {0}
                    print(i)
                    for j in range(i):
                        if int(a[j][i]) > 0:
                            w.add(colarr[j])
                    print(w)

                    curcol = 0
                    while True:
                        curcol += 1
                        if curcol not in w:
                            break
                    colarr[i] = curcol
                    return colorize(i + 1)

            colorize(0)

            def make_graf(matrix, png, colors):
                fig = pl.plt.figure()
                graf = nx.Graph()
                for i in range(1, len(matrix) + 1):
                    graf.add_node(i)
                for i in range(len(matrix)):
                    for j in range(len(matrix[1])):
                        if a[i][j] == 1:
                            graf.add_edge(i + 1, j + 1)
                nx.draw(graf, pos=nx.shell_layout(graf))
                print(graf)
                list_color = ['red', 'blue', 'yellow', 'green', 'orange', 'springgreen', 'lime', 'olive', 'indigo',
                              'fuchsia']

                for i in set(colors):
                    nodlist = []
                    for nod in range(n):
                        print(colors)
                        if colors[nod] == i:
                            nodlist.append(nod+1)
                    nx.draw(graf, pos=nx.shell_layout(graf), node_color=list_color[i - 1], nodelist=nodlist,
                            with_labels=True)
                pl.plt.show()
                fig.savefig(png)

            make_graf(a, 'file.png', colarr)

        Label(self.root, text='Завдання', font='Arial 16 bold').grid(column=1, row=1)
        Label(self.root, text='Набути теоретичні знання по темі «Розфарбування графів». \n'
                              'Створити програму розфарбування графів, яка реалізує \n'
                              'евристичний алгоритм розфарбування.',
              font='Arial 16', bg='ghostwhite', wraplength=800, justify=LEFT, padx=10).grid(column=1, row=2,
                                                                                            columnspan=4)
        Label(self.root, text='Кількість вершин графа  ', font='Arial 14', pady=20, justify=RIGHT).grid(column=1, row=3,
                                                                                                        sticky=E)
        self.e = Entry(self.root, width=5, font='Arial 14')
        self.e.grid(column=2, row=3, sticky=W)
        Button(self.root, text='Задати матрицю суміжності', font='Arial 12', bg='lightblue', command=but_bind).grid(
            column=3, row=3)
        Button(self.root, text='Завдання за варіантом', font='Arial 12', bg='lightblue', command=but_bind_2).grid(
            column=3, row=5)
        Button(self.root, text='Студент', font='Arial 12 bold', command=self.student, bg='azure').grid(column=1, row=5)

        self.root.mainloop()

    def window2(self):
        self.slave2 = Toplevel(self.root)
        self.slave2.title('Задати матрицю суміжності')
        self.slave2.focus_set()
        self.slave2.minsize(400, 400)

        def random_gen():
            tabl = self.create_tabl_random(int(self.e.get()))
            for i in range(int(self.e.get())):
                for j in range(int(self.e.get())):
                    self.list_ent[i][j].insert(END, tabl[i][j])

        for i in range(int(self.e.get()) + 1):
            for j in range(int(self.e.get()) + 1):
                if i == 0:
                    Label(self.slave2, text='{}'.format(j), font='Arial 16 bold', width=3).grid(column=j, row=i,
                                                                                                sticky=W)
                elif j == 0:
                    Label(self.slave2, text='{}'.format(i), font='Arial 16 bold', width=3).grid(column=j, row=i,
                                                                                                sticky=W)
                elif i == 0 and j == 0:
                    Label(self.slave2, text=' ', width=3).grid(column=j, row=i, sticky=W)
        self.list_ent = []
        for i in range(int(self.e.get())):
            self.list_ent.append([])
            for j in range(int(self.e.get())):
                self.list_ent[i].append(Entry(self.slave2, font='Arial 14', width=3))
                self.list_ent[i][j].grid(row=i + 1, column=j + 1, sticky=W)

        Label(self.slave2, text='   ').grid(column=2, columnspan=5, row=int(self.e.get()) + 1)
        Button(self.slave2, text='Згенерувати випадково', font='Arial 12', bg='mintcream', command=random_gen) \
            .grid(column=0, columnspan=5, row=int(self.e.get()) + 2)
        Button(self.slave2, text='Показати граф', font='Arial 12', bg='mintcream', width=15, command=self.show_gr) \
            .grid(column=5, row=int(self.e.get()) + 2, columnspan=6)
        Button(self.slave2, text='Показати розфарбований граф', font='Arial 12', bg='mintcream', width=30,
               command=self.show_colored_gr) \
            .grid(column=5, row=int(self.e.get()) + 3, columnspan=6)

    def show_gr(self):
        self.tabl = []
        for i in range(int(self.e.get())):
            self.tabl.append([])
            for j in range(int(self.e.get())):
                self.tabl[i].append(self.list_ent[i][j].get())
        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                if self.tabl[i][i] not in ['0', '1']:
                    Label(self.slave2, text='*перевірте таблицю суміжності\n'
                                            'неправильно введені дані', font='Arial 12', fg='red') \
                        .grid(column=0, row=int(self.e.get()) + 3, columnspan=5)
                    pass

        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                self.list_ent[i][j]['state'] = DISABLED

        pl.figure('Заданий граф')
        self.gr = nx.Graph()
        for i in range(int(self.e.get())):
            self.gr.add_node(i + 1)
        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                if self.tabl[i][j] != '0':
                    self.gr.add_edge(i + 1, j + 1)
        pos = nx.circular_layout(self.gr)
        nx.draw_networkx(self.gr, pos)
        pl.axis('off')
        pl.show()

    def show_colored_gr(self):
        self.tabl = []
        for i in range(int(self.e.get())):
            self.tabl.append([])
            for j in range(int(self.e.get())):
                self.tabl[i].append(self.list_ent[i][j].get())
        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                if self.tabl[i][i] not in ['0', '1']:
                    Label(self.slave2, text='*перевірте таблицю суміжності\n'
                                            'неправильно введені дані', font='Arial 12', fg='red') \
                        .grid(column=1, row=int(self.e.get()) + 3, columnspan=5)
                    pass

        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                self.list_ent[i][j]['state'] = DISABLED

        Edges = dict()
        for i in range(int(self.e.get())):
            edge_list = []
            for j in range(int(self.e.get())):
                if self.tabl[i][j] == '1':
                    edge_list.append(j + 1)
            Edges[i + 1] = edge_list

        pl.figure('Розфарбований граф')
        self.gr = nx.Graph()
        for i in range(int(self.e.get())):
            self.gr.add_node(i + 1)
        for i in range(int(self.e.get())):
            for j in range(int(self.e.get())):
                if self.tabl[i][j] != '0':
                    self.gr.add_edge(i + 1, j + 1)
        pos = nx.circular_layout(self.gr)
        node_colors = Lab4.GraphColoring(self, self.tabl, int(self.e.get())).items()
        nx.draw_networkx(self.gr, pos)
        for i in node_colors:
            nx.draw_networkx(self.gr, pos, nodelist=[i[0]], node_color=i[1])
        pl.axis('off')
        pl.show()


a = Lab4()
a.main_window()