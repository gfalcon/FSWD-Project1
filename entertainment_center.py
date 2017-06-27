import fresh_tomatoes
import media

# This file is an arbritrarily long list of movie objecs to be displayed.
# Each movie is initialized with a title, a tag line, a url link to the
# movie poster, and a url link to the movie trailer.

forrest = media.Movie(
    "Forrest Gump",
    "He's not a smart man, but he knows what love is.",
    ("http://t3.gstatic.com/images?q=tbn:ANd9GcQCFOcMb5_"
        "zkdZg4B4JvIGLlTQTvLdtLjiS5axJJDqP1FaI8Yyx"),
    "https://www.youtube.com/watch?v=uPIEn0M8su0")


bourne = media.Movie(
    "The Bourne Identity",
    ("A man seeks his past while performing spectacular, and "
        "often justified, violence."),
    "http://www.gstatic.com/tv/thumb/movieposters/28900/p28900_p_v8_ai.jpg",
    "https://www.youtube.com/watch?v=FpKaB5dvQ4g")

jp = media.Movie(
    "Jurassic Park",
    ("A theme park suffers a breakdown that allows its "
        "cloned dinosaurs to run amok."),
    ("http://waytooindie.com/wp-content/uploads/2015/09/"
        "jurassic-park-movie-cover.jpg"),
    "https://www.youtube.com/watch?v=lc0UehYemQA")

tig = media.Movie(
    "The Iron Giant",
    ("An alien war-machine befriends a young boy and overcomes "
        "its programming."),
    ("https://68.media.tumblr.com/00e25be0eeb7df2aa43b516aae9fef27/"
        "tumblr_inline_n0u0awtuQa1qcp7s1.jpg"),
    "https://www.youtube.com/watch?v=obLtyj8hfFk")

ca_tws = media.Movie(
    "Captain America: Civil War",
    ("Steve Rogers struggles to protect the last link to his past"
        " from the new family he has made in the present."),
    ("http://www.joblo.com/timthumb.php?src=/posters/images/full/"
        "Captain-America-Civil-War-main-poster.jpg&h=600&q=100"),
    "https://www.youtube.com/watch?v=dKrVegVI0Us")

tcitw = media.Movie(
    "The Cabin in the Woods",
    "You think you know the story.",
    ("http://t3.gstatic.com/images?q=tbn:ANd9GcSQrX9GYLuT1VwsNR7"
        "RPOvfW6GHwxxwaBnE9dTXwSMaSvAq77HR"),
    "https://www.youtube.com/watch?v=NsIilFNNmkY")

# Save the movie objects into a list titled -movies-.
movies = [forrest, bourne, jp, tig, ca_tws, tcitw]

# Pass the -movies- list to the fresh tomatoes page for display to the user.
fresh_tomatoes.open_movies_page(movies)

