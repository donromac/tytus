import os
from tkinter import *
from tkinter import Menu
from tkinter import filedialog
import sys
import io
import Tytus as tytus

class GUI:
    extensionArchivo = None#guarda la extensión del archivo abierto
    nombreArchivo = None
    #constructor de la ventana
    def __init__(self):
        #cambiando enconde
        sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding='latin-1')
        #END variables utilizadas durante la ejecución
        self.window = Tk()
        #propiedades de la ventana
        self.window.title("TytusDB")
        self.window.geometry("815x950")
        self.window.configure(bg = "#3b5971")
        self.window.resizable(False, False)

        #START MENU BAR
        self.menuBar = Menu(self.window)
        self.menuBar.add_cascade(label = "Abrir CSV", command = self.abrirArchivo)
        self.menuBar.add_cascade(label = "Reportes")
        self.menuBar.add_cascade(label = "Salir", command = self.salir)
        self.window.config(menu = self.menuBar)
        #END MENU BAR
        #titulo
        self.titulo = Label(self.window, text = "TYTUS DB", font = ("Arial Bold", 25), fg="#a48f60")
        self.titulo.place(x = 320, y = 5)
        self.titulo.configure(bg = "#3b5971")
        #loadCSV()
        self.loadCSV = Label(self.window, text = "loadCSV", font = ("Arial"), fg="#ffffff")
        self.loadCSV.place(x = 35, y = 75)
        self.loadCSV.configure(bg = "#3b5971")
        self.e1LoadCSV = Entry(self.window)
        self.e1LoadCSV.place(x=170, y=78)
        self.e1LoadCSV.configure(bg = "#f2f2f2")
        self.e2LoadCSV = Entry(self.window)
        self.e2LoadCSV.place(x=320, y=78)
        self.e2LoadCSV.configure(bg = "#f2f2f2")
        self.e3LoadCSV = Entry(self.window)
        self.e3LoadCSV.place(x=470, y=78)
        self.e3LoadCSV.configure(bg = "#f2f2f2")
        self.btnloadCSV = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : tytus.loadCSV(self.e1LoadCSV.get(), self.e2LoadCSV.get(), self.e3LoadCSV.get()))
        self.btnloadCSV.place(x=620, y = 75)
        
        #createTable()
        self.createTable = Label(self.window, text = "createTable", font = ("Arial"), fg="#ffffff")
        self.createTable.place(x = 35, y = 145)
        self.createTable.configure(bg = "#3b5971")
        self.e1createTable = Entry(self.window)
        self.e1createTable.place(x=170, y=148)
        self.e1createTable.configure(bg = "#f2f2f2")
        self.e2createTable = Entry(self.window)
        self.e2createTable.place(x=320, y=148)
        self.e2createTable.configure(bg = "#f2f2f2")
        self.e3createTable= Entry(self.window)
        self.e3createTable.place(x=470, y=148)
        self.e3createTable.configure(bg = "#f2f2f2")
        self.btncreateTable = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : tytus.createTable(self.e1createTable.get(), self.e2createTable.get(), self.e3createTable.get())) 
        self.btncreateTable.place(x=620, y = 145)

        #showTables()
        self.showTables = Label(self.window, text = "showTables", font = ("Arial"), fg="#ffffff")
        self.showTables.place(x = 35, y = 180)
        self.showTables.configure(bg = "#3b5971")
        self.e1showTables = Entry(self.window)
        self.e1showTables.place(x=170, y=183)
        self.e1showTables.configure(bg = "#f2f2f2")
        self.btnshowTables = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : print(tytus.showTables(self.e1showTables.get())))
        self.btnshowTables.place(x=620, y = 180)

        #alterTable()
        self.alterTable = Label(self.window, text = "alterTable", font = ("Arial"), fg="#ffffff")
        self.alterTable.place(x = 35, y = 215)
        self.alterTable.configure(bg = "#3b5971")
        self.e1alterTable = Entry(self.window)
        self.e1alterTable.place(x=170, y=218)
        self.e1alterTable.configure(bg = "#f2f2f2")
        self.e2alterTable = Entry(self.window)
        self.e2alterTable.place(x=320, y=218)
        self.e2alterTable.configure(bg = "#f2f2f2")
        self.e3alterTable= Entry(self.window)
        self.e3alterTable.place(x=470, y=218)
        self.e3alterTable.configure(bg = "#f2f2f2")
        self.btnalterTable = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : tytus.alterTable(self.e1alterTable.get(), self.e2alterTable.get(), self.e3alterTable.get()))
        self.btnalterTable.place(x=620, y = 217)

        #dropTable()
        self.dropTable = Label(self.window, text = "dropTable", font = ("Arial"), fg="#ffffff")
        self.dropTable.place(x = 35, y = 250)
        self.dropTable.configure(bg = "#3b5971")
        self.e1dropTable = Entry(self.window)
        self.e1dropTable.place(x=170, y=253)
        self.e1dropTable.configure(bg = "#f2f2f2")
        self.e2dropTable = Entry(self.window)
        self.e2dropTable.place(x=320, y=253)
        self.e2dropTable.configure(bg = "#f2f2f2")
        self.btndropTable = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda: tytus.dropTable(self.e1dropTable.get(), self.e2dropTable.get()))
        self.btndropTable.place(x=620, y = 250)

        #alterAddPK()
        self.alterAddPK = Label(self.window, text = "alterAddPK", font = ("Arial"), fg="#ffffff")
        self.alterAddPK.place(x = 35, y = 285)
        self.alterAddPK.configure(bg = "#3b5971")
        self.e1alterAddPK = Entry(self.window)
        self.e1alterAddPK.place(x=170, y=288)
        self.e1alterAddPK.configure(bg = "#f2f2f2")
        self.e2alterAddPK = Entry(self.window)
        self.e2alterAddPK.place(x=320, y=288)
        self.e2alterAddPK.configure(bg = "#f2f2f2")
        self.e3alterAddPK = Entry(self.window)
        self.e3alterAddPK.place(x=470, y=288)
        self.e3alterAddPK.configure(bg = "#f2f2f2")
        self.btnalterAddPK = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : tytus.alterAddPK(self.e1alterAddPK.get(), self.e2alterAddPK.get(), self.e3alterAddPK.get()))
        self.btnalterAddPK.place(x=620, y = 285)
        
        #alterDropPK()
        self.alterDropPK = Label(self.window, text = "alterDrop", font = ("Arial"), fg="#ffffff")
        self.alterDropPK.place(x = 35, y = 320)
        self.alterDropPK.configure(bg = "#3b5971")
        self.e1alterDropPK = Entry(self.window)
        self.e1alterDropPK.place(x=170, y=323)
        self.e1alterDropPK.configure(bg = "#f2f2f2")
        self.e2alterDropPK = Entry(self.window)
        self.e2alterDropPK.place(x=320, y=323)
        self.e2alterDropPK.configure(bg = "#f2f2f2")
        self.btnalterDropPK = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : tytus.alterDropPk(self.e1alterDropPK.get(), self.e2alterDropPK.get()))
        self.btnalterDropPK.place(x=620, y = 320)

        #extractTable()
        self.extractTable = Label(self.window, text = "extractTable", font = ("Arial"), fg="#ffffff")
        self.extractTable.place(x = 35, y = 355)
        self.extractTable.configure(bg = "#3b5971")
        self.e1extractTable = Entry(self.window)
        self.e1extractTable.place(x=170, y=358)
        self.e1extractTable.configure(bg = "#f2f2f2")
        self.e2extractTable = Entry(self.window)
        self.e2extractTable.place(x=320, y=358)
        self.e2extractTable.configure(bg = "#f2f2f2")
        self.btnextractTable = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : tytus.extractTable(self.e1extractTable.get(), self.e2extractTable.get()))
        self.btnextractTable.place(x=620, y = 355)

        #insert()
        self.insert = Label(self.window, text = "insert", font = ("Arial"), fg="#ffffff")
        self.insert.place(x = 35, y = 390)
        self.insert.configure(bg = "#3b5971")
        self.e1insert = Entry(self.window)
        self.e1insert.place(x=170, y=393)
        self.e1insert.configure(bg = "#f2f2f2")
        self.e2insert = Entry(self.window)
        self.e2insert.place(x=320, y=393)
        self.e2insert.configure(bg = "#f2f2f2")
        self.e3insert= Entry(self.window)
        self.e3insert.place(x=470, y=393)
        self.e3insert.configure(bg = "#f2f2f2")
        self.btninsert = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : tytus.insert(self.e1insert.get(), self.e2insert.get(), self.e3insert.get()))
        self.btninsert.place(x=620, y = 390)

        #update()
        self.update = Label(self.window, text = "update", font = ("Arial"), fg="#ffffff")
        self.update.place(x = 35, y = 425)
        self.update.configure(bg = "#3b5971")
        self.e1update = Entry(self.window)
        self.e1update.place(x=170, y=428)
        self.e1update.configure(bg = "#f2f2f2")
        self.e2update = Entry(self.window)
        self.e2update.place(x=320, y=428)
        self.e2update.configure(bg = "#f2f2f2")
        self.e3update= Entry(self.window)
        self.e3update.place(x=470, y=428)
        self.e3update.configure(bg = "#f2f2f2")
        self.e4update = Entry(self.window)
        self.e4update.place(x=170, y=463)
        self.e4update.configure(bg = "#f2f2f2")
        self.btnupdate = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda: tytus.update(self.e1update.get(), self.e2update.get(), self.e3update.get(), self.e4update.get()))
        self.btnupdate.place(x=620, y = 425)
        
        #delete()
        self.delete = Label(self.window, text = "delete", font = ("Arial"), fg="#ffffff")
        self.delete.place(x = 35, y = 495)
        self.delete.configure(bg = "#3b5971")
        self.e1delete = Entry(self.window)
        self.e1delete.place(x=170, y=498)
        self.e1delete.configure(bg = "#f2f2f2")
        self.e2delete = Entry(self.window)
        self.e2delete.place(x=320, y=498)
        self.e2delete.configure(bg = "#f2f2f2")
        self.e3delete = Entry(self.window)
        self.e3delete.place(x=470, y=498)
        self.e3delete.configure(bg = "#f2f2f2")
        self.btndelete = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda: tytus.delete(self.e1delete.get(), self.e2delete.get(), self.e3delete.get()))
        self.btndelete.place(x=620, y = 495)

        #truncate()
        self.truncate = Label(self.window, text = "truncate", font = ("Arial"), fg="#ffffff")
        self.truncate.place(x = 35, y = 530)
        self.truncate.configure(bg = "#3b5971")
        self.e1truncate = Entry(self.window)
        self.e1truncate.place(x=170, y=533)
        self.e1truncate.configure(bg = "#f2f2f2")
        self.e2truncate = Entry(self.window)
        self.e2truncate.place(x=320, y=533)
        self.e2truncate.configure(bg = "#f2f2f2")
        self.btntruncate = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : tytus.truncate(self.e1truncate.get(), self.e2truncate.get()))
        self.btntruncate.place(x=620, y = 530)

        #extractRow
        self.extractRow = Label(self.window, text = "extractRow", font = ("Arial"), fg="#ffffff")
        self.extractRow.place(x = 35, y = 565)
        self.extractRow.configure(bg = "#3b5971")
        self.e1extractRow = Entry(self.window)
        self.e1extractRow.place(x=170, y=568)
        self.e1extractRow.configure(bg = "#f2f2f2")
        self.e2extractRow = Entry(self.window)
        self.e2extractRow.place(x=320, y=568)
        self.e2extractRow.configure(bg = "#f2f2f2")
        self.e3extractRow= Entry(self.window)
        self.e3extractRow.place(x=470, y=568)
        self.e3extractRow.configure(bg = "#f2f2f2")
        self.btnextractRow = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : tytus.extractRow(self.e1extractRow.get(), self.e2extractRow.get(), self.e3extractRow.get()))
        self.btnextractRow.place(x=620, y = 565)

        #createDatabase()
        self.createDatabase = Label(self.window, text = "createDatabase", font = ("Arial"), fg="#ffffff")
        self.createDatabase.place(x = 35, y = 600)
        self.createDatabase.configure(bg = "#3b5971")
        self.e1createDatabase = Entry(self.window)
        self.e1createDatabase.place(x=170, y=603)
        self.e1createDatabase.configure(bg = "#f2f2f2")
        self.btncreateDatabase = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff" , command= lambda: tytus.createDatabase(self.e1createDatabase.get()))
        self.btncreateDatabase.place(x=620, y = 600)

        #showDatabases()
        self.showDatabases = Label(self.window, text = "showDatabases", font = ("Arial"), fg="#ffffff")
        self.showDatabases.place(x = 35, y = 635)
        self.showDatabases.configure(bg = "#3b5971")
        self.btnshowDatabases = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : print(tytus.showDatabases()))
        self.btnshowDatabases.place(x=620, y = 635)

        #alterDatabase()
        self.alterDatabases = Label(self.window, text = "alterDatabases", font = ("Arial"), fg="#ffffff")
        self.alterDatabases.place(x = 35, y = 670)
        self.alterDatabases.configure(bg = "#3b5971")
        e1alterDatabases = self.e1alterDatabases = Entry(self.window)
        self.e1alterDatabases.place(x=170, y=673)
        self.e1alterDatabases.configure(bg = "#f2f2f2")
        e2alterDatabases = self.e2alterDatabases = Entry(self.window)
        self.e2alterDatabases.place(x=320, y=673)
        self.e2alterDatabases.configure(bg = "#f2f2f2")
        self.btnalterDatabase = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda : tytus.alterDatabase(e1alterDatabases.get(), e2alterDatabases.get()))
        self.btnalterDatabase.place(x=620, y = 670)

        #dropDatabase()
        self.dropDatabase = Label(self.window, text = "dropDatabase", font = ("Arial"), fg="#ffffff")
        self.dropDatabase.place(x = 35, y = 705)
        self.dropDatabase.configure(bg = "#3b5971")
        self.e1dropDatabase = Entry(self.window)
        self.e1dropDatabase.place(x=170, y=708)
        self.e1dropDatabase.configure(bg = "#f2f2f2")
        self.btndropDatabase = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda: print(tytus.dropDatabase(self.e1dropDatabase.get())))
        self.btndropDatabase.place(x=620, y = 705)

        #alterAddColumn()
        self.alterAddColumn = Label(self.window, text = "alterAddColumn", font = ("Arial"), fg="#ffffff")
        self.alterAddColumn.place(x = 35, y = 740)
        self.alterAddColumn.configure(bg = "#3b5971")
        self.e1alterAddColumn = Entry(self.window)
        self.e1alterAddColumn.place(x=170, y=743)
        self.e1alterAddColumn.configure(bg = "#f2f2f2")
        self.e2alterAddColumn = Entry(self.window)
        self.e2alterAddColumn.place(x=320, y=743)
        self.e2alterAddColumn.configure(bg = "#f2f2f2")
        self.e3alterAddColumn = Entry(self.window)
        self.e3alterAddColumn.place(x=470, y=743)
        self.e3alterAddColumn.configure(bg = "#f2f2f2")
        self.btnalterAddColumn = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command= lambda: tytus.alterAddColumn(self.e1alterAddColumn.get(), self.e2alterAddColumn.get(), self.e3alterAddColumn.get()))
        self.btnalterAddColumn.place(x=620, y = 740)

        #alterDropColumn
        self.alterDropColumn = Label(self.window, text = "alterDropColumn", font = ("Arial"), fg="#ffffff")
        self.alterDropColumn.place(x = 35, y = 775)
        self.alterDropColumn.configure(bg = "#3b5971")
        self.e1alterDropColumn = Entry(self.window)
        self.e1alterDropColumn.place(x=170, y=778)
        self.e1alterDropColumn.configure(bg = "#f2f2f2")
        self.e2alterDropColumn = Entry(self.window)
        self.e2alterDropColumn.place(x=320, y=778)
        self.e2alterDropColumn.configure(bg = "#f2f2f2")
        self.e3alterDropColumn = Entry(self.window)
        self.e3alterDropColumn.place(x=470, y=778)
        self.e3alterDropColumn.configure(bg = "#f2f2f2")  
        self.btnalterDropColumn = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command= lambda: tytus.alterDropColumn(self.e1alterDropColumn.get(), self.e2alterDropColumn.get(), self.e3alterDropColumn.get()))
        self.btnalterDropColumn.place(x=620, y = 775)
        
        #extractRangeTable()
        self.extractRangeTable = Label(self.window, text = "extractRangeTable", font = ("Arial"), fg="#ffffff")
        self.extractRangeTable.place(x = 35, y = 810)
        self.extractRangeTable.configure(bg = "#3b5971")
        self.e1extractRangeTable = Entry(self.window)
        self.e1extractRangeTable.place(x=170, y=813)
        self.e1extractRangeTable.configure(bg = "#f2f2f2")
        self.e2extractRangeTable = Entry(self.window)
        self.e2extractRangeTable.place(x=320, y=813)
        self.e2extractRangeTable.configure(bg = "#f2f2f2")
        self.e3extractRangeTable = Entry(self.window)
        self.e3extractRangeTable.place(x=470, y=813 )
        self.e3extractRangeTable.configure(bg = "#f2f2f2")  
        self.e4extractRangeTable = Entry(self.window)
        self.e4extractRangeTable.place(x=170, y=848)
        self.e4extractRangeTable.configure(bg = "#f2f2f2")  
        self.btnextractRangeTable = Button(self.window, text="Ejecutar", width=20, bg = "#a48f60", fg="#ffffff", command=lambda: tytus.extractRangeTable(self.e1extractRangeTable.get(), self.e2extractRangeTable.get(), self.e3extractRangeTable.get(), self.e4extractRangeTable.get()))
        self.btnextractRangeTable.place(x=620, y = 845)


        #lanza la ventana (la muestra en pantalla)
        self.window.mainloop()















    #Permite abrir un archivo de texto y mostrar su contenido en el ScrolledText de entrada
    def abrirArchivo(self):
        nameFile = filedialog.askopenfilename(title="Abrir", filetypes=(("Arvhivos csv", "*.csv"), ("Todos los archivos", "*.*")))
        extension = os.path.splitext(nameFile)
        self.extensionArchivo = extension[1] #guarda la extension del archivo cargado al ScrolledText
        # nombre del archivo
        nombre = os.path.split(nameFile)
        self.nombreArchivo = nombre[1]
        if nameFile != '':
            archivo = open(nameFile, "r", encoding="utf-8")
            contenido = archivo.read()
            archivo.close()
            print(contenido)

    #Cierra la ventana
    def salir(self):
        self.window.destroy()






#inicia la clase GUI
start = GUI()
