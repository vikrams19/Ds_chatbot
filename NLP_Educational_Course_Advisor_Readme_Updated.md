
# NEU COURSE COMPANION 

***"Our mission is to simplify the course selection process for NEU students, enhancing their academic experience."***

Website Link : 
[NEU Course Companion](https://657a63672a791f3f6d5934ac--incomparable-nasturtium-750cfb.netlify.app/)

## Description
This project is designed to assist Northeastern University (NEU) students in streamlining the course selection process for their degree. The project involves fine-tuning the LLaMA 2.7B language model for chatbot applications using the Hugging Face Transformers library. The trained model is then stored on the Hugging Face Model Hub for easy access and sharing. Additionally, the chatbot project includes the generation of prompts for course recommendations and graduation plans, providing a comprehensive tool for students to navigate their academic journey.

## Components
- `advice.py`: Trains and fine-tunes the "NousResearch/Llama-2-7b-chat-hf" model on the "fightfei/INFO6105-llama2" dataset.
- `con_dataset.py`: Processes 'concentration.csv' to create a dataset for the NLP model.
- `integration_trial7a.html`: Frontend interface for interacting with the trained chatbot.

## Usage
1. Prepare the dataset with `con_dataset.py`.
2. Train the model using `advice.py`.
3. Launch `integration_trial7.html` in a web browser to use the chatbot.

## Dependancy Configuration
```
accelerate==0.21.0
peft==0.4.0
bitsandbytes==0.40.2
transformers==0.4.7
datasets==1.14.0
torch==1.10.0
```

## Collecting the Data
The data is manually collected from the NEU official website: [NEU Course Descriptions](https://catalog.northeastern.edu/course-descriptions/info/)

### CSV File Creation
Create a CSV file with the following fields:
- Course Code
- Course Number
- Course Name
- Hours

### Alternative Data Collection using APIs
Refer to the [SerachNEU API list](https://jennydaman.gitlab.io/nubanned/dark.html#studentregistrationssb-search-get).

#### Using Search Courses API:
```
GET https://nubanner.neu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_subject=CS&txt_courseNumber=2500&txt_term=201930&startDatepicker=&endDatepicker=&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc
```
Note: The response “data” key is coming as “null”. Hence, it was not integrated into this project.

## Data Generation script ( Combination_genration.ipynb )
```python
import pandas as pd
from itertools import combinations

# Read the existing CSV into a DataFrame
df = pd.read_csv('Data_science_proj.csv')  # Replace 'Data_science_proj.csv' with the actual name of your CSV file

# Function to handle '1/8 Hours' and '1/4 Hours' cases
def handle_hours(hours_str):
    if '1/8' in str(hours_str):
        return [float(i) for i in range(1, 9)]
    elif '1/4' in str(hours_str):
        return [float(i) for i in range(1, 5)]
    else:
        return [float(hours_str)]

# Explode the DataFrame based on the lists in the 'Hours' column
df_exploded = df.copy()
df_exploded['Hours'] = df_exploded['Hours'].apply(handle_hours)
df_exploded = df_exploded.explode('Hours')

# Define the target total hours
target_total_hours = 32

# Identify the mandatory course
mandatory_course = "INFO 5100"

# Filter out the mandatory course
mandatory_course_data = df_exploded[df_exploded['Course Code'] + " " + df_exploded['Course number'].astype(str) == mandatory_course]

# Remove the mandatory course from the DataFrame
df_exploded = df_exploded[df_exploded['Course Code'] + " " + df_exploded['Course number'].astype(str) != mandatory_course]

# Initialize variables
selected_courses_list = []

# Generate combinations for the remaining courses
remaining_combinations = combinations(df_exploded.iterrows(), 7)  # Adjust the number in the combination as needed

# Iterate through combinations and select courses until the total hours reach the target
for combination in remaining_combinations:
    total_hours = mandatory_course_data['Hours'].sum()
    selected_courses = [mandatory_course]

    for index, course in combination:
        selected_courses.append(course['Course Code'] + " " + str(course['Course number']))
        total_hours += course['Hours']

        if total_hours >= target_total_hours:
            break

    if total_hours == target_total_hours:
        # Append the selected courses to the list
        selected_courses_list.append(selected_courses)
```
### Usage
- Prepare your course data in a CSV format. The CSV should have columns for course code, course number, and hours.
- Replace 'Data_science_proj.csv' in the script with the actual name of your CSV file.
- Set the target_total_hours variable to the total number of hours you need to achieve.
- Identify the mandatory course by setting the mandatory_course variable. It should be in the format "CourseCode CourseNumber".
- Run the script. It will read your CSV, process the data, and output a list of course combinations that meet the target hours.
- The script handles courses with variable hours (e.g., '1/8 Hours', '1/4 Hours') by generating all possible hour values for such courses.

### Notes
- The script assumes that the data in the CSV file is well-structured and clean.
- The script currently supports only one mandatory course. If you have multiple mandatory courses, modifications to the script will be needed.
- The number of courses to be combined is set to 7 by default in the combinations() function. Adjust this number based on your specific requirements.

### Troubleshooting
- If you encounter errors related to file not found, ensure the CSV file name and path are correct.
- If the script does not return any combinations, check if the target_total_hours is reasonable considering the courses' hours.
- For any other errors, check the Python error message for hints on what might be wrong.

### Conclusion
This script is a handy tool for academic planning, allowing users to efficiently find course combinations that meet specific hourly requirements. It automates what can be a time-consuming and error-prone process, especially when dealing with a large number of courses and complex schedules.
## Next Steps
Use the above script to create possible course combinations and train the Llama2 model.

## Next Step: Prepare the dataset
Use the above script to create possible course combinations and train the Llama2 model.
As Llama2 model format is different when compared to the course combination file generated, use con_dataset.py to generate the code to train the dataset.

## Training and Finetuning the model
Use advice.py to train and finetune the model.

## Integrate the model with frontend.
