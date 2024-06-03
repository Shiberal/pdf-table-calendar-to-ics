from Lezioni import Lezioni
class Lezione:

    def __init__(self,  ora_inizio : str, ora_fine : str, unita : str, materia : str, professore:str):
        #parse orario from "10 00" to icalendar compatible
        ora_inizio = self.fix_hours(ora_inizio)
        ora_fine = self.fix_hours(ora_fine)
        self.ora_inizio = ora_inizio
        self.ora_fine = ora_fine
        self.unita = unita
        if materia.lower() == " ":
            self.materia = unita
        else:
            self.materia = materia
        self.professore = professore

    def fix_hours(self, ora):
        ora = ora.replace("'", "")
        ora = ora.split(" ")
        ora = ora[0] + ":00"
        return ora

    def __str__ (self):
        return f"Ora Inizio: {self.ora_inizio} Ora Fine: {self.ora_fine} \nUnita: {self.unita} Materia: {self.materia} Professore: {self.professore}"

