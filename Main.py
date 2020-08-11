#-*-coding: utf-8 -*-
import socket
import functions as func
import datetime


ip_for_start = {1:'localhost', 2:'192.168.43.226',3:'192.168.1.1'}

changed_ip = int(input("""Change your host:
1 - Local
2 - Xiaomi
3 - Veronica\n"""))

print("start")
def req(text):
    conn.send(bytes(str(text), encoding="UTF-8"))

while (1):
    try:
        sock = socket.socket()
        sock.bind((ip_for_start[changed_ip],9091))
        #sock.bind(('192.168.43.226',9091))
        #sock.bind(('192.168.1.12', 9091))
        sock.listen(1)
        conn, addr = sock.accept()

        ip = "\n\n А вот и твой ip \n "+str(addr)+"\n"

        print("connected: ",addr)



        while True:
            data = conn.recv(4096)
            if not data:
                break
            msg=str(data.decode("UTF-8"))
            print(msg)
            if ( msg.lower() == "/stop"):
                break
            elif (msg.lower() == "/start"):
                new_ip = str(addr)
                new_ip = new_ip.replace("(", "")
                new_ip = new_ip.replace(")", "")
                new_ip = new_ip.replace("'", "")
                new_ip = new_ip.replace(",", ":")
                new_ip = new_ip.replace(" ", "")
                print(new_ip[0:len(new_ip) - 6])

                file = open('ip.txt')
                i = 0
                print("Entering...")
                for line in file:
                    ips = new_ip[0:len(new_ip) - 6]
                    if (str(line) == (new_ip[0:len(new_ip) - 6] + "\n")):
                        print("Connect")
                        f = open('names.txt')
                        file = open('ip_n.txt')
                        for line in file:
                            s=str(line)
                            if(s.find(ips)!=-1):
                                pos = s.rfind(" ")
                                id_f = s[0:pos]
                        file.close()


                        for lines in f:
                            st = str(lines)
                            if (st.find(id_f) != -1):
                                pos1 = st.rfind(":")
                                name = st[pos1+1:len(s)]
                        f.close()

                        req("Connect wits server\n")
                        req("Hello " + name + "\n")

                        #отправляем клиенту историю прошлых сообщений
                        try:
                            #file_names = str(datetime.date.today()) + ".txt"
                            #f = open(file_names)
                            f = open('chat_log.txt')
                            last_dialog = f.read()
                            f.close()

                            #f =  open(file_names,'r')
                            f = open('chat_log.txt','r')
                            cnt_first = len(f.readlines())
                            f.close()
                            print("сейчас количство строк:"+str(cnt_first))
                            req(last_dialog)

                            i = 1
                        except FileNotFoundError:
                            #f = open(file_names,'a')
                            f = open('chat_log.txt','a')
                            f.close()
                        break

                if (i==0):
                    req("Please enter your name or login")
                    req("--------------------------------")

                else:
                    break

            elif(str(msg[0:4]) =="/reg"):
                req("user was registered with name " + str(msg[5:len(msg)]))
                new_ip = str(addr)
                print(new_ip)
                new_ip = new_ip.replace("(", "")
                new_ip = new_ip.replace(")", "")
                new_ip = new_ip.replace("'", "")
                new_ip = new_ip.replace(",", ":")
                new_ip = new_ip.replace(" ", "")

                file = open('names.txt','a')
                f = open('ip_n.txt','r')
                fl = open('ip.txt', 'a')
                fl.write(new_ip[0:len(new_ip) - 6] + '\n')
                fl.close()

                cnt = 0
                for line in f:
                    #print(str(line))
                    cnt = cnt + 1
                f.close()
                f = open('ip_n.txt','a')
                f.write("id"+str(cnt)+" ip:"+new_ip[0:len(new_ip)-6]+"\n")
                file.write("id"+str(cnt)+" Name:"+msg[5:len(msg)]+"\n")
                file.close()
                f.close()

            elif((msg.lower()=="/ip")or(msg.lower()=="/Ip")or(msg.lower()=="/iP")or(msg.lower()=="/IP")):
                req(func.get_ip(addr))

            elif((msg.lower()=="/test")or(msg.lower()=="/Test")or(msg.lower()=="/TEST")):
                req("Test")

            elif((msg.lower()[0:5]=="/chat")or(msg.lower()=="1")):
                req("chatting\n"+str(datetime.date.today()))
                file_name = str(datetime.date.today())+".txt"
                f=open(file_name,'a')
                name = func.get_name(addr)
                f.write(name)
                f.close()

            elif(msg.lower()=="/request"):
                #f  = open(file_names,'r')
                f = open('chat_log.txt','r')
                cnt_now  = len(f.readlines())
                f.close()
                if(cnt_now>cnt_first):
                    #f = open(file_names)
                    f = open('chat_log.txt')
                    stroki = 1
                    for ln in f:
                        print(ln)
                        if (stroki > int(cnt_first) and (stroki <= int(cnt_now))):
                            my_msg = ln

                        stroki=stroki+1
                    print("Сообщение для отправки: "+my_msg)
                    req(my_msg)
                    print("Отправили ответ")

                    f.close()
                    cnt_first=cnt_now
                else:
                    req("/nothing")
                    pass



            else:
                new_ip = str(addr)
                new_ip = new_ip.replace("(", "")
                new_ip = new_ip.replace(")", "")
                new_ip = new_ip.replace("'", "")
                new_ip = new_ip.replace(",", ":")
                new_ip = new_ip.replace(" ", "")
                #print(new_ip[0:len(new_ip)-6])

                #conn.send(data.upper() + bytes(ip,encoding="UTF-8"))
                conn.send(data.upper())

                file_name = str(datetime.date.today()) + ".txt"
                f = open(file_name, 'a')

                #f = open('chat_log.txt','a')
                name = func.get_name(addr)
                message = str(name[0:len(name)-1]+": "+data.decode("UTF-8")+"           "+str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))+"\n")
                print(message)
                f.write(message)
                f.close()

                #запись в общий лог
                f = open('chat_log.txt','a')
                message = str(name[0:len(name) - 1] + ": " + data.decode("UTF-8") + "           " + str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")) + "\n")
                print(message)
                f.write(message)
                f.close()


                flag = 0
                file = open('ip.txt')
                i = 0
                for line in file:
                    #print(str(line))
                    i = i + 1
                    if (str(line) == (new_ip[0:len(new_ip)-6]+"\n")):
                        flag = flag + 1
                        #print("одинаковые строки")

                file.close()

                if (flag == 0):
                    file = open('ip.txt', 'a')
                    file.write(new_ip[0:len(new_ip)-6]+'\n')
                    file.close()
                else:
                    #print("одинаковых строк " + str(flag))
                    flag = 0
                i = 0
        #req("Server was stopped")
        conn.close()
        if((msg == "/stop")or(msg=="/STOP")):
            break
    except (ConnectionResetError,NameError):
        print("Problem with user")

