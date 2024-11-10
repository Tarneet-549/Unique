import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Expanded sample data for demonstration
sample_game_data = np.array([
    [10, 20, 30],  # Maths Quiz
    [15, 25, 35],  # Memory Game
    [10, 30, 40],  # Word Scramble
    [5, 15, 25],  # Number Sorting Game
    [20, 30, 50],  # Logic Puzzle
    [12, 22, 32],  # Relaxation Exercise
    [18, 28, 38],  # Typing Challenge
    [14, 21, 29],  # Additional Data
    [16, 26, 37],  # Additional Data
    [13, 31, 41]  # Additional Data
])

# Labels for best game (1 = best, 0 = not best)
sample_labels = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1, 1])

# Sample labels for time utilized prediction (in minutes)
time_utilized_labels = np.array([30, 45, 40, 25, 55, 35, 50, 40, 52, 36])

# Sample labels for learning effectiveness (1 = learning, 0 = not learning)
learning_labels = np.array([1, 1, 0, 0, 1, 1, 1, 0, 1, 0])

# Game names for reference
game_names = [
    "Maths Quiz",
    "Memory Game",
    "Word Scramble",
    "Number Sorting Game",
    "Logic Puzzle",
    "Relaxation Exercise",
    "Typing Challenge"
]


class PerformanceModel:
    def __init__(self):
        # Create pipelines with scaler and decision tree classifiers
        self.model = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', DecisionTreeClassifier())
        ])
        self.time_model = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', DecisionTreeClassifier())
        ])
        self.learning_model = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', DecisionTreeClassifier())
        ])

    def train_model(self, game_data, labels, time_labels, learning_labels):
        # Fit the models with the provided game data and labels
        self.model.fit(game_data, labels)
        self.time_model.fit(game_data, time_labels)
        self.learning_model.fit(game_data, learning_labels)
        print("Model training complete.")

    def predict_best_game(self, data):
        # Use the trained model to predict the best game
        predictions = self.model.predict(data)
        return predictions

    def predict_time_utilized(self, data):
        # Use the trained time model to predict the time utilized
        predictions = self.time_model.predict(data)
        return predictions

    def predict_learning_effectiveness(self, data):
        # Use the trained learning model to predict if the user is learning
        predictions = self.learning_model.predict(data)
        return predictions

    def track_performance(self, game_data):
        # Predict the best game
        best_game_indices = self.predict_best_game(game_data)
        results = []
        for i in range(len(game_data)):
            best_game_index = best_game_indices[i]  # Index of the best game for the current user
            best_game_name = game_names[best_game_index] if best_game_index == 1 else "Maths Quiz"

            # Predict time utilized
            time_utilized = self.predict_time_utilized(game_data)[i]  # Time utilized for the current user

            # Predict learning effectiveness
            learning_effectiveness = "Yes" if self.predict_learning_effectiveness(game_data)[i] == 1 else "No"

            result = {
                "Best Game": best_game_name,
                "Time Utilized (minutes)": time_utilized,
                "Learning Effectiveness": learning_effectiveness
            }
            results.append(result)

        return results

    def plot_performance(self, results):
        users = [f"User {i + 1}" for i in range(len(results))]
        best_games = [result['Best Game'] for result in results]
        time_utilized = [result['Time Utilized (minutes)'] for result in results]
        learning_effectiveness = [result['Learning Effectiveness'] for result in results]

        # Plotting the Best Game
        plt.figure(figsize=(18, 5))

        plt.subplot(1, 3, 1)
        plt.bar(users, best_games, color='skyblue')
        plt.xlabel('Users')
        plt.ylabel('Best Game')
        plt.title('Predicted Best Game')

        # Plotting Time Utilized
        plt.subplot(1, 3, 2)
        plt.bar(users, time_utilized, color='salmon')
        plt.xlabel('Users')
        plt.ylabel('Time Utilized (minutes)')
        plt.title('Time Utilized')

        # Plotting Learning Effectiveness
        plt.subplot(1, 3, 3)
        plt.bar(users, [1 if le == 'Yes' else 0 for le in learning_effectiveness], color='lightgreen')
        plt.xlabel('Users')
        plt.ylabel('Learning Effectiveness')
        plt.title('Learning Effectiveness')
        plt.yticks([0, 1], ['No', 'Yes'])

        plt.tight_layout()
        plt.show()


# Initialize the model
performance_model = PerformanceModel()

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(sample_game_data, sample_labels, test_size=0.3, random_state=42)
_, _, time_train, time_test = train_test_split(sample_game_data, time_utilized_labels, test_size=0.3, random_state=42)
_, _, learn_train, learn_test = train_test_split(sample_game_data, learning_labels, test_size=0.3, random_state=42)

# Train the model
performance_model.train_model(X_train, y_train, time_train, learn_train)

# Test the model with all sample data for diverse results
results = performance_model.track_performance(sample_game_data)

# Plot the performance results
performance_model.plot_performance(results[:5])  # Display results for the first 6 users
