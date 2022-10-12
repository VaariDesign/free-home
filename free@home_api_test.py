import requests
import json

import input_data

from classes import Light
from classes import Heating

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

def make_light(sysap,device,channel,displayname,inputchannel):
    value = package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannel]["value"]
    name =str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName'])
    variable_name = name.replace(" ","_")
    locals()[variable_name] = Light(sysap,device,channel, displayname, value, inputchannel)
    locals()[variable_name].status()
    return locals()[variable_name]

def make_heating(sysap,device,channel,displayname,inputchannel, outputchannel, temperature_channel):
    target = package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][outputchannel]["value"]
    temperature = package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][temperature_channel]["value"]
    name =str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName'])
    variable_name = name.replace(" ","_")
    #print(variable_name)
    locals()[variable_name] = Heating(sysap,device,channel, displayname, target, inputchannel,outputchannel, temperature_channel,temperature)
    locals()[variable_name].current_temperature()
    locals()[variable_name].target_temperature()
    return locals()[variable_name]



lights = []
light_obj = []
shades = []
shades_obj = []
heating = []
heating_obj = []


user = input_data.user
password = input_data.password #same as log in your free@home
url = input_data.url

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
        # Dont want unused names in list
        if len(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']) <= 2:
            print("Too short device name: Less than 2 characters")

        # Lights
        elif package_json[sysap]['devices'][str(device)]['channels'][channel]['functionID'] == '7':
            light_name1 = (str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']))
            light_name = light_name1.replace(" ","_")
            lights.append(light_name)
            displayname = package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']

            for inputchannel in package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs']:
                if package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannel]["pairingID"] == 1:
                    light_obj.append(make_light(sysap,device,channel,displayname,inputchannel))


        # Heating
        elif package_json[sysap]['devices'][str(device)]['channels'][channel]['functionID'] == '23':
            heating.append(str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']))
            heat_name1 = (str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']))
            heat_name = heat_name1.replace(" ","_")
            heating.append(heat_name)
            displayname = package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']

            # Find input channel to find where we can give inputs
            for inputchannel_look in package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs']:
                if package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannel_look]["pairingID"] == 51:
                    inputchannel = inputchannel_look

            for outputchannel_look in package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs']:
                if package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][outputchannel_look]["pairingID"] == 51:
                    outputchannel = outputchannel_look

                if package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][outputchannel_look]["pairingID"] == 304:
                    temperature_channel = outputchannel_look
            heating_obj.append(make_heating(sysap, device, channel, displayname, inputchannel, outputchannel, temperature_channel))

        elif package_json[sysap]['devices'][str(device)]['channels'][channel]['functionID'] == '9':
            shades.append(str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']))


        for inputchannels in package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs']:
            channel_names += str(' ' + package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannels]['value'] )
    channel_names += str(' \n')
    channel_names += str(' \n')


# make txt file from channel names txt-file. Easier to watch with notepad
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


#print(lights)
#print(shades)
#print(heating)

#print(len(light_obj))
#i = 0
#for obj in light_obj:
#    print(str(i) + " ")
#    obj.status()
#    i+=1
#print(light_obj[0].name)
#print(heating_obj[0].name)

#heating_obj[0].new_target("22.5")

light_obj[0].light_on()

time.sleep(5)

light_obj[0].light_off()
#heating_obj[0].new_target("23")



print("!!!!!!!!!!!!!!!!!! Ended succesfully !!!!!!!!!!!!!!!!!!!")
