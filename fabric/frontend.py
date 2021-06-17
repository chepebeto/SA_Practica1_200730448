from fabric import Connection
#connection = Connection(host="chepebeto_1590@34.136.129.108", connect_kwargs = {"password":"123456"})

connection = Connection(
    host="34.136.129.108",
    user="chepebeto_1590",
    connect_kwargs={
        "key_filename": "/home/chepebeto_1590/.ssh/id_rsa.pub",
    }   
)

connection.run("pwd")