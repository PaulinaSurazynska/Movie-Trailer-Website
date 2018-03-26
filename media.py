"""module with allows to open URLs in interactive browser applications."""
import webbrowser


class Movie():
    """class with defines variables: title, storyline, poster and youtube_trailer
    with will be used by instances (objects) of this class created in
    marvel_best_movies.py
    """

    def __init__(
        """ constructor method initializing all the data associated
        with the instances of movie class
        """
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube
            ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """method to show movie's trailer"""
        webbrowser.open(self.trailer_youtube_url)

