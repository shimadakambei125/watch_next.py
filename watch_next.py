# We import spacy module
import spacy

# We use spacy.load to load the  english module
nlp = spacy.load("en_core_web_md")

# We write the decription of the move in the task using a multiline string
# and we store it under the variable description
description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for
the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on planet Sakaar where he is sold into
slavery and trained as a gladiator"""

# We pass the string value of variable description into the module
nlp_description = nlp(description)


# We define a function called similar_movie that take a movie description
# the goal is to return the title of the movie
def similar_movie(movie_description):

    # We use the syntax below to open and read the movies.txt and read it
    # We use the readlines() method to read each entry and store in a list
    # We declare a variable highest_score and assign an initial value of 0
    # We use a for loop to load each movie and description into the module
    # and use conditional statements to return the highest_score which means the most similar movie
    # We use a split method to allow us to return the title of the movie only..
    with open("movies.txt", "r") as data:
        movie_data = data.readlines()
        highest_score = 0
        for movie in movie_data:
            movie_data = movie.strip()
            movie_nlp = nlp(movie_data)
            if movie_nlp.similarity(nlp_description) > highest_score:
                highest_score = movie_nlp.similarity(nlp_description)
                if highest_score == movie_nlp.similarity(nlp_description):
                    closest_movie = movie_nlp.text.split(":")

        return closest_movie[0]

# We call the function through the print method
print(similar_movie(nlp_description))