import requests
import json


from Classes import Light

import time



def get_devices(url,user,password,sysap):
    """
    :param url: IP-adrress of system accesspoint free@home
    :param user: Username free@home
    :param password: Password for free@home
    :param sysap: free@home sysap (first number combination of json files)
    :return: List of devices in free@home configuration
    """
    devices = requests.get('http://'+url+'/fhapi/v1/api/rest/devicelist',auth=(user, password))
    devices_str = json.dumps(devices.json(),indent=2)
    with open('devices.txt','w') as f:
        f.write(devices_str)
    device_list = devices.json()[sysap]
    return device_list



lights = []
shades = []
heating = []


#Login data for free@home: Settings---> Local API ---> Username
user =  'Username'
password = 'Password' #same as log in your free@home
url = 'IP-Address'

#Get configuration of the free@home system
confiq = requests.get('http://'+url+'/fhapi/v1/api/rest/configuration',auth=(user, password))
package_json = confiq.json() #Turn data to json
package_str = json.dumps(package_json, indent=2)

sysap = package_str[5:41] #get the sysap name from configuration

#make txt file from confiq string. Easier to watch with notepad
with open('confiq.txt','w') as f:
    f.write(package_str)

#Get device list of all devices and input values
channel_names = ""
device_list = get_devices(url,user,password,sysap)
for device in device_list:
    channel_names += str(device +' '+ package_json[sysap]['devices'][str(device)]['displayName'])
    for channel in package_json[sysap]['devices'][str(device)]['channels']:
        channel_names += str(' \n'+channel+' '+ package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName'])
        
        # adding to lists
        if package_json[sysap]['devices'][str(device)]['channels'][channel]['functionID'] == '7':
            lights.append(str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']))
            displayname = package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']

            for inputchannel in package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs']:
                if package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannel]["pairingID"] == 1:
                    print("pass")
                    value = package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannel]["value"]
                    locals()[str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName'])] =\
                        Light(device,channel, displayname, value, inputchannel)
                    print("pass")




        if package_json[sysap]['devices'][str(device)]['channels'][channel]['functionID'] == '27':
            heating.append(str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']))

        if package_json[sysap]['devices'][str(device)]['channels'][channel]['functionID'] == '9':
            shades.append(str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']))
        
        
        for inputchannels in package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs']:
            channel_names += str(' ' + package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannels]['value'] )
    channel_names += str(' \n')
    channel_names += str(' \n')


#make txt file from channel names txt-file. Easier to watch with notepad
with open('channel_names.txt','w', errors='ignore') as f:
    f.write(channel_names)


#Following is configuration specific data, it varies system to system
#Getting temperatures
temperature_livingroom = package_json[sysap]['devices']['ABB7F597AE14']['channels']['ch0000']['outputs']['odp0010']['value']
temperature_bedroom = package_json[sysap]['devices']['ABB7F597AD39']['channels']['ch0000']['outputs']['odp0010']['value']
temperature_bathroom = package_json[sysap]['devices']['ABB7F597AD18']['channels']['ch0000']['outputs']['odp0010']['value']
temperature_outside = package_json[sysap]['devices']['ED0100003361']['channels']['ch0002']['outputs']['odp0001']['value']

#Data from roof sensor
light_outside = package_json[sysap]['devices']['ED0100003361']['channels']['ch0000']['outputs']['odp0001']['value']
wind_outside = package_json[sysap]['devices']['ED0100003361']['channels']['ch0003']['outputs']['odp0003']['value']
windscale_outside = package_json[sysap]['devices']['ED0100003361']['channels']['ch0003']['outputs']['odp0001']['value']

print(temperature_livingroom +" Livingroom")
print(temperature_bedroom +" Bedroom")
print(temperature_bathroom +" Bathroom")
print(temperature_outside +" Outside")

print(light_outside +" Lux Outside")
print(wind_outside +" m/s Outside")
print(windscale_outside +" bft Outside(The Beaufort scale)")


print(lights)
print(shades)
print(heating)
for valo in lights:
    print(locals()[valo].status())


#Testing light on off
#light_on = "1"
#light_off = "0"

#print("test wohnen light")

#print("Light on")
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0003.idp0000',auth=(user, password), data=light_on)
#print("wait 5 sec")
#time.sleep(5)
#print("light off")
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0003.idp0000',auth=(user, password),data=light_off)


# Moving lights
#livingroom
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0003.idp0000',auth=(user, password), data=light_on)
#dining
#time.sleep(1)
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0003.idp0000',auth=(user, password), data=light_off)
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0002.idp0000',auth=(user, password), data=light_on)
#kitchen
#time.sleep(1)
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22F603D51.ch0000.idp0000',auth=(user, password), data=light_on)
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0002.idp0000',auth=(user, password), data=light_off)
#flur
#time.sleep(1)
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0000.idp0000',auth=(user, password), data=light_on)
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22F603D51.ch0000.idp0000',auth=(user, password), data=light_off)
#wohnen
#time.sleep(1)
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0003.idp0000',auth=(user, password), data=light_on)
#requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/00000000-0000-0000-0000-000000000000/ABB22D573D51.ch0000.idp0000',auth=(user, password), data=light_off)


