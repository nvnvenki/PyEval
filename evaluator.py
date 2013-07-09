import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from math import *

class Evaluator(QDialog):

	def __init__(self):

		QDialog.__init__(self)

		# have text browser to display the result

		self.browser = QTextBrowser()

		# have a line edit to input the expression

		self.lineedit = QLineEdit("Enter the expression")
		self.lineedit.selectAll()

		# have a layout to add the widgets 

		layout = QVBoxLayout()
		# put the line edit n push button in hbox

		button = QPushButton("Evaluate",self)
		hlayout = QHBoxLayout() # horizontal layout
		hlayout.addWidget(self.lineedit) # add line edit to hlayout
		hlayout.addWidget(button) # add button to the sam hlayout

		# add hbox layout n text browser to vbox layout
		layout.addWidget(self.browser)
		layout.addLayout(hlayout)
		
		# set the layout of the window to be vbox layout

		self.setLayout(layout)

		self.lineedit.setFocus()

		# nw play with signals!! hey remember not this signnal " <3 " mind it!! Its dangerous ;)
		# connect the button signal n expression evaluating function
		self.connect(button,SIGNAL("clicked()"),self.CalculateResult)

		# Add title n other stuffs 
		self.setWindowTitle("Simple Expression Evaluator")
		self.setWindowIcon(QIcon("icon.png"))
		self.setGeometry(200,200,350,100)
		self.show()


	def CalculateResult(self):

		expression = str(self.lineedit.text())
		if expression == "help()" or expression == "help" or expression == "dir" or expression == "dir()":
			expression = "invalid" #just a junk statement to get evaluated to invalid :p
		self.browser.append(expression)
		self.browser.clear()
		self.lineedit.setText("")
		
		if expression:
		
			try:
				self.browser.append("<font color=blue><b> %s = %s </b></font>" % (expression,eval(expression)))
			except:
				self.browser.append("<font color=red><b>Invalid expression!! Please enter a valid expression</b> </font>")
		else:
			self.browser.append("<font color=red><b> Please enter a expression!</b> </font>")


if __name__ =="__main__": 
	app = QApplication(sys.argv)
	e = Evaluator()
	sys.exit(app.exec_())
