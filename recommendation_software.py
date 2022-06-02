#Program created by Night Librarian/Mozzarella Monster
from movies_data import *
from quicksort import *
from maxheap import MaxHeap

def recommend():
    print("Welcome to my horror movie recommendation software!")
    print("Here are the different tags you can use for the type of film you wish to view.")
    print(tags)

    user_tags = input("Please type in the tags you want your movie to have, separated by spaces: ")
    user_tags_list = user_tags.split()
    found_tags = []
    
    for tag in user_tags_list:
        for movie in movies:
            if tag in movies[movie]:
                if tag not in found_tags:
                    found_tags.append(tag)
    print("The found tags are: " + str(found_tags))



recommend()