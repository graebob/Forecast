import forecastio

def main():
    
    print ("Beginning query")
    
    keyFile = open("C:/Users/owner/documents/visual studio 2015/Projects/Forecast/api_key.txt", "r")
    if keyFile.closed == False:   
        api_key = keyFile.readline()
        print ("API Key read successfully")
    keyFile.close()

    lat = 52.0059
    lng = -0.7277
    
    forecast = forecastio.load_forecast(api_key, lat, lng)

    print ("Query successful")

    print ("---Current Conditions---")
    rightNow = forecast.currently()
    
    print("It is currently", rightNow.summary, "and", round(rightNow.temperature, 1), "C")

    print ("---Forecast---")
    byHour = forecast.hourly()
    print ("24 hour Summary: %s" % (byHour.summary))

    print ("--- The next 6 hours---")
    count = 0
       
    for hourly_data_point in byHour.data[:6]:
        print (hourly_data_point.time, hourly_data_point.summary, "and", round(hourly_data_point.temperature, 1), "C")


if __name__ == "__main__":
    main()