class DBmServer:

    def __init__(self, name, port, use_ssl):
        self.name = name
        self.port = port
        self.use_ssl = use_ssl

    def __str__(self):
        return self.name + ":" + self.port

    def __repr__(self):
        return self.name + ":" + self.port

