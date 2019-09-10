from faker import Faker
import random

fake = Faker()

name = fake.name()

small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

small_1 = random.choice(small_letters)
small_2 = random.choice(small_letters)
small_3 = random.choice(small_letters)

big_1 = random.choice(big_letters)
big_2 = random.choice(big_letters)
big_3 = random.choice(big_letters)

small_all = small_1 + big_2 + small_3
big_all = big_1 + small_2 + big_3

small_all = str(small_all)
big_all = str(big_all)

num = random.randint(0,1000)
num = str(num)

name_crop = name[0:4]
name_crop = name_crop.replace(" ","")

name_crop += small_all
name_crop += big_all
name_crop += num

name = name_crop

print(name)




