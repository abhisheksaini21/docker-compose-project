import os
from pyfiglet import Figlet
#from os import system,path

def render(text,style):
	f=Figlet(font=style)
	print('\n'*1)
	print(f.renderText(text))
os.system("clear")
os.system("tput setaf 10")
render('DOCKER-COMPOSE LAUNCHING MULTIPLE CONTAINERS','bubble')

os.system("tput setaf 3")
render('\t BY ABHISHEK  SAINI','digital')

print("To continue.... press any key")
input()

while True:
      os.system("clear")
      os.system("tput setaf 33")
      render('DOCKER COMPOSE','epic')
      os.system("tput setaf 2")
                
      print("Press 1. Run wordpress/mysql infrastructure(docker-compose)")
      print("Press 2. Stop docker-compose")
      print("Press 3. Start docker-compose")
      print("Press 4. Remove complete infrastructure")
      print("Press 5. EXIT")
      print("Enter Your Choice: ",end=" ")
      ch2=input()
      os.system("tput setaf 3")
                
      if int(ch2)==1:
           os.system("docker-compose up -d")
           print("Infrastructure Setup Complete.....")
           input()
                     

      elif int(ch2)==2:
            os.system("docker-compose stop")
            print("Stopped.....")
            input()
                     

      elif int(ch2)==3:
            os.system("docker-compose start")
            print("Started.....")
            input()
                     
      elif int(ch2)==4:
            os.system("docker-compose rm")
            print("Removed.....")
            input()
                     

      elif int(ch2)==5:
            os.system("clear")
            os.system("tput setaf 3")
            render('THANK YOU','sblood')
            os.system("tput setaf 7")
            break
        
   

 
