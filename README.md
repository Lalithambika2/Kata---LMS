# Kata---LMS
# Library Management System

A simple library management system that allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books.

## Features
- **Add Books**: Add new books with unique ISBN, title, author, and publication year.
- **Borrow Books**: Borrow a book from the library if it's available.
- **Return Books**: Return a borrowed book and update its availability.
- **View Available Books**: View a list of all books currently available in the library.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Lalithambika2/Kata---LMS
   cd Kata---LMS

2. **Navigate to the project directory (if applicable)**:
   cd library-management-system

3. **If there are any dependencies, install them:**
   pip install -r requirements.txt

4. **Run the tests to ensure everything is working (optional, if using a test framework like pytest):**
   pytest

5. Start using the system by running the main program (depending on how the system is set up).

## Usage
After running the system, you can interact with it through the command line or any user interface you've set up. The basic commands available will include:

   *Add Book*: Add a new book with details like title, author, and ISBN.
   *Borrow Book*: Borrow a book by selecting it from the available list.
   *Return Book*: Return a borrowed book to the library.
   *View Available Books*: Display all books currently available in the library.

## Test Results

To ensure the functionality of the system, tests have been written using Python's `unittest` framework. All tests have passed successfully.

You can run the tests locally by using the following command:

```bash
python -m unittest test_library.py


## Example Output:
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK


## Contributing:
Feel free to fork the repository, make improvements, and submit pull requests. Contributions are welcome!
