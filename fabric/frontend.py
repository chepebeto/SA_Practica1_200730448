from fabric import Connection
connection = Connection(host="chepebeto_1590@34.136.129.108", connect_kwargs = {"password":"123456"})


from fabric import Connection

from fabric import Connection

c = Connection(
    host="34.136.129.108",
    user="chepebeto_1590",
    connect_kwargs={
        "key_filename": "/home/chepebeto_1590/.ssh/id_rsa.pub",
        "passphrase": ""
    },
)

with c.cd("practica2"):

    result = c.run("ls")
    result = c.run("apt-get update")
    result = c.run("apt-get upgrade")
    resutl = c.run("apt-get install docker-ce docker-ce-cli containerd.io")
    result = c.run("docker login -u deployToken -p x_m1vY1WaD6csbew38Nt registry.gitlab.com")
    result = c.run("docker-compose down --rmi=all")
    result = c.run("docker-compose pull")
    result = c.run("docker-compose build")
    result = c.run("docker-compose up -d")
    result = c.run("docker logout")

    c.close()