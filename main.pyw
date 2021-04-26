import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import urllib.request

class MainApp(QMainWindow):
    """ the main class of our app """
    def __init__(self):
        """ init things here """
        super().__init__()                         # parent class initializer

        # window title
        self.title = "Google Doc Clone"
        self.setWindowTitle(self.title)
        
        # editor section
        self.editor = QTextEdit(self) 
        self.setCentralWidget(self.editor)

        # create menubar and toolbar first
        self.create_menu_bar()
        self.create_toolbar()

        # after creating toolabr we can call and select font size
        font = QFont('Times', 12)
        self.editor.setFont(font)
        self.editor.setFontPointSize(12)

        # stores path
        self.path = ''

    def create_menu_bar(self):
        menuBar = QMenuBar(self)

        """ add elements to the menubar """
        # App icon will go here
        app_icon = menuBar.addMenu(QIcon("doc_icon.png"), "icon")

        # file menu **
        file_menu = QMenu("File", self)
        menuBar.addMenu(file_menu)

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.file_save)
        file_menu.addAction(save_action)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.file_open)
        file_menu.addAction(open_action)

        rename_action = QAction('Rename', self)
        rename_action.triggered.connect(self.file_saveas)
        file_menu.addAction(rename_action)

        pdf_action = QAction("Save as PDF", self)
        pdf_action.triggered.connect(self.save_pdf)
        file_menu.addAction(pdf_action)
        

        # edit menu **
        edit_menu = QMenu("Edit", self)
        menuBar.addMenu(edit_menu)

        # paste
        paste_action = QAction('Paste', self)
        paste_action.triggered.connect(self.editor.paste)
        edit_menu.addAction(paste_action)

        # clear 
        clear_action = QAction('Clear', self)
        clear_action.triggered.connect(self.editor.clear)
        edit_menu.addAction(clear_action)

        # select all
        select_action = QAction('Select All', self)
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)

        # view menu **
        view_menu = QMenu("View", self)
        menuBar.addMenu(view_menu)

        # fullscreen
        fullscr_action = QAction('Full Screen View', self)
        fullscr_action.triggered.connect(lambda : self.showFullScreen())
        view_menu.addAction(fullscr_action)

        # normal screen
        normscr_action = QAction('Normal View', self)
        normscr_action.triggered.connect(lambda : self.showNormal())
        view_menu.addAction(normscr_action)

        # minimize
        minscr_action = QAction('Minimize', self)
        minscr_action.triggered.connect(lambda : self.showMinimized())
        view_menu.addAction(minscr_action)

        self.setMenuBar(menuBar)

    def create_toolbar(self):
        # Using a title
        ToolBar = QToolBar("Tools", self)

        # undo
        url3 = "https://cdn4.iconfinder.com/data/icons/navigation-40/24/rotate-2-512.png"
        data3 = urllib.request.urlopen(url3).read()
        pixmap3 = QPixmap()
        pixmap3.loadFromData(data3)
        
        undo_action = QAction(QIcon(pixmap3), 'Undo', self)
        undo_action.triggered.connect(self.editor.undo)
        ToolBar.addAction(undo_action)

        # redo
        url4 = "https://cdn4.iconfinder.com/data/icons/vectory-multimedia-1/40/redo_2-512.png"
        data4 = urllib.request.urlopen(url4).read()
        pixmap4 = QPixmap()
        pixmap4.loadFromData(data4)

        redo_action = QAction(QIcon(pixmap4), 'Redo', self)
        redo_action.triggered.connect(self.editor.redo)
        ToolBar.addAction(redo_action)

        # adding separator
        ToolBar.addSeparator()

        # copy
        url5 = "https://cdn3.iconfinder.com/data/icons/business-912/24/copy-512.png"
        data5 = urllib.request.urlopen(url5).read()
        pixmap5 = QPixmap()
        pixmap5.loadFromData(data5)

        copy_action = QAction(QIcon(pixmap5), 'Copy', self)
        copy_action.triggered.connect(self.editor.copy)
        ToolBar.addAction(copy_action)

        # cut 
        url6 = "https://cdn2.iconfinder.com/data/icons/picons-basic-2/57/basic2-032_scissors_cut-512.png"
        data6 = urllib.request.urlopen(url6).read()
        pixmap6 = QPixmap()
        pixmap6.loadFromData(data6)

        cut_action = QAction(QIcon(pixmap6), 'Cut', self)
        cut_action.triggered.connect(self.editor.cut)
        ToolBar.addAction(cut_action)

        # paste
        url7 = "https://cdn1.iconfinder.com/data/icons/material-core/22/content-paste-512.png"
        data7 = urllib.request.urlopen(url7).read()
        pixmap7 = QPixmap()
        pixmap7.loadFromData(data7)

        paste_action = QAction(QIcon(pixmap7), 'Paste', self)
        paste_action.triggered.connect(self.editor.paste)
        ToolBar.addAction(paste_action)

        # adding separator
        ToolBar.addSeparator()
        ToolBar.addSeparator()

        # fonts
        self.font_combo = QComboBox(self)
        self.font_combo.addItems(["Courier Std", "Hellentic Typewriter Regular", "Helvetica", "Arial", "SansSerif", "Helvetica", "Times", "Monospace"])
        self.font_combo.activated.connect(self.set_font)      # connect with function
        ToolBar.addWidget(self.font_combo) 

        # font size
        self.font_size = QSpinBox(self)   
        self.font_size.setValue(12)  
        self.font_size.valueChanged.connect(self.set_font_size)      # connect with funcion
        ToolBar.addWidget(self.font_size)

        # separator
        ToolBar.addSeparator()

        # bold
        url = "https://cdn2.iconfinder.com/data/icons/font-awesome/1792/bold-512.png"
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        bold_action = QAction(QIcon(pixmap), 'Bold', self)
        bold_action.triggered.connect(self.bold_text)
        ToolBar.addAction(bold_action)

        # underline
        url2 = "https://cdn1.iconfinder.com/data/icons/feather-2/24/underline-512.png"
        data2 = urllib.request.urlopen(url2).read()
        pixmap2 = QPixmap()
        pixmap2.loadFromData(data2)
        underline_action = QAction(QIcon(pixmap2), 'Underline', self)
        underline_action.triggered.connect(self.underline_text)
        ToolBar.addAction(underline_action)

        # italic
        url1 = "https://cdn4.iconfinder.com/data/icons/feather/24/italic-512.png"
        data1 = urllib.request.urlopen(url1).read()
        pixmap1 = QPixmap()
        pixmap1.loadFromData(data1)
        italic_action = QAction(QIcon(pixmap1), 'Italic', self)
        italic_action.triggered.connect(self.italic_text)
        ToolBar.addAction(italic_action)

        # separator
        ToolBar.addSeparator()

        # text alignment
        url8 = "https://cdn1.iconfinder.com/data/icons/feather-2/24/align-right-512.png"
        data8 = urllib.request.urlopen(url8).read()
        pixmap8 = QPixmap()
        pixmap8.loadFromData(data8)

        right_alignment_action = QAction(QIcon(pixmap8), 'Align Right', self)
        right_alignment_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignRight))
        ToolBar.addAction(right_alignment_action)

        url9 = "https://cdn1.iconfinder.com/data/icons/feather-2/24/align-left-512.png"
        data9 = urllib.request.urlopen(url9).read()
        pixmap9 = QPixmap()
        pixmap9.loadFromData(data9)

        left_alignment_action = QAction(QIcon(pixmap9), 'Align Left', self)
        left_alignment_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignLeft))
        ToolBar.addAction(left_alignment_action)

        url10 = "https://cdn2.iconfinder.com/data/icons/viiva-content-editor/32/justify-512.png"
        data10 = urllib.request.urlopen(url10).read()
        pixmap10 = QPixmap()
        pixmap10.loadFromData(data10)

        justification_action = QAction(QIcon(pixmap10), 'Center/Justify', self)
        justification_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignCenter))
        ToolBar.addAction(justification_action)

        # separator
        ToolBar.addSeparator()

        # zoom in
        url11 = "https://cdn1.iconfinder.com/data/icons/feather-2/24/zoom-in-512.png"
        data11 = urllib.request.urlopen(url11).read()
        pixmap11 = QPixmap()
        pixmap11.loadFromData(data11)

        zoom_in_action = QAction(QIcon(pixmap11), 'Zoom in', self)
        zoom_in_action.triggered.connect(self.editor.zoomIn)
        ToolBar.addAction(zoom_in_action)

        # zoom out
        url12 = "https://cdn1.iconfinder.com/data/icons/feather-2/24/zoom-out-512.png"
        data12 = urllib.request.urlopen(url12).read()
        pixmap12 = QPixmap()
        pixmap12.loadFromData(data12)

        zoom_out_action = QAction(QIcon(pixmap12), 'Zoom out', self)
        zoom_out_action.triggered.connect(self.editor.zoomOut)
        ToolBar.addAction(zoom_out_action)


        # separator
        ToolBar.addSeparator()
        
        self.addToolBar(ToolBar)

    def italic_text(self):
        # if already italic, change into normal, else italic
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not(state))

    def underline_text(self):
        # if already underlined, change into normal, else underlined
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not(state))

    def bold_text(self):
        # if already bold, make normal, else make bold
        if self.editor.fontWeight() != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)
            return
        self.editor.setFontWeight(QFont.Normal)

    def set_font(self):
        font = self.font_combo.currentText()
        self.editor.setCurrentFont(QFont(font))

    def set_font_size(self):
        value = self.font_size.value()
        self.editor.setFontPointSize(value)

        # we can also make it one liner without writing such function.
        # by using lamba function -
        # self.font_size.valueChanged.connect(self.editor.setFontPointSize(self.font_size.value()))  


    def file_open(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "All files (*.*)")

        try:
            #  if self.path.endswith(('.doc', '.docx')):
            #      text = textract.process(self.path)
            #      print(text)
            #      doc = Document(self.path)
            #      text = ''
            #      for line in doc.paragraphs:
            #          text+=line.text
            # else:
            with open(self.path, 'r') as f:
                text = f.read()
        except Exception as e:
            print(e)
        else:
            self.editor.setText(text)
            self.update_title()

    def file_save(self):
        print(self.path)
        if self.path == '':
            # If we do not have a path, we need to use Save As.
            self.file_saveas()

        text = self.editor.toPlainText()

        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def file_saveas(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "text documents (*.text);Text documents (*.txt);All files (*.*)")

        if self.path == '':
            return   # If dialog is cancelled, will return ''

        text = self.editor.toPlainText()

        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def update_title(self):
        self.setWindowTitle(self.title + ' ' + self.path)

    def save_pdf(self):
        f_name, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All files()")
        print(f_name)

        if f_name != '':  # if name not empty
           printer = QPrinter(QPrinter.HighResolution)
           printer.setOutputFormat(QPrinter.PdfFormat)
           printer.setOutputFileName(f_name)
           self.editor.document().print_(printer)
    

app = QApplication(sys.argv)
window = MainApp()
window.show()
sys.exit(app.exec_())