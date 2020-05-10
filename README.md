# Trova stringhe in files

Semplice routine per cercare una serie di stringhe in alcuni files.

```
Uso: trova.py -f <nome_file_ricerca> -d <directory_log> [-c <int>] [-s]

dove

(OBBLIGATORI)
<nome_file_ricerca>    file che contiene le stringhe da cercare
<directory_log>        directory che contiene i file in cui cercare

(opzionali)
-c <int>               numero minimo di occorrenze per la visualizzazione
-s                     case sensitive = True
