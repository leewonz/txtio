import time

def read_all():
    with open("txtio.txt",'r+t') as file_r:
        print(" " + "=" * 20)
        while True:
            line = file_r.readline()
            if not line: break
            print(" " + line,end = "")
        print(" " + "=" * 20)

def write_comment(input_str):
    with open("txtio.txt",'a+t') as file_w:
        print(input_str, file = file_w)
        print(" %d/%d/%d %d:%d:%d" % (time_now.tm_year, time_now.tm_mon, time_now.tm_mday,
                                      time_now.tm_hour, time_now.tm_min, time_now.tm_sec)
              , file = file_w)

def delete_all():
    with open("txtio.txt",'w') as file_w:
        pass
    print("All comments deleted.")
    
#MAIN

while True:
    time_now = time.localtime(time.time())
    
    read_all()
    
    input_str = input("Write a comment. \n(Type 'Q' to quit,'D' to delete all.)\n")
    if input_str == 'Q' or input_str == 'q' :
        break
    elif input_str == 'D' or input_str == 'd' :
        delete_confirm = input("Delete? (Y/N)\n")
        if delete_confirm == 'Y' or delete_confirm == 'y':
            delete_all()
    else:
        write_comment(input_str)

