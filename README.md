PROG211_Salieu Babah Sesay_6235_Assignment1
CROP MANAGEMENT SYSTEM
README File

1. Project Description
The Crop Management System is a Python-based application designed to help farmers record and manage crop information. The system can be used to register crops, view crop records, update crop growth status, record harvested quantities, and organise farm information.
The project uses Object-Oriented Programming (OOP) concepts, such as classes and objects. A Python dictionary is used to organise crop records by their unique crop IDs, making it easier to search for and manage records.

2. Problem the Project Solves
Farmers may find it difficult to keep accurate records of their crops when they depend only on notebooks or memory. Records can be lost, damaged, or difficult to update.

The Crop Management System provides a simple digital method of keeping crop records. It can help users organise planting information, monitor crop progress, and record harvest results.

3. Main Features
	Register new crops.
	View all registered crops.
	Search for crops using their IDs.
	Update crop information and growth status.
	Record harvested quantities.
	Delete crop records when necessary.
	Display a summary of crop information.
	Save and retrieve records using file storage.

4. Technologies Used
	Programming language: Python
	Programming approach:  Object-Oriented Programming
	Data structure: Dictionary
	Data storage: JSON file
	Standard libraries: Modules such as `json`, `pathlib`, and `datetime`, where used in the implementation.

5. Alignment with the Digital Public Goods Standard
The Digital Public Goods Standard provides criteria for identifying digital solutions that can contribute to sustainable development and public benefit. The Crop Management System supports several principles associated with the standard.

5.1 Open Source
The project can be shared with other students, developers, and agricultural organisations. If it is released under an appropriate recognised open-source licence, others can inspect, reuse, and improve the code.

Current status: The source code is available as a project file, but it is not automatically open-source until it is released under an appropriate licence.
5.2 Public Benefit
The system addresses a practical agricultural need by helping farmers organise crop records. Better record-keeping may help farmers monitor planting activities and harvest results.
5.3 Accessibility and Inclusion
The program uses a simple menu-based interface that may be suitable for users with basic computer skills. Future improvements could include local languages, mobile access, and interfaces designed for users with different abilities.
5.4 Privacy and Data Protection
The system should collect only information necessary for crop management. If personal details, farm locations, or farmers' contact information are added, those details should be protected against unauthorised access.
5.5 Security
Crop records should be protected against accidental loss and unauthorised changes. Future versions could introduce user authentication, access controls, and secure backups.
5.6 Reusability and Adaptability
The system can be adapted for different crops, farms, and agricultural settings. Other developers could extend it with features such as planting calendars, fertiliser records, pest monitoring, and yield reports.
5.7 Documentation and Transparency
This README explains the project's purpose, technologies, features, and possible improvements. Clear documentation makes the system easier for other people to understand, operate, and maintain.
5.8 Sustainability
Python is a widely used programming language, and the project can be maintained and improved by people with basic programming knowledge. Future development should consider long-term maintenance, backups, and compatibility with users' devices.

6. Limitations in Meeting the Standard
Although the project supports several Digital Public Goods principles, it should not be described as a formally recognised Digital Public Good at this stage.
Formal alignment would require a more complete assessment against the official Digital Public Goods Standard. This could include verifying the open-source licence, documenting privacy and security practices, reviewing applicable laws, and assessing the project's development and maintenance arrangements.

7. How the Project Could Be Improved
The following improvements could strengthen its alignment with the standard:
1. Publish the source code under an appropriate open-source licence.
2. Provide clear installation and user instructions.
3. Add data validation and secure backup procedures.
4. Protect any personal or confidential information.
5. Test the system with farmers and other intended users.
6. Improve accessibility and consider local-language support.
7. Document future changes and maintenance responsibilities.

8. How to Run the Program
1. Install Python on your computer.
2. Save `Crop_Management_System.py` in a folder.
3. Open Command Prompt or a terminal in that folder.
4. Run: `python Crop_Management_System.py`

5. Follow the menu instructions displayed by the program.
The exact command and data-file location should match the submitted Python implementation.

9. Example Usage (Sample Input/Output)
This section demonstrates an example of how the Crop Management System may be used to register a crop, view its details, and record a harvest.

Example 1: Adding a New Crop

Sample input:
```text
Enter your choice: 1
Crop ID: C001
Crop Name: Rice
Farm Location: Waterloo
Planting Date: 2026-06-10
Quantity Planted: 5 bags of seeds
```

Sample output:

```text
Crop registered successfully!
Crop ID: C001
Crop Name: Rice
Farm Location: Waterloo
Planting Date: 2026-06-10
Quantity Planted: 5 bags of seeds
Status: Planted
```

Example 2: Viewing Crop Records**
Sample input:
```text
Enter your choice: 2
```

Sample output:
```text
CROP RECORDS

Crop ID: C001
Crop Name: Rice
Farm Location: Waterloo
Planting Date: 2026-06-10
Status: Planted
Example 3: Updating Crop Status

Sample input:
```text
Enter your choice: 3
Enter Crop ID: C001
New Status: Growing

Sample output:
```text
Crop status updated successfully!

Crop ID: C001
Crop Name: Rice
Status: Growing
```

Example 4: Recording Harvest Information

Sample input:
```text
Enter your choice: 4
Enter Crop ID: C001
Harvested Quantity: 20 bags
```

Sample output:

```text
Harvest information recorded successfully!

Crop ID: C001
Crop Name: Rice
Harvested Quantity: 20 bags
```
Note: These examples illustrate the expected interaction and are illustrative rather than verified output from the actual program. Menu numbers, field names, and messages should be adjusted to match the submitted Python code.

11. Expected Result
The Crop Management System should help users organise crop information, monitor crop growth, and maintain harvest records. If JSON storage is implemented, saved records should remain available when the program is reopened.
These examples show how a simple Python application can help improve agricultural record-keeping.

10. Conclusion
The Crop Management System is a small digital solution intended to improve agricultural record-keeping. It supports public-benefit, accessibility, reusability, documentation, and sustainability principles. However, these qualities alone do not establish formal compliance with the Digital Public Goods Standard. Further development, appropriate licensing, testing, and assessment would be needed before making that claim.

### 11. Reference
Digital Public Goods Alliance. (n.d.). *Digital Public Goods Standard*. https://standard.digitalpublicgoods.net/
Python Software Foundation. (n.d.). *Python documentation*. https://docs.python.org/3/
