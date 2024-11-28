import multiprocessing 
def sum_of_squares (numbers, result, index): 
    total =sum(x*x for x in numbers)  
    result[index] = total
def parallel_sum_of_squares (numbers, num_processes): 
    chunk_size =len(numbers) // num_processes 
    chunks = [numbers[i * chunk_size: (i+1) * chunk_size]
    for i in range(num_processes)] 
    if len(numbers) % num_processes !=0: 
         chunks[-1].extend(numbers[num_processes* chunk_size:])    
         result= multiprocessing.Array('i',num_processes)  
         processes=[] 
 
    for i in range (num_processes): 
        p= multiprocessing.Process(target=sum_of_squares,args=(chunks[i],result,i))       
        processes.append(p) 
        p.start() 
 
    for p in processes: 
        p.join() 
 
    total_sum=sum(result)     
    return total_sum 
 
if __name__=='__main__':    
    n=int(input("How many No ?:"))   
    numbers=list(range(1,n+1)) 
    num_processes=multiprocessing.cpu_count() 
 
    total=parallel_sum_of_squares(numbers,num_processes)    
    print(f"The sum of squres is :{total}") 
