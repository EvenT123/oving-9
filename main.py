class Flervalgspørsmål:
    def __init__(self, spørsmåltekst, svaralternativ, riktigSvar):
        self.x = spørsmåltekst
        self.y = svaralternativ
        self.z = riktigSvar

    def sjekk_svar(self, svar, fasit):
        self.f = svar
        if self.f == fasit + 1:
            print("Riktig!")
        else:
            print("Feil!")
    def __str__(self):
        return f"{self.x} \n1: {self.y[0]} \n2: {self.y[1]} \n3: {self.y[2]}"

spørsmåltekst1 = "\nHvilken bil er fra italia?"
svarAlternativ1 = ["Ferari", "Audi", "Mazda"]
riktigSvar1 = 0

spørsmåltekst2 = "\nHvilken skole er best?"
svarAlternativ2 = ["UIO", "UIS", "OsloMet"]
riktigSvar2 = 1

spm1 = Flervalgspørsmål(spørsmåltekst1, svarAlternativ1, riktigSvar1)
print(str(spm1))
brukerSvar1 = int(input("Hvilket svar er riktig?: "))
spm1.sjekk_svar(brukerSvar1, riktigSvar1)

spm2 = Flervalgspørsmål(spørsmåltekst2, svarAlternativ2, riktigSvar2)
print(str(spm2))
brukerSvar2 = int(input("Hvilket svar er riktig?: "))
spm1.sjekk_svar(brukerSvar2, riktigSvar2)
