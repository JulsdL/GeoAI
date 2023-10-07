# Number of lines you want in your smaller file
num_lines_to_keep = 100  # Adjust this number based on your needs

# Paths to your original and new split files
original_split_file = './data_splits/multi_temporal_crop_classification/training_data.txt'
smaller_split_file = './data_splits/multi_temporal_crop_classification/small_training_data.txt'

# Read the original file and get the first 'num_lines_to_keep' lines
with open(original_split_file, 'r') as f:
    lines = f.readlines()[:num_lines_to_keep]

# Write the smaller split file
with open(smaller_split_file, 'w') as f:
    f.writelines(lines)

print(
    f"Created smaller split file with {len(lines)} lines at {smaller_split_file}"
)
