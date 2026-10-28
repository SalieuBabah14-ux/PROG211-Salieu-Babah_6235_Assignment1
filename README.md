# PROG211-Salieu-Babah_6235_Assignment1
Crop Management System

import pypandoc

readme = """# CROP MANAGEMENT SYSTEM

1. Project Description
The Crop Management System is a simple Python application developed to help users record and manage information about crops. It can be used to keep track of crop records, planting details, growth status, and harvested quantities.

2. Main Features
- Add a new crop record.
- View registered crop records.
- Search for a crop using its ID.
- Update crop status and notes.
- Record harvested quantities.
- Delete a crop record after confirmation.
- Display a summary of crop records.
- Save and load records using JSON file storage.

3. Programming Concepts
The project uses Object-Oriented Programming (OOP), including classes and objects. It uses a Python dictionary to organise crop records by their unique crop IDs. The `json`, `pathlib`, and `datetime` modules may be used for data storage, file paths, and date handling.

4. Requirements
- Python 3.8 or later
- No additional third-party packages are required if the program uses only Python's standard library.

5. How to Run the Program
1. Place `Crop_Management_System.py` in a folder on your computer.
2. Open Command Prompt or a terminal in that folder.
3. Run this command:

   `python Crop_Management_System.py`

4. Follow the menu options shown by the program.

If your computer uses the `python3` command, run:

   `python3 Crop_Management_System.py`

6. Data Storage
The program may create a file named `crop_records.json` to save crop information. Keep this JSON file in the location expected by the program so saved records can be loaded again.

7. Suggested Testing
- Add a crop such as rice or cassava.
- View the crop list and confirm the new record appears.
- Search using the crop ID.
- Update the crop's growth status.
- Record a harvested quantity.
- Close and reopen the program to check whether saved data is loaded.
- Test deletion only with a record you are comfortable removing.

8. Limitations
This is a basic educational project. It may not include user accounts, a graphical interface, cloud backup, or advanced farm analytics. These features could be added in future versions.

9. Future Improvements
Possible improvements include user login, a graphical user interface, crop yield reports, reminders for planting and harvesting, and backup options.

10. Author
Student Name: SALIEU BABAH SESAY

Course: DIPLOMA IN INFORMATION COMMUNICATION TECHNOLOGY

Institution: LIMKOKWING UNIVERSITY OF CREATIVE TECHNOLOGY
Date: 28 OCTOBER, 2026
"""

output_path = "/mnt/data/Crop_Management_System_README.txt"
pypandoc.convert_text(readme, "plain", format="md", outputfile=output_path, extra_args=["--standalone"])
print(f"Created: {output_path}")
