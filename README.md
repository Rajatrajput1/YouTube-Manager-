# YouTube-Manager-
YouTube Manager  Project using Python
### Project Description: YouTube Video Manager

The YouTube Video Manager is a command-line application designed to help users manage a list of YouTube videos, allowing them to perform basic CRUD (Create, Read, Update, Delete) operations. The project is implemented in Python and leverages the `json` module to handle data storage and retrieval in a JSON file, making it simple to save and load video information.

 ### Libraries Used:
- **json**: The `json` module is utilized to encode and decode data in JSON format, allowing the program to store video information in a structured text file (`youtube.txt`). This provides a persistent storage solution for the list of videos managed by the application.

 ### How the Project Works:

1. **Loading Data**:
   - The application begins by attempting to load existing video data from `youtube.txt`. This is achieved using the `load_data()` function, which reads and parses the JSON data. If the file is not found or the JSON is malformed, the 
      program handles these exceptions gracefully by returning an empty list or displaying an appropriate error message.

2. **Listing Videos**:
   - The `list_all_videos()` function allows users to view all the videos currently stored in the system. The function iterates over the list of videos, displaying the name and duration of each one in a numbered format.

3. **Adding a Video**:
   - Users can add new videos to the list using the `add_a_video()` function. The function prompts the user for the video name and time, then appends this information as a dictionary to the list. The updated list is then saved to the file using the `save_data_helper()` function.

4. **Updating a Video**:
   - The `update_a_video()` function enables users to modify the details of an existing video. The user is prompted to select the video by its index number, and then input the new name and time. The video information is updated in the list, and the changes are saved to the file.

5. **Deleting a Video**:
   - To remove a video, the `delete_a_video()` function is used. The user selects the video by its index number, and the function deletes the video from the list. The updated list is then saved back to the file.

6. **Program Flow**:
   - The main control loop of the application is handled by the `main()` function, which continuously prompts the user to choose an action (list, add, update, delete, or exit). Based on the user's input, the corresponding function is called. The loop continues until the user decides to exit the application.

#### Conclusion:
This YouTube Video Manager project is a straightforward yet effective way to manage a list of videos. It demonstrates fundamental programming concepts such as file handling, exception handling, and list manipulation in Python. The project is well-structured, with clear separation of concerns between different functionalities, making it easy to understand, maintain, and extend.
