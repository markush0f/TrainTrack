# TrainTrack

Welcome to Train Track, an application designed to enhance communication and tracking for local sports teams in the Canary Islands. Our mission is to provide a comprehensive platform that facilitates information exchange among coaches, players, and parents, promoting active participation within the sports community.

## Project Overview

Train Track offers a transparent window into the sports world of children. Parents can closely monitor their children's progress through updated statistics, information about upcoming events, and a messaging system. This enables them to actively participate in their children's sports development and stay informed about their performance in the team.

In addition to detailed player tracking, Train Track includes various additional features that enhance the user experience. Personalized notifications keep users informed about important events, schedule changes, and fee payment reminders, ensuring seamless and continuous participation in their children's sports life.

## Technologies Used

- **Vue.js**: A progressive JavaScript framework for building user interfaces.
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Other technologies**: Include any other major frameworks or libraries used in your project.

## Features

- **Parent Dashboard**: Track children's progress, view statistics, and receive updates on upcoming events.
- **Messaging System**: Communicate directly with coaches and other parents.
- **Notification System**: Receive personalized notifications for events, schedule changes, and fee reminders.
- **User Authentication**: Secure login and registration for coaches, parents, and players.

## Setup and Installation

To set up and run this project on your local machine, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Backend Setup (Django):**
    - Create and activate a virtual environment:
      ```sh
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```
    - Install the required packages:
      ```sh
      pip install -r requirements.txt
      ```
    - Apply migrations and start the Django server:
      ```sh
      python manage.py migrate
      python manage.py runserver
      ```

3. **Frontend Setup (Vue.js):**
    - Navigate to the frontend directory:
      ```sh
      cd frontend
      ```
    - Install the required packages:
      ```sh
      npm install
      ```
    - Start the Vue development server:
      ```sh
      npm run serve
      ```

## Usage

After completing the setup, you can access the application by opening your web browser and navigating to `http://localhost:8000` for the Django backend and `http://localhost:8080` for the Vue frontend.

## Contributing

This project is open to contributions and feedback. Feel free to fork the repository, make changes, and submit pull requests.

---

*Note: This project is developed with a focus on enhancing communication and tracking for local sports teams in the Canary Islands.*
