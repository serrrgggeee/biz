from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
def contacts(request):
    template = loader.get_template('main.html')
    #context = RequestContext(request, {
    #    'battery_voltage_nominal': battery_voltage_nominal,
    #    'input_frequency_nominal': input_frequency_nominal,
    #    'input_voltage': input_voltage,
    #    'input_voltage_fault': input_voltage_fault,
    #    'output_voltage': output_voltage,
    #    'ups_load': ups_load,
     #   'input_frequency': input_frequency,
    #    'battery_voltage': battery_voltage,
     #   'ups_temperature': ups_temperature,

    #})


    return HttpResponse(template.render())
