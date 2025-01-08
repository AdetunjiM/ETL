from methods import *
import names
import random

"""
Users: generate 100 people firstname and last name , unique SSn , give customerId  and unique address 
    
    """

def generate_name():
    firstname=names.get_full_name().split(" ")[0]
    lastname=names.get_full_name().split(" ")[1]
    return firstname ,lastname

def generate_ssn():
    part1=random.randint(100,999)
    part2=random.randint(10,99)
    part3=random.randint(1000,9999)
    
    return f"{part1}-{part2}-{part3}"


def generate_cust_id(no,lastname):
    if len(lastname)>=3:
        return f"{no}{lastname[0:2]}"
    else:
        return f"{no}{lastname}"

    




def generate_all(number):
    individual =set()
    for i in range(number):
        
        collection =list()
        first,last = generate_name()
        ssn =generate_ssn()
        customer_id=generate_cust_id(i,last)
        collection=(customer_id,first,last,ssn)
        
        individual.add(collection)
    return individual

def save_files(file_name,input_set):
    with open(file_name,"w") as file :
        for items in input_set:
            file.write(",".join(items)+"\n")
    
def main():
    
    output_csv='customers.csv'
    input_set = generate_all(20)
    save_files(output_csv,input_set)
        



if __name__ == '__main__':
    main()