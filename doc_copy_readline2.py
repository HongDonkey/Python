import re 

f=open('c:\\work\\PV3.txt','rt', encoding='utf-8')
g=open('c:\\work\\PV3_copy.txt','wt', encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
cnt = 0
while (line != ''):
    if (re.search("error", line)):
        g.write(line + "\n")
        cnt+=1
        print(cnt + "건의 에러 발생")
    line = f.readline()

f.close() 
g.close()








