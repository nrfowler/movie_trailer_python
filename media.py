class Movie():
    """
    Args:
        title (str): String containing the title of the film.
        trailer_youtube_url (str): String containing the youtube url of the trailer.
        poster_image_url (str): String containing the image url of the film poster.

    Attributes:
        title (str): String containing the title of the film.
        trailer_youtube_url (str): String containing the youtube url of the trailer.
        poster_image_url (str): String containing the image url of the film poster.
    """
    def __init__(self, title, trailer_youtube_url, poster_image_url):
        self.title=title
        self.poster_image_url=poster_image_url
        self.trailer_youtube_url=trailer_youtube_url
