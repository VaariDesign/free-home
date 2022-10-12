import requests
import input_data


class Light:
    def __init__(self, sysap, device, channel, displayname, value, inputchannel):
        self.sysap = sysap
        self.device = device
        self.channel = channel
        self.name = displayname
        self.value = value
        self.inputchannel = inputchannel


    def light_on(self):
        requests.put('http://'+input_data.url+'/fhapi/v1/api/rest/datapoint/'+self.sysap+'/'+self.device+'.'+self.channel+'.'+self.inputchannel, auth=(input_data.user, input_data.password), data ="1")

    def light_off(self):
        requests.put('http://'+input_data.url+'/fhapi/v1/api/rest/datapoint/'+self.sysap+'/'+self.device+'.'+self.channel+'.'+self.inputchannel, auth=(input_data.user, input_data.password), data ="0")

    def status(self):
        if self.value == '1':
            print(self.name +" is ON")
        else:
            print(self.name +" is OFF")

    def show_name(self):
        print(self.name)


class Heating:
    def __init__(self, sysap, device, channel, displayname, target, inputchannel, outputchannel, temperature_channel, temperature):
        self.sysap = sysap
        self.device = device
        self.channel = channel
        self.name = displayname
        self.target = target
        self.inputchannel = inputchannel
        self.outputchannel = outputchannel
        self.temperature_channel = temperature_channel
        self.temperature = temperature


    def target_temperature(self):
        print("Target temperature in "+self.name + " is "+self.target)

    def current_temperature(self):
        print("Current temperature in "+self.name + " is "+self.temperature)

    def new_target(self,target):
        print("Set target temperature in "+ self.name + " to "+target)
        print(self.device + " "+self.channel + " "+self.inputchannel + " ")
        requests.put('http://'+input_data.url+'/fhapi/v1/api/rest/datapoint/'+self.sysap+'/'+self.device+'.'+self.channel+'.'+self.inputchannel, auth=(input_data.user, input_data.password), data=target)

