print("hello_world")

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print('First Name: ', self.first_name)
        print('Last Name: ', self.last_name)
        print('Email: ', self.email)
        print('Age: ', self.age)
        print('Rewards Member: ', self.is_rewards_member)
        print('Rewards Points: ', self.gold_card_points)
        print('__________________________________')
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        elif self.is_rewards_member == True:
            print("Already a member")
        return self.is_rewards_member
    def spend_points(self, amount):
        if self.gold_card_points > amount and self.is_rewards_member == True:
            self.gold_card_points = self.gold_card_points - amount

user1 = User('Will', 'Pearce', 'someemail@somthin.com', 33)
user2 = User('Steph', 'Wolcotte', 'anotheremail@somthin.com', 30)
user3 = User('Don', 'Teflon', 'lastemail@somthin,com', 37)

user1.display_info()
user2.display_info()
user3.display_info()

user1.enroll()
# user1.display_info()
# user1.enroll()
# user1.display_info()
user1.spend_points(50)
# user1.display_info()

user2.enroll()
user2.spend_points(80)
# user2.spend_points(130)
# user2.display_info()

user1.display_info()
user2.display_info()
user3.display_info()
