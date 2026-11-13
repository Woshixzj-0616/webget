import socket

def get_content_length(head: bytes):
    for line in head.split(b"\r\n"): #根据\r\n继续分割换行，还是ai教我怎么用split的
        if line.lower().startswith(b"content-length:"): 
            #根据content-length字段提取长度，注意大小写转换。
            return int(line.split(b":", 1)[1].strip())
    return None

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=input('Choose your host:')
port=int(input('Choose your port:'))
s.connect((host,port))
req=b"GET / HTTP/1.1\r\nHost: "+host.encode()+b"\r\n\r\n"
s.sendall(req)
buf=b""
n=0
while b"\r\n\r\n" not in buf:
    chunk =s.recv(4096)
    if not chunk:
        break
    n+=1
    print(n,':',len(chunk))
    buf+=chunk
head,body =buf.split(b"\r\n\r\n",1)
#根据\r\n\r\n来划分head和body
bodylen=get_content_length(head)
#body中间可能被切开，先加上原本前面收到body的长度。
curlen=len(body)
while curlen<bodylen:
    #根据函数里面提取的bodylen来设置循环结束条件。
    chunk=s.recv(4096)
    if not chunk:
        break
    n+=1
    print(n,':Recv ',len(chunk),' B\n')
    body+=chunk
    curlen+=len(chunk)
print('Recv num:',n)
statue_line=head.split(b"\r\n",1)[0]
print(statue_line)
print('\n\n')
print(head)
print('\n\n')
print(body)
with open("body.bin", "wb") as f:
    f.write(body)