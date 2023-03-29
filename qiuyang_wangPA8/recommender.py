# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #8
#
# Description: This program can give users two kinds of recommendation of books based on what users have chosen

#define the main function
def main():
    intro_message()
    operation()

#define the function to print the introduction message on the console to inform the user about the way to use the program
def intro_message():
    print("Welcome to the Book Recommender. Type the word in the")
    print("left column to do the action on the right.")
    print("recommend : recommend books for a particular user")
    print("averages : output the average ratings of all books in the system")
    print("quit : exit the program")

#define the function to process the given text into a booklist and a rating dictionary for further operation
#return one dictionary and one list
def recommendations_preparation():
    #read the given text
    lines = open("ratings.txt").readlines()
    book_titles = set()
    for i in range(1, len(lines), 3):
        #add the book name from the text file
        book_titles.add(lines[i].strip())
    book_titles = list(book_titles)

    users_ratings = {}
    for j in range(0, len(lines), 3):
        if lines[j].strip() not in users_ratings.keys():
            #create a key in this dictionary
            users_ratings[lines[j].strip()] = [0] * len(book_titles)
        #map the key with the corresponding rating value
        users_ratings[lines[j].strip()][book_titles.index(lines[j + 1].strip())] = int(lines[j + 2])
    return users_ratings, book_titles

#define the function to recommend books for users based on the average ratings from high to low
def averages():
    users_ratings, book_titles = recommendations_preparation()
    books_averages_recommend = [0] * len(book_titles)
    for k in range(len(book_titles)):
        total_rating = 0
        count = 0
        for i in users_ratings.keys():
            #make sure the rating is non-zero
            if int(users_ratings[i][k]) != 0:
                total_rating += int(users_ratings[i][k])
                count += 1
        #make the list into a 2D list with tuples containing the average rating for a book first and the title of that book second
        books_averages_recommend[k] = (total_rating / count, book_titles[k])
    books_averages_recommend.sort()
    books_averages_recommend.reverse()
    for (avg_ratings, book_name) in books_averages_recommend:
        print(book_name, avg_ratings)

#define the function that the system will generate recommended books for users based on similarity
def recommendations():
    users_ratings, book_titles = recommendations_preparation()
    user = input("user? ")
    if user not in users_ratings.keys():
        averages()
    else:
        user_similarity = [0] * (len(users_ratings.keys()) - 1)
        count = 0
        for user_name in users_ratings:
            similarity = 0
            #make sure the users will not get the similarity from themselves
            if user_name != user:
                for i in range(len(book_titles)):
                    #use dot product to calculate the similarity
                    similarity += users_ratings[user_name][i] * users_ratings[user][i]
                #put the similarity and corresponding user's name into tuples within a list
                user_similarity[count] = (similarity, user_name)
                count += 1
        user_similarity.sort()
        user_similarity.reverse()

        recommend_avg_ratings = [0] * len(book_titles)
        books_recommend = []
        for j in range(len(recommend_avg_ratings)):
            non_zero_count = 0
            #the first three users with the relative high similarity will become the reference to organize a recommendation
            for k in range(3):
                high_similarity_user = user_similarity[k][1]    #"[1]" ensures the function will select the "name" instead of "ratings"
                #make sure the rating is non-zero
                if users_ratings[high_similarity_user][j] != 0:
                    recommend_avg_ratings[j] += users_ratings[high_similarity_user][j]
                    non_zero_count += 1
            #only recommends those with average ratings higher than 0
            if non_zero_count != 0 and recommend_avg_ratings[j] > 0:
                recommend_avg_ratings[j] /= non_zero_count
                #put the ratings and the book name into tuples within a list
                books_recommend.append((recommend_avg_ratings[j], book_titles[j]))
        books_recommend.sort()
        books_recommend.reverse()
        for (recommend_avg_ratings, book_name) in books_recommend:
            print(book_name, recommend_avg_ratings)

#define the function to operate and call diffenrent functions to follow the user's want
def operation():
    task = input("next task? ")
    while task != "quit":
        if task == "recommend":
            recommendations()
        elif task == "averages":
            averages()
        else:
            print("Please choose the correct task!")
        print()
        task = input("next task? ")
    
main()