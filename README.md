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

# Background to include
- language acquisition theory - 5 hypotheses
  - how does our app put this in practice? how did we figure out the grammar/theory part so the user doesn't have to?
- why use CEFR as a difficulty scale
- the apis we used
    - youtube
    - transcript
    - cathoven
- how we're incrementing the difficulty using analysis from cathoven

# YouLingo: YouTube Language Acquisition

This project is made for U of T Hacks 12 Hackathon.

YouLingo is a web application designed to help users learn new languages by making YouTube videos into language lessons. Users can explore various videos, add their own video URLs, and manage their favorite videos.

## Libraries Used

- React
- React Router
- Reactstrap
- Auth0 React
- Bootstrap
- React Icons

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