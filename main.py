from Calendario import Calendario
from Giorno import Lezione
import tabula
import pandas as pd

def parse_pdf (filename):
    file = "./" + filename
    tables = tabula.read_pdf(file, pages="all", multiple_tables=False, guess=True)

    headers = []
    #extract [1] as header
    headers = [clean_input(repr(i)) for i in tables[0].iloc[0]] #this is a list comprehension

    #last element is empty
    headers[ len(headers)-1 ] = "Professore"

    print (headers)
    #remove first row    
    tables[0] = tables[0].iloc[1:]

    #create dataframe
    dataframe = pd.DataFrame(tables[0], ) #converted to pd dataframe to be able to rename
    
    #rename columns
    for i in range(1, len(headers)):
        dataframe = dataframe.rename(columns={ dataframe.columns[i] : headers[i] }, inplace = False, errors="raise")

    return dataframe

def parse_excel (filename, header):
    file = "./" + filename
    dataframe = pd.read_excel(file,  header=1)
    #clean the dataframe
    dataframe = clean_input(dataframe)
    #rename columns
    for i in range(1, len(header)):
        dataframe = dataframe.rename(columns={ dataframe.columns[i] : header[i] }, inplace = False, errors="raise")
    
    return dataframe

def put_in_calendario (dataframe, calendario):
    valid_rows = dataframe[
        (dataframe.iloc[:, 0] != "Domenica") &
        (dataframe.iloc[:, 0] != "Sabato") &
        (dataframe.iloc[:, 7].notna()) &
        (dataframe.iloc[:, 8].notna())
    ]

    for _, row in valid_rows.iterrows():
        data = cleanDataRows(row)
        lezione = Lezione(*data.iloc[[2, 3, 7, 8, 10]].astype(str))
        calendario.add_lezione_to_date(data.iloc[1], lezione)

    return calendario

def cleanDataRows(data):
    for i in range(len(data)):
        data.iloc[i] = repr(data.iloc[i])
        data.iloc[i] = clean_input(data.iloc[i])
        if data.iloc[i].lower() == "nan":
            data.iloc[i] = data.iloc[i] = " "
    return data

def clean_input(inputText): #removes special characters, and stuff that can screw up the calendar creation
    filter_space = ["\\r", "\\n", "\\t"]
    for i in filter_space:
        inputText = inputText.replace(i, " ")
    inputText = inputText.replace(",", " ")
    inputText = inputText.replace(".", "")
    inputText = inputText.replace("'", "")
    return inputText



if __name__ == "__main__":
    header = ['nan', 'Data', 'Orario inizio', 'Orario fine', 'Ore formazion e', 'Ore Gruppi', 'Ore COD', 'Unità formativa', 'Materia', 'Sede', 'Professore']
    # dataframeA = parse_pdf("input.pdf") 
    dataframe = parse_excel("calendario.xlsx", header)
    



    calendario = Calendario() #create calendar object
    calendario = put_in_calendario(dataframe, calendario) #put lezioni in calendar

    calendario.to_ical() #convert calendar to ical
    print(calendario)