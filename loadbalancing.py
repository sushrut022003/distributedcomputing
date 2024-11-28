class RoundBinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0
    def get_next_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server
    def add_server(self, server):
        self.servers.append(server) 
    def remove_server(self, server):
        self.servers.remove(server)
        if self.index >= len(self.servers):
            self.index = 0
if __name__ == "__main__":
    servers = input("Enter the server names: ").split(',')
    load_balancer = RoundBinLoadBalancer(servers)
            
    for i in range(11):
        server = load_balancer.get_next_server()
        print(f"Request {i+1} is handled by {server}")  

