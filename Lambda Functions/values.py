

def list_tuples(file_list):
    return_max = max(file_list,key=lambda item:item[1])[1]
    return_min = min(file_list,key=lambda item:item[1])[1]
    return return_max, return_min


final_list = [] 
line = input("Enter the list of tuples:\n") 
while(line != ''): 
    final_list.append(tuple(line.split())) 
    line = input() 
 
print(list_tuples(final_list))
