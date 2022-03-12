from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys 

def getMainWindow():
    mw=QMainWindow()
    mw.setWindowTitle('测试')
    mw.resize(400,300)

    cw=QWidget()
    hl=QHBoxLayout()
    
    label=QLabel('标签')
    font=label.font()
    font.setPointSize(30)
    label.setFont(font)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter )
    hl.addWidget(label)

    cb=QComboBox()
    cb.addItems(['1','3','4'])
    #cb.currentIndexChanged.connect(lambda x: label.setNum(x))
    cb.currentTextChanged.connect(lambda x: label.setText(x))
    cb.textHighlighted.connect(lambda x:print(x,' is hilighted'))
    hl.addWidget(cb)

    def showdlg():
        dlg=QDialog(mw)
        dlg.setWindowTitle('对话框')
        print(dlg.exec())
        
    bt1=QPushButton('打开')
    bt1.clicked.connect(showdlg)
    hl.addWidget(bt1)

    cw.setLayout(hl)
    mw.setCentralWidget(cw)

    
    toolbar=QToolBar('this')
    
    mw.addToolBar(toolbar)

    def doac1(s):
        print('action 1:',s)
    ac1=QAction(QIcon('./a.png') ,'click',mw)
    ac1.setStatusTip("This is a tip !")
    ac1.setCheckable(True)
    ac1.triggered.connect(showdlg)
    toolbar.addAction(ac1)


    #menu
    menu=mw.menuBar()
    menu.setNativeMenuBar(False)

    file_menu=menu.addMenu('&File')
    file_menu.addAction(ac1)

    return mw 

if __name__=='__main__':
    app=QApplication(sys.argv)

    mainwindow=getMainWindow()
    mainwindow.show()
    app.exec()
