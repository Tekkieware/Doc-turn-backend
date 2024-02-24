 # Doc-turn backend
This repository contains the backend codebase for a document manipulation application built using Python and Django REST Framework. The application allows users to upload documents, convert them from one format to another, merge documents, split documents, and perform various document-related tasks.
## Live link
Coming soon

## Key Features:
- **Document Upload:** Authenticated users can upload documents of various formats.

- **Document Conversion:** Conversion of documents from one format to another (e.g., PDF to DOCX, DOCX to PDF, etc.).

- **Document Merging:** Ability to merge multiple documents into a single document.
- **Document Splitting** Capability to split a document into multiple smaller documents.

- **RESTful API:** Implementation of a RESTful API using Django REST Framework for seamless communication between the frontend and backend.

## Technologies Used:
**Python:** The primary programming language for backend development.
**Django:** A high-level Python web framework for rapid development and clean, pragmatic design.
**Django REST Framework (DRF):** A powerful and flexible toolkit for building Web APIs in Django.
Other Python Libraries: Utilizing various Python libraries for document manipulation tasks.

## Getting Started

   1. Clone the repository:
   
   ```bash
   git clone (https://github.com/Tekkieware/Doc-turn-backend/).git
   ```
  2. Navigate to the project directory:
     
   ```bash
   cd Doc-turn-backend
   ```
  3. Install dependencies:
     
  ```bash
  pip install -r requirements.txt
  ```
  4. Apply migrations:
     
  ```bash
  python manage.py migrate
  ```
  5. Run the development server:
     
  ```bash
  python manage.py runserver
  ```
  6. Access the API using the url in your terminal.

## Usage:
  Interact with the API endpoints using tools like cURL, Postman, or integrate them directly into your frontend application.
   

## Contributing
- Fork the repository.
- Create a new branch
  ```bash
  git checkout -b feature/your-feature
  ```
- Make your changes and commit them
  ```bash
  git commit -am 'Add some feature
  ```
- Push to the branch
  ```bash
  git push origin feature/your-feature
  ```
- Create a new Pull Request.

## Feel free to reach out with any questions or feedback!

