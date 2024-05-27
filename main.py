import json
from Calendario import Calendario
from Giorno import Lezione
import tabula
import pandas as pd


def parse_pdf (filename):
    file = "./" + filename
    tables = tabula.read_pdf(file, pages="all", multiple_tables=False, guess=True)

    headers = []
    #extract [1] as header
    for i in tables[0].iloc[0]:
        i = str(i)
        i = repr(i)
        #remove \r and \n , replace with space
        i = i.replace("\\r", " ")
        i = i.replace("\\n", " ")
        i = i.replace("\\t", " ")
        i = i.replace(",", " ")
        i = i.replace(".", " ")
        i = f"{i}"
        headers.append(i)
    #last element is empty
    headers[ len(headers)-1 ] = "Professore"
    print (headers)

    #remove first row    
    tables[0] = tables[0].iloc[1:]

    #create dataframe
    dataframe = pd.DataFrame(tables[0])
    
    for i in range(1, len(headers)):
        dataframe = dataframe.rename(columns={ dataframe.columns[i] : headers[i] }, inplace = False, errors="raise")
    return dataframe

def put_in_calendario (dataframe, calendario):
    for row in dataframe.iterrows():
        data = row[1]
        if data[0] == "Domenica" or data[0] == "Sabato":
            continue
        if str(data[7]).lower() == "nan" or str( data[8]).lower() == "nan" or data[7] == None or data[8] == None:
            continue
        for i in range(len(data)):
            
            data[i] = repr(data[i])
            data[i] = data[i].replace("\\n", " ")
            data[i] = data[i].replace("\\r", "")
            data[i] = data[i].replace("\\t", " ")
            data[i] = data[i].replace(",", " ")
            if data[i].lower() == "nan":
                data[i] = " "
            

        lezione = Lezione(data[2], data[3], data[7], data[8], data[10])
        calendario.add_lezione_to_date(data[1], lezione)

    return calendario


def main ():
    dataframe = parse_pdf("input.pdf")
    #print (dataframe)
    calendario = Calendario()
    calendario = put_in_calendario(dataframe, calendario)
    calendario.to_ical()

    

    

    print(calendario)
if __name__ == "__main__":
    main()