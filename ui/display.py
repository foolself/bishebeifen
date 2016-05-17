#-*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from xmlparse import Parser

LBPER = ["Permissions Issue", 
		"Description: \nSecurity problems caused by irrational \nPermissions."]
LBINJ = ["JavaScript Injection", 
		"Description: \nApplication may be attacked by Javascript\n injection who contain the webView"]
LBDAT = ["Data Loss", 
		"Description: \nDatabase "]

BTINF = "summary_info"
BTATT = "Attack_Surface"
BTACT = "Activities"
BTBRO = "Broadcast"
BTPRO = "Providers"
BTSER = "Services"
BTPER = "Permissions"
BTURI = "URIs"

BTBWS = "Browsable"
BTINJ = "Injection"
BTSQL = "SqlTables"

class Example(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.isfileopen = False
		self.initUI()

	def initUI(self):
		self.widget = QWidget()
		self.setCentralWidget(self.widget)

		self.reportWidget = QWidget()
		self.detailWidget = QWidget()

		# self.reportWidget.setStyleSheet(" QWidget{ background-color: red }")

		self.textEdit = QTextEdit()
		self.textEdit.setReadOnly(True)
		# self.textEdit.setPointSize(18)

		self.bt_report = QPushButton("Report", self.widget)
		self.bt_detail = QPushButton("Detail", self.widget)
		self.lb_per1 = QLabel(LBPER[0], self.reportWidget)
		self.lb_per2 = QLabel("...", self.reportWidget)
		self.lb_per3 = QLabel(LBPER[1], self.reportWidget)
		self.lb_inj1 = QLabel(LBINJ[0], self.reportWidget)
		self.lb_inj2 = QLabel("...", self.reportWidget)
		self.lb_inj3 = QLabel(LBINJ[1], self.reportWidget)

		self.lb_db1 = QLabel(LBDAT[0], self.reportWidget)
		self.lb_db2 = QLabel("...", self.reportWidget)
		self.lb_db3 = QLabel(LBDAT[1], self.reportWidget)
		self.lb_per1.setStyleSheet("border:0px solid black")
		self.lb_inj1.setStyleSheet("border:0px solid black")
		self.lb_db1.setStyleSheet("border:0px solid black")
		self.bt_info = QPushButton(BTINF, self.detailWidget)
		self.bt_Permissions = QPushButton(BTPER, self.detailWidget)
		self.bt_attack = QPushButton(BTATT, self.detailWidget)
		self.bt_Activity = QPushButton(BTACT, self.detailWidget)
		self.bt_Broadcast = QPushButton(BTBRO, self.detailWidget)
		self.bt_Provider = QPushButton(BTPRO, self.detailWidget)
		self.bt_Service = QPushButton(BTSER, self.detailWidget)
		self.bt_Uri = QPushButton(BTURI, self.detailWidget)
		self.bt_Bws = QPushButton(BTBWS, self.detailWidget)
		self.bt_Inj = QPushButton(BTINJ, self.detailWidget)
		self.bt_Sql = QPushButton(BTSQL, self.detailWidget)

		self.bt_report.clicked.connect(self.bt_rep_clicked)
		self.bt_detail.clicked.connect(self.bt_det_clicked)

		self.bt_info.clicked.connect(self.buttonClicked)
		self.bt_Permissions.clicked.connect(self.buttonClicked)
		self.bt_attack.clicked.connect(self.buttonClicked)
		self.bt_Activity.clicked.connect(self.buttonClicked)
		self.bt_Broadcast.clicked.connect(self.buttonClicked)
		self.bt_Provider.clicked.connect(self.buttonClicked)
		self.bt_Service.clicked.connect(self.buttonClicked)
		self.bt_Uri.clicked.connect(self.buttonClicked)
		self.bt_Bws.clicked.connect(self.buttonClicked)
		self.bt_Inj.clicked.connect(self.buttonClicked)
		self.bt_Sql.clicked.connect(self.buttonClicked)

		mainVbox = QVBoxLayout()

		topHbox = QHBoxLayout()
		reportHbox = QHBoxLayout()
		detailHbox = QHBoxLayout()
		
		self.repWidget1 = QWidget(self.reportWidget)
		self.repWidget2 = QWidget(self.reportWidget)
		self.repWidget3 = QWidget(self.reportWidget)
		self.repWidget1.setStyleSheet("border:2px solid black;border-color:#008B00;border-radius:10px;margin: 10px 20px 10px 20px")
		self.repWidget2.setStyleSheet("border:2px solid black;border-color:#CD3700;border-radius:10px;margin: 10px 20px 10px 20px")
		self.repWidget3.setStyleSheet("border:2px solid black;border-color:#EE4000;border-radius:10px;margin: 10px 20px 10px 20px")
		repGrid1 = QGridLayout()
		repGrid2 = QGridLayout()
		repGrid3 = QGridLayout()
		# repVbox1.setStyleSheet(" QVBoxLayout{ background-color: red }")

		repGrid1.addWidget(self.lb_per1, 0, 0, 1, 1)
		repGrid1.addWidget(self.lb_per2, 1, 0, 5, 1)
		repGrid1.addWidget(self.lb_per3)
		repGrid2.addWidget(self.lb_inj1, 0, 0, 1, 1)
		repGrid2.addWidget(self.lb_inj2, 1, 0, 5, 1)
		repGrid2.addWidget(self.lb_inj3)
		repGrid3.addWidget(self.lb_db1, 0, 0, 1, 1)
		repGrid3.addWidget(self.lb_db2, 1, 0, 5, 1)
		repGrid3.addWidget(self.lb_db3)

		self.repWidget1.setLayout(repGrid1)
		self.repWidget2.setLayout(repGrid2)
		self.repWidget3.setLayout(repGrid3)
		reportHbox.addWidget(self.repWidget1)
		reportHbox.addWidget(self.repWidget2)
		reportHbox.addWidget(self.repWidget3)

		leftVbox = QVBoxLayout()

		topHbox.addWidget(self.bt_report)
		topHbox.addWidget(self.bt_detail)

		leftVbox.addWidget(self.bt_info)
		leftVbox.addWidget(self.bt_Permissions)
		leftVbox.addWidget(self.bt_attack)
		leftVbox.addWidget(self.bt_Activity)
		leftVbox.addWidget(self.bt_Broadcast)
		leftVbox.addWidget(self.bt_Provider)
		leftVbox.addWidget(self.bt_Service)
		leftVbox.addWidget(self.bt_Uri)
		leftVbox.addWidget(self.bt_Bws)
		leftVbox.addWidget(self.bt_Inj)
		leftVbox.addWidget(self.bt_Sql)
		
		detailHbox.addLayout(leftVbox)
		detailHbox.addWidget(self.textEdit)

		mainVbox.addLayout(topHbox)
		self.reportWidget.setLayout(reportHbox)
		self.detailWidget.setLayout(detailHbox)
		mainVbox.addWidget(self.reportWidget)
		mainVbox.addWidget(self.detailWidget)

		# self.reportWidget.show()
		self.detailWidget.hide()

		self.widget.setLayout(mainVbox)

		self.statusBar()
		openFile = QAction(QIcon('open.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.showDialog)
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)

		# self.setGeometry(100, 100, 800, 500)
		self.setWindowTitle('Android App Info')
		self.setWindowIcon(QIcon('icon.png'))

		# self.show()
		self.showMaximized()
	def initData(self, fname):
		self.parser = Parser(fname)

	def bt_rep_clicked(self):
		self.detailWidget.hide()
		self.reportWidget.show()
		if self.isfileopen:
			self.lb_per2.setText(self.parser.get_iss_permissions(1))
			self.lb_inj2.setText(self.parser.get_Browsable(1))
			self.lb_db2.setText(self.parser.get_SqlTables(1))
	def bt_det_clicked(self):
		self.reportWidget.hide()
		self.detailWidget.show()

	def buttonClicked(self):
		sender = self.sender()
		# self.statusBar().showMessage(sender.text())
		if self.isfileopen:
			if sender.text() == BTINF:
				content = self.parser.get_package_info()
				self.textEdit.setText(content)
			elif sender.text() == BTPER:
				content = self.parser.get_Permissions()
				self.textEdit.setText(content)
			elif sender.text() == BTATT:
				content = self.parser.get_Attack_Surface()
				self.textEdit.setText(content)
			elif sender.text() == BTACT:
				content = self.parser.get_Activities()
				self.textEdit.setText(content)
			elif sender.text() == BTBRO:
				content = self.parser.get_Broadcast()
				self.textEdit.setText(content)
			elif sender.text() == BTPRO:
				content = self.parser.get_Provider()
				self.textEdit.setText(content)
			elif sender.text() == BTSER:
				content = self.parser.get_Service()
				self.textEdit.setText(content)
			elif sender.text() == BTURI:
				content = self.parser.get_Uri()
				self.textEdit.setText(content)
			elif sender.text() == BTBWS:
				content = self.parser.get_Browsable()
				self.textEdit.setText(content)
			elif sender.text() == BTINJ:
				content = self.parser.get_Injection()
				self.textEdit.setText(content)
			elif sender.text() == BTSQL:
				content = self.parser.get_SqlTables()
				self.textEdit.setText(content)
			else:
				pass

	def showDialog(self):
		try:
			fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/john/design/report')
		except:
			fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/john/design')
		if fname[0]:
			self.isfileopen = True
			# self.textEdit.setText(fname[0])
			self.initData(fname[0])
			self.statusBar().showMessage(fname[0])
			content = self.parser.get_package_info()
			self.textEdit.setText(content)
			self.bt_rep_clicked()

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes |
		QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())