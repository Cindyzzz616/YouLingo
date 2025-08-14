import os
import json
import shutil
import matplotlib.pyplot as plt
import numpy as np

ENGLISH_FOLDER = "video_analysis/sampled_json_subset"
NO_SPEECH_FOLDER = "video_analysis/no_speech_json"
NON_ENGLISH_FOLDER = "video_analysis/non_english_json"
METADATA_JSON = "video_analysis/metadata_summary.json"

BLUE = "#76abb7"
YELLOW = "#ebc554"
RED = "#e1b0b5"
BEIGE = "#dddcd6"
DARK_GRAY = "#49423c"
GRAY = "#5d5d5d"
MID_GRAY = "#737373"
LIGHT_GRAY = "#b4b1b0"

def move_no_speech_videos(folder_path: str, no_speech_folder: str):
    """
    Process the JSON video data in a folder.
    """

    for filename in os.listdir(folder_path):

        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)  # data is now a Python dict/list, depending on file structure
                
            # Check if transcript.segments exists and is empty
            segments = data.get("transcript", {}).get("segments", [])
            if not segments:  # empty list
                print(f"Moving {filename} (empty segments)")
                shutil.move(file_path, os.path.join(no_speech_folder, filename))

            # Access your JSON information here
            # print(f"File: {filename}")
            # print(data)  # or data['key'] if you know the structure

def move_non_english_videos(folder_path: str, non_english_folder: str):
    """
    Process the JSON video data in a folder.
    """

    for filename in os.listdir(folder_path):

        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                language = data.get("language")
                if language != 'en':
                    print(f"Moving {filename}")
                    shutil.move(file_path, os.path.join(non_english_folder, filename))

def get_metadata(folder_path: str, destination_path: str):
    """
    Process the JSON video data in a folder.
    """

    metadata_dict = {
        "path": [],
        "audio_path": [],
        "length_sec": [],
        "vad_duration_sec": [],
        "total_segment_length_sec": [],
        "word_count": [],
        "mean_sentence_length_words": [],
        "wpm": [],
        "spm": [],
        "average_ptr": []
    }

    for filename in os.listdir(folder_path):

        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                keys = ["path", 
                        "audio_path", 
                        "length_sec", 
                        "vad_duration_sec",
                        "total_segment_length_sec",
                        "word_count",
                        "mean_sentence_length_words",
                        "wpm",
                        "spm",
                        "average_ptr"]
                for key in keys:
                    metadata_dict[key].append(data[key])
    
    # Save the metadata dictionary as a json file
    with open(f"{destination_path}/metadata_summary.json", "w", encoding="utf-8") as f:
        json.dump(metadata_dict, f, ensure_ascii=False, indent=4)

    return metadata_dict

def plot_speech_and_language(english_folder: str, no_speech_folder: str, non_english_folder: str):
    english_count = sum(1 for f in os.listdir(english_folder) if os.path.isfile(os.path.join(english_folder, f)))
    no_speech_count = sum(1 for f in os.listdir(no_speech_folder) if os.path.isfile(os.path.join(no_speech_folder, f)))
    other_count = 0

    languages = {}
    for filename in os.listdir(non_english_folder):

        if filename.endswith(".json"):
            file_path = os.path.join(non_english_folder, filename)
            
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data["language"] not in languages.keys():
                    languages[data["language"]] = 1
                else:
                    languages[data["language"]] += 1
                other_count += 1
    
    languages["English"] = english_count
    languages["No speech"] = no_speech_count
    languages["Other"] = other_count

    # Group the non-English videos together
    labels = ["English", "No speech", "Other"]
    counts = [english_count, no_speech_count, other_count]

    # Data
    # labels = list(languages.keys())
    # counts = list(languages.values())
    colors = [BEIGE, LIGHT_GRAY, MID_GRAY]
    #explode = (0, 0.1, 0, 0)  # "explode" the 2nd slice (Bananas)

    # Create pie chart
    plt.pie(
        counts, 
        # explode=explode, 
        labels=labels, 
        # labeldistance=3, 
        textprops={'fontsize': 10, 'weight': 'regular'},
        colors=colors, 
        autopct='%1.1f%%',   # Format percentages
        radius=1.5,
        # shadow=True, 
        # startangle=140       # Rotate so slices are in a nice order
    )

    plt.axis('equal')  # Equal aspect ratio for a perfect circle
    plt.title("Language distribution of videos")
    plt.show()


def analyze_metadata(metadata_json_path):
    with open(metadata_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    plt.style.use('seaborn-v0_8-whitegrid')  # or 'ggplot', 'fivethirtyeight'

    # Plot word count
    word_counts = data["word_count"]
    mean_val = np.mean(word_counts)
    median_val = np.median(word_counts)
    plt.hist(word_counts, bins=50, color=YELLOW, edgecolor='black')
    plt.axvline(mean_val, color=DARK_GRAY, linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.1f}')
    plt.axvline(median_val, color=LIGHT_GRAY, linestyle='dashed', linewidth=2, label=f'Median: {median_val:.1f}')
    plt.xlabel('Word count')
    plt.ylabel('Number of videos')
    plt.title('Distribution of word counts across videos')
    plt.legend()
    plt.show()

    # Plot duration (for English videos)
    durations = data["length_sec"]
    mean_val = np.mean(durations)
    median_val = np.median(durations)
    plt.hist(durations, bins=50, color=BEIGE, edgecolor='black')
    plt.axvline(mean_val, color=DARK_GRAY, linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.1f}')
    plt.axvline(median_val, color=LIGHT_GRAY, linestyle='dashed', linewidth=2, label=f'Median: {median_val:.1f}')
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Number of videos')
    plt.title('Distribution of durations across videos')
    plt.legend()
    plt.show()

    # Plot mean sentence length
    mean_sentence_length_words = data["mean_sentence_length_words"]
    mean_val = np.mean(mean_sentence_length_words)
    median_val = np.median(mean_sentence_length_words)
    plt.hist(mean_sentence_length_words, bins=50, color=RED, edgecolor='black')
    plt.axvline(mean_val, color=DARK_GRAY, linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.1f}')
    plt.axvline(median_val, color=LIGHT_GRAY, linestyle='dashed', linewidth=2, label=f'Median: {median_val:.1f}')
    plt.xlabel('Length (words)')
    plt.ylabel('Number of videos')
    plt.title('Distribution of mean sentence lengths across videos')
    plt.legend()
    plt.show()

    # Plot words per minute
    wpm = data["wpm"]
    mean_val = np.mean(wpm)
    median_val = np.median(wpm)
    plt.hist(wpm, bins=50, color=BLUE, edgecolor='black')
    plt.axvline(mean_val, color=DARK_GRAY, linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.1f}')
    plt.axvline(median_val, color=LIGHT_GRAY, linestyle='dashed', linewidth=2, label=f'Median: {median_val:.1f}')
    plt.xlabel('Words/minute')
    plt.ylabel('Number of videos')
    plt.title('Distribution of speech rates across videos (in words/minute)')
    plt.legend()
    plt.show()

    # Plot syllables per minute
    spm = data["spm"]
    mean_val = np.mean(spm)
    median_val = np.median(spm)
    plt.hist(spm, bins=50, color=BLUE, edgecolor='black')
    plt.axvline(mean_val, color=DARK_GRAY, linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.1f}')
    plt.axvline(median_val, color=LIGHT_GRAY, linestyle='dashed', linewidth=2, label=f'Median: {median_val:.1f}')
    plt.xlabel('Syllables/minute')
    plt.ylabel('Number of videos')
    plt.title('Distribution of speech rates across videos (in syllables/minute)')
    plt.legend()
    plt.show()

    # Plot articulation ratio
    average_ptr = data["average_ptr"]
    mean_val = np.mean(average_ptr)
    median_val = np.median(average_ptr)
    plt.hist(average_ptr, bins=50, color=BLUE, edgecolor='black')
    plt.axvline(mean_val, color=DARK_GRAY, linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.3f}')
    plt.axvline(median_val, color=LIGHT_GRAY, linestyle='dashed', linewidth=2, label=f'Median: {median_val:.3f}')
    plt.xlabel('Articulation ratio')
    plt.ylabel('Number of videos')
    plt.title('Distribution of articulation ratios across videos (from 0 to 1)')
    plt.legend()
    plt.show()

def plot_correlations(metadata_json_path):
    with open(metadata_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Data series
    word_counts = data["word_count"]
    durations = data["length_sec"]
    mean_sentence_length_words = data["mean_sentence_length_words"]
    wpm = data["wpm"]
    spm = data["spm"]
    average_ptr = data["average_ptr"]

    # Plot word count as a function of duration
    # NOTE positive correlation
    plt.figure(figsize=(8, 6))
    plt.scatter(durations, word_counts, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Word Count vs. Video Length', fontsize=14, fontweight='bold')
    plt.xlabel('Video Length (seconds)', fontsize=12)
    plt.ylabel('Word Count', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    # Plot mean sentence length as a function of duration
    plt.figure(figsize=(8, 6))
    plt.scatter(durations, mean_sentence_length_words, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Mean Sentence Length vs. Video Length', fontsize=14, fontweight='bold')
    plt.xlabel('Video Length (seconds)', fontsize=12)
    plt.ylabel('Mean Sentence Length', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    # Plot wpm as a function of duration
    plt.figure(figsize=(8, 6))
    plt.scatter(durations, wpm, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Speech rate (words/minute) vs. Video Length', fontsize=14, fontweight='bold')
    plt.xlabel('Video Length (seconds)', fontsize=12)
    plt.ylabel('Speech rate (words/minute)', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    # Plot wpm as a function of duration
    plt.figure(figsize=(8, 6))
    plt.scatter(durations, spm, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Speech rate (syllables/minute) vs. Video Length', fontsize=14, fontweight='bold')
    plt.xlabel('Video Length (seconds)', fontsize=12)
    plt.ylabel('Speech rate (syllables/minute)', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    # Plot articulation ratio as a function of duration
    plt.figure(figsize=(8, 6))
    plt.scatter(durations, average_ptr, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Articulation ratio vs. Video Length', fontsize=14, fontweight='bold')
    plt.xlabel('Video Length (seconds)', fontsize=12)
    plt.ylabel('Articulation ratio (0 to 1)', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    #####

    # Plot word count as a function of mean sentence length
    # NOTE positive correlation
    plt.figure(figsize=(8, 6))
    plt.scatter(mean_sentence_length_words, word_counts, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Word Count vs. Mean Sentence Length', fontsize=14, fontweight='bold')
    plt.xlabel('Mean Sentence Length (words)', fontsize=12)
    plt.ylabel('Word Count', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    # Plot wpm as a function of mean sentence length
    # NOTE positive correlation
    plt.figure(figsize=(8, 6))
    plt.scatter(mean_sentence_length_words, wpm, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Speech Rate (words/minute) vs. Mean Sentence Length', fontsize=14, fontweight='bold')
    plt.xlabel('Mean Sentence Length (words)', fontsize=12)
    plt.ylabel('Speech Rate (words/minute)', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    # Plot spm as a function of mean sentence length
    # NOTE positive correlation
    plt.figure(figsize=(8, 6))
    plt.scatter(mean_sentence_length_words, spm, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Speech Rate (syllables/minute) vs. Mean Sentence Length', fontsize=14, fontweight='bold')
    plt.xlabel('Mean Sentence Length (words)', fontsize=12)
    plt.ylabel('Speech Rate (spm)', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    # Plot articulation ratio as a function of mean sentence length
    plt.figure(figsize=(8, 6))
    plt.scatter(mean_sentence_length_words, average_ptr, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Articulation Ratio vs. Mean Sentence Length', fontsize=14, fontweight='bold')
    plt.xlabel('Mean Sentence Length (words)', fontsize=12)
    plt.ylabel('Articulation ratio (0 to 1)', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    #####

    # Plot word count as a function of wpm
    # NOTE positive correlation
    plt.figure(figsize=(8, 6))
    plt.scatter(wpm, word_counts, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Word Count vs. Speech Rate (words/minute)', fontsize=14, fontweight='bold')
    plt.xlabel('Speech Rate (words/minute)', fontsize=12)
    plt.ylabel('Word Count', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    # Plot spm as a function of wpm
    # NOTE positive correlation
    plt.figure(figsize=(8, 6))
    plt.scatter(wpm, spm, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Speech Rate (syllables/minute) vs. Speech Rate (words/minute)', fontsize=14, fontweight='bold')
    plt.xlabel('Speech Rate (words/minute)', fontsize=12)
    plt.ylabel('Speech Rate (syllables/minute)', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    # Plot articulation ratio as a function of wpm
    plt.figure(figsize=(8, 6))
    plt.scatter(wpm, average_ptr, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Articulation Ratio vs. Speech Rate (words/minute)', fontsize=14, fontweight='bold')
    plt.xlabel('Speech Rate (words/minute)', fontsize=12)
    plt.ylabel('Articulation Ratio', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    #####

    # Plot word count as a function of spm
    # NOTE positive correlation
    plt.figure(figsize=(8, 6))
    plt.scatter(spm, word_counts, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Word Count vs. Speech Rate (syllables/minute)', fontsize=14, fontweight='bold')
    plt.xlabel('Speech Rate (syllables/minute)', fontsize=12)
    plt.ylabel('Word Count', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    # Plot articulation rate as a function of spm
    plt.figure(figsize=(8, 6))
    plt.scatter(spm, average_ptr, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Articulation Rate vs. Speech Rate (syllables/minute)', fontsize=14, fontweight='bold')
    plt.xlabel('Speech Rate (syllables/minute)', fontsize=12)
    plt.ylabel('Articulation Rate (0 to 1)', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    #####

    # Plot word count as a function of articulation rate
    # NOTE some weird correlation
    plt.figure(figsize=(8, 6))
    plt.scatter(average_ptr, word_counts, s=30, color=LIGHT_GRAY, alpha=0.7, edgecolor='black')
    plt.title('Word Count vs. Articulation Rate', fontsize=14, fontweight='bold')
    plt.xlabel('Articulation Rate (0 to 1)', fontsize=12)
    plt.ylabel('Word Count', fontsize=12)
    # Optional grid and style tweaks
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()


if __name__ == '__main__':
    # move_no_speech_videos("video_analysis/sampled_json_subset", "video_analysis/no_speech_json")
    # move_non_english_videos("video_analysis/sampled_json_subset", "video_analysis/non_english_json")
    # get_metadata("video_analysis/sampled_json_subset", "video_analysis")
    # plot_speech_and_language(ENGLISH_FOLDER, NO_SPEECH_FOLDER, NON_ENGLISH_FOLDER)
    # analyze_metadata(METADATA_JSON)
    plot_correlations(METADATA_JSON)