# Valutazione carte 2


In input si ricevono due liste di 5 carte, dove ogni carta è indicate con una
stringa di 2 caratteri, valore-seme, come nell'esercizio precedente.
Le due liste si chiamano `carteA` e `carteB`.

L'obiettivo è determinare quale dei due giocatori ha una combinazione di valore
maggiore. Determinare la combinazione corrispondente ad *una* lista di 5 carte è
stato l'esercizio precedente.

Le combinazioni, in ordine decrescente di valore sono:

*  scala reale: i valori di tutte le carte sono consecutivi (ad esempio 9, 10, J, Q, K) e tutti
dello stesso seme. Esempio: `["2Q", "3Q", "4Q", "5Q", "6Q"]`
*  poker: quattro carte con lo stesso valore. Esempio: `["2Q", "5Q", "5C", "5P", "5F"]`
*  full: tre carte con lo stesso valore e altre 2 carte con lo stesso valore.
   Esempio: `["5Q", "5C", "5P", "1Q", "1F"]`
*  colore: cinque carte con lo stesso seme. Esempio: `["4Q", "5Q",  "0Q", "KQ", "1Q" ]`
*  scala: i valori di tutte le carte sono consecutivi. Esempio: `["0Q", "JQ", "QC", "KF", "1Q"]`
*  tris: tre carte con lo stesso valore. Esempio: `["5Q", "5C", "5P", "0F", "1Q"]`
*  doppia coppia: due coppie di carte con lo stesso valore. Esempio: `["5Q", "5C", "KF", "1Q", "1P"]`
*  coppia: due carte con lo stesso valore. Esempio: `["5C", "5P", "7F", "0Q", "1Q"]`
*  carta singola: nessuna delle combinazioni precedenti. Esempio: `["2Q", "4C", "6Q", "7P", "9F"]`


Le carte nella lista sono in  ordine crescente di valore e le liste non contengono carte ripetute.
Se due giocatori hanno la stessa combinazione, si ha un pareggio.

### Varianti

Le seguenti varianti rendono decisamente più complicata la soluzione. Non è
obbligatorio risolverle.

1.  Nel caso i due giocatori abbiano stessa combinazione, si seguono dei criteri
    aggiuntivi:
    *  scala o scala reale. Si guarda il valore dell'ultima carta (quella di
       valore più elevato). Vince chi ha la carta di valore più elevato, a
       parità di valore il seme della carta, nell'ordine (dal migliore al
       peggiore) "C", "Q", "F", "P";
    *  poker. si guarda il valore delle quattro carte identiche;
    *  tris o full. si guarda il valore delle tre carte identiche;
    *  colore. Si guarda il valore della carta di massimo valore;
    *  coppia. Si guarda il valore delle due carte identiche. In caso di parità
       si guarda chi ha la carta di cuori.
    *  doppia coppia. Si guarda il valore delle due carte identiche di valore maggiore. In caso di parità
       si guarda il valore delle due carte identiche di valore minore. In caso
       di ulteriore parità si guarda il valore (e il seme) della quinta carta.
2.  Le carte in input non sono già ordinate.
