# Document Conversion Project

This project is a document conversion application built using Python and Django. It provides functionality to convert various types of documents into different formats, making it easier for users to work with different file types. This README file provides an overview of the project, instructions for installation and usage, as well as additional information about the project structure.

## Features

- Convert documents from one format to another
- Support for multiple file types, including PDF, DOCX, TXT, and more
- Preserve the structure and formatting of the original document during conversion
- User-friendly web interface for easy interaction
- Robust and scalable design

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/rahullo/FileMorpher.git
   ```

2. Change into the project directory:

   ```bash
   cd FileMorpher
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Linux/Mac:

     ```bash
     source venv/bin/activate
     ```

   - For Windows (PowerShell):

     ```bash
     .\venv\Scripts\Activate.bat
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

1. Upon accessing the application, you will be presented with the home page.
2. Select an option to perform desired output.
3. Click on the "Upload File" button to select a document you want to convert.
4. Click the "Convert" button to initiate the conversion process.
5. Once the conversion is complete, you will be able to download the converted file.
6. You have to download it before 25sec. (File got deleted after 25 sec to free the storage)
7. You can repeat the process for additional document conversions.

## Project Structure

The project follows the standard structure of a Django application. Here is a brief overview of the main directories and files:

- **`doccon`**: This is main folder.
   - **`doc_conv`**: The Django project management script.
      - **`converters`**: Project settings file.
         - **`static`**: WSGI application entry point.
         - **`templates`**: WSGI application entry point.
         - **`__init__`**: WSGI application entry point.
         - **`admin`**: WSGI application entry point.
         - **`apps`**: WSGI application entry point.
         - **`models`**: all the models.
         - **`tests`**: test.
         - **`urls`**: all defined urls.
         - **`views`**: all the routes.
        
      - **`doc_conv`**: URL configuration file.
         - **`__pycache__`**: WSGI application entry point.
         - **`__init__`**: WSGI application entry point.
         - **`asgi`**: WSGI application entry point.
         - **`settings`**: WSGI application entry point.
         - **`urls`**: WSGI application entry point.
         - **`wsgi`**: WSGI application entry point.
        
      - **`db.sqlite3`**: WSGI application entry point.
      - **`manage.py`**: WSGI application entry point.
   - **`include`**: The Django project directory.
 
   - **`lib`**: The main Django app directory.
   - **`Scripts`**: The main Django app directory.
   - **`pyvenv`**: The main Django app directory.
 

Feel free to explore the project structure and modify the code as per your requirements.

## Contribution

If you would like to contribute to this project, you are welcome to submit pull requests. Before making changes, please open an issue to discuss the proposed improvements or bug fixes.

#### Please take a moment to appreciate my work. If you like this repo, kindly give it a ⭐ on GitHub.

When submitting a pull request, ensure that your code follows the project's coding conventions and include appropriate tests if necessary.

## License

This project is licensed under the MIT licence
