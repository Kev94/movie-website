# Movie Website Project created by: Kevin Belasco
import fresh_tomatoes
import media
# import the file with my Movie class

# create the instances of class Movie
ferris_buellers_day_off = media.Movie("Ferris Bueller's Day Off",
                                      "A highschool senior takes us through a journey of his day when he skips school",
                                      "https://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg",
                                      "https://www.youtube.com/watch?v=D6gABQFR94U",
                                      "Release Date: 1986")

valkyrie = media.Movie("Valkyrie",
                       "A german soldier in WWII collects a team of fellow soldiers to try to overthrow Hitler and the Third Reich",
                       "https://upload.wikimedia.org/wikipedia/en/b/b8/Valkyrie_poster.jpg",
                       "https://www.youtube.com/watch?v=Ww9IWCGZeyw",
                       "Release Date: 2008")


the_departed = media.Movie("The Departed",
                           "A detective must take down a crime boss in Boston",
                           "https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
                           "https://www.youtube.com/watch?v=n4O3x5BH18E",
                           "Release Date: 2006")

step_brothers = media.Movie("Step Brothers",
                            "Two middle aged men who stil live at home must learn to become step brothers",
                            "https://upload.wikimedia.org/wikipedia/en/d/d9/StepbrothersMP08.jpg",
                            "https://www.youtube.com/watch?v=8QKE96wZTkw",
                            "Release Date: 2008")

american_pie = media.Movie("American Pie",
                           "A group of friends learn how to move onto adulthood",
                           "https://upload.wikimedia.org/wikipedia/en/c/c8/American_Pie1.jpg",
                           "https://www.youtube.com/watch?v=Sithad108Og",
                           "Release Date: 1999")

gladiator = media.Movie("Gladiator",
                        "A soldier who's family is murdered by the Roman army is captured and seeks revenge by becoming a gladiator in Rome",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=ol67qo3WhJk",
                        "Release Date: 2000")

saving_private_ryan = media.Movie("Saving Private Ryan",
                                  "A company of American soldiers during WWII must find a soldier to bring him home after the death of his brothers",
                                  "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
                                  "https://www.youtube.com/watch?v=RYID71hYHzg",
                                  "Release Date: 1998")
logan = media.Movie("Logan",
         "The famous wolverine x-man goes on his final journey, where he must protect a little girl who is somehow connected to him",
         "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
         "https://www.youtube.com/watch?v=Div0iP65aZo",
         "Release Date: 2017")

shot_caller = media.Movie("Shot Caller",
                          "A journey about how a businessman and family man turned gangster after an unfortunate event that would change his life forever",
                          "https://upload.wikimedia.org/wikipedia/en/2/25/Shot_Caller_poster.jpg",
                          "https://www.youtube.com/watch?v=QQxjyRr9k2E",
                          "Release Date: 2017")

# create an empty array and fill it with my movies
movies = [ferris_buellers_day_off,valkyrie,the_departed,step_brothers,american_pie,gladiator,saving_private_ryan,logan,shot_caller]
# now call the function open_movies_page() from my fresh_tomatoes.py file
# outputs the website with all of the correct functionalities 
fresh_tomatoes.open_movies_page(movies)

# to print out documentation of the class Movie:
print(media.Movie.__doc__)
