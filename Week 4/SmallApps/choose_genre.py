def read_genres_from_file(file_path):
    with open("movies.txt", 'r') as file:
        return [line.strip() for line in file]

# Function to filter genres based on user input
def filter_genres(genres):
    print("Available genres:")
    for count, genre in enumerate(genres, start=1):
        print(f"{count}. {genre}")

    user_input = input("Enter the numbers of the genres you want to watch (comma-separated): ")
    selected_indices = [int(index) - 1 for index in user_input.split(",")]

    selected_genres = [genres[index] for index in selected_indices]
    return selected_genres

def main():
    genres_file_path = "movies.txt"
    genres = read_genres_from_file("movies.txt")

    selected_genres = filter_genres(genres)

    if selected_genres:
        print("\nSelected genres:")
        for genre in selected_genres:
            print(genre)
    else:
        print("No genres selected.")

if __name__ == "__main__":
    main()
