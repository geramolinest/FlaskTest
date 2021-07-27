import requests as r
from .geoTableI import TableInfo,DataTableInfo
from geopy import distance

#I created this class for make all operations about the problem, for better order of my project

class ResponseAddress:
    #Constants for the HTTP requests using the requests library from python and the Yandex Geocoder API
    API_KEY = '9c5e5076-baaf-462b-9eac-28267a4967b8'
    BASE_URL = 'https://geocode-maps.yandex.ru/1.x/?apikey='+ API_KEY +'&format=json&geocode='
    BASE_URL_MKAD = 'https://geocode-maps.yandex.ru/1.x/?apikey='+ API_KEY +'&format=json&geocode=Moscow+Ring+Road&lang=en-US'
    
    def __init__(self,address):
        self.address = address
    
    #I use this function to get all records that were geocoded from the given address
    def get_response_address(self):
        try:
            #I construct the url for the http request, indicating the language and the address to the defined constant            
            url = self.BASE_URL + self.address +'&lang=en-US'     
            response = r.get(url) #I make the http request 
            #I check the status of the http request to return a value that allows me to do a validation later
            if response.status_code ==400: 
                return None 
            print(url) #Print url for debbug         
            return response.json()#If all goes well, I return the result of the request in json format
        #These lines are for handling errors that may arise when making an http request
        except r.exceptions.RequestException as err:
            print (err) 
        except r.exceptions.HTTPError as e:            
            print(e.strerror)

    #This function returns the records found based on the address, 
    #accessing the content of the dictionary returned by the function making the http request.
    def founded_registers(self): 
        response = self.get_response_address()
        if response is None:
            return 0
        founded = response['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found']
        return founded

    #This function returns the records found in the geocoded MKAD address
    def founded_registers_mkad(self):
        founded = self.found_mkad_locations()['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found']
        return founded
    
    #Obtaining MKAD records through an http request
    def found_mkad_locations(self):
        try:
            response_mkad = r.get(self.BASE_URL_MKAD)
            return response_mkad.json()
        except r.exceptions.RequestException as err:
            print (err.strerror)
        except r.exceptions.HTTPError as e:
            print(e.strerror)
        
    #This is the most important function of the class,
    #it shapes all the information displayed in the results
    def generate_data_template(self):
        response = self.get_response_address() #Obtaining data from address
        response_mkad = self.found_mkad_locations() #Obtaining mkad data
        
        if response is None:
            return []

        #In the next two lines, the access to the list with the members 
        #that have the properties that allow to process the information, in them are the coordinates
        geo_objects_list = response['response']['GeoObjectCollection']['featureMember']
        geo_objects_list_mkad = response_mkad['response']['GeoObjectCollection']['featureMember']
        
        #Defining variables for origin location of calculus
        address_from = ''
        coordenates_from = ''
        #List for the data, a list of objects is made below
        data_table = []

        #Defining variables for destine location of calculus
        address_destine = ''
        coordenates_destine = ''

        #Variable for distance result
        distance = 0
        #List for calculated point data
        list_data = []

        #In the following lines the most logical operations of the application are made, 
        # we have a cycle that goes through each of the points of the MKAD area and we 
        # have another nested cycle that goes through each of the records of the geocoded address,
        #  based on this, the results are added to the lists to show them later
        for mkad in geo_objects_list_mkad:
            address_from = mkad['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
            coordenates_from = mkad['GeoObject']['Point']['pos']
            list_data.clear()
            for geo in geo_objects_list:
                address_destine = geo['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
                coordenates_destine = geo['GeoObject']['Point']['pos']
                #Boolean function to validate that the address is not in the MKAD area 
                if not self.mkad_area(geo['GeoObject']['Point']['pos'],response_mkad):                  
                    distance = str(self.distance_calculator(coordenates_from,coordenates_destine)) + ' miles'
                    list_data.append(DataTableInfo(address_destine,coordenates_destine,distance))
                else:
                    list_data.append(DataTableInfo(address_destine,coordenates_destine,'The address is inside MKAD'))
            data_table.append(TableInfo(address_from,coordenates_from,list_data)) 
                   
        return data_table               
    #This function calculates the distance between 
    #the coordinates of the MKAD address and the address entered, using the python geopy library
    def distance_calculator(self, coordenates_from: str, coordenates_destine:str):
        x_lat_from = 0
        y_long_from = 0

        x_lat_to = 0
        y_long_to = 0

        #Latitude and longitude come in a single string, so use the split function to get each one separately
        y_long_from,x_lat_from = coordenates_from.split()

        y_long_to,x_lat_to = coordenates_destine.split()

        #Calculation of the distance between the points, using the geopy library, and indicating 
        # that the calculation will be in miles
        distance_from_to = distance.distance((x_lat_from,y_long_from),(x_lat_to,y_long_to)).miles
        if not distance_from_to is None:
            return distance_from_to
        return 0                  

    def mkad_area(self,coordenates,mkad_response): #This function confirm if the location is inside of the MKAD area, if not return false

        response = mkad_response
        geo_objects_list = response['response']['GeoObjectCollection']['featureMember']        
        for geo in geo_objects_list:
            if str(coordenates) == geo['GeoObject']['Point']['pos']:
                return True
        
        return False

