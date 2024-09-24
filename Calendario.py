from datetime import datetime
from datetime import timedelta
from Giorno import Lezione, Lezioni
from ics import Calendar, Event

class Calendario:
    def __init__(self):
        self.giorni = []

    def aggiungi_giorno(self, data):
        self.giorni.append(Lezioni(data))
    
    def do_Date_Exist(self, data):
        for giorno in self.giorni:
            if data == giorno.data:
                return True
        return False
    
    def add_lezione_to_date(self, data, lezione):
        if self.do_Date_Exist(data):
            self.aggiungi_lezione(data, lezione)
        else:
            self.aggiungi_giorno(data)
            self.aggiungi_lezione(data, lezione)

    def rimuovi_giorno(self, giorno_toremove):
        self.giorni.remove(giorno_toremove)

    def aggiungi_lezione(self, data, lezione):
        for giorno in self.giorni:
            if data == giorno.data:
                giorno.aggiungi_lezione(lezione)

    def rimuovi_lezione(self, data, lezione_toremove):
        for giorno in self.giorni:
            if data == giorno.data:
                giorno.rimuovi_lezione(lezione_toremove)

    def __str__(self):
        out = ""
        for giorno in self.giorni:
            out += str(giorno) + "\n"
        return out
    
    def toList(self):
        out = []
        for giorno in self.giorni:
            out.append(giorno)
        return out
    
    def to_ical(self):
        cal = Calendar()
        for giorno in self.giorni:
            for lezione in giorno.lezioni:
                
                date = self.fix_date_format(giorno)

                lezione.ora_inizio = lezione.ora_inizio.strip("'")
                lezione.ora_fine = lezione.ora_fine.strip("'")


                start_time = datetime.strptime(lezione.ora_inizio, "%H:%M")
                end_time = datetime.strptime(lezione.ora_fine, "%H:%M")


                #subtract one hour from start and end time
                start_time = start_time - timedelta(hours=1)
                end_time = end_time - timedelta(hours=1)

                #parse orario from "10 00" to icalendar compatible
                date_start = self.fix_date(1, date, start_time)
                date_end   = self.fix_date(1, date, end_time)

                print (date_start, date_end)


                calendar = self.newEvent(cal, lezione, date_start, date_end)

        with open("output.ics", 'w') as my_file:
            my_file.writelines(calendar)

    def newEvent(self, cal, lezione, date_start, date_end):
        e = Event()
        e.name = f"{lezione.materia} \ncon {lezione.professore} "
        e.description = f" {lezione.unita} " 
        e.begin = date_start
        e.end = date_end
        cal.events.add(e)
        return str(cal)

    def fix_date (self, delta, date, time):

        date = date + timedelta(hours=time.hour-delta, minutes=time.minute)
        # 

        return date

    def fix_date_format(self, giorno):
        # date_format = str(giorno.data)
        # date_format = date_format.strip("'")
        # date_format = date_format.split("-")
        # print (date_format)
        # date_format = datetime(int(date_format[2]), int(date_format[1]), int(date_format[0]))
        # date = date_format
        date = giorno.data
        #convert Timestamp(2024-06-03 00:00:00) to datetime
        #remove Timestamp, the ( ) and the 00:00:00
        date = str(date).replace("Timestamp", "").replace("(", "").replace(")", "").replace("00:00:00", "")
        print (date)
        date = ( len(date.split("-")) > 1 ) and date.split("-") or date.split("/")
        
        print (date, " :to: " , (int(date[0]), int(date[1]), int(date[2]))) 

        date = datetime(int(date[2]), int(date[1]), int(date[0]))

        return date