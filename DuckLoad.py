# Importo le librerie necessarie
from pyflipper.pyflipper import PyFlipper
from rich.console import Console
from rich.style import Style
import time, platform, sys, requests

# Init dell'oggetto Console()
console = Console()

# Controllo il sistema operativo e in base a questo 
# seleziono la porta USB
if(platform.system() == 'Windows'):
    flipper = PyFlipper(com="COM6")
elif(platform.system() == 'Linux'):
    flipper = PyFlipper(com="/dev/ttyACM0")

# Gestione Ascii Art 
myStyle = Style(color="#ffd700", bold=True)
myStyle2 = Style(color="#CC5500", bold=True)
myStyle3 = Style(color="#70d095", bold=True)
myStyle4 = Style(color="#c70039", bold=True)
link = "Github: https://github.com/Kobra3390"

try:
    def print_help():
        help_text = """
        Usage:
        \tDuckLoad.py -h               [ Show this help message and exit ]
        \tDuckLoad.py -d               [ Delete a file from FlipperZero storage ]
        \tDuckLoad.py -c               [ Upload a payload to FlipperZero storage ]
        \tDuckLoad.py -cve             [ Get information about a CVE code ]
        \tDuckLoad.py -convert         [ Convert Duckyscript to Arduino code ]
        """
        console.print(help_text, style=myStyle3)

    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        print_help()
    

    if sys.argv[1] == "-d":
        # Gestione Ascii Art 
        console.print("""
                __\t ____          _   __              _ 
            ___( o)>\t|    \ _ _ ___| |_|  |   ___ ___ _| |
            \ <_. )\t|  |  | | |  _| '_|  |__| . | .'| . |
             `---'   \t|____/|___|___|_,_|_____|___|__,|___|
        """ + "\n" + link, style=myStyle)
        console.print("-" * 60, style=myStyle)

        console.print("\n[ Enter the path of the file to delete (Example: /ext/foo/bar.txt) ]", style=myStyle)
        path = input("FlipperZero-DuckLoad:~$ ")
        time.sleep(2)
        flipper.storage.remove(file=path)
        time.sleep(2)
        console.print("\n[ Deletion of BadUSB Payload Completed. ]", style=myStyle)
        sys.exit()



    elif sys.argv[1] == "-c":
        # Gestione Ascii Art 
        console.print("""
                __\t ____          _   __              _ 
            ___( o)>\t|    \ _ _ ___| |_|  |   ___ ___ _| |
            \ <_. )\t|  |  | | |  _| '_|  |__| . | .'| . |
             `---'   \t|____/|___|___|_,_|_____|___|__,|___|
        """ + "\n" + link, style=myStyle)
        console.print("-" * 60, style=myStyle)
        # Prendo in input la patch locale del payload da caricare
        console.print("\n[ Enter a local path of payload ]", style=myStyle)
        path = input("FlipperZero-DuckLoad:~$ ")

        # Prendo in input il nome con cui apparirá il payload sul flipper
        console.print("\n[ Enter the name of the payload with which it will be displayed in the Flipper ]", style=myStyle)
        name_payload = input("FlipperZero-DuckLoad:~$ ")

        # "/ext/badkb/MyPayloads/DockerPayloads/{name_payload}.txt" 
        # "/ext/badkb/MyPayloads/MetasploitPayloads/{name_payload}.txt" 
        # "/ext/badkb/MyPayloads/VSFVenomPayloads/{name_payload}.txt" 
        # "/ext/badkb/MyPayloads/TermuxPayloads/{name_payload}.txt" 
        # "/ext/badkb/MyPayloads/{name_payload}.txt"

        myfile = f"/ext/badkb/MyPayloads/MetasploitPayloads/{name_payload}.txt" 
        mytime = True

        with open(path, 'r') as file_origine:
            print("\n")
            with console.status("[#ffd700] Loading a BadUSB Payload...", spinner="aesthetic") as status:
                while mytime:
                    # Leggi il contenuto del file
                    text = file_origine.read()
                    flipper.storage.write.start(myfile)
                    time.sleep(2)
                    flipper.storage.write.send(text)
                    time.sleep(2)
                    flipper.storage.write.stop()
                    mytime = False

        console.print("[ Upload Complete... ]", style=myStyle)

    elif sys.argv[1] == "-cve":
        # Gestione Ascii Art 
        console.print("""                                         
                                                 
             ____          _   _____ _____ _____ 
            |    \ _ _ ___| |_|     |  |  |   __|
            |  |  | | |  _| '_|   --|  |  |   __|
            |____/|___|___|_,_|_____|\___/|_____|
                                     

            """ + link, style=myStyle2)
        console.print("-" * 60, style=myStyle2)
        def get_cve_info():
            console.print("\n[ Insert CVE Code ]", style=myStyle2)
            cve_code = input("DuckLoad#cve-info> ")
            url = f"https://cve.circl.lu/api/cve/{cve_code}"
            response = requests.get(url)

            if response.status_code == 200:
                cve_info = response.json()
                console.print("\nInformation about the CVE:", style=myStyle2)
                console.print(f"Code: {cve_info['id']}", style=myStyle2)
                console.print(f"Description: {cve_info['summary']}", style=myStyle2)
                console.print(f"CVSS: {cve_info['cvss']}", style=myStyle2)
                if isinstance(cve_info['cvss'], dict):
                    console.print(f"Number of CVSS vectors: {cve_info['cvss']['vectorString']}", style=myStyle2)
                console.print(f"Publication Date: {cve_info['Published']}", style=myStyle2)
                console.print(f"Date of Last Modification: {cve_info['Modified']}", style=myStyle2)

                if 'references' in cve_info:
                    references = cve_info['references']
                    if references:
                        console.print("\nReferences to learn more:", style=myStyle2)
                        for reference in references:
                            console.print(f"- {reference}", style=myStyle2)

            else:
                console.print("The CVE was not found or an error occurred while requesting.")

        get_cve_info()

    elif sys.argv[1] == "-convert":
        console.print("""   
                                            
     ____          _   _____     _____         
    |    \ _ _ ___| |_|_   _|___|     |___ ___ 
    |  |  | | |  _| '_| | | | . |-   -|   | . |
    |____/|___|___|_,_| |_| |___|_____|_|_|___|
                                            


    """ + link, style=myStyle3)
        console.print("-" * 60, style=myStyle3)

        def convert_to_arduino(duckyscript):
            arduino_code = []
            lines = duckyscript.split("\n")
            for line in lines:
                tokens = line.strip().split(" ")
                command = tokens[0]
                if command == "DELAY":
                    delay_time = int(tokens[1])
                    arduino_code.append(f"delay({delay_time});")
                elif command == "STRING":
                    text = " ".join(tokens[1:])
                    arduino_code.append(f'Keyboard.print("{text}");')
                elif command == "REM":
                    comment = " ".join(tokens[1:])
                    arduino_code.append(f"// {comment}")
                elif command == "ENTER":
                    arduino_code.append('Keyboard.write(KEY_ENTER);')
                elif command == "ALT":
                    arduino_code.append('Keyboard.write(KEY_LEFT_ALT);')
                elif command == "CTRL":
                    arduino_code.append('Keyboard.write(KEY_LEFT_CTRL);')
                elif command == "SHIFT":
                    arduino_code.append('Keyboard.write(KEY_LEFT_SHIFT);')
                elif command == "GUI":
                    arduino_code.append('Keyboard.write(KEY_LEFT_GUI);')
                elif command == "CTRL-ALT" and len(tokens) > 1 and tokens[1] == "t":
                    arduino_code.append('Keyboard.write(KEY_LEFT_CTRL);')
                    arduino_code.append('Keyboard.write(KEY_LEFT_ALT);')
                    arduino_code.append('Keyboard.write(\'t\');')
                else:
                    # Unsupported command, ignore and proceed
                    print(f"Unsupported Duckyscript command: {command}")

            arduino_code.insert(0, "#include <Keyboard.h>")  

            return "\n".join(arduino_code)


        filename = input("Enter a badusb payload path: ")

        with open(filename, "r") as file:
            duckyscript_code = file.read()

        arduino_code = convert_to_arduino(duckyscript_code)

        with open("output_arduino_code.ino", "w") as file:
            file.write(arduino_code)
        console.print("\n[ Conversion Completed. ]\n", style=myStyle3)

except KeyboardInterrupt:
    console.print("\n\nAborting...\n\n", style=myStyle4)
