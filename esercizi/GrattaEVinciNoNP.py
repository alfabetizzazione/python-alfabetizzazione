import math as m
def ricalcolaProb(nBigl, tabMontepremi, lProb):
    for i in range(lProb.size):
        lProb[i] = tabMontepremi[i][0] / float(nBigl)


def estrai(lProb):
    pTotVincenti = sum(lProb)
    numRnd = m.random()
    # numRnd = 1e-9
    # print "numRnd ", numRnd
    if numRnd < pTotVincenti:
        cumulata = lProb[0]
        i = 1
        while i < len(lProb):
            # print "cumul ", cumulata, " premio ", i
            if numRnd < cumulata:
                return i - 1
            else:
                cumulata += lProb[i]
                i += 1
        return i - 1
    else:
        return len(lProb)


def aggiornaPremi(tabMontepremi, iPremio):
    if tabMontepremi[iPremio][0] > 0:
        tabMontepremi[iPremio][0] -= 1


biglietti = input('inserire il numero massimo di biglietti ')
capitale = input('inserire il capitale iniziale ')

fileName = 'GrattaEVinci.csv'
montepremi = np.genfromtxt(fileName, delimiter=';', skip_header=2, dtype=int)
montepremiBkUp = montepremi.copy()
numBiglietti = 50400000

probVincita = montepremi[:, 0] / float(numBiglietti)

giocata = 0
while giocata < biglietti and capitale > 0:
    capitale -= 5
    numBiglietti -= 1
    indicePremio = estrai(probVincita)
    # print "indicePremio" , indicePremio
    if indicePremio < montepremi.shape[0]:
        # print "::: ", indicePremio, " :::", montepremi[indicePremio, 1]
        aggiornaPremi(montepremi, indicePremio)
        capitale += montepremi[indicePremio, 1]
    # print montepremi
    # print capitale
    ricalcolaProb(numBiglietti, montepremi, probVincita)
    giocata += 1

print "capitale finale = ", capitale
print "premi vinti:"
print montepremiBkUp[:, 0] - montepremi[:, 0]
