import json

# Load the data.json file with specified encoding
with open(r'D:\Django-projects\TTL_Logistic-django-master\data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create a dictionary to store unique combinations of app_label and model
content_types = {}

# Iterate through each entry in the data.json file
for entry in data:
    # Check if the entry has the 'app_label' key
    if 'app_label' in entry['fields']:
        # Extract app_label and model fields
        app_label = entry['fields']['app_label']
        model = entry['fields']['model']
        
        # Check if the combination of app_label and model already exists in the dictionary
        if (app_label, model) in content_types:
            print(f"Duplicate entry found: app_label='{app_label}', model='{model}'")
        else:
            # If not, add it to the dictionary
            content_types[(app_label, model)] = entry
    else:
        print("Error: 'app_label' key is missing in entry:", entry)

print("Duplicate check completed.")

# If duplicates are found, remove or modify them in the 'data' variable

# Save the modified data back to the data.json file
with open(r'D:\Django-projects\TTL_Logistic-django-master\data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print("Modified data saved back to data.json file.")
