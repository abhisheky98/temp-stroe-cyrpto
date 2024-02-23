from collections import OrderedDict
from User import User
class Datastore:
    def __init__(self):
        self.data = {}  # Initialize an empty dictionary to store users and balances
        self.creditor_queue = OrderedDict()
        self.debtor_queue = OrderedDict()

    def print_users(self):
        print("All Users and Balances:")
        for user, balance_info in self.data.items():
            print(f"User: {user}, Balance: {balance_info[0]}, Owed: {balance_info[1]}")
            
    def add_user(self, user):
        """
        Add a user to the datastore.
        """
        self.data[user.name] = [user.balance, user.owed]
        
    def get_users(self):
        return self.data

    def get_balance(self, user_name):
        """
        Get the balance of a user.
        """
        return self.data.get(user_name)

    def update_balance(self, user_name, amount, owed):
        """
        Update the balance of a user.
        """
        if user_name in self.data:
            self.data[user_name][0] += amount
            self.data[user_name][1] -= owed
        else:
            print(f"User '{user_name}' not found in the datastore.")
    
            

    def transaction(self, sender, receiver, amount):
        """
        Perform a transaction between two users.
        """
        
        
        sender_balance = self.get_balance(sender.name)
        
        print("sender balance",sender_balance[0])
        receiver_balance = self.get_balance(receiver.name)

        if sender_balance is None:
            print(f"Sender '{sender.name}' not found in the datastore.")
            return

        if receiver_balance is None:
            print(f"Receiver '{receiver.name}' not found in the datastore.")
            return
        
        
        
        if sender_balance[0] >= amount:
            
            
            if sender.name in self.creditor_queue:
                del self.creditor_queue[sender.name]
                
            self.update_balance(sender.name, -amount, -amount)
            
            
            self.creditor_queue[sender.name]=sender_balance
            
            
            
            if receiver.name in self.debtor_queue:
                del self.debtor_queue[receiver.name]
                
            self.update_balance(receiver.name,amount,amount)
            
            
            
            self.debtor_queue[receiver.name]=receiver_balance
            print(f"Transaction: {sender.name} sent ---------------- {amount} to {receiver.name}")
           # print("creditor",self.creditor_queue)
           # print("debtor",self.debtor_queue)
            
            
        else:
            print(f"Insufficient balance for transaction: {sender.name}")
            
    def settleup(self):
        
        
        n=10
        while self.creditor_queue and self.debtor_queue and n>0:
            n-=1
            if self.creditor_queue:
                creditor_key, creditor_info = next(iter(self.creditor_queue.items()))
            else:
                break  # Break the loop if creditor_queue is empty
            if self.debtor_queue:
                debtor_key, debtor_info = next(iter(self.debtor_queue.items()))
            else:
                break  # Break the loop if debtor_queue is empty
            
            print("credito list",self.creditor_queue)
            print("debtor list",self.debtor_queue)
            
            print(f"Processing transaction between {creditor_key} and {debtor_key}")
            print(f"Creditor Info: {creditor_info}")
            print(f"Debtor Info: {debtor_info}")
            print("lalal")
            print(self.debtor_queue)
            
            if creditor_info[1] <= 0  and creditor_key in self.creditor_queue.keys() :
                print(f"Deleting creditor '{creditor_key}' from creditor_queue")
               
                del self.creditor_queue[creditor_key]
                continue  # Skip to the next iteration if creditor's owed is already settled
            if debtor_info[1] >=0 and debtor_key in self.debtor_queue.keys():
                
                print(f"Deleting debtor '{debtor_key}' from debtor_queue")
                
                
                del self.debtor_queue[debtor_key]
                print("Debtor Queue after deletion:", self.debtor_queue)
                continue  # Skip to the next iteration if debtor's owed is already settled
            
            creditor_object = User(creditor_key)  # Assuming User is the class for user objects
            debtor_object = User(debtor_key)  # Assuming User is the class for user objects
            
            if creditor_info[1] >= -(debtor_info[1]) and -(debtor_info[1]) > 0:
                self.transaction(debtor_object, creditor_object, -(debtor_info[1]))
                self.debtor_queue[debtor_key] = debtor_info

            elif creditor_info[1] < -(debtor_info[1]):
                self.transaction(debtor_object, creditor_object, creditor_info[1])
                self.creditor_queue[creditor_key] = creditor_info

        print("After settling up:")
        print("Creditor Queue:", self.creditor_queue)
        print("Debtor Queue:", self.debtor_queue)


                
                
                
        
        
        
            
        
        