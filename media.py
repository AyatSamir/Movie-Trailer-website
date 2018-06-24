""" This project made by Ayat Samir """
import webbrowser # import module named webbrowser

class Movie():   #create class name Movie
   

    # this function initialize space on memory when create objects or instances and define prporties of class Movie
    def __init__(self, movie_title, poster_image, trailer_youtube):

        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
     # this method show youtube url trailer on web browser
     
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        

