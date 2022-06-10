#Program created by Night Librarian/Mozzarella Monster
from movies_data import tags, movies
from heapsort import heapsort

def recommendations():
    print("\nWelcome to my horror movie recommendation software!")
    print("Here are the different tags you can use for the type of film you wish to view.")
    
    count = 0
    for idx in range(len(tags)):
        count += 1
        if count % 10 == 0:
            print(tags[idx] + " / ")
        else:
            print(tags[idx] + " / ",end="")
    print("\n")

    user_tags_list = []
    rec_movies = {}
    finished = False
    tag_count = 0
    print("Please try to choose at least three tags to get the most accurate recommendations. Choosing one tag will not work at all.")
    # Get user input
    while not finished:
        user_tag = input("Please type in the beginning of the tag you want to add, type STOP to finish, or type REMOVE to remove a tag: ")
        if user_tag == "STOP":
            finished = True
            continue
        elif user_tag == "REMOVE":
            tag_to_remove = input("Please type in the beginning of the tag you want to remove: ")
            for tag in user_tags_list:
                if tag.startswith(tag_to_remove):
                    user_tags_list.remove(tag)
            print("Tag removed")
            print("The tags you have chosen so far: " + " / ".join(user_tags_list) + "\n")
            continue
        for tag in tags:
            if tag.startswith(user_tag) and tag not in user_tags_list:
                user_tags_list.append(tag)
        print("The tags you have chosen so far: " + " / ".join(user_tags_list) + "\n")
        
    print("Finding movies for you...\n")

    # Get movies that contain user-selected tags
    for tag in user_tags_list:
        for movie in movies:
            if tag in movies[movie] and movie not in rec_movies:
                rec_movies[movie] = 0

    # Get number of tags the movies satisfy    
    for movie in rec_movies:
        for tag in user_tags_list:
            if tag in movies[movie]:
                tag_count += 1
        rec_movies[movie] = tag_count
        tag_count = 0
    
    # Trim the selection to only include movies that satisfy multiple tags
    rec_movies = {key:value for key, value in rec_movies.items() if value > 1}

    # Make dictionary into a list of tuples
    rec_movies_tuples = [(key, value) for key, value in rec_movies.items()]
    # Use heapsort algorithm and select the top three movies
    rec_top_three = heapsort(rec_movies_tuples)[:3]
    
    # Print recommended movies
    print("Your tags: " + " / ".join(user_tags_list))
    print("The movies with those tags are: " + ", ".join("{0} ({1})".format(key, value) for key, value in rec_movies.items()) + "\n")
    print("Your top three movies are: " + ", ".join("{0} ({1})".format(key, value) for key, value in rec_top_three))

recommendations()
