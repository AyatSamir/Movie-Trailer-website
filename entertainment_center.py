import fresh_tomatoes  # import or include fresh_tomatoes file
import media

#create multiple instance of class 
post_it = media.Movie("Post It", "https://i.imgur.com/SXokgf8.jpg",
                      "https://www.youtube.com/watch?v=aVgeJ5eqlSM")

killer_in_red = media.Movie("Killer in Red", "https://i.imgur.com/cqeqHkJ.jpg",
                            "https://www.youtube.com/watch?v=8_nRZjJfD7Y")

cup_of_positivity = media.Movie("A cup of Positivity","https://i.imgur.com/u71ghry.jpg",
                                "https://www.youtube.com/watch?v=FJxjBJ7JLMY")

dream_with_me = media.Movie("Dream with me","https://i.imgur.com/lOGxeTh.jpg",
                            
                            "https://www.youtube.com/watch?v=H-k6kiTz9Vg")

translator = media.Movie("The Translator","https://i.imgur.com/Z0X52iY.jpg",
                         "https://www.youtube.com/watch?v=PA8HTX6CXBs")

elevator = media.Movie("The Elevator","https://i.imgur.com/lnrxGas.jpg",
                       "https://www.youtube.com/watch?v=Q-TQQE1y68c")
movies = [post_it, killer_in_red, cup_of_positivity, dream_with_me, translator , elevator]

fresh_tomatoes.open_movies_page(movies)
