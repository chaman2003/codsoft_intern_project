import random
import difflib
import re

# List of movies with attributes
movies_data = {
    'Avatar': {'genres': 'Action, Adventure, Fantasy'},
    'Titanic': {'genres': 'Drama, Romance'},
    'Avengers: Endgame': {'genres': 'Action, Adventure, Drama'},
    'The Lion King (2019)': {'genres': 'Animation, Adventure, Drama'},
    'Jurassic Park': {'genres': 'Action, Adventure, Sci-Fi'},
    'The Avengers': {'genres': 'Action, Adventure, Sci-Fi'},
    'Frozen II': {'genres': 'Animation, Adventure, Comedy'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Harry Potter and the Deathly Hallows – Part 2': {'genres': 'Adventure, Drama, Fantasy'},
    'The Lord of the Rings: The Return of the King': {'genres': 'Action, Adventure, Drama'},
    'Star Wars: Episode I – The Phantom Menace': {'genres': 'Action, Adventure, Fantasy'},
    'Black Panther': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Philosopher\'s Stone': {'genres': 'Adventure, Family, Fantasy'},
    'Star Wars: The Last Jedi': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World: Fallen Kingdom': {'genres': 'Action, Adventure, Sci-Fi'},
    'Beauty and the Beast (2017)': {'genres': 'Family, Fantasy, Musical'},
    'Incredibles 2': {'genres': 'Animation, Action, Adventure'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Iron Man 3': {'genres': 'Action, Adventure, Sci-Fi'},
    'Minions': {'genres': 'Animation, Adventure, Comedy'},
    'Aquaman': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Captain Marvel': {'genres': 'Action, Adventure, Sci-Fi'},
    'Transformers: Dark of the Moon': {'genres': 'Action, Adventure, Sci-Fi'},
    'Skyfall': {'genres': 'Action, Adventure, Thriller'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Toy Story 4': {'genres': 'Animation, Adventure, Comedy'},
    'Alice in Wonderland (2010)': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book (2016)': {'genres': 'Adventure, Drama, Family'},
    'Finding Dory': {'genres': 'Animation, Adventure, Comedy'},
    'Star Wars: Episode III – Revenge of the Sith': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Fellowship of the Ring': {'genres': 'Action, Adventure, Drama'},
    'Harry Potter and the Order of the Phoenix': {'genres': 'Action, Adventure, Family'},
    'The Dark Knight': {'genres': 'Action, Crime, Drama'},
    'Harry Potter and the Half-Blood Prince': {'genres': 'Action, Adventure, Family'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Shrek 2': {'genres': 'Animation, Adventure, Comedy'},
    'Finding Nemo': {'genres': 'Animation, Adventure, Comedy'},
    'Harry Potter and the Goblet of Fire': {'genres': 'Adventure, Family, Fantasy'},
    'Spider-Man: No Way Home': {'genres': 'Action, Adventure, Fantasy'},
    'Harry Potter and the Chamber of Secrets': {'genres': 'Adventure, Family, Fantasy'},
    'The Lord of the Rings: The Fellowship of the Ring': {'genres': 'Action, Adventure, Drama'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Pirates of the Caribbean: On Stranger Tides': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World': {'genres': 'Action, Adventure, Sci-Fi'},
    'The Lion King': {'genres': 'Animation, Adventure, Drama'},
    'The Avengers': {'genres': 'Action, Adventure, Sci-Fi'},
    'The Avengers: Age of Ultron': {'genres': 'Action, Adventure, Sci-Fi'},
    'Frozen': {'genres': 'Animation, Adventure, Comedy'},
    'Beauty and the Beast': {'genres': 'Animation, Family, Fantasy'},
    'Incredibles 2': {'genres': 'Animation, Action, Adventure'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Iron Man 3': {'genres': 'Action, Adventure, Sci-Fi'},
    'Minions': {'genres': 'Animation, Adventure, Comedy'},
    'Aquaman': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Skyfall': {'genres': 'Action, Adventure, Thriller'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Alice in Wonderland': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book': {'genres': 'Adventure, Drama, Family'},
    'Finding Dory': {'genres': 'Animation, Adventure, Comedy'},
    'Star Wars: Episode III – Revenge of the Sith': {'genres': 'Action, Adventure, Fantasy'},
    'Harry Potter and the Order of the Phoenix': {'genres': 'Action, Adventure, Family'},
    'Harry Potter and the Half-Blood Prince': {'genres': 'Action, Adventure, Family'},
    'Shrek 2': {'genres': 'Animation, Adventure, Comedy'},
    'Finding Nemo': {'genres': 'Animation, Adventure, Comedy'},
    'Harry Potter and the Goblet of Fire': {'genres': 'Adventure, Family, Fantasy'},
    'The Lord of the Rings: The Return of the King': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: No Way Home': {'genres': 'Action, Adventure, Fantasy'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Chamber of Secrets': {'genres': 'Adventure, Family, Fantasy'},
    'Jurassic Park': {'genres': 'Action, Adventure, Sci-Fi'},
    'Star Wars: Episode I – The Phantom Menace': {'genres': 'Action, Adventure, Fantasy'},
    'Black Panther': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Philosopher\'s Stone': {'genres': 'Adventure, Family, Fantasy'},
    'Star Wars: The Last Jedi': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World: Fallen Kingdom': {'genres': 'Action, Adventure, Sci-Fi'},
    'Beauty and the Beast': {'genres': 'Family, Fantasy, Musical'},
    'Toy Story 4': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book (2016)': {'genres': 'Adventure, Drama, Family'},
    'Alice in Wonderland (2010)': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Lord of the Rings: The Fellowship of the Ring': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'The Lion King (2019)': {'genres': 'Animation, Adventure, Drama'},
    'Transformers: Dark of the Moon': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Deathly Hallows – Part 2': {'genres': 'Adventure, Drama, Fantasy'},
    'Star Wars: Episode I – The Phantom Menace': {'genres': 'Action, Adventure, Fantasy'},
    'Black Panther': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Philosopher\'s Stone': {'genres': 'Adventure, Family, Fantasy'},
    'Star Wars: The Last Jedi': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World: Fallen Kingdom': {'genres': 'Action, Adventure, Sci-Fi'},
    'Beauty and the Beast (2017)': {'genres': 'Family, Fantasy, Musical'},
    'Incredibles 2': {'genres': 'Animation, Action, Adventure'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Iron Man 3': {'genres': 'Action, Adventure, Sci-Fi'},
    'Minions': {'genres': 'Animation, Adventure, Comedy'},
    'Aquaman': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Captain Marvel': {'genres': 'Action, Adventure, Sci-Fi'},
    'Transformers: Dark of the Moon': {'genres': 'Action, Adventure, Sci-Fi'},
    'Skyfall': {'genres': 'Action, Adventure, Thriller'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Toy Story 4': {'genres': 'Animation, Adventure, Comedy'},
    'Alice in Wonderland (2010)': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book (2016)': {'genres': 'Adventure, Drama, Family'},
    'Finding Dory': {'genres': 'Animation, Adventure, Comedy'},
    'Star Wars: Episode III – Revenge of the Sith': {'genres': 'Action, Adventure, Fantasy'},
    'Harry Potter and the Order of the Phoenix': {'genres': 'Action, Adventure, Family'},
    'Harry Potter and the Half-Blood Prince': {'genres': 'Action, Adventure, Family'},
    'Shrek 2': {'genres': 'Animation, Adventure, Comedy'},
    'Finding Nemo': {'genres': 'Animation, Adventure, Comedy'},
    'Harry Potter and the Goblet of Fire': {'genres': 'Adventure, Family, Fantasy'},
    'The Lord of the Rings: The Return of the King': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: No Way Home': {'genres': 'Action, Adventure, Fantasy'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Chamber of Secrets': {'genres': 'Adventure, Family, Fantasy'},
    'Jurassic Park': {'genres': 'Action, Adventure, Sci-Fi'},
    'Star Wars: Episode I – The Phantom Menace': {'genres': 'Action, Adventure, Fantasy'},
    'Black Panther': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Philosopher\'s Stone': {'genres': 'Adventure, Family, Fantasy'},
    'Star Wars: The Last Jedi': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World: Fallen Kingdom': {'genres': 'Action, Adventure, Sci-Fi'},
    'Beauty and the Beast (2017)': {'genres': 'Family, Fantasy, Musical'},
    'Incredibles 2': {'genres': 'Animation, Action, Adventure'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Iron Man 3': {'genres': 'Action, Adventure, Sci-Fi'},
    'Minions': {'genres': 'Animation, Adventure, Comedy'},
    'Aquaman': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Captain Marvel': {'genres': 'Action, Adventure, Sci-Fi'},
    'Transformers: Dark of the Moon': {'genres': 'Action, Adventure, Sci-Fi'},
    'Skyfall': {'genres': 'Action, Adventure, Thriller'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Toy Story 4': {'genres': 'Animation, Adventure, Comedy'},
    'Alice in Wonderland (2010)': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book (2016)': {'genres': 'Adventure, Drama, Family'},
    'Finding Dory': {'genres': 'Animation, Adventure, Comedy'},
    'Star Wars: Episode III – Revenge of the Sith': {'genres': 'Action, Adventure, Fantasy'},
    'Harry Potter and the Order of the Phoenix': {'genres': 'Action, Adventure, Family'},
    'Harry Potter and the Half-Blood Prince': {'genres': 'Action, Adventure, Family'},
    'Shrek 2': {'genres': 'Animation, Adventure, Comedy'},
    'Finding Nemo': {'genres': 'Animation, Adventure, Comedy'},
    'Harry Potter and the Goblet of Fire': {'genres': 'Adventure, Family, Fantasy'},
    'The Lord of the Rings: The Return of the King': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: No Way Home': {'genres': 'Action, Adventure, Fantasy'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Chamber of Secrets': {'genres': 'Adventure, Family, Fantasy'},
    'Jurassic Park': {'genres': 'Action, Adventure, Sci-Fi'},
    'Star Wars: Episode I – The Phantom Menace': {'genres': 'Action, Adventure, Fantasy'},
    'Black Panther': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Philosopher\'s Stone': {'genres': 'Adventure, Family, Fantasy'},
    'Star Wars: The Last Jedi': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World: Fallen Kingdom': {'genres': 'Action, Adventure, Sci-Fi'},
    'Beauty and the Beast (2017)': {'genres': 'Family, Fantasy, Musical'},
    'Incredibles 2': {'genres': 'Animation, Action, Adventure'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Iron Man 3': {'genres': 'Action, Adventure, Sci-Fi'},
    'Minions': {'genres': 'Animation, Adventure, Comedy'},
    'Aquaman': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Captain Marvel': {'genres': 'Action, Adventure, Sci-Fi'},
    'Transformers: Dark of the Moon': {'genres': 'Action, Adventure, Sci-Fi'},
    'Skyfall': {'genres': 'Action, Adventure, Thriller'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Toy Story 4': {'genres': 'Animation, Adventure, Comedy'},
    'Alice in Wonderland (2010)': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book (2016)': {'genres': 'Adventure, Drama, Family'},
    'Finding Dory': {'genres': 'Animation, Adventure, Comedy'},
    'Star Wars: Episode III – Revenge of the Sith': {'genres': 'Action, Adventure, Fantasy'},
    'Harry Potter and the Order of the Phoenix': {'genres': 'Action, Adventure, Family'},
    'Harry Potter and the Half-Blood Prince': {'genres': 'Action, Adventure, Family'},
    'Shrek 2': {'genres': 'Animation, Adventure, Comedy'},
    'Finding Nemo': {'genres': 'Animation, Adventure, Comedy'},
    'Harry Potter and the Goblet of Fire': {'genres': 'Adventure, Family, Fantasy'},

}

# Add more movies and genres
additional_movies = {
     'Avatar': {'genres': 'Action, Adventure, Fantasy'},
    'Titanic': {'genres': 'Drama, Romance'},
    'Avengers: Endgame': {'genres': 'Action, Adventure, Drama'},
    'The Lion King (2019)': {'genres': 'Animation, Adventure, Drama'},
    'Jurassic Park': {'genres': 'Action, Adventure, Sci-Fi'},
    'The Avengers': {'genres': 'Action, Adventure, Sci-Fi'},
    'Frozen II': {'genres': 'Animation, Adventure, Comedy'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Harry Potter and the Deathly Hallows – Part 2': {'genres': 'Adventure, Drama, Fantasy'},
    'The Lord of the Rings: The Return of the King': {'genres': 'Action, Adventure, Drama'},
    'Star Wars: Episode I – The Phantom Menace': {'genres': 'Action, Adventure, Fantasy'},
    'Black Panther': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Philosopher\'s Stone': {'genres': 'Adventure, Family, Fantasy'},
    'Star Wars: The Last Jedi': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World: Fallen Kingdom': {'genres': 'Action, Adventure, Sci-Fi'},
    'Beauty and the Beast (2017)': {'genres': 'Family, Fantasy, Musical'},
    'Incredibles 2': {'genres': 'Animation, Action, Adventure'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Iron Man 3': {'genres': 'Action, Adventure, Sci-Fi'},
    'Minions': {'genres': 'Animation, Adventure, Comedy'},
    'Aquaman': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Captain Marvel': {'genres': 'Action, Adventure, Sci-Fi'},
    'Transformers: Dark of the Moon': {'genres': 'Action, Adventure, Sci-Fi'},
    'Skyfall': {'genres': 'Action, Adventure, Thriller'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Toy Story 4': {'genres': 'Animation, Adventure, Comedy'},
    'Alice in Wonderland (2010)': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book (2016)': {'genres': 'Adventure, Drama, Family'},
    'Finding Dory': {'genres': 'Animation, Adventure, Comedy'},
    'Star Wars: Episode III – Revenge of the Sith': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Fellowship of the Ring': {'genres': 'Action, Adventure, Drama'},
    'Harry Potter and the Order of the Phoenix': {'genres': 'Action, Adventure, Family'},
    'The Dark Knight': {'genres': 'Action, Crime, Drama'},
    'Harry Potter and the Half-Blood Prince': {'genres': 'Action, Adventure, Family'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Shrek 2': {'genres': 'Animation, Adventure, Comedy'},
    'Finding Nemo': {'genres': 'Animation, Adventure, Comedy'},
    'Harry Potter and the Goblet of Fire': {'genres': 'Adventure, Family, Fantasy'},
    'Spider-Man: No Way Home': {'genres': 'Action, Adventure, Fantasy'},
    'Harry Potter and the Chamber of Secrets': {'genres': 'Adventure, Family, Fantasy'},
    'The Lord of the Rings: The Fellowship of the Ring': {'genres': 'Action, Adventure, Drama'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Pirates of the Caribbean: On Stranger Tides': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World': {'genres': 'Action, Adventure, Sci-Fi'},
    'The Lion King': {'genres': 'Animation, Adventure, Drama'},
    'The Avengers': {'genres': 'Action, Adventure, Sci-Fi'},
    'The Avengers: Age of Ultron': {'genres': 'Action, Adventure, Sci-Fi'},
    'Frozen': {'genres': 'Animation, Adventure, Comedy'},
    'Beauty and the Beast': {'genres': 'Animation, Family, Fantasy'},
    'Incredibles 2': {'genres': 'Animation, Action, Adventure'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Iron Man 3': {'genres': 'Action, Adventure, Sci-Fi'},
    'Minions': {'genres': 'Animation, Adventure, Comedy'},
    'Aquaman': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Skyfall': {'genres': 'Action, Adventure, Thriller'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Alice in Wonderland': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book': {'genres': 'Adventure, Drama, Family'},
    'Finding Dory': {'genres': 'Animation, Adventure, Comedy'},
    'Star Wars: Episode III – Revenge of the Sith': {'genres': 'Action, Adventure, Fantasy'},
    'Harry Potter and the Order of the Phoenix': {'genres': 'Action, Adventure, Family'},
    'Harry Potter and the Half-Blood Prince': {'genres': 'Action, Adventure, Family'},
    'Shrek 2': {'genres': 'Animation, Adventure, Comedy'},
    'Finding Nemo': {'genres': 'Animation, Adventure, Comedy'},
    'Harry Potter and the Goblet of Fire': {'genres': 'Adventure, Family, Fantasy'},
    'The Lord of the Rings: The Return of the King': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: No Way Home': {'genres': 'Action, Adventure, Fantasy'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Chamber of Secrets': {'genres': 'Adventure, Family, Fantasy'},
    'Jurassic Park': {'genres': 'Action, Adventure, Sci-Fi'},
    'Star Wars: Episode I – The Phantom Menace': {'genres': 'Action, Adventure, Fantasy'},
    'Black Panther': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Philosopher\'s Stone': {'genres': 'Adventure, Family, Fantasy'},
    'Star Wars: The Last Jedi': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World: Fallen Kingdom': {'genres': 'Action, Adventure, Sci-Fi'},
    'Beauty and the Beast': {'genres': 'Family, Fantasy, Musical'},
    'Toy Story 4': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book (2016)': {'genres': 'Adventure, Drama, Family'},
    'Alice in Wonderland (2010)': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Lord of the Rings: The Fellowship of the Ring': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'The Lion King (2019)': {'genres': 'Animation, Adventure, Drama'},
    'Transformers: Dark of the Moon': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Deathly Hallows – Part 2': {'genres': 'Adventure, Drama, Fantasy'},
    'Star Wars: Episode I – The Phantom Menace': {'genres': 'Action, Adventure, Fantasy'},
    'Black Panther': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Philosopher\'s Stone': {'genres': 'Adventure, Family, Fantasy'},
    'Star Wars: The Last Jedi': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World: Fallen Kingdom': {'genres': 'Action, Adventure, Sci-Fi'},
    'Beauty and the Beast (2017)': {'genres': 'Family, Fantasy, Musical'},
    'Incredibles 2': {'genres': 'Animation, Action, Adventure'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Iron Man 3': {'genres': 'Action, Adventure, Sci-Fi'},
    'Minions': {'genres': 'Animation, Adventure, Comedy'},
    'Aquaman': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Captain Marvel': {'genres': 'Action, Adventure, Sci-Fi'},
    'Transformers: Dark of the Moon': {'genres': 'Action, Adventure, Sci-Fi'},
    'Skyfall': {'genres': 'Action, Adventure, Thriller'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Toy Story 4': {'genres': 'Animation, Adventure, Comedy'},
    'Alice in Wonderland (2010)': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book (2016)': {'genres': 'Adventure, Drama, Family'},
    'Finding Dory': {'genres': 'Animation, Adventure, Comedy'},
    'Star Wars: Episode III – Revenge of the Sith': {'genres': 'Action, Adventure, Fantasy'},
    'Harry Potter and the Order of the Phoenix': {'genres': 'Action, Adventure, Family'},
    'Harry Potter and the Half-Blood Prince': {'genres': 'Action, Adventure, Family'},
    'Shrek 2': {'genres': 'Animation, Adventure, Comedy'},
    'Finding Nemo': {'genres': 'Animation, Adventure, Comedy'},
    'Harry Potter and the Goblet of Fire': {'genres': 'Adventure, Family, Fantasy'},
    'The Lord of the Rings: The Return of the King': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: No Way Home': {'genres': 'Action, Adventure, Fantasy'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Chamber of Secrets': {'genres': 'Adventure, Family, Fantasy'},
    'Jurassic Park': {'genres': 'Action, Adventure, Sci-Fi'},
    'Star Wars: Episode I – The Phantom Menace': {'genres': 'Action, Adventure, Fantasy'},
    'Black Panther': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Philosopher\'s Stone': {'genres': 'Adventure, Family, Fantasy'},
    'Star Wars: The Last Jedi': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World: Fallen Kingdom': {'genres': 'Action, Adventure, Sci-Fi'},
    'Beauty and the Beast (2017)': {'genres': 'Family, Fantasy, Musical'},
    'Incredibles 2': {'genres': 'Animation, Action, Adventure'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Iron Man 3': {'genres': 'Action, Adventure, Sci-Fi'},
    'Minions': {'genres': 'Animation, Adventure, Comedy'},
    'Aquaman': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Captain Marvel': {'genres': 'Action, Adventure, Sci-Fi'},
    'Transformers: Dark of the Moon': {'genres': 'Action, Adventure, Sci-Fi'},
    'Skyfall': {'genres': 'Action, Adventure, Thriller'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Toy Story 4': {'genres': 'Animation, Adventure, Comedy'},
    'Alice in Wonderland (2010)': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book (2016)': {'genres': 'Adventure, Drama, Family'},
    'Finding Dory': {'genres': 'Animation, Adventure, Comedy'},
    'Star Wars: Episode III – Revenge of the Sith': {'genres': 'Action, Adventure, Fantasy'},
    'Harry Potter and the Order of the Phoenix': {'genres': 'Action, Adventure, Family'},
    'Harry Potter and the Half-Blood Prince': {'genres': 'Action, Adventure, Family'},
    'Shrek 2': {'genres': 'Animation, Adventure, Comedy'},
    'Finding Nemo': {'genres': 'Animation, Adventure, Comedy'},
    'Harry Potter and the Goblet of Fire': {'genres': 'Adventure, Family, Fantasy'},
    'The Lord of the Rings: The Return of the King': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: No Way Home': {'genres': 'Action, Adventure, Fantasy'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Chamber of Secrets': {'genres': 'Adventure, Family, Fantasy'},
    'Jurassic Park': {'genres': 'Action, Adventure, Sci-Fi'},
    'Star Wars: Episode I – The Phantom Menace': {'genres': 'Action, Adventure, Fantasy'},
    'Black Panther': {'genres': 'Action, Adventure, Sci-Fi'},
    'Harry Potter and the Philosopher\'s Stone': {'genres': 'Adventure, Family, Fantasy'},
    'Star Wars: The Last Jedi': {'genres': 'Action, Adventure, Fantasy'},
    'Jurassic World: Fallen Kingdom': {'genres': 'Action, Adventure, Sci-Fi'},
    'Beauty and the Beast (2017)': {'genres': 'Family, Fantasy, Musical'},
    'Incredibles 2': {'genres': 'Animation, Action, Adventure'},
    'The Fate of the Furious': {'genres': 'Action, Adventure, Crime'},
    'Iron Man 3': {'genres': 'Action, Adventure, Sci-Fi'},
    'Minions': {'genres': 'Animation, Adventure, Comedy'},
    'Aquaman': {'genres': 'Action, Adventure, Fantasy'},
    'The Lord of the Rings: The Two Towers': {'genres': 'Action, Adventure, Drama'},
    'Spider-Man: Far From Home': {'genres': 'Action, Adventure, Sci-Fi'},
    'Captain Marvel': {'genres': 'Action, Adventure, Sci-Fi'},
    'Transformers: Dark of the Moon': {'genres': 'Action, Adventure, Sci-Fi'},
    'Skyfall': {'genres': 'Action, Adventure, Thriller'},
    'The Dark Knight Rises': {'genres': 'Action, Thriller'},
    'Toy Story 4': {'genres': 'Animation, Adventure, Comedy'},
    'Alice in Wonderland (2010)': {'genres': 'Adventure, Family, Fantasy'},
    'Pirates of the Caribbean: Dead Man\'s Chest': {'genres': 'Action, Adventure, Fantasy'},
    'Despicable Me 3': {'genres': 'Animation, Adventure, Comedy'},
    'The Jungle Book (2016)': {'genres': 'Adventure, Drama, Family'},
    'Finding Dory': {'genres': 'Animation, Adventure, Comedy'},
    'Star Wars: Episode III – Revenge of the Sith': {'genres': 'Action, Adventure, Fantasy'},
    'Harry Potter and the Order of the Phoenix': {'genres': 'Action, Adventure, Family'},
    'Harry Potter and the Half-Blood Prince': {'genres': 'Action, Adventure, Family'},
    'Shrek 2': {'genres': 'Animation, Adventure, Comedy'},
    'Finding Nemo': {'genres': 'Animation, Adventure, Comedy'},
    'Harry Potter and the Goblet of Fire': {'genres': 'Adventure, Family, Fantasy'},

}

movies_data.update(additional_movies)

# Function to recommend movies based on user preferences
def recommend_movies(movie, movies_data):
    # Extract genres of the input movie
    input_genres = movies_data.get(movie, {}).get('genres', '')
    
    # Find movies with similar genres
    similar_movies = []
    for title, attributes in movies_data.items():
        if title != movie:
            if input_genres in attributes.get('genres', ''):
                similar_movies.append(title)
    
    return similar_movies[:5]  # Return top 5 similar movies

# Function to print a separator line
def print_separator():
    print('-' * 50)

# Function to find the closest matching movie name
def find_closest_movie(user_input, movies_data):
    user_input_processed = re.sub(r'\W+', '', user_input).lower()  # Remove non-alphanumeric characters and convert to lowercase
    for movie_title in movies_data.keys():
        movie_title_processed = re.sub(r'\W+', '', movie_title).lower()  # Remove non-alphanumeric characters and convert to lowercase
        if user_input_processed in movie_title_processed:
            return movie_title
    return None

# Main loop
while True:
    print_separator()
    user_movie = input("Enter a movie name (type 'exit' to quit): ").strip()

    if user_movie.lower() == 'exit':
        print("Exiting...")
        break

    # Find the closest matching movie name
    matched_movie = find_closest_movie(user_movie, movies_data)
    if matched_movie:
        user_movie = matched_movie
    else:
        print("Movie not found! Please enter a valid movie name.")
        continue

    print_separator()
    print("Movie:", user_movie)
    print("Genre:", movies_data[user_movie]['genres'])

    print_separator()
    print("Recommended movies:")
    similar_movies = recommend_movies(user_movie, movies_data)
    for idx, movie in enumerate(similar_movies, start=1):
        print(idx, ".", movie)

    print_separator()
