import media
import fresh_tomatoes

# initialize movie objects
lotr=media.Movie("Lord of the Rings","https://www.youtube.com/watch?v=Pki6jbSb"
                 "XIY","http://www.gstatic.com/tv/thumb/movieposters/28828/p288"
                 "28_p_v8_as.jpg")
starship_troopers=media.Movie( "Starship Troopers","https://www.youtube.com/wat"
                               "ch?v=Y07I_KER5fE","http://t1.gstatic.com/images?"
                               "q=tbn:ANd9GcS9ruFwuwTIUlc89xcDElR-70LOip6oyah-O3"
                               "XEUslEXuJRrSaG")
uhf=media.Movie("UHF", "https://www.youtube.com/watch?v=tIJ6utj-DcU","http://www"
                ".gstatic.com/tv/thumb/movieposters/7906/p7906_p_v8_ab.jpg")
# create array of movie objects
listMovies = [lotr,starship_troopers,uhf]
# open the movies page
fresh_tomatoes.open_movies_page(listMovies)
