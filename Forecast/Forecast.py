import forecastio

def main():
    
    #Query 
    #Query the forecast.io server for info
    #to do: implement error if server/api file not present
    
    print ("Beginning query")
    
    keyFile = open("C:/Users/owner/documents/visual studio 2015/Projects/Forecast/api_key.txt", "r")
    if keyFile.closed == False:   
        api_key = keyFile.readline()
        print ("API Key read successfully")
    keyFile.close()

    #lat/long of milton keynes. Possibly make this readable?
    lat = 52.0059
    lng = -0.7277
    
    forecast = forecastio.load_forecast(api_key, lat, lng)

    print ("Query successful") #note; this is stupid, as it will print even if the query is not successful
    #end query

    #Show the current conditions    
    print ("---Current Conditions---")
    rightNow = forecast.currently()
    
    print("It is currently", rightNow.summary, "and", round(rightNow.temperature, 1), "C") 

    #show a forecast in plain text
    print ("---Forecast---")
    byHour = forecast.hourly()
    print ("24 hour Summary: %s" % (byHour.summary))

    #show the next 6 hours
    print ("--- The next 6 hours---")
       
    for hourly_data_point in byHour.data[:6]:
        print (hourly_data_point.time, hourly_data_point.summary, "and", round(hourly_data_point.temperature, 1), "C")


if __name__ == "__main__":
    main()