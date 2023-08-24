# Introduzione a DuckLoad

DuckLoad é uno script in python3 che sfrutta la libreria `pyflipper` scritta da [wh00hw]([https://link-url-here.org](https://github.com/wh00hw/pyFlipper)https://github.com/wh00hw/pyFlipper) per interagire con il device Flipper Zero.

La funzione base di DuckLoad é quella di caricare / cancellare payload badusb, ma non sono, le funzioni specifiche vengono spiegate di seguito: 

- `-d`: Cancella un payload badusb dallo storage interno del Flipper Zero, dovrá essere specificata la path interna del file che si vuole cancellare.
- `-c`: Permette di caricare un payload badusb dal computer locale allo storage interno del Flipper Zero, per farlo, lo script necessitá della path locale del computer dove risiede il payload. Oltre questo va specificato il nome con cui il payload verrá mostrato all'interno del Flipper. **Nota:** sará necessario modificare la seguente variabile per specificare la path interna dove lo script caricherá il payload: `myfile = f"/ext/badkb/MyPayloads/{name_payload}.txt"`.
- `-cve`: Essendo che lo script puó automatizzare l'esecuzione di moduli Metasploit codificati in payload badusb, questa funzione permette di ricercare info su CVE pubbliche nel formato CVE-XXX-XXX.
- `-convert`: Permette di convertire un payload badusb in un programma .ino, questa funzione puó essere utile per riutilizzare payload su board come la DigiSpark.

---

# Casi d'Uso
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
- http://www.kb.cert.org/vuls/id/584653
- http://nvidia.custhelp.com/app/answers/detail/a_id/4609
- https://www.vmware.com/us/security/advisories/VMSA-2018-0002.html
- https://www.exploit-db.com/exploits/43427/
- https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180104-cpusidechannel
- https://support.citrix.com/article/CTX231399
- https://security.netapp.com/advisory/ntap-20180104-0001/
- http://www.securityfocus.com/bid/102376
- http://packetstormsecurity.com/files/145645/Spectre-Information-Disclosure-Proof-Of-Concept.html
- http://nvidia.custhelp.com/app/answers/detail/a_id/4614
- http://nvidia.custhelp.com/app/answers/detail/a_id/4613
- http://nvidia.custhelp.com/app/answers/detail/a_id/4611
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00016.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00014.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00013.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00012.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00009.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00008.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00007.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00006.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00005.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00004.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00003.html
- http://lists.opensuse.org/opensuse-security-announce/2018-01/msg00002.html
- https://www.vmware.com/us/security/advisories/VMSA-2018-0004.html
- https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03805en_us
- https://usn.ubuntu.com/usn/usn-3516-1/
- http://www.oracle.com/technetwork/security-advisory/cpujan2018-3236628.html
- https://access.redhat.com/errata/RHSA-2018:0292
- https://www.debian.org/security/2018/dsa-4120
- http://www.arubanetworks.com/assets/alert/ARUBA-PSA-2018-001.txt
- https://security.FreeBSD.org/advisories/FreeBSD-SA-18:03.speculative_execution.asc
- https://usn.ubuntu.com/3597-2/
- https://usn.ubuntu.com/3597-1/
- https://usn.ubuntu.com/3594-1/
- https://usn.ubuntu.com/3582-2/
- https://usn.ubuntu.com/3582-1/
- https://usn.ubuntu.com/3581-2/
- https://usn.ubuntu.com/3581-1/
- https://usn.ubuntu.com/3580-1/
- https://usn.ubuntu.com/3561-1/
- https://usn.ubuntu.com/3560-1/
- https://usn.ubuntu.com/3549-1/
- https://usn.ubuntu.com/3531-1/
- https://usn.ubuntu.com/3542-2/
- https://www.vmware.com/security/advisories/VMSA-2018-0007.html
- https://usn.ubuntu.com/3541-2/
- https://usn.ubuntu.com/3540-2/
- https://usn.ubuntu.com/3531-3/
- https://usn.ubuntu.com/3620-2/
- https://www.debian.org/security/2018/dsa-4188
- https://www.debian.org/security/2018/dsa-4187
- https://lists.debian.org/debian-lts-announce/2018/05/msg00000.html
- https://cert.vde.com/en-us/advisories/vde-2018-003
- https://cert.vde.com/en-us/advisories/vde-2018-002
- https://www.kb.cert.org/vuls/id/180049
- https://developer.arm.com/support/arm-security-updates/speculative-processor-vulnerability
- https://www.debian.org/security/2018/dsa-4213
- https://usn.ubuntu.com/3690-1/
- https://lists.debian.org/debian-lts-announce/2018/07/msg00016.html
- https://lists.debian.org/debian-lts-announce/2018/07/msg00015.html
- http://www.oracle.com/technetwork/security-advisory/cpujul2018-4258247.html
- https://support.hpe.com/hpsc/doc/public/display?docLocale=en_US&docId=emr_na-hpesbhf03871en_us
- https://lists.debian.org/debian-lts-announce/2018/09/msg00007.html
- https://lists.debian.org/debian-lts-announce/2018/09/msg00017.html
- http://www.oracle.com/technetwork/security-advisory/cpuoct2018-4428296.html
- https://usn.ubuntu.com/3777-3/
- https://www.mitel.com/en-ca/support/security-advisories/mitel-product-security-advisory-18-0001
- https://security.gentoo.org/glsa/201810-06
- https://help.ecostruxureit.com/display/public/UADCO8x/StruxureWare+Data+Center+Operation+Software+Vulnerability+Fixes
- https://seclists.org/bugtraq/2019/Jun/36
- http://www.arubanetworks.com/assets/alert/ARUBA-PSA-2019-003.txt
- https://www.oracle.com/technetwork/security-advisory/cpujul2019-5072835.html
- https://cert-portal.siemens.com/productcert/pdf/ssa-608355.pdf
- https://security.FreeBSD.org/advisories/FreeBSD-SA-19:26.mcu.asc
- https://seclists.org/bugtraq/2019/Nov/16
- http://packetstormsecurity.com/files/155281/FreeBSD-Security-Advisory-FreeBSD-SA-19-26.mcu.html
- https://security.paloaltonetworks.com/CVE-2017-5715
- https://lists.debian.org/debian-lts-announce/2020/03/msg00025.html
- https://lists.debian.org/debian-lts-announce/2021/08/msg00019.html
```

Conversione Payload BadUSB in Programma .ino:
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
