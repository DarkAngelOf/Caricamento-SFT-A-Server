print("""
 $$$$$$\  $$$$$$$$\ $$$$$$$$\ $$$$$$$\         $$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ $$$$$$$$\  $$$$$$\  $$$$$$$$\  $$$$$$\  $$$$$$$\  
$$  __$$\ $$  _____|\__$$  __|$$  __$$\       $$  __$$\ $$  __$$\ $$$\  $$ |$$$\  $$ |$$  _____|$$  __$$\ \__$$  __|$$  __$$\ $$  __$$\ 
$$ /  \__|$$ |         $$ |   $$ |  $$ |      $$ /  \__|$$ /  $$ |$$$$\ $$ |$$$$\ $$ |$$ |      $$ /  \__|   $$ |   $$ /  $$ |$$ |  $$ |
\$$$$$$\  $$$$$\       $$ |   $$$$$$$  |      $$ |      $$ |  $$ |$$ $$\$$ |$$ $$\$$ |$$$$$\    $$ |         $$ |   $$ |  $$ |$$$$$$$  |
 \____$$\ $$  __|      $$ |   $$  ____/       $$ |      $$ |  $$ |$$ \$$$$ |$$ \$$$$ |$$  __|   $$ |         $$ |   $$ |  $$ |$$  __$$< 
$$\   $$ |$$ |         $$ |   $$ |            $$ |  $$\ $$ |  $$ |$$ |\$$$ |$$ |\$$$ |$$ |      $$ |  $$\    $$ |   $$ |  $$ |$$ |  $$ |
\$$$$$$  |$$ |         $$ |   $$ |            \$$$$$$  | $$$$$$  |$$ | \$$ |$$ | \$$ |$$$$$$$$\ \$$$$$$  |   $$ |    $$$$$$  |$$ |  $$ |
 \______/ \__|         \__|   \__|             \______/  \______/ \__|  \__|\__|  \__|\________| \______/    \__|    \______/ \__|  \__|                                                                                                                                                                                                                                                                                                                                      
""")

print("""

                               _                _     _                 _____                   _                                        _    ____     __ 
                              | |              | |   | |               |  __ \                 | |        /\                            | |  / __ \   / _|
   ___   _ __    ___    __ _  | |_    ___    __| |   | |__    _   _    | |  | |   __ _   _ __  | | __    /  \     _ __     __ _    ___  | | | |  | | | |_ 
  / __| | '__|  / _ \  / _` | | __|  / _ \  / _` |   | '_ \  | | | |   | |  | |  / _` | | '__| | |/ /   / /\ \   | '_ \   / _` |  / _ \ | | | |  | | |  _|
 | (__  | |    |  __/ | (_| | | |_  |  __/ | (_| |   | |_) | | |_| |   | |__| | | (_| | | |    |   <   / ____ \  | | | | | (_| | |  __/ | | | |__| | | |  
  \___| |_|     \___|  \__,_|  \__|  \___|  \__,_|   |_.__/   \__, |   |_____/   \__,_| |_|    |_|\_\ /_/    \_\ |_| |_|  \__, |  \___| |_|  \____/  |_|  
                                                               __/ |                                                       __/ |                          
                                                              |___/                                                       |___/                           
                                                                                             
""")


import paramiko

def connect_sftp(server_ip, username, password):
    try:
        # Creazione dell'oggetto SSHClient
        client = paramiko.SSHClient()

        # Aggiungi la chiave dell'host automaticamente (se non presente)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connessione al server SFTP
        client.connect(server_ip, username=username, password=password)
        print(f"\nConnesso al server {server_ip}")
        
        print(f"\n Connesso con l'utente {username}")

        # Avvia la sessione SFTP
        sftp = client.open_sftp()

        # Funzione per mostrare il menu
        def show_menu():
            print("\nMenu:")
            print("1. Cambia directory")
            print("2. Vedi i file nella directory corrente")
            print("3. Carica un file")
            print("4. Chiudi la connessione")

        # Funzione per cambiare directory
        def change_directory():
            new_dir = input("Inserisci il nome della directory in cui vuoi entrare: ")
            try:
                sftp.chdir(new_dir)
                print(f"\nSei ora nella directory: {sftp.getcwd()}")
            except IOError:
                print("Errore: la directory non esiste.")

        # Funzione per vedere i file nella directory corrente
        def list_files():
            print("\nContenuto della directory corrente: ")
            files = sftp.listdir()
            for file in files:
                print(file)

        # Funzione per caricare un file
        def upload_file():
            filename = input("Inserisci il percorso del file da caricare: ")
            try:
                sftp.put(filename, f'{sftp.getcwd()}/{filename}')  # Modifica il percorso remoto come necessario
                print(f"File '{filename}' caricato con successo!")
            except FileNotFoundError:
                print("Errore: file non trovato.")
            except Exception as e:
                print(f"Errore durante il caricamento del file: {e}")

        # Funzione per chiudere la connessione
        def close_connection():
            sftp.close()
            client.close()
            print("Connessione chiusa.")

        # Ciclo principale per mostrare il menù e interagire con l'utente
        while True:
            show_menu()
            choice = input("Seleziona un'opzione (1-4): ")

            if choice == '1':
                change_directory()
            elif choice == '2':
                list_files()
            elif choice == '3':
                upload_file()
            elif choice == '4':
                close_connection()
                break
            else:
                print("Scelta non valida. Per favore scegli un'opzione tra 1 e 4.")
    except Exception as e:
        print(f"Errore SFTP: {e}")

# Chiedi all'utente di inserire l'indirizzo IP, username e password
ip = input("Inserisci l'indirizzo IP del server SFTP --> ")
username = input("Inserisci l'username --> ")
password = input("Inserisci la password --> ")

# Chiama la funzione per connetterti
connect_sftp(ip, username, password)
