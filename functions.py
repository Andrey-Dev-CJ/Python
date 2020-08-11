def find_id(ip):
    f = open('ip_n.txt')
    for line in f:
        #print(line)
        if(ip==line[line.rfind(":")+1:len(line)-1]):
            id = line[0:line.rfind(" ")]
            #print(id)
    f.close()
    return str(id)


def find_name(id):
    f = open('names.txt')
    for lines in f:
        idf = lines[0:lines.find(" ")]

        if(id==idf):

            name = lines[lines.rfind(":")+1:len(lines)-1]
    f.close()
    return str(name)

def get_ip(addr):
    new_ip = str(addr)
    new_ip = new_ip.replace("(", "")
    new_ip = new_ip.replace(")", "")
    new_ip = new_ip.replace("'", "")
    new_ip = new_ip.replace(",", ":")
    new_ip = new_ip.replace(" ", "")
    new_ip=new_ip[0:len(new_ip) - 6]
    return str(new_ip)

def get_name(addr):

    file = open('ip.txt')
    for line in file:
        ips = get_ip(addr)
        if (str(line) == (ips + "\n")):
            print("Connect")
            f = open('names.txt')
            file = open('ip_n.txt')
            for line in file:
                s = str(line)
                if (s.find(ips) != -1):
                    pos = s.rfind(" ")
                    id_f = s[0:pos]
            file.close()

            for lines in f:
                st = str(lines)
                if (st.find(id_f) != -1):
                    pos1 = st.rfind(":")
                    name = st[pos1 + 1:len(s)]
            f.close()
    return str(name)
