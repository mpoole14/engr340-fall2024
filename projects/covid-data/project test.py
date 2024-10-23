import sys
import numpy as np
import pandas as pa



def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    # your code here
    ground_zero_rockingham_county = None # placeholder variables for both rockingham and Harrisonburg
    ground_zero_harrisonburg = None # the prefix ground zero is used because it sounds cooler then first case
    for (date, county, state, cases, deaths) in data: #checking the different parts of data in the data including everything that the line lists
        if county == "Rockingham" and state == "Virginia" and cases > 0 and not ground_zero_rockingham_county: #line basically says while looking through the data if county and state match and cases are greater then zero then its the first case
            ground_zero_rockingham_county = date #saying if all information matches then variable ground zero is equal to the date
        if county == "Harrisonburg city" and state == "Virginia" and cases > 0 and not ground_zero_harrisonburg: #the "and not" is there to stop the code from updating after finding the first case (had issue of it updating after first)
            ground_zero_harrisonburg = date
        if ground_zero_rockingham_county and ground_zero_harrisonburg: # if both are found cycle is broken
            break
    print(f"the first case in Rockingham County: {ground_zero_rockingham_county}") #basic print statement to print the result of the date
    print(f"the first case in Harrisonburg: {ground_zero_harrisonburg}")

    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # your code here
    #max_infection_rockingham_county = None #placeholder variables for the greatest number of cases for both harrisonburg and rockingham
    #max_infection_harrisonburg = None
    #for (date,county, state, cases, deaths) in data:
       # if county == "Rockingham" and state == "Virginia" and cases > 100:
            #max_infection_rockingham_county = date
        #if max_infection_rockingham_county:
            #break
    #print(f"the greatest day of cases for Rockingham was {max_infection_rockingham_county}")
    #I mentioned in question one I was having issues with the first date being over-writed, I had hopes that the code would overwrite to the largest value of cases but no such luck :(
    # the 100 value was just a number used for testing to see if a number greater than zero would allow for updating
    #max_infection_rockingham = None
    #max_infection_rockingham_number = 0
    #max_infection_harrisonburg = None
    #max_infection_harrisonburg_number = 0


    #for (date, county, state, cases, deaths) in data:
        #if county == "Rockingham" and state == "Virginia":
            #new_cases = cases
            #if new_cases > max_infection_rockingham_number:
                #max_infection_rockingham_number = new_cases
                #max_infection_rockingham = date


        #elif county == "Harrisonburg city" and state == "Virginia":
            #new_cases = cases
            #if new_cases > max_infection_harrisonburg_number:
                #max_infection_harrisonburg_number = new_cases
                #max_infection_harrisonburg = date





    #print (f"test outcome rockingham {max_infection_rockingham}")
    #print (f"test outcome harrisonburg {max_infection_harrisonburg}")
    # my second idea was to have 2 values for max infection one that was a number and the other the date, I had hoped the number would allow for it to be updated past the first time cases appeared which it did.
    #sadly it just updated to the last possible date and im not sure what to change to fix that
    #both blocks of code runs just spits out an incorrect answer or I assume to be incorrect
    #I have realized its not doing what I want and its just pulling the last date

    return


def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    #I played around with pandas but wasnt finding it very helpful for this problem
    #I was using the pig latin assignment as reference but seeing as I struggled with that assignment I dont have much faith in this question
    #week_harrisonburg = None
    #week_rockingham = None
    #for (date, county, state, cases, deathes) in data: #sorta place holder code I was playing around with
        #if county == "Rockingham" and state == "Virginia":
            #date = week_rockingham
    #I assume like the pig latin assignment your suppose to splice the list but I played around with the code and couldnt really figure it out
    print("its a mystery to me")




    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    for (date, county, state, cases, deaths) in data:
        print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)