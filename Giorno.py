
class Lezione:

    def __init__(self,  ora_inizio : str, ora_fine : str, unita : str, materia : str, professore:str):
        #parse orario from "10 00" to icalendar compatible
        ora_inizio = ora_inizio.split(" ")
        ora_inizio = ora_inizio[0] + ":00"

        ora_fine = ora_fine.split(" ")
        ora_fine = ora_fine[0] + ":00"

        self.ora_inizio = ora_inizio
        self.ora_fine = ora_fine
        self.unita = unita
        self.materia = materia
        self.professore = professore

    def __str__ (self):
        return f"Ora Inizio: {self.ora_inizio} Ora Fine: {self.ora_fine} \nUnita: {self.unita} Materia: {self.materia} Professore: {self.professore}"

class Lezioni:
    def __init__(self, data):
        self.data = data
        self.lezioni = []

    def aggiungi_lezione(self,lezione):
        self.lezioni.append(lezione) 
    
    

    def rimuovi_lezione(self, lezione_toremove):
        for lezione in self.lezioni:
            if lezione == lezione_toremove:
                self.lezioni.remove(lezione)

    def __str__ (self):
        out = ""
        out += f"Data: {self.data}\n"
        for lezione in self.lezioni:
            out += str(lezione) + "\n"
        return out