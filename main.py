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


import ftplib

# Funzione per connettersi al server FTP
def connect_ftp(server_ip, username, password):
    try:
        # Creazione dell'oggetto FTP
        server = ftplib.FTP()
        
        # Connessione al server
        server.connect(server_ip)
        print(f"Connesso al server {server_ip}")
        
        # Login con le credenziali
        server.login(username, password)
        print(f"Login riuscito con l'utente {username}")

        server.retrlines('LIST')  

        # Chiudi la connessione
        server.quit()
        print("Connessione chiusa.")
    except ftplib.all_errors as e:
        print(f"Errore FTP: {e}")

# Chiedi all'utente di inserire l'indirizzo IP, username e password
ip = input("Inserisci l'indirizzo IP del server FTP --> ")
username = input("Inserisci l'username --> ")
password = input("Inserisci la password --> ") 

# Chiama la funzione per connetterti
connect_ftp(ip, username, password)
