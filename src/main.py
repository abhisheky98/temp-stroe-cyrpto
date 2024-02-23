# main.py
from Datastore import Datastore

#from BlockchainMicroservice import BlockchainMicroservice
from User import User


# Creating sample users
user1 = User("Alice", 100, 0)
user2 = User("Bob", 500, 0)
user3 = User("Charlie", 200, 0)
user4 = User("Dominic", 3000, 0)
user5 = User("Elizabeth", 400, 0)


storage = Datastore()

storage.add_user(user1)
storage.add_user(user2)
storage.add_user(user3)
storage.add_user(user4)
storage.add_user(user5)

storage.print_users()


storage.transaction(user1, user2, 400)
storage.print_users()
storage.settleup()
storage.transaction(user1, user2, 20)
storage.print_users()
storage.transaction(user2, user3, 20)
storage.print_users()
storage.transaction(user3, user5, 60)
storage.print_users()


storage.transaction(user1, user2, 50)

storage.transaction(user4, user3, 10)
storage.transaction(user2, user5, 30)
storage.transaction(user4, user2, 11200)

storage.transaction(user2, user4, 20)
storage.transaction(user3, user5, 20)


storage.print_users()
print("lolol before ---------------------------------------------settleup")

print(storage.creditor_queue)
print(storage.debtor_queue)

storage.settleup()
print("after settleup")
print(storage.creditor_queue)
print(storage.debtor_queue)

storage.print_users()