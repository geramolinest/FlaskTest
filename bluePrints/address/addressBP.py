from flask import Blueprint, render_template,request,redirect
from .addressAPI import ResponseAddress
#In this file i create the blueprint for the process

address = Blueprint('address',__name__)

#Adding routes for the blueprint, and defining the http methods
@address.route('/address',methods=['GET','POST'])
def index():
    #If the method is post, it redirects to the result template where it will show all the results
    if request.method == 'POST':
        address_geocode = request.form['address']
        #Valid that the address is not empty, to avoid errors in the http request
        if not address_geocode:            
            return render_template('fail.html')
        
        #Making instance of the class that previously i created
        response_address = ResponseAddress(address_geocode)
        #Obtaining the data from the class function for print in the html file
        data_table = response_address.generate_data_template()
        #Obtaining the number of records of each petition for print in html template
        address_registers = response_address.founded_registers()
        mkad_registers = response_address.founded_registers_mkad()
        
        #Redirect to result template, in this html we can see the results
        return render_template('result.html',data_table = data_table,address_registers=address_registers,mkad_registers = mkad_registers)
        
    return render_template('address.html')

