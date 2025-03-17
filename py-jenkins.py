import jenkins

server = jenkins.Jenkins('http://172.22.224.165:8080', username = 'admin', password = 'Tifalockheart@0215')

print(server.get_whoami())
print(server.jobs_count())