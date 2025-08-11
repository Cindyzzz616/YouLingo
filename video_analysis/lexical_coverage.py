# NOTE don't forget to return two measures of coverage: raw coverage and coverage with inference
# NOTE don't forget that we didn't use implement word families in this code, only surface forms of words
# NOTE we need a better function to estimate inference percentage

from User import User
from Video import Video

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

L = 82.42
k = 0.59
x0 = 89.10

def logistic(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

def lexical_coverage(video: Video, user: User) -> tuple:
    """
    Calculate lexical coverage of a transcript against a user's lexicon.
    Use types, not tokens.
    
    :param transcript: A dictionary containing the transcript text.
    :param user: An instance of User containing the user's lexicon.
    :return: A tuple containing raw coverage and coverage with inference.
    """
    words_in_transcript = video.types
    user_lexicon = set(user.lexicon) # NOTE shouldn't need to use set because the users's lexicon contains unique words only.
    
    # Raw coverage
    raw_coverage = len(words_in_transcript.intersection(user_lexicon)) / len(words_in_transcript) if words_in_transcript else 0.0
    print(len(words_in_transcript), len(user_lexicon))
    # NOTE double check if we should calculate the lexical coverage with tokens or types
    # print(words_in_transcript.intersection(user_lexicon))
    print(len(words_in_transcript.intersection(user_lexicon)))

    # Coverage with inference (assuming some words can be inferred)
    inference_percentage = logistic(raw_coverage * 100, L, k, x0) / 100
    print(inference_percentage)
    inferred_coverage = raw_coverage + (1 - raw_coverage) * inference_percentage

    return raw_coverage, inferred_coverage

if __name__ == "__main__":
    ### Approximation of inferencing percentage as a function of lexical coverage ###

    # Data
    coverage = np.array([90, 95, 98])
    inferencing = np.array([52, 80, 82])

    # Initial guesses: L = max %, k = steepness, x0 = midpoint
    initial_guess = [100, 1, 95]

    # Fit the model
    params, _ = curve_fit(logistic, coverage, inferencing, p0=initial_guess)
    L, k, x0 = params
    print(f"Fitted parameters: L={L:.2f}, k={k:.2f}, x0={x0:.2f}")

    # Generate x values for smooth curve
    x_vals = np.linspace(0, 100, 300)
    y_vals = logistic(x_vals, *params)

    # Plot
    plt.scatter(coverage, inferencing, label="Data", color="blue")
    plt.plot(x_vals, y_vals, label="Logistic Fit", color="red")
    plt.title("Inferencing as a Function of Coverage Level")
    plt.xlabel("Coverage Level (%)")
    plt.ylabel("Inferencing (%)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()