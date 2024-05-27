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
    
    def to_ical(self):
        cal = Calendar()

        for giorno in self.giorni:

            for lezione in giorno.lezioni:
                date_format = giorno.data.strip("'")
                date_format = date_format.split("/")
                date_format = datetime(int(date_format[2]), int(date_format[1]), int(date_format[0]))
                date = date_format
                lezione.ora_inizio = lezione.ora_inizio.strip("'")
                lezione.ora_fine = lezione.ora_fine.strip("'")

                start_time = datetime.strptime(lezione.ora_inizio, "%H:%M")
                end_time = datetime.strptime(lezione.ora_fine, "%H:%M")

                #subtract one hour from start and end time
                start_time = start_time - timedelta(hours=1)
                end_time = end_time - timedelta(hours=1)

                date_start = date.replace(hour=start_time.hour-1, minute=start_time.minute)
                date_end = date.replace(hour=end_time.hour-1, minute=end_time.minute)
                e = Event()
                e.name = lezione.materia
                e.description = f" {lezione.unita} \ncon {lezione.professore}" 

                e.begin = date_start
                e.end = date_end

                cal.events.add(e)
                e = None

        with open("output.ics", 'w') as my_file:
            my_file.writelines(cal)