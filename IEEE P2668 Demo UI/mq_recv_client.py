# coding: utf-8
import threading
import sys
sys.path.append('C:/Users/hwang/PycharmProjects/OneNET-MQ-Demo-Python-20190830/OneNET-MQ-Demo-Python/')

import paho.mqtt.client as mqtt
import time
import ast
import mq.onenet_mq_pb2 as proto
from sastoken import sas_token
from _ssl import CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED

from Ui_IEEE_1451_NCAP import *
from client import *
from PyQt5 import QtCore, QtGui, QtWidgets

log = []

def set_acc( percentage ):
    result = "Accuracy: " + str(percentage) + "%"
    return result

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
    def __init__(self, host, port, namespace, access_key, topic_name, sub_name, srv, clt):

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
        self.srv = srv
        self.clt = clt
        self.templist = []
        self.humlist = []

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

    def variable_name(self):

        global content

    def on_connect(self, client, userdata, flags, rc):
        ts_print("<<<<CONNACK")
        ts_print("connected with result code " + mqtt.connack_string(rc), rc)

        if rc == 0:
            ts_print('订阅topic: %s' % self.topic)
            client.subscribe(self.topic, qos=1)

    def on_message(self, client, userdata, msg):

        self.count += 1
        proto_msg = proto.Msg()
        proto_msg.ParseFromString(msg.payload)
        ##ts_print(self.count, proto_msg.msgid, proto_msg.data.decode(), proto_msg.timestamp, time.time())
        dec_msg = proto_msg.data.decode()
        content = ast.literal_eval(dec_msg)

        H=proto_msg.data.decode()
        print("[RCV]",H)

        if(content["datastream"] == "temperatrue"):
            temp = content["body"]
            self.srv.label_temp_value.setText(str(content["body"]))
            self.clt.label_temp_value.setText(str(content["body"]))
            self.templist.append(temp >= 20 and temp <= 30)
            if (len(self.templist) > 10):
                self.templist.pop(0)
            acc = int(sum(self.templist) / len(self.templist)*100)
            ##print("h", self.templist)
            self.srv.label_temp_accuracy.setText(set_acc(acc))
            self.clt.label_temp_accuracy.setText(set_acc(acc))
            if(acc>90):
                self.srv.label_idex_value.setText("<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">5</span></p></body></html>")
                self.clt.label_idex_value.setText("5")
            elif(acc>80):
                self.srv.label_idex_value.setText("<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">4</span></p></body></html>")
                self.clt.label_idex_value.setText("4")
            elif(acc>70):
                self.srv.label_idex_value.setText("<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">3</span></p></body></html>")
                self.clt.label_idex_value.setText("3")
            elif(acc>60):
                self.srv.label_idex_value.setText("<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">2</span></p></body></html>")
                self.clt.label_idex_value.setText("2")
            else:
                self.srv.label_idex_value.setText("<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">1</span></p></body></html>")
                self.clt.label_idex_value.setText("1")
            if(acc<=70):
                self.clt.alarm.show()
                print("Alarm on")
            else:
                self.clt.alarm.hide()
                print("Alarm off")


        if(content["datastream"] == "humidity"):
            hum = content["body"]
            self.srv.label_humidity_value.setText(str(hum))
            self.clt.label_humidity_value.setText(str(hum))
            self.humlist.append(hum>=30 and hum <= 70)
            if (len(self.humlist) > 10):
                self.humlist.pop(0)
            acc = int(sum(self.humlist) / len(self.humlist)*100)
            ##print("h", self.humlist)
            self.srv.label_humidity_accuracy.setText(set_acc(acc))
            self.clt.label_humidity_accuracy.setText(set_acc(acc))

        return H





    def on_subscribe(self, client, obj, mid, granted_qos):
        ts_print("Subscribed: mid: " + str(mid) + "  qos:", granted_qos[0])

    def on_disconnect(self, client, userdata, rc):
        ts_print('DISCONNECTED with result code: %d' % rc, mqtt.connack_string(rc))
        #重新设置一下password,防止重连时token过期
        password = sas_token('sha256', self.namespace, access_key)
        self.client.username_pw_set(username=self.namespace,password=password)

    def run(self):
        if self.status:
            try:
                self.client.connect(host=self.host, port=self.port, keepalive=120)
            except Exception as e:
                ts_print('服务器连接失败 %s' % str(e))
                return
            self.client.loop_start()


if __name__ == '__main__':

    host = '183.230.40.96'
    port = 8883

    access_key = 'MnG4fm6PHioLbp9/TZx8gL8yobG3niM4xJqiUCydesw=' #acckey
    namespace = 'cityu_test_only'   #Mqid
    topic_name1 = 'w123' #topic
    sub_name1 = 'w222' #sub

    mq = MQClient(host, port, namespace, access_key, topic_name1, sub_name1)
    mq.run()
    while True:
        time.sleep(1)




