from mq_recv_client import MQClient
import sys
from Ui_IEEE_1451_NCAP import *
from client import *
from PyQt5 import QtCore, QtGui, QtWidgets
import time

def set_acc( percentage ):
    result = "Accuracy: " + str(percentage) + "%"
    return result

if __name__ == '__main__':

    host = '183.230.40.96'
    port = 8883
    
    access_key = 'MnG4fm6PHioLbp9/TZx8gL8yobG3niM4xJqiUCydesw=' #acckey
    namespace = 'cityu_test_only'   #Mqid
    topic_name1 = 'w123' #topic
    sub_name1 = 'w222' #sub

    '''
    host = '47.52.102.24'
    port = 11006

    access_key = '+v0grRb/gau8ZlRqnyJF8dr/hCNF5DI2rePHY9QN//4=' #acckey
    namespace = 'IEEE_P2668_MQTT'   #Mqid
    topic_name1 = 'IEEE_P2668_NBIOT' #topic
    sub_name1 = 'DemoClient' #sub
    '''

    app = QtWidgets.QApplication(sys.argv)

    # Set up NCAP
    server_widget = QtWidgets.QWidget()
    srv = Ui_IEEE_1451_NCAP()
    srv.setupUi(server_widget)

    #Set up Client
    client_widget = QtWidgets.QWidget()
    clt = Ui_client()
    clt.setupUi(client_widget)

    #Set up both widgets
    clt.alarm.hide()
    server_widget.show()
    client_widget.show()

    mq = MQClient(host, port, namespace, access_key, topic_name1, sub_name1, srv, clt)
    mq.run()




    sys.exit(app.exec_())




    '''
    mq = MQClient(host, port, namespace, access_key, topic_name1, sub_name1)
    mq.run()
    while True:
        time.sleep(1)
    
    
        #Manipulation
    srv.label_temp_value.setText("44")
    srv.label_humidity_value.setText("33")
    srv.label_temp_accuracy.setText(set_acc("22"))
    srv.label_humidity_accuracy.setText(set_acc("11"))
    clt.label_temp_value.setText("99")
    clt.label_humidity_value.setText("88")
    clt.label_temp_accuracy.setText(set_acc("77"))
    clt.label_humidity_accuracy.setText(set_acc("66"))
    
    '''

