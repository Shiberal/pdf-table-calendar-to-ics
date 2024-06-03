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
    
    def toList(self):
        out = []
        for lezione in self.lezioni:
            out.append(lezione)
        return out