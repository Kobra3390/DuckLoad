# Introduzione a DuckLoad

DuckLoad é uno script in python3 che sfrutta la libreria pyflipper scritta da [wh00hw]([https://link-url-here.org](https://github.com/wh00hw/pyFlipper)https://github.com/wh00hw/pyFlipper) per interagire con il device Flipper Zero.

La funzione base di DuckLoad é quella di caricare / cancellare payload badusb, ma non sono, le funzioni specifiche vengono spiegate in seguito: 

- -d: Cancella un payload badusb dallo storage interno del Flipper Zero, dovrá essere specificata la path interna del file che si vuole cancellare
- -c: Permette di caricare un payload badusb dal computer locale allo storage interno del Flipper Zero, per farlo, lo script necessitá della path locale del computer dove risiede il payload. Oltre questo va specificato il nome con cui il payload verrá mostrato all'interno del Flipper.
- -cve: Essendo che lo script puó automatizzare l'esecuzione di modulo Metasploit codificati in payload badusb, questa funzione permette di ricercare info su CVE pubbliche nel formato CVE-XXX-XXX
- -convert: Permette di convertire un payload badusb in programmi .ino, questa funzione puó essere utile per riutilizzare payload su board come la DigiSpark.

---

# Come usare lo script
