def server_config(file_path,key,value):

    with open(file_path,"r") as file:
        lines=file.readlines()  #temp variable for storage

        with open(file_path,"w") as file:
            for i in lines:
                if key in i:
                    file.write(key+"="+value+"\n")
                    print("Done")
                else:
                    file.write(i)
        
            

server_config("03_File_operation/server.conf","max","000")