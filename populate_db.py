import os
import sys
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','blogger.settings')

import django
django.setup()

# start populating
from blog.models import User, Article
from faker import Faker
from datetime import date
fgen = Faker()

# method to populate any no of records in db
def add_users(n=10):
    for i in range(n):
        # django model object
        user_obj = User()
        # fetching data for a fake profile
        profile = fgen.profile()
        phone_no = fgen.phone_number()
        # assign the data to User object
        user_obj.name       = profile['name']
        user_obj.username   = profile['username']
        user_obj.email      = profile['mail']
        birthdate = profile['birthdate']
        user_obj.dob        = date(int(birthdate[:4]),int(birthdate[5:7]),int(birthdate[8:10]))
        user_obj.contact_no = phone_no
        user_obj.address    = profile['address']
        user_obj.sex        = profile['sex']
        user_obj.company    = profile['company']
        user_obj.websites   = "#".join(profile['website'])
        # commit to db
        user_obj.save()
        print "Create user %d :"%(i), user_obj

def add_articles(n=50):
    all_users = User.objects.all()
    for i in range(n):
        # django model object
        article_obj = Article()
        # fetching data for fake article
        article_obj.title = fgen.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        article_obj.text  = fgen.text(max_nb_chars=random.randint(700,1200))
        article_obj.date_published = fgen.past_date(start_date='-2y')
        article_obj.author = random.choice(all_users)
        # commit to db
        article_obj.save()
        print "Created article %d :"%(i), article_obj

# main
if __name__ == "__main__":
    add_users(15)
    add_articles(100)