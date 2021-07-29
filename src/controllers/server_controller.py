from mcstatus import MinecraftServer

server = MinecraftServer.lookup("ccserver:25565")


def status():
    response = {}
    try:
        current_status = server.status()
        response["players"] = current_status.players
        response["version"] = current_status.version
        response["latency"] = current_status.latency
        response["status"] = "online"

    except:
        response["status"] = "offline"

    return response


def query():
    return server.query()
