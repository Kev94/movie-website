import webbrowser

class Movie():
# class documentation
    """ This class provides a method of storing movie related information and allows the viewer of the page to see the movie trailer. """


#created init function that creates space / initializes pieces of info like storyline and title
# inputs: information needed for each movie
# No output
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,release_date):
        # initialize the movie variables (self.title = movie_title.. etc)
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release = release_date

# now create an instance method to show the youtube trailer and import webbrowser
#input for both: the instances created for the class Movie
#output: when clicked for the show_trailer() funct. it opens the movie trailer from youtube
# output for show_poster() is the image seen on the site page of the movie from wikimedia/wikipedia
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# then create the instance method that shows the movie poster
    def show_poster(self):
        webbrowser.open(self.poster_image_url)
