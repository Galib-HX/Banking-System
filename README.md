## Banking System - A Simple ATM-like Application


<img width="408" alt="Screenshot 2024-11-29 at 9 30 12 AM" src="https://github.com/user-attachments/assets/7d2bf6f8-cf56-4d33-8ce3-8604fa91430c">





**This Python code will implements a basic ATM-like application that allows users to:**
- **Create an Account:** Users can register for a new account by providing a username and password. Their information is stored securely (simulated) in a text file.

- **Login:** Existing users can log in using their registered credentials.

- **Deposit Funds (Cash In):** Users can add money to their account.
- **Withdraw Funds (Cash Out):** Users can withdraw money from their account, subject

- **Check Balance:** Users can view their current account balance.
- **Logout:** Users can exit the application.


## Features

- **User Interface:** Leverages the design module (assumed to be a custom module) to provide a visually appealing and interactive interface.

- **Transaction Logging:** Deposits and withdrawals are recorded in a text file ("Data.txt") for basic transaction history tracking.
- **Error Handling:** Includes basic error handling for invalid user choices and insufficient account balance during withdrawals.

## Installation

1.Ensure you have Python installed.

2.Clone this repository:

```bash
 git clone git@github.com:Galib-HX/Banking-System.git
```
    
3.Navigate to the project directory:

```bash
 cd Banking-System
```
4.Verify the Repository:
```bash
 ls
```
## Usage

1.Run the script from your terminal:

```bash
python banking_system.py
```

2.Follow the on-screen instructions to create an account, log in, or exit.


## Structure

- **File Handaling:** Data is saved in text file to keep track of all transaction history .

 
## Technologies Used

- **Python**: Language for implementing the banking system.
- **File I/O**: Used for saving and retrieving all transaction data in files.

## Contributing
Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests.
