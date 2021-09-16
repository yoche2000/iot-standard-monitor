from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
sys.path.append('C:/Users/hwang/PycharmProjects/OneNET-MQ-Demo-Python-20190830/OneNET-MQ-Demo-Python/')

import paho.mqtt.client as mqtt
import time
import mq.onenet_mq_pb2 as proto
from sastoken import sas_token
from _ssl import CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED
import logging
import random
import sys
from time import sleep
import time
import paho.mqtt.client as mqtt
from mq_recv_client import MQClient
import time

from PyQt5.QtCore import QMutex, QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTextBrowser,
)


logging.basicConfig(format="%(message)s", level=logging.INFO)

content = 'Start'
display ='\n'
balance=100
mutex = QMutex()

log = []

def ts_print(*args):
    t = time.strftime("[%Y-%m-%d %H:%M:%S.")
    ms = str(time.time()).split('.')[1][:3]
    t += ms + ']:'
    print(t, *args)

    temp = t
    for x in args:
        temp += ' ' + str(x)
    temp += '\n'
    if len(log) < 100:
        log.append(temp)


class MQClient:
    def __init__(self, host, port, namespace, access_key, topic_name, sub_name):

        self.status = False
        self.namespace = namespace
        self.access_key = access_key
        self.topic_name = topic_name
        self.sub_name = sub_name
        self.host = host
        self.port = port
        self.topic = '$sys/pb/consume/%s/%s/%s' % (self.namespace, self.topic_name, self.sub_name)
        self.count = 0
        self.msg_id = 0

        client_id = self.topic_name  # clientid：用户自定义合法的UTF-8字符串，可为空
        username = self.namespace  # 填写涉及的ns，目前不支持除数字、字母、-、下划线以外的特殊字符
        try:
            password = sas_token('sha256', self.namespace, access_key)
        except Exception as e:
            ts_print('参数错误，生产token失败：' + str(e))
            return

        ts_print('username: ' + username)
        ts_print('password: ' + password)

        self.client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv311)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe
        self.client.on_disconnect = self.on_disconnect

        self.client.tls_set(ca_certs='certificate.pem', cert_reqs=CERT_REQUIRED)
        self.client.tls_insecure_set(True)

        self.client.username_pw_set(username=username, password=password)
        self.status = True





    def on_connect(self, client, userdata, flags, rc):
        ts_print("<<<<CONNACK")
        ts_print("connected with result code " + mqtt.connack_string(rc), rc)

        if rc == 0:
            ts_print('订阅topic: %s' % self.topic)
            client.subscribe(self.topic, qos=1)

    def on_message(self, client, userdata, msg):
        global content
        self.count += 1
        proto_msg = proto.Msg()
        proto_msg.ParseFromString(msg.payload)
        #ts_print(self.count, proto_msg.msgid, proto_msg.data.decode(), proto_msg.timestamp, time.time())
        content = proto_msg.data.decode()
        print(content)








        H=proto_msg.data.decode()
        return H

    def on_subscribe(self, client, obj, mid, granted_qos):
        ts_print("Subscribed: mid: " + str(mid) + "  qos:", granted_qos[0])

    def on_disconnect(self, client, userdata, rc):
        ts_print('DISCONNECTED with result code: %d' % rc, mqtt.connack_string(rc))
        #重新设置一下password,防止重连时token过期
        password = sas_token('sha256', self.namespace, self.access_key)
        self.client.username_pw_set(username=self.namespace,password=password)

    def run(self):
        if self.status:
            try:
                self.client.connect(host=self.host, port=self.port, keepalive=120)
            except Exception as e:
                ts_print('服务器连接失败 %s' % str(e))
                return
            self.client.loop_start()
class AccountManager(QObject):
    finished = pyqtSignal()

    updatedText = pyqtSignal()

    def connection1(self):

        self.client.connect(self.mqttBroker)
        print('success')


    def on_message(self, client, userdata, message):
        #global content

        print("received message: ", str(message.payload.decode("utf-8")))
        #content = str(message.payload.decode("utf-8"))



    def connection(self):
        host = '183.230.40.96'
        port = 8883

        access_key = 'MnG4fm6PHioLbp9/TZx8gL8yobG3niM4xJqiUCydesw='  # acckey
        namespace = 'cityu_test_only'  # Mqid
        topic_name1 = 'w123'  # topic
        sub_name1 = 'w222'  # sub
        mq = MQClient(host, port, namespace, access_key, topic_name1, sub_name1)
        mq.run()
        '''''
        mqttBroker = "mqtt.eclipseprojects.io"

        client = mqtt.Client("Smartphone")
        client.connect(mqttBroker)

        client.loop_start()

        client.subscribe("123")
        client.on_message = self.on_message
        
        time.sleep(1)
        client.loop_stop()
        print('content2', content)
        '''''
        sleep(5)
        self.updatedText.emit()
        self.finished.emit()

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.threads = []
        self.display = '123'

        #self.mqttBroker = "mqtt.eclipseprojects.io"

        #self.client = mqtt.Client("Smartphone")
        #self.client.connect(self.mqttBroker)
        print('test')

    def setupUi(self):
        self.setWindowTitle("Account Manager")
        self.resize(1000, 550)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        button = QPushButton("Click to Receive")
        self.textbrowser = QTextBrowser(self.centralWidget)
        button.clicked.connect(self.startThreads)
        self.balanceLabel = QLabel(f"mqtt")
        layout = QVBoxLayout()
        layout.addWidget(self.balanceLabel)
        layout.addWidget(button)
        layout.addWidget(self.textbrowser)
        self.centralWidget.setLayout(layout)

    def createThread(self):
    #def createThread(self, person, amount):
        thread = QThread()
        worker = AccountManager()
        worker.moveToThread(thread)

        print('1')
        thread.started.connect(lambda: worker.connection())
        print('3')
        #thread.started.connect(lambda: worker.withdraw(person, amount))
        worker.updatedText.connect(self.updateBalance)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        return thread

    def updateBalance(self):

        #self.balanceLabel.setText(f"Current Balance: ${balance:,.2f}")
        self.display = self.display+content+'\n'
        self.textbrowser.setText(('Received Message:\n'+self.display))
        #self.textbrowser.setText(('Received Message:\n' + content))
        self.textbrowser.setFont(QFont('Arial', 15))

    def startThreads(self):
        self.threads.clear()
        self.threads = [self.createThread()]
        '''''
        people = {
            "Alice": random.randint(100, 10000) / 100,
            "Bob": random.randint(100, 10000) / 100,
        }
        self.threads = [
            self.createThread(person, amount)
            for person, amount in people.items()
        ]
       '''''
        for thread in self.threads:
            thread.start()
            print('4')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())






