import pandas as pd
import glob

# List of CSV files
csv_files = ["image_dataBLB.csv", "image_dataBS.csv", "image_dataHRL.csv", "image_dataLB.csv", "image_dataLS.csv", "image_dataNBLS.csv", "image_dataRH.csv", "image_dataSB.csv"]

# Initialize an empty dictionary to store data
image_data = {}

# Process each file
for idx, file in enumerate(csv_files):
    df = pd.read_csv(file)  # Read CSV
    class_column = f"class_{idx+1}"  # Generate class column name

    for image_id in df['Image_Id']:  
        if image_id not in image_data:
            image_data[image_id] = [0] * 8  # Initialize all class columns to 0
        image_data[image_id][idx] = 1  # Set 1 for matching class

# Convert dictionary to DataFrame
merged_df = pd.DataFrame.from_dict(image_data, orient="index", columns=[f"class_{i+1}" for i in range(8)])
merged_df.reset_index(inplace=True)
merged_df.rename(columns={"index": "Image_Id"}, inplace=True)

# Save final CSV
merged_df.to_csv("merged_output.csv", index=False)

print("Merged CSV saved as 'merged_output.csv'")