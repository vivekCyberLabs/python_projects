import ftplib
import paramiko
import mysql.connector

targets = {
    "ftp": {"host" : "127.0.0.1","port" : 21},
    "ssh": {"host" : "127.0.0.1","port" : 22},
    "mysql": {"host" : "127.0.0.1","port" : 3306}
    }

default_creds = [
    ("admin","admin"),
    ("root","toor"),
    ("Anonymous","Anonymous"),
    ("vivek","vivek"),
     ("user", "user")  
]

def ftp_check(host,port,user,password):
    try:
      Ftp = ftplib.FTP()
      Ftp.connect(host,port)
      Ftp.login(user,password)
      print(f"Ftp login succssfull.. username = {user} and password = {password}")
      Ftp.quit()
      return True
    except Exception as e:
        print(f" Ftp Connection failed")
        return False


def ssh_check(host,port,user,password):
   try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,port=port,username=user,password=password)
    print(f"SSH connection succesful {user} and {password}")
    ssh.close()
    return True
   except Exception as e:
      print(f"ssh login failed")
      return False
   


def mysql_check(host,port,user,password):
  try:
     conn = mysql.connector.connect(
      host = host,
      port = port,
      user = user,
      password = password,
      connection_timeout = 5
   )
     conn.close()
     print(f"mysql connection successful {user}/{password}")
  except Exception as e:
     print(f"Mysql connection was not successful ")




for service, info in targets.items(): 
    print(f"Targeting on {info['host']} port {info['port']} service {service}")
    for user,password in default_creds:
        if service == "ftp" and ftp_check(info["host"],info["port"],user,password):
            break
        elif service == "ssh" and ssh_check(info["host"],info["port"],user,password):
           break
        elif service == "mysql" and mysql_check(info["host"],info["port"],user,password):
           break
            
