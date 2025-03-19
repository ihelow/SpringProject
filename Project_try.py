class Genre: #class for the genre
    def __init__(self, name):
        self.name = name

class MusicSuggestor: #main body that contains all the funcitons
    def __init__(self):
        self.genres = ["Rock", "Pop", "Jazz", "Hip-Hop", 
                       "Classical", "Electronic", "Country", "Reggae"] # available genresn to the user
        self.favorite_genres = [] #initilizing the empty list for the user
        self.songs = {       #dictionary of the different songs that corresponds to the specific genre
            "Rock": ["Bohemian Rhapsody - Queen", "Stairway to Heaven - Led Zeppelin"],
            "Pop": ["Blinding Lights - The Weeknd", "Shape of You - Ed Sheeran"],
            "Jazz": ["Take Five - Dave Brubeck", "So What - Miles Davis"],
            "Hip-Hop": ["Sicko Mode - Travis Scott", "Lose Yourself - Eminem"],
            "Classical": ["Moonlight Sonata - Beethoven", "The Four Seasons - Vivaldi"],
            "Electronic": ["Strobe - Deadmau5", "Titanium - David Guetta"],
            "Country": ["Take Me Home, Country Roads - John Denver", "Jolene - Dolly Parton"],
            "Reggae": ["No Woman, No Cry - Bob Marley", "Bad Boys - Inner Circle"]
        }
    
    def greet_user(self): #funciton for greeeting the user
        print("Welcome to the Music Suggestor")
        print("Here are the available genres you can choose from:")
        print(", ".join(self.genres)) #prints out the available genres to the user
    
    def add_genre(self): #function for adding a genre to the previously created list
        print("Available genres:", ", ".join(self.genres))
        genre = input("Enter a genre to add: ").strip().title()
        if genre in self.genres and genre not in self.favorite_genres:
            self.favorite_genres.append(genre)
            print(f"{genre} added to favorites.")
        else:
            print("Invalid or duplicate genre")
    
    def remove_genre(self): #function for removing a genre from the previously created list
        genre = input("Enter a genre to remove: ").strip().title()
        if genre in self.favorite_genres:
            self.favorite_genres.remove(genre)
            print(f"{genre} removed from favorites")
        else:
            print("Genre not found in favorites")
    
    def view_favorites(self): #this function will allow the user to view the list they created
        if self.favorite_genres:
            print("\nYour favorite genres:", ", ".join(self.favorite_genres))
        else:
            print("\nYou have no favorite genres yet")
    
    def view_songs(self): #after they created the list of genreds they will be able to veiw the list of corresponding songs
        if not self.favorite_genres:
            print("\nYou have no favorite genres yet. Add some to see song suggestions")
            return
        print("\nHere are songs from your favorite genres:")
        for genre in self.favorite_genres:
            print(f"\n{genre}:")
            for song in self.songs.get(genre, []):
                print(f"- {song}")
    
    def run(self): #runs the main program loop where all the interactions with the user are stored
        self.greet_user()
        while True:
            print("\nOptions: 1. Add Genre  2. Remove Genre  3. View Favorites  4. View Songs  5. Quit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.add_genre() #adds genres to the favorite list
            elif choice == "2":
                self.remove_genre() #removes the genre from the favorites list
            elif choice == "3":
                self.view_favorites() #allows to view the list
            elif choice == "4":
                self.view_songs() #allows to see the songs that correspond to the favorite genres
            elif choice == "5": #quits the program
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again") #if the user chooses a different number 

#calling the functions
music_suggestor = MusicSuggestor()
music_suggestor.run()
