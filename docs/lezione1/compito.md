#  Scelta treno

Un treno viene rappresentato con una lista di cinque elementi: il codice del
treno, la stazione di partenza, la stazione di arrivo, ora di partenza, minuto
di partenza.
Si prenda come esempio `treno1 = ['AV1002', 'Milano Centrale', 'Napoli
Centrale', 18, 30]` che corrisponde al treno con codice `AV1002` che parte da
Milano Centrale alle 18:30, con destinazione Napoli Centrale.

Si ricevono in ingresso 4 treni:
1.  `treno1 = ['AV1002', 'Milano Centrale', 'Napoli Centrale', 18, 30]`
2.  `treno2 = ['AV1022', 'Milano Centrale', 'Napoli Centrale', 19, 10]`
3.  `treno3 = ['AV1012', 'Napoli Centrale', 'Milano Centrale', 18, 50]`
4.  `treno4 = ['AV1011', 'Napoli Centrale', 'Milano Centrale', 19, 00]`

Scrivere un notebook che determini:
1.  il primo treno che parte dopo le 18:45
1.  il primo treno che parte da Milano Centrale dopo le 18:45
1.  il primo treno che parte da Milano Centrale dopo le 20:00

Riflettere sui seguenti aspetti:

1.  Come posso gestire un elenco arbitrario di treni, di cui non conosco la
    numerosità?
1.  Come posso essere sicuro di non avere due treni con lo stesso codice?
