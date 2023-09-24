# Introduzione a DuckLoad

DuckLoad é uno script in python3 che sfrutta la libreria `pyflipper` di [wh00hw](https://github.com/wh00hw/pyFlipper) per interagire con il device Flipper Zero.

La funzione base di DuckLoad é quella di caricare / cancellare payload badusb, ma non solo, le funzioni specifiche vengono spiegate di seguito: 

- `-h`: Mostra l'healper di DuckLoad.
- `-d`: Cancella un payload badusb dallo storage interno del Flipper Zero, dovrá essere specificata la path interna del file che si vuole cancellare.
- `-c`: Permette di caricare un payload badusb dal computer locale allo storage interno del Flipper Zero, per farlo, lo script necessita della path locale del computer dove risiede il payload. Oltre questo va specificato il nome con cui il payload verrá mostrato all'interno del Flipper. **Nota:** sará necessario modificare la seguente variabile per specificare la path interna dove lo script caricherá il payload: `myfile = f"/ext/badkb/MyPayloads/{name_payload}.txt"`.
- `-cve`: Essendo che lo script puó automatizzare l'esecuzione di moduli Metasploit codificati in payload badusb, questa funzione permette di ricercare info su CVE pubbliche nel formato CVE-XXX-XXX.
- `-convert`: Permette di convertire un payload badusb in un programma .ino, questa funzione puó essere utile per riutilizzare payload su board come la DigiSpark.
- `-db`: Permette di convertire una directory con payload badusb in formato .txt in un database. 

---

# Casi d'Uso
**Nota**: per poter usare le seguenti funzioni bisognerá collegare il Flipper al proprio computer e in seguito avviare lo script. 

Caricare un Payload:
```powershell
PS C:\Users\User\Desktop\DuckLoad> python .\DuckLoad.py -c

                __       ____          _   __              _ 
            ___( o)>    |    \ _ _ ___| |_|  |   ___ ___ _| |
            \ <_. )     |  |  | | |  _| '_|  |__| . | .'| . |
            `---'       |____/|___|___|_,_|_____|___|__,|___|
        
Github: https://github.com/Kobra3390
------------------------------------------------------------

[ Enter a local path of payload ]
FlipperZero-DuckLoad:~$ input.txt

[ Enter the name of the payload with which it will be displayed in the Flipper ]
FlipperZero-DuckLoad:~$ input


[ Upload Complete... ]
PS C:\Users\User\Desktop\DuckLoad>
```

Eliminare un Payload:
```powershell
PS C:\Users\User\Desktop\DuckLoad> python .\DuckLoad.py -d

                __       ____          _   __              _ 
            ___( o)>    |    \ _ _ ___| |_|  |   ___ ___ _| |
            \ <_. )     |  |  | | |  _| '_|  |__| . | .'| . |
            `---'       |____/|___|___|_,_|_____|___|__,|___|
        
Github: https://github.com/Kobra3390
------------------------------------------------------------

[ Enter the path of the file to delete (Example: /ext/foo/bar.txt) ]
FlipperZero-DuckLoad:~$ /ext/badkb/MyPayloads/MetasploitPayloads/input.txt          

[ Deletion of BadUSB Payload Completed. ]
```

Ricercare Info su una CVE:
```powershell
PS C:\Users\User\Desktop\DuckLoad> python .\DuckLoad.py -cve


             ____          _   _____ _____ _____ 
            |    \ _ _ ___| |_|     |  |  |   __|
            |  |  | | |  _| '_|   --|  |  |   __|
            |____/|___|___|_,_|_____|\___/|_____|


            Github: https://github.com/Kobra3390
------------------------------------------------------------

[ Insert CVE Code ]
DuckLoad#cve-info> CVE-2017-5715

Information about the CVE:
Code: CVE-2017-5715
Description: Systems with microprocessors utilizing speculative execution and indirect branch prediction may allow unauthorized disclosure of information to an attacker with local user access via 
a side-channel analysis.
CVSS: 1.9
Publication Date: 2018-01-04T13:29:00
Date of Last Modification: 2021-08-16T09:15:00

References to learn more:
- https://www.synology.com/support/security/Synology_SA_18_01
- https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/
- https://support.lenovo.com/us/en/solutions/LEN-18282
- https://support.f5.com/csp/article/K91229003
- https://spectreattack.com/
- https://security-center.intel.com/advisory.aspx?intelid=INTEL-SA-00088&languageid=en-fr
- https://security.googleblog.com/2018/01/todays-cpu-vulnerability-what-you-need.html
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV180002
- https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-with-side.html
- https://blog.mozilla.org/security/2018/01/03/mitigations-landing-new-class-timing-attack/
- https://aws.amazon.com/de/security/security-bulletins/AWS-2018-013/
- https://access.redhat.com/security/vulnerabilities/speculativeexecution
- http://xenbits.xen.org/xsa/advisory-254.html
- http://www.securitytracker.com/id/1040071
<SNIP>
```

Conversione Payload BadUSB in Programma `.ino`:
```powershell
PS C:\Users\User\Desktop\DuckLoad> python .\DuckLoad.py -convert
   

     ____          _   _____     _____
    |    \ _ _ ___| |_|_   _|___|     |___ ___ 
    |  |  | | |  _| '_| | | | . |-   -|   | . |
    |____/|___|___|_,_| |_| |___|_____|_|_|___|



    Github: https://github.com/Kobra3390
------------------------------------------------------------
Enter a badusb payload path: input.txt

[ Conversion Completed. ]
```

**Nota**: per quest'ultima funzionalità consiglio di dare sempre una doverosa controllata al codice `.ino` che viene generato, perchè in alcune casistiche potrebbe generare codice errato. 

Convertire una Directory contente payload BadUSB in un Database:
```powershell
PS C:\Users\User\Desktop\DuckLoad> python .\DuckLoad.py -db

[ Enter the path to the directory containing text files ]
DuckLoad-DB:~$ DatabaseBadUSBPayloadFlipperZero

[ Enter the SQLite database name ]
DuckLoad-DB:~$ test-db.db
The files in the directory 'DatabaseBadUSBPayloadFlipperZero' and its subdirectories have been inserted into the 'test-db.db' database.
```
Una volta creato il file .db, può essere visualizzato, ad esempio su Visual Studio Code con l'estensione SQLite Viewer.

---

# Prerequisiti per Usare lo Script
Per poter usare DuckLoad bisogna avere sulla propria macchina installato l'interprete Python3 aggiornato all'ultima versione. Oltre a questo DuckLoad necessita dei seguenti pacchetti: _pyflipper_, _rich_.

Per poterli installare usiamo il gestore di pacchetti pip3 con il file `requirements.txt`:

```powershell
pip3 install -r requirements.txt
```




























