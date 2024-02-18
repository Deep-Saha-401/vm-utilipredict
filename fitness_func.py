
def fitness_function(predicted_utilization, historical_utilizations):
    # Calculate the relative error between predicted and historical utilizations
    relative_error = abs(predicted_utilization - historical_utilizations.mean()) / historical_utilizations.mean()

    # Convert relative error to accuracy (lower relative error implies higher accuracy)
    accuracy = 1.0 - relative_error

    # Convert accuracy to percentage
    accuracy_percentage = accuracy * 100.0

    return accuracy_percentage
