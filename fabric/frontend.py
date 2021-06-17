#from fabric import Connection
#connection = Connection(host="chepebeto_1590@34.136.129.108", connect_kwargs = {"password":"123456"})
#connection.run("sudo adduser jenkins")

import paramiko
client = paramiko.SSHClient()

ssh.connect(hostname='34.136.129.108', username='chepebeto_1590', password='123456')
shh.connect.run("pwd")

