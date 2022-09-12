import requests
import json
import time

#Login data for free@home: Settings---> Local API ---> Username
user = 'Username'
password = 'Password' #same as log in your free@home

#Diffrenet IP address
confiq = requests.get('http://192.168.2.55/fhapi/v1/api/rest/configuration',auth=(user, password))
package_json = confiq.json() #Turn data to json
package_str = json.dumps(package_json, indent=2)

#make txt file from confiq string
with open('confiq.txt','w') as f:
    f.write(package_str)


#Getting temperatures
temperature_livingroom = package_json['00000000-0000-0000-0000-000000000000']['devices']['ABB7F597AE14']['channels']['ch0000']['outputs']['odp0010']['value']
temperature_bedroom = package_json['00000000-0000-0000-0000-000000000000']['devices']['ABB7F597AD39']['channels']['ch0000']['outputs']['odp0010']['value']
temperature_bathroom = package_json['00000000-0000-0000-0000-000000000000']['devices']['ABB7F597AD18']['channels']['ch0000']['outputs']['odp0010']['value']
temperature_outside = package_json['00000000-0000-0000-0000-000000000000']['devices']['ED0100003361']['channels']['ch0002']['outputs']['odp0001']['value']

#Data from roof sensor
light_outside = package_json['00000000-0000-0000-0000-000000000000']['devices']['ED0100003361']['channels']['ch0000']['outputs']['odp0001']['value']
wind_outside = package_json['00000000-0000-0000-0000-000000000000']['devices']['ED0100003361']['channels']['ch0003']['outputs']['odp0003']['value']
windscale_outside = package_json['00000000-0000-0000-0000-000000000000']['devices']['ED0100003361']['channels']['ch0003']['outputs']['odp0001']['value']

print(temperature_livingroom +" Livingroom")
print(temperature_bedroom +" Bedroom")
print(temperature_bathroom +" Bathroom")
print(temperature_outside +" Outside")

print(light_outside +" Lux Outside")
print(wind_outside +" m/s Outside")
print(windscale_outside +" bft Outside(The Beaufort scale)")


#Testing light on off
light_on = "1"
light_off = "0"

print("test wohnen light")

print("Light on")
on = requests.put('http://192.168.2.55/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0003.idp0000',auth=(user, password), data=light_on)
on2 = requests.get('http://192.168.2.55/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0003.idp0000',auth=(user, password), data=light_on)

print("wait 5 sec")
confiq = requests.get('http://192.168.2.55/fhapi/v1/api/rest/configuration',auth=(user, password))
package_json = confiq.json() #Turn data to json
package_str = json.dumps(package_json, indent=2)

with open('confiq1.txt','w') as f:
    f.write(package_str)
time.sleep(5)
print("light off")
off = requests.put('http://192.168.2.55/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0003.idp0000',auth=(user, password),data=light_off)
print(off.text)
confiq = requests.get('http://192.168.2.55/fhapi/v1/api/rest/configuration',auth=(user, password))
package_json = confiq.json() #Turn data to json
package_str = json.dumps(package_json, indent=2)
with open('confiq2.txt','w') as f:
    f.write(package_str)
