import requests
import input_data

class Light:
    def __init__(self, sysap, device, channel, displayname, value, inputchannel):
        self.sysap = sysap
        self.device = device
        self.channel = channel
        self.name = displayname
        self.value = value              # only thing to update
        self.inputchannel = inputchannel
        self.button = None
        self.buttonvalue = None


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

    def toggle(self):
        if self.value == "1":
            self.light_off()
            self.value = "0"
            print(self.name +" is OFF")
        elif self.value == "0":
            self.light_on()
            self.value = "1"
            print(self.name +" is ON")
        else:
            print("Something is wrong with value it is "+ self.value)
            print(type(self.value))



class Heating:
    def __init__(self, sysap, device, channel, displayname, target, inputchannel, outputchannel, temperature_channel, temperature):
        self.sysap = sysap
        self.device = device
        self.channel = channel
        self.name = displayname
        self.target = target            # update
        self.inputchannel = inputchannel
        self.outputchannel = outputchannel
        self.temperature_channel = temperature_channel
        self.temperature = temperature     #update
        self.buttonvalue = None
        self.button_plus = None
        self.button_minus = None


    def target_temperature(self):
        print("Target temperature in "+self.name + " is "+self.target)

    def current_temperature(self):
        print("Current temperature in "+self.name + " is "+self.temperature)

    def new_target(self,target):
        print("Set target temperature in "+ self.name + " to "+target)
        print(self.device + " "+self.channel + " "+self.inputchannel + " ")
        requests.put('http://'+input_data.url+'/fhapi/v1/api/rest/datapoint/'+self.sysap+'/'+self.device+'.'+self.channel+'.'+self.inputchannel, auth=(input_data.user, input_data.password), data=target)

    def target_up(self):
        requests.put('http://'+input_data.url+'/fhapi/v1/api/rest/datapoint/'+self.sysap+'/'+self.device+'.'+self.channel+'.'+self.inputchannel, auth=(input_data.user, input_data.password), data=str(float(self.target) + 0.5))

    def target_down(self):
        requests.put('http://'+input_data.url+'/fhapi/v1/api/rest/datapoint/'+self.sysap+'/'+self.device+'.'+self.channel+'.'+self.inputchannel, auth=(input_data.user, input_data.password), data=str(float(self.target) - 0.5))



class Shade:
    def __init__(self, sysap, device, channel, displayname, input_pos, input_ang, output_pos, output_ang, position, angle):
        self.sysap = sysap
        self.device = device
        self.channel = channel
        self.name = displayname
        self.input_pos = input_pos
        self.input_ang = input_ang
        self.output_pos = output_pos
        self.output_ang = output_ang
        self.position = position #update
        self.angle = angle      #update
        self.button1 = None
        self.button2 = None
        self.buttonvaluepos = None
        self.buttonvalueang = None



    def status(self):
        print(self.name +" is "+ self.position + "% down and angle of shades are " + self.angle)


    def move_position(self, position):
        requests.put('http://'+input_data.url+'/fhapi/v1/api/rest/datapoint/'+self.sysap+'/'+self.device+'.'+self.channel+'.'+self.input_pos, auth=(input_data.user, input_data.password), data=str(position))


    def move_angle(self, angle):
        requests.put('http://'+input_data.url+'/fhapi/v1/api/rest/datapoint/'+self.sysap+'/'+self.device+'.'+self.channel+'.'+self.input_ang, auth=(input_data.user, input_data.password), data=str(angle))


class Weather:
    def __init__(self, sysap, device, channel, displayname, outputchannel, value):
        self.sysap = sysap
        self.device = device
        self.channel = channel
        self.name = displayname
        self.outputchannel = outputchannel
        self.value = value    #update
