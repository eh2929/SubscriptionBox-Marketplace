# SubscriptionBox-Marketplace

This project is a Python-based web application that serves as a backend API for a subscription-based service. It provides endpoints for managing users, orders, subscriptions, and boxes. The frontend is developed using React.js to offer a user-friendly interface for interacting with the backend functionalities.

## Backend

### Technology Stack

- **Python:** Flask framework is used for building the backend server.
- **Database:** SQLAlchemy is utilized for database operations.
- **RESTful API:** Flask-RESTful is employed for creating API endpoints.
- **Authentication:** Flask-Login is integrated for user authentication.
- **Migration:** Flask-Migrate is used for database migrations.

### Usage

The backend provides endpoints for managing users, orders, subscriptions, and boxes. Here's a brief overview of the available routes:

- `/users`: Allows users to be retrieved and created.
- `/orders`: Provides functionalities for retrieving and creating orders.
- `/subscriptions`: Enables the retrieval and creation of subscription plans.
- `/boxes`: Allows the retrieval and creation of boxes containing items for subscription plans.
- `/login` and `/logout`: Routes for user authentication.

### Installation

Follow these steps to set up the backend on your local machine:

1. Ensure Python 3 is installed.
2. Clone the repository to your local machine.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Set up the database by running `flask db upgrade`.
5. Start the server by running `python3 your_file_name.py`.

## Frontend

The frontend of this project is developed using React.js to provide an interactive user interface. It offers functionalities for user authentication, browsing products, managing orders, and more.

### Technology Stack

- **JavaScript:** React.js library is used for building the frontend components.
- **Routing:** React Router is employed for client-side routing.
- **State Management:** Local state and React hooks are utilized for managing state within components.

### Usage

The frontend offers various routes for different functionalities, including:

- `/`: Homepage displaying available products.
- `/profile`: User profile page showing user information.
- `/cart`: Cart page displaying user's orders.
- `/login`: Login page for user authentication.
- `/create-box`: Page for creating subscription boxes.
- `/signup`: Signup page for new users.
- `/logout`: Logout functionality.

### Installation

Follow these steps to set up the frontend on your local machine:

1. Ensure Node.js and npm are installed.
2. Navigate to the frontend directory.
3. Install dependencies by running `npm install`.
4. Start the frontend server by running `npm start`.
