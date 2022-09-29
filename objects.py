import requests

class Light:
    def __init__(self,device, channel, displayname, value, inputchannel):
        self.device = device
        self.channel = channel
        self.name = displayname
        self.value = value
        self.inputchannel = inputchannel

    def light_on(self,url,sysap,user,password):
        requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/'+sysap+'/'+self.device+'.'+self.channel+'.'+self.inputchannel, auth=(user, password), data ="1")

    def light_off(self,url,sysap,user,password):
        requests.put('http://'+url+'/fhapi/v1/api/rest/datapoint/'+sysap+'/'+self.device+'.'+self.channel+'.'+self.inputchannel, auth=(user, password), data ="0")
