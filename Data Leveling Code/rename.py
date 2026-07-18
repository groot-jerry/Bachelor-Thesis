import os
import filecmp

def get_available_filename(folder_path, base_name, extension):
    """Find the next available filename if a conflict occurs."""
    count = 1
    new_name = f"{base_name}_{count:05d}{extension}"
    new_path = os.path.join(folder_path, new_name)
    
    while os.path.exists(new_path):
        count += 1
        new_name = f"{base_name}_{count:05d}{extension}"
        new_path = os.path.join(folder_path, new_name)
    
    return new_path

def rename_images(folder_path, overwrite=False):
    images = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')])

    for index, image in enumerate(images, start=4653):
        new_name = f"image_{index:05d}.jpg"
        old_path = os.path.join(folder_path, image)
        new_path = os.path.join(folder_path, new_name)

        if os.path.exists(new_path):
            if overwrite and filecmp.cmp(old_path, new_path, shallow=False):
                os.remove(old_path)
                print(f'Skipped (identical): {image}')
                continue
            else:
                # Find an available filename
                new_path = get_available_filename(folder_path, "image", ".jpg")
        
        os.rename(old_path, new_path)
        print(f'Renamed: {image} -> {os.path.basename(new_path)}')

# Set your folder path here
folder_path = r"E:\Junaed_Jibon\RiceyLeafDisease Bangladesh\Augmented\Augmented Images\Bacterial Leaf Blight"  # Change this to your folder path
rename_images(folder_path, overwrite=True)
