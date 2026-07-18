import os
import csv

def generate_csv_from_images(image_folder, output_csv):
    # Get all image files from the folder
    image_extensions = {'.jpg'}  # Only process .jpg files
    image_files = [f for f in os.listdir(image_folder) if os.path.splitext(f)[1].lower() in image_extensions]
    
    # Extract Image IDs (filenames without extensions)
    image_ids = [os.path.splitext(f)[0] for f in image_files]
    
    # Write to CSV
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image_Id', 'BLB'])  # Header
        for image_id in image_ids:
            writer.writerow([image_id, 1])
    
    print(f"CSV file '{output_csv}' has been created successfully with {len(image_ids)} image IDs.")

# Example Usage
image_folder = r"E:\Junaed_Jibon\RiceyLeafDisease Bangladesh\Augmented\Augmented Images\Bacterial Leaf Blight" # Change this to your image folder path
output_csv = 'image_dataBLB.csv'  # Output CSV filename
generate_csv_from_images(image_folder, output_csv)
