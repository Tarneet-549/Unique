import pandas as pd

import numpy as np

# Generate sample data for 50 users
np.random.seed(42)  # For reproducibility
num_users = 50
data = {
    'User_ID': np.arange(1, num_users + 1),
    'Score': np.random.randint(50, 100, size=num_users),
    'Time_Utilized': np.random.randint(10, 60, size=num_users),
    'Learning_Progress': np.random.randint(1, 5, size=num_users)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('user_game_data.csv', index=False)
print("CSV file 'user_game_data.csv' has been created successfully.")

