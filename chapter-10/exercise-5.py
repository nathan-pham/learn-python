handle = open("files/mbox-short.txt", "r")
hosts = {}

for line in handle:
  if line.startswith("From") and len(line.split()) > 2 and "@" in line:
    host_index = line.find("@")
    space_index = line.find(" ", host_index)
    host = line[host_index + 1:space_index]
    hosts[host] = hosts.get(host, 0) + 1

print(hosts)