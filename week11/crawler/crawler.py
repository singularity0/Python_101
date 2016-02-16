# import flask
import requests
import re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import consts


pattern = consts.host_pattern

start = consts.host_to_start

rr = requests.get(start)
doc_visited = open('doc_visited.txt' , 'w')
doc_srv_list = open('srv_list.txt', 'w')

visited = []
soup = BeautifulSoup(rr.text,  'html.parser')

for link in soup.find_all('a'):
    href = link.get("href")
    if href:
        if href.startswith('http'):

            l = re.search(pattern, href).group()
            visited.append(l)

        elif href.startswith('link.php?id'):

            visited.append(start + '/' +(href))

for i in visited:
    # print(i)
    doc_visited.write(i)
    doc_visited.write('\n')
print(len(visited))


result = {}
failed_requests = 0
for index in range(0, len(visited)):
    try: 
        r = requests.get(visited[index])

        for i in r.headers:
            if i == 'Server':
                server_used = r.headers["Server"]
                doc_srv_list.write(server_used)
                doc_srv_list.write('\n')
                if server_used.startswith('Apache'):
                    server_used = 'Apache'
                if server_used not in result:
                    result[server_used] = 1
                else:
                    result[server_used] += 1
    except:
        failed_requests += 1

print(result)

x_axis = [x for x in range(len(result))]
y_axis = []
servers = []
for k, v in result.items():
    servers.append(k)
    y_axis.append(v)
plt.xticks(x_axis, servers)
plt.title("Server distribution for domains \n linking {}: ".format(consts.host_to_start))
plt.xlabel("Server type")
plt.ylabel('number of servers')
plt.bar(x_axis, y_axis, align = 'center')
plt.show()

