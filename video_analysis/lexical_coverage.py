# NOTE don't forget to return two measures of coverage: raw coverage and coverage with inference
# NOTE don't forget that we didn't use implement word families in this code, only surface forms of words
# NOTE we need a better function to estimate inference percentage

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pickle

from User import User
from Video import Video

L = 82.42
k = 0.59
x0 = 89.10

# Reading the word family frequency database
with open("video_analysis/external_data/word_families.pkl", "rb") as f:
    WORD_FAMILIES = pickle.load(f)

def logistic(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

def lexical_coverage(video: Video, user: User) -> tuple:
    """
    Calculate lexical coverage of a transcript against a user's lexicon of word families.
    Use types, not tokens.
    """
    overlapping_families = {}
    non_overlapping = []
    words_in_transcript = video.types
    # TODO what if a two types in a video belong to the same family?
    for word_obj in words_in_transcript:
        word = word_obj.text
        for head in user.family_lexicon.keys():
            for w, f in user.family_lexicon[head]:
                if w.lower() == word.lower():
                    overlapping_families[head] = user.family_lexicon[head]
                else:
                    non_overlapping.append(word)
    non_overlapping = set(non_overlapping)
    print(overlapping_families, "\n")
    print(non_overlapping)
    raw_coverage = len(overlapping_families)/len(video.types)

    # # Old coverage calculation based on surface form of words
    # # Raw coverage
    # raw_coverage = len(words_in_transcript.intersection(user_lexicon)) / len(words_in_transcript) if words_in_transcript else 0.0
    # print(len(words_in_transcript), len(user_lexicon))
    # # print(words_in_transcript.intersection(user_lexicon))
    # print(len(words_in_transcript.intersection(user_lexicon)))

    # Coverage with inference (assuming some words can be inferred)
    inference_percentage = logistic(raw_coverage * 100, L, k, x0) / 100
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