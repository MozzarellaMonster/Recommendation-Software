#Program created by Night Librarian/Mozzarella Monster
from multiprocessing.sharedctypes import Value
from movies_data import tags, movies
from heapsort import heapsort
from maxheap import MaxHeap

def recommendations():
    print("\nWelcome to my horror movie recommendation software!")
    print("Here are the different tags you can use for the type of film you wish to view.")
    print(" / ".join(tags) + "\n")

    user_tags_list = []
    rec_movies = {}
    finished = False
    tag_count = 0
    while not finished:
        user_tag = input("Please type in the beginning of the tag you want to add or type STOP to finish: ")
        if user_tag == "STOP":
            finished = True
            continue
        for tag in tags:
            if tag.startswith(user_tag) and tag not in user_tags_list:
                user_tags_list.append(tag)
        print("The tags you have chosen so far: " + " / ".join(user_tags_list))
        
    print("Finding movies for you...\n")

    for tag in user_tags_list:
        for movie in movies:
            if tag in movies[movie] and movie not in rec_movies:
                rec_movies[movie] = 0
        
    for movie in rec_movies:
        for tag in user_tags_list:
            if tag in movies[movie]:
                tag_count += 1
        rec_movies[movie] = tag_count
        tag_count = 0

    rec_movies_tuples = make_tuples(rec_movies)
    rec_top_three = top_three(rec_movies_tuples)
        
    print("Your tags: " + " / ".join(user_tags_list))
    print("The movies with those tags are: " + ", ".join("{0} ({1})".format(key, value) for key, value in rec_movies.items()) + "\n")
    print("Your top three movies are: " + ", ".join("{0} ({1})".format(key, value) for key, value in rec_top_three))

def make_tuples(rec_movies):
    # Takes a dictionary with movie names as keys and
    # number of tags it satisfies as the value
    return [(key, value) for key, value in rec_movies.items()]

def top_three(rec_movies_tuples):
    # Takes a list of tuples with movie names as the first index
    # and number of tags that satisfy as the second
    top_three_list = []
    for i in range(3):
        rec_movies_tuples = heapsort(rec_movies_tuples[i:])
        top_three_list.append(rec_movies_tuples[0])
    return top_three_list
    #return [heapsort(rec_movies_tuples[i:])[0] for i in range(3)]

def test():
    outliers = []
    for movie in movies:
        for tag in movies[movie]:
            if tag not in tags:
                outliers.append(tag)
    print(outliers)

recommendations()
