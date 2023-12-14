import csv
from datasets import Dataset

csv_file_path = 'concentration.csv'

data_list = []

# Open the CSV file and read its contents
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data_list.append(row)

# Now data_list contains the data from the CSV file
# print(data_list) 
concen = []

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    Give me a course in {l['concentration']} concentration.[/INST] \
                    Sure! Here is a course in {l['concentration']} concentration: {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    What course should I take for a concentration in {l['concentration']}? [/INST] \
                    A suitable course for {l['concentration']} concentration is {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    Can you recommend a course in the field of {l['concentration']} concentration? [/INST] \
                    Yes, for {l['concentration']}, consider {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    I'm looking for a course in {l['concentration']}, any suggestions? [/INST] \
                    In {l['concentration']}, you migh find {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}, very helpful</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    Which course is good for studying {l['concentration']}? [/INST]\
                    A recommended course for {l['concentration']} is {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST\
                    I need a course {l['concentration']}, any advice? [/INST]\
                    For {l['concentration']}, consider {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    Suggest a course for the {l['concentration']} concentration. [/INST]\
                    A suitable course for {l['concentration']} is {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})
    

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    What course can I take in {l['concentration']}? [/INST]\
                    For {l['concentration']}, you might consider {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    Is there a course focused on {l['concentration']}? [/INST]\
                    Yes, in {l['concentration']}, {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']} would be an excellent choice</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    Can you give me a course option for {l['concentration']}? [/INST]\
                    For {l['concentration']}, consider {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    Can you suggest a course in {l['concentration']}? [/INST]\
                    In {l['concentration']}, consider taking {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    What is a good course for learning about {l['concentration']}? [/INST]\
                    For {l['concentration']}, {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}, is highly recommended</s>"})


for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    I am interested in {l['concentration']}, any course suggestions? [/INST]\
                    A great course for {l['concentration']} is {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    What courses are available in {l['concentration']}? [/INST]\
                    In {l['concentration']}, you may take {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    Is there a course related to {l['concentration']}? [/INST]\
                    Yes, for {l['concentration']}, you can take {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}</s>"})

for i in range(len(data_list)):
    l = data_list[i]
    concen.append({'text': f"<s>[INST]\
                    Recommend me a course in {l['concentration']}. [/INST]\
                    For {l['concentration']}, {l['Course Code']}{l['Course number']}, course name: {l['Course Name']}, Credit Hours: {l['Hours']}, would be a good fit. </s>"})

print(len(concen))
# print(concen[0])

########################################################################
import csv
from datasets import Dataset

input_file_path = '/Users/fightfei/Desktop/Northeastern/23Fall/INFO6105/project/selected_courses_combine_final.csv'

# Read the courses from the input CSV file
courses = []
with open(input_file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row)
        combination = []
        # Assuming each row contains a single string of courses
        combination.extend(row[0].split(','))  # Split the courses
        combination = [element.replace("[", "").replace("]", "").replace("'", "").strip() for element in combination]
        courses.append(combination)

courses.pop(0)
courses = [element for element in courses if len(element) == 8]

for i in range(100):
    concen.append({'text': f"<s>[INST]\
                    Give me a path to graduate. [/INST]\
                    One advice for your path to graduate is to take {courses[i][0]} and {courses[i][1]} in the first semester, {courses[i][2]} and {courses[i][3]} in the second, {courses[i][4]} and {courses[i][5]} in the third and take {courses[i][6]}, {courses[i][7]} in your last term. </s>"})

for i in range(100):
    concen.append({'text': f"<s>[INST]\
                    What's the recommended path to graduation? [/INST]\
                    A suggested path to graduation is to take {courses[i][0]} and {courses[i][1]} in the first semester, {courses[i][2]} and {courses[i][3]} in the second, {courses[i][4]} and {courses[i][5]} in the third, and complete your program with {courses[i][6]} and {courses[i][7]} in your final term. </s>"})

for i in range(100):
    concen.append({'text': f"<s>[INST]\
                    Can you provide a graduation plan? [/INST]\
                    To graduate efficiently, consider enrolling in {courses[i][0]} and {courses[i][1]} in the first semester, {courses[i][2]} and {courses[i][3]} in the second, {courses[i][4]} and {courses[i][5]} in the third, and finish strong with {courses[i][6]} and {courses[i][7]} in your last term.</s>"})

for i in range(100):
    concen.append({'text': f"<s>[INST]\
                    I need guidance on my path to graduation. [/INST]\
                    Here's a suggested path to graduation: Take {courses[i][0]} and {courses[i][1]} in your first semester, {courses[i][2]} and {courses[i][3]} in the second, {courses[i][4]} and {courses[i][5]} in the third, and complete your degree with {courses[i][6]} and {courses[i][7]} in your final term.</s>"})

for i in range(100):
    concen.append({'text': f"<s>[INST]\
                    Provide me with a graduation roadmap. [/INST]\
                    Consider this path to graduate: {courses[i][0]} and {courses[i][1]} in the first semester, {courses[i][2]} and {courses[i][3]} in the second, {courses[i][4]} and {courses[i][5]} in the third, and wrap up your studies with {courses[i][6]} and {courses[i][7]} in your last term.</s>"})

for i in range(100):
    concen.append({'text': f"<s>[INST]\
                    I'm looking for a plan to graduate on time.[/INST]\
                    To graduate on time, consider enrolling in {courses[i][0]} and {courses[i][1]} in the first semester, {courses[i][2]} and {courses[i][3]} in the second, {courses[i][4]} and {courses[i][5]} in the third, and completing your degree with {courses[i][6]} and {courses[i][7]} in your final term.</s>"})

for i in range(100):
    concen.append({'text': f"<s>[INST]\
                    What's the ideal graduation path?[/INST]\
                    An ideal graduation path includes taking {courses[i][0]} and {courses[i][1]} in the first semester, {courses[i][2]} and {courses[i][3]} in the second, {courses[i][4]} and {courses[i][5]} in the third, and concluding your program with {courses[i][6]} and {courses[i][7]} in your last term.</s>"})
    
for i in range(100):
    concen.append({'text': f"<s>[INST]\
                    I need a plan to ensure timely graduation.[/INST]\
                    To ensure timely graduation, plan to take {courses[i][0]} and {courses[i][1]} in the first semester, {courses[i][2]} and {courses[i][3]} in the second, {courses[i][4]} and {courses[i][5]} in the third, and finish with {courses[i][6]} and {courses[i][7]} in your final term.</s>"})

for i in range(100):
    concen.append({'text': f"<s>[INST]\
                    What's the recommended course sequence for graduation?[/INST]\
                    The recommended course sequence for graduation includes {courses[i][0]} and {courses[i][1]} in the first semester, {courses[i][2]} and {courses[i][3]} in the second, {courses[i][4]} and {courses[i][5]} in the third, and {courses[i][6]} and {courses[i][7]} in your last term.</s>"})

########################################################################
dataset = Dataset.from_list(concen)
print(dataset)

train_test_split_ratio = 0.99
split_dataset = dataset.train_test_split(test_size=1 - train_test_split_ratio)
print(split_dataset)

split_dataset.push_to_hub("INFO6105-llama2")