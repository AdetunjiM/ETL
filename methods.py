"""
    Create the Persons  Class : Firstname , Lastname ,SSN, Customer_id ,Address ,
    Create the Account class which has Account Number , In , Out , Account Type , balance 
    Create Products list class : Product_id ,Product name ,cost 
    Create Inventory List class : product id ,product_name Quantity In , Quantity out 
    Create sales person class: Seller_id , First Name , Last Name 
    Create Sales Class : product id, seller_id , product_name , customer_id ,quantiy , Price 
    
    """


class customer :
    def __init__(self,firstname,lastname,ssn,Customer_id,address):
        self.firstname=firstname
        self.lastname=lastname
        self.ssn=ssn
        self.customer_id=Customer_id
        self.address=address
        
    def __str__(self):
        pass
    
class staff :
    def __init__(self,firstname,lastname,staff_id,designation):
        self.firstname=firstname
        self.lastname=lastname
        self.staff_id=staff_id
        self.designation=designation

    def __str__(self):
        pass
    
class inventory :
    def __init__(self,product_id ,product_name,quantity,quantity_in,price):
        self.product_id=product_id
        self.product_name=product_name
        self.quantity=quantity
        self.quantity_in=quantity_in
        self.price=price
        
    def add_inventory(self ,quantity,quantity_in):
        quantity += quantity_in
    
    def __str__(self):
        pass
    
class products(inventory) :
    def __init__(self,product_id,product_name,price):
        super().__init__(product_id,product_name,price)
    
    def __str__(self):
        pass
    
class sales(customer,staff,inventory) :
    def __init__(self,product_name,customer_id,staff_id,product_id,price,quantity,quantity_bought,):
        customer.__init__(self,customer_id)
        staff.__init__(self,staff_id)
        inventory.__init__(self,product_id,price,quantity)
        self.quantity=quantity_bought
        
    def update_quantity(self,quantity,quantity_bought):
        quantity=-quantity_bought
    
    
    def __str__(self):
        pass
