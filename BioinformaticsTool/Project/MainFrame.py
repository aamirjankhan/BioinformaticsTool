import sys
from PyQt5.QtWidgets import *
from Project.Functions import Function1
from Project.Function2 import Function2
from Allignment import Allignment_




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MPL BIOINFORMATICS TOOL")
        self.setGeometry(500,200,550,550)
        self.UI()

    def UI(self):
        ############layouts###########
        hbox=QHBoxLayout()
        vbox=QVBoxLayout()
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()
        gridlayout=QGridLayout()
        self.editor1=QTextEdit(self)
        self.editor1.setPlaceholderText("4. Input data here...")
        self.editor2=QTextEdit(self)
        self.editor2.setPlaceholderText("5. Output data will be shown here...")
        self.path1=QLineEdit(self)
        self.path1.setPlaceholderText("1. Enter path of first fasta file .faa format")
        self.path2=QLineEdit(self)
        self.path2.setPlaceholderText("2. Enter path of second fasta file .faa format")
        self.path3=QLineEdit(self)
        self.path3.setPlaceholderText("3. Enter path for any other file...")
        fileButton=QPushButton("Open File")
        fileButton.clicked.connect(self.openFile)
        alignButton=QPushButton("Align")
        alignButton.clicked.connect(self.alignSequences)
        self.combo2=QComboBox(self)
        self.combo2.addItems(["Global Alignment","Local Alignment"])
        fontButton=QPushButton("Change Font")
        fontButton.clicked.connect(self.changeFont)
        colorButton=QPushButton("Change Color")
        colorButton.clicked.connect(self.changeColor)
        ToProtein=QPushButton("To Ptotein")
        ToProtein.clicked.connect(self.convertToProtein)
        self.combo=QComboBox(self)
        self.combo.addItems(["FFrame1","FFrame2","FFrame3","RFrame1","RFrame2","RFrame3"])
        reverse_Dna=QPushButton("Reverse DNA")
        reverse_Dna.clicked.connect(self.reverseDNA)
        compliment_Dna=QPushButton("Compliment DNA")
        compliment_Dna.clicked.connect(self.getCompliment)
        reverse_Compliment=QPushButton("Reverse Compliment")
        reverse_Compliment.clicked.connect(self.getReverseCompliment)
        GC_Content=QPushButton("GC Content")
        GC_Content.clicked.connect(self.getGCContent)
        GC_Skew=QPushButton("GC Skew")
        GC_Skew.clicked.connect(self.getGCSkewContent)
        To_RNA=QPushButton("To RNA")
        To_RNA.clicked.connect(self.toRna)
        exitButton=QPushButton("Exit")
        exitButton.clicked.connect(self.exitFunc)
        ############menubar###########
        vbox.addWidget(self.path1)
        vbox.addWidget(self.path2)
        vbox.addWidget(self.path3)
        vbox.addWidget(self.editor1)
        vbox.addWidget(self.editor2)



        gridlayout.addWidget(fileButton,0,0)
        hbox2.addWidget(alignButton)
        hbox2.addWidget(self.combo2)
        gridlayout.addLayout(hbox2,0,1)
        gridlayout.addWidget(colorButton,0,2)
        gridlayout.addWidget(fontButton,1,0)
        hbox1.addWidget(ToProtein)
        hbox1.addWidget(self.combo)
        gridlayout.addLayout(hbox1,1,1)
        gridlayout.addWidget(reverse_Dna,1,2)
        gridlayout.addWidget(compliment_Dna,2,0)
        gridlayout.addWidget(reverse_Compliment,2,1)
        gridlayout.addWidget(GC_Content,2,2)
        gridlayout.addWidget(GC_Skew,3,0)
        gridlayout.addWidget(To_RNA,3,1)
        gridlayout.addWidget(exitButton,3,2)
        hbox.addLayout(gridlayout)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.show()

    def exitFunc(self):
        mbox=QMessageBox.information(self,"Warning","Are you sure to exit?",QMessageBox.Yes|QMessageBox.No| QMessageBox.Cancel,QMessageBox.No)
        if mbox==QMessageBox.Yes:
            sys.exit()

    def openFile(self):
        url = QFileDialog.getOpenFileName(self,"Open a file","","All Files(*);;*txt;;*pdb;;*py;;*csv;;*faa")
        print(url)
        fileUrl=url[0]
        print(fileUrl)
        file =open(fileUrl,'r')
        content = file.read()
        self.editor1.setText(content)

    def alignSequences(self):
        file1=self.path1.text()
        file2=self.path2.text()
        value=self.combo2.currentText()
        mbox1=QMessageBox()
        if value == "Global Alignment":
            if Allignment_.pairwise_align_global(file1,file2) == 'Fatal':
                mbox1.information(self,'Error','File not Found in Box1 or Box2!!!')
            else:
                _,align = Allignment_.pairwise_align_global(file1,file2)
                self.editor2.setText(align)

        elif value == "Local Alignment":
            if Allignment_.pairwise_align_local(file1,file2) == 'Fatal':
                mbox1.information(self,'Error','File not Found in Box1 or Box2!!!')
            else:
                _,align = Allignment_.pairwise_align_local(file1,file2)
                self.editor2.setText(align)



    def changeFont(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.editor1.setCurrentFont(font)
            self.editor2.setCurrentFont(font)

    def changeColor(self):
        color=QColorDialog.getColor()
        self.editor1.setTextColor(color)
        self.editor2.setTextColor(color)

    def convertToProtein(self):
        mbox1=QMessageBox()
        try:
            file=self.path3.text()
            fr=open(file,'r').read().split('\n')
            dna="".join(fr)
            rdna=dna[::-1]
            selected_DNA=""
            value=self.combo.currentText()
            if value == "FFrame1":
                selected_DNA=dna
            elif value == "FFrame2":
                selected_DNA=dna[1:]
            elif value == "FFrame3":
                selected_DNA=dna[2:]
            elif value == "RFrame1":
                selected_DNA=rdna
            elif value == "RFrame2":
                selected_DNA=rdna[1:]
            elif value == "RFrame3":
                selected_DNA=rdna[2:]
            protein=Function2.ConvertToProtein(selected_DNA)
            self.editor2.setText(protein)
        except FileNotFoundError:
            mbox1.information(self,'Error','File not found in Box3!!!')


    def reverseDNA(self):
        mbox1=QMessageBox()
        dna = self.editor1.toPlainText()
        if dna == "":
            mbox1.information(self,'Information','Enter something in Box4!!!')
        else:
            self.editor2.setText(Function1.ReverseDna(dna))

    def getCompliment(self):
        mbox1=QMessageBox()
        dna = self.editor1.toPlainText()
        if dna == "":
            mbox1.information(self,'Information','Enter something in Box4!!!')
        else:
            self.editor2.setText(Function1.ComplimentDna(dna))

    def getReverseCompliment(self):
        mbox1=QMessageBox()
        dna = self.editor1.toPlainText()
        if dna == "":
            mbox1.information(self,'Information','Enter something in Box4!!!')
        else:
            self.editor2.setText(Function1.reverseComplimentDna(dna))

    def getGCContent(self):
        mbox1=QMessageBox()
        dna = self.editor1.toPlainText()
        if dna == "":
            mbox1.information(self,'Information','Enter something in Box4!!!')
        else:
            gc=Function1.GC_Content(dna)
            self.editor2.setText("GC content is: "+str(gc))

    def getGCSkewContent(self):
        mbox1=QMessageBox()
        dna = self.editor1.toPlainText()
        if dna == "":
            mbox1.information(self,'Information','Enter something in Box4!!!')
        else:
            gc=Function1.GC_Content(dna)
            self.editor2.setText("GC content is: "+str(gc))
            gc=Function1.GC_SkewContent(dna)
            self.editor2.setText("GC skew content is: "+str(gc))

    def toRna(self):
        mbox1=QMessageBox()
        dna = self.editor1.toPlainText()
        if dna == "":
            mbox1.information(self,'Information','Enter something in Box4!!!')
        else:
            gc=Function1.GC_Content(dna)
            self.editor2.setText("GC content is: "+str(gc))
            self.editor2.setText(Function1.ToRna(dna))







def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()
