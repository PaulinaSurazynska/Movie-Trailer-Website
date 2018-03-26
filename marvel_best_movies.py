import media
import fresh_tomatoes

"""defining objects of Movie class"""
iron_man1 = media.Movie(
                        "Iron Man 1",
                        "After being held captive in an Afghan cave,"
                        "billionaire engineer Tony Stark creates a unique"
                        "weaponized suit of armor to fight evil.",
                        "https://upload.wikimedia.org/"
                        "wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://www.youtube.com/watch?v=8hYlB38asDY"
                        )

iron_man2 = media.Movie(
                        "Iron Man 2",
                        "With the world now aware of his identity as Iron Man,"
                        "Tony Stark must contend with both his declining"
                        "health and a vengeful mad man"
                        "with ties to his father's legacy.",
                        "https://upload.wikimedia.org/"
                        "wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                        "https://www.youtube.com/watch?v=wKtcmiifycU"
                        )

iron_man3 = media.Movie(
                        "Iron Man 3",
                        "When Tony Stark's world is torn apart by"
                        "a formidable terrorist called the Mandarin,"
                        "he starts an odyssey of rebuilding and retribution.",
                        "https://upload.wikimedia.org/"
                        "wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc"
                        )

capitan_america1 = media.Movie(
                                "Captain America: The First Avenger",
                                "Steve Rogers,"
                                "a rejected military soldier"
                                "transforms into Captain America"
                                "after taking"
                                "a dose of a 'Super-Soldier serum'."
                                "But being Captain America comes at a price as"
                                "he attempts to take down a war monger and"
                                "a terrorist organization.",
                                "https://upload.wikimedia.org/wikipedia/"
                                "en/3/37/Captain_America_The_First"
                                "_Avenger_poster.jpg",
                                "https://www.youtube.com/watch?v=JerVrbLldXw"
                                )

capitan_america2 = media.Movie(
                               "Captain America: The Winter Soldier",
                               "As Steve Rogers struggles to embrace"
                               "his role in the modern world, he teams"
                               "up with a fellow Avenger"
                               "and S.H.I.E.L.D agent,"
                               "Black Widow, to battle a new"
                               "threat from history"
                               ": an assassin known as"
                               "the Winter Soldier.",
                               "https://upload.wikimedia.org/wikipedia/en"
                               "/e/e8/Captain_America_The_Winter_Soldier.jpg",
                               "https://www.youtube.com/watch?v=7SlILk2WMTI"
                               )

capitan_america3 = media.Movie(
                               "Captain America: Civil War",
                               "Political involvement in the Avengers'"
                               "activities causes a rift between Captain"
                               "America and Iron Man.",
                               "https://upload.wikimedia.org/"
                               "wikipedia/en/5/53/"
                               "Captain_America_Civil_War_poster.jpg",
                               "https://www.youtube.com/watch?v=1L3c17AmCZw"
                               )

"""list of movies that will be a input for open_movies_page()"""
movies = [
        iron_man1,
        iron_man2,
        iron_man3,
        capitan_america1,
        capitan_america2,
        capitan_america3
        ]
fresh_tomatoes.open_movies_page(movies)
