# Cathoven levels key
final_levels:
- general
- vocab
- tense
- clause

The integer part of the float can be converted to CEFR level as following:
• 0 -> A1
• 1 -> A2
• 2 -> B1
• 3 -> B2
• 4 -> C1
• 5 -> C2

TODO
- deal with cases where there's no available transcript or translation
- rank videos based on matching score
- *levelling up when video is watched x times*

# Background to include
- language acquisition theory - 5 hypotheses
  - how does our app put this in practice? how did we figure out the grammar/theory part so the user doesn't have to?
- the apis we used
    - youtube
    - transcript
    - cathoven
- how we're incrementing the difficulty using analysis from cathoven

# YouLingo: YouTube Language Acquisition

This project is made for U of T Hacks 12 Hackathon.

YouLingo is a web application designed to help users learn new languages by making YouTube videos into language lessons. Users can explore various videos, add their own video URLs, and manage their favorite videos.

## Background
### Hypotheses of Language Acquisition
This application is based on the language acquisition theory posited by Stephen Krashen, an renowned American linguist who has written more than 500 articles and books on the second language acquisition and related fields. [1]
In his theory, he outlined six hypotheses about how to effectively gain fluency in a second language. They are:  
1. **The Acquisition-Learning hypothesis:** learning a language involves consciously obtaining knowledge _about_ a language, while the
process of acquisition is unconscious and involves direct interaction _with_ a language. The former approach is used in formal
language education, which often yields unsatisfactory results. In comparison, the latter approach is the process through which
children come to master their native language.
2. **The Monitor hypothesis:** when we are consciously learning a language, there is an internal monitor that judges and corrects the every
utterance. As a result, fluency is sacrificed to maximize accuracy, which hinders the progress of the learner in the long run.
3. **The Natural Order hypothesis:** children first acquire the comprehension capacities, then production capacities; they also master languages
in spoken forms before learning the written forms. Therefore, the natural order of language acquisition is _listening_, _speaking_, _reading_,
then _writing_. There are also orders of acquiring different grammatical structures. When adults follow the same order, they are able to
communicate more fluently and effectively.
4. **The Input hypothesis:** language input can only be helpful to a learner when they are comprehensible. When they wish to progress,
they must take small steps by consuming content that encompass the previous material with small additions. This can be described by the
analogy "i+1", where i represents the current knowledge and 1 represents the small addition on that basis.
5. **The Affective Filter hypothesis:** when learners are in stressful surroundings, their brains filter out the input
and render it useless. Their interest in the content they consume can also affect how well they internalize the language. 
Therefore, it is important for them to be in a relaxed environment where they can engage with the materials of their choosing and make mistakes.
6. **The Reading Hypothesis:** our vocabulary expands when we read materials from real-life contexts, rather than engage in rote
memorization of vocabulary lists. [2]
These hypotheses have proven to be effective from their significant transformation of language instruction and successful results.

### Our Implementation
YouLingo instantiates these hypotheses in concrete and innovative ways:
1. It does not explicitly instruct users to learn and memorize grammar rules, conjugations and vocabulary lists. Instead, it provides
users with natural input sourced from the wealth of videos on YouTube, which are created by real individuals in real-life contexts.
This is similar to how a child picks up their native language from listening to conversations in their surroundings.
2. When a user is focused on the content of their favourite videos, they are subconsciously taking in their target language without
pressure to perform in a grammatically impeccable manner.
3. Our application focuses on the first stage of the language acquisition process, since that is the key stage that is often skipped
or skimmed through. When users are ready, it also provides the potential for them to practice other aspects of the language - for
example, they can read the transcripts and hone their production abilities with the quizzes the app generates. Overall, they
are grounded in the practice of content consumption to ensure sufficient input.
4. This hypothesis is implemented by the flagship feature of our application.
5. Similar to the second hypothesis, this principle emphasizes the importance of a good environment and emotional state in efficacy
of acquisition. Our application provides content tailored to the user's preferences and expertise, so they can feel at ease with
the subject of the materials.
6. While our application does not focus on reading, the principles from the sixth hypothesis can be generalized to listening materials.
As mentioned

### Why CEFR?


### Sources  
[1] https://rossier.usc.edu/faculty-research/directory/stephen-krashen  
[2] https://sites.ualberta.ca/~obilash/krashen.html#:~:text=Application%20for%20Teaching-,The%20Acquisition%2DLearning%20hypothesis,of%20just%20'learning'%20it.


## Libraries Used

- React
- React Router
- Reactstrap
- Auth0 React
- Bootstrap
- React Icons

## APIs Used
- CEFR Statistics API by Cathoven
  - https://enterpriseapi.cathoven.com/cefr
- YouTube Transcript API by jedpoix
  - https://github.com/jdepoix/youtube-transcript-api
- YouTube Data API v.3 by Google
  - https://www.googleapis.com/youtube/v3

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Node.js
- npm (Node Package Manager)
- Python
- pip (Python Package Installer)

### Installation

1. Clone the repository:

```sh
git clone https://github.com/your-username/YouLingo.git
cd YouLingo/you-jujube
```

2. Install the dependencies for the frontend:

```sh
npm install
```

3. Install the dependencies for the backend:

```sh
cd ../flask_backend
pip install -r requirements.txt
```

### Running the Application

#### Running the Frontend

To run the frontend application in a development environment, use the following command:

```sh
npm start
```

This will start the development server and open the application in your default web browser. The application will automatically reload if you make any changes to the source code.

#### Running the Backend

To run the Flask backend, use the following command:

```sh
cd ../flask_backend
flask run
```

This will start the Flask server. Make sure you have your `serviceAccountKey.json` file in the `flask_backend` directory and your `.env` file properly configured.

### Folder Structure

- `src/`: Contains the source code for the application.
  - `components/`: Contains reusable React components.
  - `services/`: Contains service files for API calls.
  - `App.js`: The main application component.
  - `Home.js`: The home page component.
  - `Explore.js`: The explore page component.
  - `VideoLesson.js`: The video lesson page component.
  - `MyVideos.js`: The my videos page component.
- `flask_backend/`: Contains the Flask backend code.
  - `app.py`: The main Flask application file.
  - `requirements.txt`: The dependencies for the Flask application.

### Authentication

This application uses Auth0 for authentication. Make sure to configure your Auth0 credentials in the application.

### Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.
