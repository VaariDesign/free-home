import requests
import json

import input_data
from classes import Light
from classes import Heating
from classes import Shade

def make_light(sysap,device,channel,displayname,inputchannel):
    value = package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannel]["value"]
    name =str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName'])
    variable_name = name.replace(" ","_")
    locals()[variable_name] = Light(sysap,device,channel, displayname, value, inputchannel)
    return locals()[variable_name]


def make_heating(sysap,device,channel,displayname,inputchannel, outputchannel, temperature_channel):
    target = package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][outputchannel]["value"]
    temperature = package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][temperature_channel]["value"]
    name =str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName'])
    variable_name = name.replace(" ","_")
    #print(variable_name)
    locals()[variable_name] = Heating(sysap,device,channel, displayname, target, inputchannel,outputchannel, temperature_channel,temperature)
    return locals()[variable_name]


def make_shade(sysap, device, channel, displayname, input_pos, input_ang, output_pos, output_ang):
    position = package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][output_pos]["value"]
    angle = package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][output_ang]["value"]
    name =str(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName'])
    variable_name = name.replace(" ","_")
    print(variable_name)
    locals()[variable_name] = Shade(sysap, device, channel, displayname, input_pos, input_ang, output_pos, output_ang, position, angle)
    locals()[variable_name].status()
    return locals()[variable_name]

def update(light_obj, heating_obj, shades_obj):
    #Get configuration of the free@home system
    confiq = requests.get('http://'+url+'/fhapi/v1/api/rest/configuration', auth=(user, password))
    package_json = confiq.json() #Turn data to json
    package_str = json.dumps(package_json, indent=2)
    with open('confiq.txt','w') as f:
        f.write(package_str)

    # Update all values
    for light in light_obj:
        light.value = package_json[light.sysap]['devices'][str(light.device)]['channels'][light.channel]['inputs'][light.inputchannel]["value"]

    for shade in shades_obj:
        shade.position = package_json[shade.sysap]['devices'][str(shade.device)]['channels'][shade.channel]['outputs'][shade.output_pos]["value"]
        shade.angle = package_json[shade.sysap]['devices'][str(shade.device)]['channels'][shade.channel]['outputs'][shade.output_ang]["value"]

    for heat in heating_obj:
        heat.target = package_json[heat.sysap]['devices'][str(heat.device)]['channels'][heat.channel]['outputs'][heat.outputchannel]["value"]
        heat.temperature = package_json[heat.sysap]['devices'][str(heat.device)]['channels'][heat.channel]['outputs'][heat.temperature_channel]["value"]




user = input_data.user
password = input_data.password #same as log in your free@home
url = input_data.url

#Get configuration of the free@home system
confiq = requests.get('http://'+url+'/fhapi/v1/api/rest/configuration', auth=(user, password))
package_json = confiq.json() #Turn data to json
package_str = json.dumps(package_json, indent=2)


sysap = package_str[5:41] #get the sysap name from configuration

#make txt file from confiq string. Easier to watch with notepad
with open('confiq.txt','w') as f:
    f.write(package_str)




light_obj = []
shades_obj = []
heating_obj = []



for device in package_json[sysap]['devices']:
    for channel in package_json[sysap]['devices'][str(device)]['channels']:
        if len(package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']) <= 2:
            print("Too short device name: Less than 2 characters")
            # Lights
        elif package_json[sysap]['devices'][str(device)]['channels'][channel]['functionID'] == '7':
            displayname = package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']

            for inputchannel in package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs']:
                if package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannel]["pairingID"] == 1:
                    light_obj.append(make_light(sysap,device,channel,displayname,inputchannel))


            # Heating
        elif package_json[sysap]['devices'][str(device)]['channels'][channel]['functionID'] == '23':
            displayname = package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']

            # Find input channel to find where we can give inputs
            for inputchannel_look in package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs']:
                if package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannel_look]["pairingID"] == 320:
                    inputchannel = inputchannel_look

            for outputchannel_look in package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs']:
                if package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][outputchannel_look]["pairingID"] == 51:
                    outputchannel = outputchannel_look

                if package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][outputchannel_look]["pairingID"] == 304:
                    temperature_channel = outputchannel_look
            heating_obj.append(make_heating(sysap,device,channel,displayname,inputchannel, outputchannel, temperature_channel))


            # Shades / Blinds
        elif package_json[sysap]['devices'][str(device)]['channels'][channel]['functionID'] == '9':
            displayname = package_json[sysap]['devices'][str(device)]['channels'][channel]['displayName']

            for inputchannel in package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs']:
                if package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannel]["pairingID"] == 35:
                    input_pos = inputchannel

                if package_json[sysap]['devices'][str(device)]['channels'][channel]['inputs'][inputchannel]["pairingID"] == 36:
                    input_ang = inputchannel

            for outputchannel in package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs']:
                if package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][outputchannel]["pairingID"] == 289:
                    output_pos = outputchannel


                if package_json[sysap]['devices'][str(device)]['channels'][channel]['outputs'][outputchannel]["pairingID"] == 290:
                    output_ang = outputchannel

            shades_obj.append(make_shade(sysap, device, channel, displayname, input_pos, input_ang, output_pos, output_ang))



#Following is configuration specific data, it varies system to system
#Getting temperatures
#temperature_livingroom = package_json[sysap]['devices']['ABB7F597AE14']['channels']['ch0000']['outputs']['odp0010']['value']
#temperature_bedroom = package_json[sysap]['devices']['ABB7F597AD39']['channels']['ch0000']['outputs']['odp0010']['value']
#temperature_bathroom = package_json[sysap]['devices']['ABB7F597AD18']['channels']['ch0000']['outputs']['odp0010']['value']
#temperature_outside = package_json[sysap]['devices']['ED0100003361']['channels']['ch0002']['outputs']['odp0001']['value']

#Data from roof sensor
#light_outside = package_json[sysap]['devices']['ED0100003361']['channels']['ch0000']['outputs']['odp0001']['value']
#wind_outside = package_json[sysap]['devices']['ED0100003361']['channels']['ch0003']['outputs']['odp0003']['value']
#windscale_outside = package_json[sysap]['devices']['ED0100003361']['channels']['ch0003']['outputs']['odp0001']['value']

#print(temperature_livingroom +" Livingroom")
#print(temperature_bedroom +" Bedroom")
#print(temperature_bathroom +" Bathroom")
#print(temperature_outside +" Outside")

#print(light_outside +" Lux Outside")
#print(wind_outside +" m/s Outside")
#print(windscale_outside +" bft Outside(The Beaufort scale)")





print("!!!!!!!!!!!!!!!!!! Ended succesfully !!!!!!!!!!!!!!!!!!!")
