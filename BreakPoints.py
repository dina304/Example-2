
def loop_it_out(num_of_rounds):
    sum=0
    if num_of_rounds%2==0:
        for i in range(1,num_of_rounds):
            sum=sum+i
    return sum


result=loop_it_out(5)
print(result)