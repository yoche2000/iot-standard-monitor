# IEEE P2668 Demo UI
This is project for the IEEE P2668 Demonstration.
There are 2 UIs, one for NCAP-side and the other for client-side, to demonstrate the P2668 implementation and data transmission.

## mqtt client
An mqtt client example, subscribed to a topic of a device.
The mqtt server platform used in this case is Onenet by CMHK.
The data be published are 'temperature' and 'humidity'

## Server UI

![NCAP UI](https://i.imgur.com/mA2cL4W.jpg)
The server UI demonstrates the receiving data at the server side, showing the realtime temperature humidity. The IDex value is derived based on the data accuracy (In this case, based on temperature data to make it simple). 2 IEEE 1451 TEDS charts are also shown on the UI.

##Client UI

![Client UI](https://i.imgur.com/LD412uL.jpg)
The client UI also shows the temp/num data, and the current IDex value. When the IDex value reaches a certain low-level, an alarm will be shown to alert the client of the integrity of the data might have been compromised. 



