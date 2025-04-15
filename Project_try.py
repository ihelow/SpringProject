import json
import random

class Genre:
    """Represents a music genre with a name and optional description."""
    def __init__(self, name, description="No description available"):
        self.name = name
        self.description = description

class MusicSuggestor:
    """A class that helps users select favorite music genres and get song suggestions."""
    
    def __init__(self):
        """Initializes available genres, user preferences, and a song library."""
        self.genres = {
            "Rock": Genre("Rock", "A genre characterized by strong rhythms and electric guitars."),
            "Pop": Genre("Pop", "Popular and catchy tunes often found in the mainstream."),
            "Jazz": Genre("Jazz", "A genre known for improvisation and swing rhythms."),
            "Hip-Hop": Genre("Hip-Hop", "A genre with rhythmic beats and spoken word lyrics."),
            "Classical": Genre("Classical", "Music rooted in the traditions of Western culture."),
            "Electronic": Genre("Electronic", "Music produced using electronic instruments."),
            "Country": Genre("Country", "A genre with storytelling lyrics and simple harmonies."),
            "Reggae": Genre("Reggae", "A genre with offbeat rhythms and socially conscious lyrics."),
        }

        self.favorite_genres = set()  # Using a set for efficiency
        self.songs = {
            "Rock": ["Bohemian Rhapsody - Queen", "Stairway to Heaven - Led Zeppelin"],
            "Pop": ["Blinding Lights - The Weeknd", "Glamorous - Fergie"],
            "Jazz": ["Take Five - Dave Brubeck", "So What - Miles Davis"],
            "Hip-Hop": ["Sicko Mode - Travis Scott", "Lose Yourself - Eminem"],
            "Classical": ["Moonlight Sonata - Beethoven", "The Four Seasons - Vivaldi"],
            "Electronic": ["Strobe - Deadmau5", "Titanium - David Guetta"],
            "Country": ["Take Me Home, Country Roads - John Denver", "Jolene - Dolly Parton"],
            "Reggae": ["No Woman, No Cry - Bob Marley", "Bad Boys - Inner Circle"]
        }

        self.load_favorites()  # Load saved preferences if available

    def greet_user(self):
        """Displays a welcome message and available genres."""
        print("\nWelcome to the Music Suggestor!")
        print("\nThis program will allow you to create your own collection of favorite genres and songs!")
        print()
        print("Available genres:")
        for genre_name, genre in self.genres.items():
            print(f"- {genre_name}: {genre.description}")

    def add_genre(self):
        """Adds a genre to the user's favorite list after validation."""
        print("Available genres:", ", ".join(self.genres.keys()))
        genre = input("Enter a genre to add: ").strip().title()

        if not genre:
            print("Invalid input! Genre name cannot be empty.")
            return

        if genre in self.genres and genre not in self.favorite_genres:
            self.favorite_genres.add(genre)
            self.save_favorites()
            print(f"{genre} added to favorites.")
        else:
            print("Invalid genre or already in favorites.")

    def remove_genre(self):
        """Removes a genre from the user's favorites list."""
        if not self.favorite_genres:
            print("\nYou have no favorite genres to remove.")
            return

        genre = input("Enter a genre to remove: ").strip().title()

        if genre in self.favorite_genres:
            self.favorite_genres.remove(genre)
            self.save_favorites()
            print(f"{genre} removed from favorites.")
        else:
            print("Genre not found in favorites.")

    def view_favorites(self):
        """Displays the user's favorite genres."""
        if self.favorite_genres:
            print("\nYour favorite genres:", ", ".join(self.favorite_genres))
        else:
            print("\nYou have no favorite genres yet.")

    def view_songs(self):
        """Shows songs corresponding to the user's favorite genres."""
        if not self.favorite_genres:
            print("\nYou have no favorite genres yet. Add some to see song suggestions.")
            return

        print("\nHere are songs from your favorite genres:")
        for genre in self.favorite_genres:
            print(f"\n{genre}:")
            for song in self.songs.get(genre, []):
                print(f"- {song}")

    def suggest_random_song(self):
        """Suggests a random song from the user's favorite genres."""
        if not self.favorite_genres:
            print("\nYou have no favorite genres yet. Add some to get song suggestions!")
            return

        possible_songs = [song for genre in self.favorite_genres for song in self.songs.get(genre, [])]
        if possible_songs:
            print(f"\n🎵 You might like: {random.choice(possible_songs)} 🎵")
        else:
            print("\nNo songs available for your selected genres.")

    def save_favorites(self):
        """Saves the user's favorite genres to a file for persistence."""
        with open("favorites.json", "w") as file:
            json.dump(list(self.favorite_genres), file)

    def load_favorites(self):
        """Loads the user's favorite genres from a file if it exists."""
        try:
            with open("favorites.json", "r") as file:
                self.favorite_genres = set(json.load(file))
        except (FileNotFoundError, json.JSONDecodeError):
            self.favorite_genres = set()

    def run(self):
        """Runs the main program loop where the user interacts with the system."""
        self.greet_user()

        while True:
            print("\nOptions: \n1. Add Genre  \n2. Remove Genre  \n3. View Favorites  \n4. View Songs  \n5. Suggest a Song  \n6. Quit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_genre()
            elif choice == "2":
                self.remove_genre()
            elif choice == "3":
                self.view_favorites()
            elif choice == "4":
                self.view_songs()
            elif choice == "5":
                self.suggest_random_song()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

# Running the program
music_suggestor = MusicSuggestor()
music_suggestor.run()

