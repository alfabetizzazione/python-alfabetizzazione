# Valutazione carte

In input si riceve una lista di 5 carte, dove ogni carta è indicate con una stringa di 2 caratteri, valore-seme.
Ad esempio **8P** è 8 di picche, **JC** il jack di cuori e **0Q** il 10 di
quadri.
Le carte nella lista non sono ordinate e la lista non contiene carte ripetute.

Dalla lista, determinare quale combinazione di poker corrisponde alla lista,
secondo i seguenti criteri:

*  scala reale: i valori di tutte le carte sono consecutivi (ad esempio 9, 10, J, Q, K) e tutti
dello stesso seme. Esempio: `["5Q", "2Q", "1Q", "4Q", "3Q"]`
*  poker: quattro carte con lo stesso valore. Esempio: `["5Q", "5C", "1Q", "5P", "5F"]`
*  full: tre carte con lo stesso valore e altre 2 carte con lo stesso valore. Esempio: `["5Q", "5C", "1Q", "5P", "1F"]`
*  colore: cinque carte con lo stesso seme. Esempio: `["5Q", "4Q", "KQ", "0Q", "1Q"]`
*  scala: i valori di tutte le carte sono consecutivi. Esempio: `["KF", "JQ", "1Q", "0Q", "QC"]`
*  tris: tre carte con lo stesso valore. Esempio: `["5Q", "5C", "1Q", "5P", "0F"]`
*  doppia coppia: due coppie di carte con lo stesso valore. Esempio: `["5Q", "5C", "1Q", "1P", "KF"]`
*  coppia: due carte con lo stesso valore. Esempio: `["0Q", "5C", "1Q", "5P", "7F"]`
*  carta singola: nessuna delle combinazioni precedenti. Esempio: `["5Q", "5C", "1Q", "5P", "5F"]`

Nel caso in cui la lista di carte soddisfa più di un caso (ad esempio, se
realizza  *doppia coppia*, allora realizza anche *coppia*), bisogna restituire
la prima combinazione dell'elenco. Nel caso `["5Q", "5C", "1Q", "1P", "KF"]`,
bisogna restituire *doppia coppia*
