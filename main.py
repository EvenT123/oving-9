class Flervalgspørsmål:
    def __init__(self, spørsmåltekst, svaralternativ, riktigSvar):
        self.x = spørsmåltekst
        self.y = svaralternativ
        self.z = riktigSvar

    def __str__(self):
        return f"{self.x} \n1: {self.y[0]} \n2: {self.y[1]} \n3: {self.y[2]}"

    def sjekk_svar(self, svar):
        self.f = svar
        if self.f == riktigSvar + 1:
            print("Riktig!")
        else:
            print("Feil!")


spørsmåltekst = "Hvilken bil er fra italia?"
svarAlternativ = ["Ferari", "Audi", "Mazda"]
riktigSvar = 0

x = Flervalgspørsmål(spørsmåltekst, svarAlternativ, riktigSvar)
print(str(x))
brukerSvar = int(input("Hvilket svar er riktig?: "))
x.sjekk_svar(brukerSvar)
