import os
import shutil

# Define input and output folders
input_folder = r"C:/Users/idont/Documents/New folder 3"
output_folder = r"C:/Users/idont/Documents/New folder 4"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each file in the input folder
for filename in sorted(os.listdir(input_folder)):
    if filename.endswith(".jpg"):#im using .jpg formats
        try:
            # Extract the numeric part from the filename
            number = int(os.path.splitext(filename)[0])  # Convert '1.jpg' to 1
            
            # Increment by a number, here i put 8
            new_number = number + 88
            new_filename = f"{new_number}.jpg"
            
            # Define source and destination paths
            src_path = os.path.join(input_folder, filename)
            dest_path = os.path.join(output_folder, new_filename)
            
            # Copy the file with the new name
            shutil.copy(src_path, dest_path)
            print(f"Renamed: {filename} → {new_filename}")

        except ValueError:
            print(f"Skipping {filename} (not a valid numbered filename)")
