import webbrowser

# create a class to represent a movie object


class Movie():
    # valid movie ratings.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # the Movie constructor takes itself, and several explicitly named movie
    # elements.
    def __init__(
            self,
            movie_title,
            movie_story,
            poster_image,
            trailer_youtube):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # this function will open a browser and play the trailer that was passed
    # in the constructor.
    def show_trailer(self):

        # This line opens the trailer within the main page.
        webbrowser.open(self.trailer_youtube_url)
