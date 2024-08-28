import json

def load_data():
    try:
        with open("youtube.txt", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
        return []

def save_data_helper(videos):
    try:
        with open("youtube.txt", 'w') as file:
            json.dump(videos, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def list_all_videos(videos):
    if not videos:
        print("No videos available.")
        return
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']} | Time: {video['time']}\n")
        
def add_a_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_a_video(videos):
    index = int(input("Enter the index of the video to update: ")) - 1
    if 0 <= index < len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index.")

def delete_a_video(videos):
    index = int(input("Enter the index of the video to delete: ")) - 1
    if 0 <= index < len(videos):
        videos.pop(index)
        save_data_helper(videos)
    else:
        print("Invalid index.")

def main():
    videos = load_data()
    while True:
        print("YouTube Manager  |  Choose an Option")
        print("1. List all videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit app")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_videos(videos)
        elif choice == "2":
            add_a_video(videos)
        elif choice == "3":
            update_a_video(videos)
        elif choice == "4":
            delete_a_video(videos)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
    

