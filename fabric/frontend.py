from fabric import Connection
#connection = Connection(host="chepebeto_1590@34.136.129.108", connect_kwargs = {"password":"123456"})

connection = Connection(
    host="4.136.129.108",
    user="chepebeto_159",
    connect_kwargs={
        "key_filename": "~/.ssh/id_rsa.pub",
    },
)