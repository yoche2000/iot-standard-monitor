from mq_recv_client import MQClient
import time
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from UI_Design import *

if __name__ == '__main__':

    host = '183.230.40.96'
    port = 8883

    access_key = 'MnG4fm6PHioLbp9/TZx8gL8yobG3niM4xJqiUCydesw=' #acckey
    namespace = 'cityu_test_only'   #Mqid
    topic_name1 = 'w123' #topic
    sub_name1 = 'w222' #sub

    #mq = MQClient(host, port, namespace, access_key, topic_name1, sub_name1)
    #mq.run()
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    UI = Ui_MainWindow()
    UI.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
    #while True:
     #   time.sleep(1)