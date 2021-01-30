# Issuance of loans

## Vision

“Issuance of loans” is web-application which allows users to record information about clients, credits and the loan applications.

**Application should provide:**

* Storing loan applications, clients and credits in a database;
* Display list of loan applications;
* Updating the list of loan applications (adding, editing, removing);
* Display list of clients;
* Updating the list of clients (adding, editing, removing);
* Display list of loans;
* Updating the list of loans (adding, editing, removing);
* Display number of the orders for credits and clients;
* Filtering by date for loan applications and clients;
* Filtering by Loan interest rate.

## 1.Loan applications
#### 1.1Display list of loan applications
The mode is designed to view the list of loan applications, if it possible to display the number of orders for a specified period of time.

**Main scenario:**

* User selects item “Loan applications”;
* Application displays list of Loan applications.

![Picture interface of where is viewing the loan applications list]
(images/1_1_loan_applications_list.png)

Pic. 1.1 View the Loan applications list.

**The list displays the following columns:**

* Loan name - unique loan name;
* client passport number - unique client passport number;
* add date - date of adding a loan order;
* loan rate - interest rate on the selected loan expressed as a percentage;
* credit amount - loan amount to be issued to the client;
* credit term - the number of months during which the client will have to repay the loan;
* loan unterest - overpayment amount for the client;

Aggregate function: Loan_unterest = credit_amount * (loan_rate * (1+loan_rate)^credit_term) / (1+loan_rate)^credit_term - 1

**Filtering by date:**

* In the loan applications list view mode, the user sets a date filter and presses the refresh list button (to the right of the date entry field);
* The application will display a form to view the list of orders with updated data.

#### 1.2 Add loan applications

**Main scenario:**

* User clicks the “Add” button in the loan applications list view mode;
* Application displays form to enter Loan applications data;
* User enters loan applications data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then record is adding to database;
* If error occurs, then error message is displaying;
* If new loan applications record is successfully added, then list of loan applications with added records is displaying.

**Cancel operation scenario:**

* User clicks the “Add” button in the loan applications list view mode;
* Application displays form to enter loan applications data;
* User enters loan applications data and presses “Cancel” button;
* Data don’t save in data base, then list of loan applications records is displaying to user.
* If the user selects the menu item "Loan applications”, ”Clients” or "loans", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Picture interface of where is adding the loan application]
(1_2_loan_applications_add.png)

Pic. 1.2 Add loan applications.

**When adding a loan applications, the following details are entered:**

* Loan name - It is necessary to select the name of the loan from the existing ones in the database;
* Client name - It is necessary to select the initials of the client that are contained in the database;
* loan amount ($) - You must enter the loan amount;
* loan term (mo.) - You must enter the loan term in months;
* Add date - You must enter the date of issue of the loan to the client;

#### 1.3 Edit loan applications.

**Main scenario:**

* User clicks the “Edit” button in the loan applications list view mode;
* Application displays form to enter loan applications data;
* User enters loan applications data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then edited data is added to database;
* If error occurs, then error message is displaying;
* If loan applications record is successfully edited, then list of loan applications with added records is displaying.

**Cancel operation scenario:**

* User clicks the “Edit” button in the loan applications list view mode;
* Application displays form to enter loan applications data;
* User enters loan applications data and presses “Cancel” button;
* Data don’t save in data base, then list of loan applications records is displaying to user.
* If the user selects the menu item "Loan applications”, ”Clients” or "Loans", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Picture interface of where is editing the loan application]
(1_3_loan_applications_edit.png)

Pic. 1.3 Edit loan applications.

**When editing a loan applications, the following details are entered:**

* Loan name - It is necessary to select the name of the loan from the existing ones in the database;
* Client name - It is necessary to select the initials of the client that are contained in the database;
* loan amount ($) - You must enter the loan amount;
* loan term (mo.) - You must enter the loan term in months;
* Add date - You must enter the date of issue of the loan to the client;

**Constraints for data validation :**

* Loan name - It is necessary that at least one loan was selected;
* Client name - It is necessary that at least one client was selected;
* loan amount ($) - Only whole numbers, the minimum amount is 100 and the maximum amount is 100,000;
* loan term (mo.) - Only whole numbers, the minimum number of months is 1, the maximum number of months is 60;
* Add date - loan application add date in format dd/mm/yyyy.

#### 1.4 Removing the order

**Main scenario:**

* The user, while in the list of loan applications, presses the "Delete" button in the selected loan application line;
* If the loan application can be removed, a confirmation dialog is displayed;
* The user confirms the removal of the loan application;
* Record is deleted from database;
* If error occurs, then error message displays;
* If loan application record is successfully deleted, then list of loan applications without deleted records is displaying.

![Picture interface of where is deleting the one loan application]
(1_4_loan_applications_delete.png)

Pic. 1.4 Delete loan application dialog.

**Cancel operation scenario:**

* User is in display mode of loan applications list and press “Delete” button;
* Application displays confirmation dialog “Please confirm delete loan application?”;
* User press “Cancel” button;
* List of loan applications without changes is displaying.



# # 2. Clients

# # # # 2.1 Display list of Clients

This mode is intended for viewing and editing the clients list.

**Main scenario:**

* User selects item “Clients”;
* Application displays list of clients.

![Picture interface of where is viewing the loan applications list]
(2_1_clients_list_view.png)

Pic 2.1 View the clients list.

**The list displays the following columns:**

* First name - client’s first name;
* Last name  client’s last name;
* Registration date - client’s date registration;
* Number of orders - client’s number of loan applications;
* Passport number - client’s passport number

**Filtering by date:**

* In the clients list view mode, the user sets a date filter and presses the refresh list button (to the
right of the date entry field);
* The application will show the clients only for a certain period of time.

**Restrictions:**

* Start date of the period should be less then end date of the period;
* If start date is blank, then filtering by end date only.
* If end date is blank, then filtering by start date only.
* Updating data after selecting the filtering conditions is carried out by pressing the “Refresh” button.

# # # # 2.2 Add client

**Main scenario:**

* User clicks the “Add” button in the clients list view mode;
* Application displays form to enter client data;
* User enters client’s data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then record is adding to database;
* If error occurs, then error message is displaying;
* If new client record is successfully added, then list of clients with added records is displaying.

**Cancel operation scenario:**

* User clicks the “Add” button in the clients list view mode;
* Application displays form to enter client’s data;
* User enters client’s data and presses “Cancel” button;
* Data don’t save in data base, then list of clients records is displaying to user.
* If the user selects the menu item "Loan applications”, ”Clients” or "Loans", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Picture interface of where is adding the client]
(2_2_client_add.png)

Pic. 2.2 Add client.

**When adding a client, the following details are entered:**

* First name – client’s first name;
* Last name – client’s last name;
* Passport number – client’s unique passport number;
* Registration date – client’s date registration.

**Constraints for data validation:**

First name – maximum length of 45 characters;
Last name – maximum length of 45 characters;
Passport number – unique, maximum length of 30 characters;
Registration date – client’s registration date in format dd/mm/yyyy.

# # # # 2.3 Edit client

**Main scenario:**

* User clicks the “Edit” button in the clients list view mode;
* Application displays form to enter client data;
* User enters client’s data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then edited data is added to database;
* If error occurs, then error message is displaying;
* If client’s record is successfully edited, then list of clients with added records is displaying.

**Cancel operation scenario:**

* User clicks the “Edit” button in the clients list view mode;
* Application displays form to enter client data;
* User enters client data and presses “Cancel” button;
* Data don’t save in data base, then list of clients records is displaying to user.
* If the user selects the menu item "Loan applications”, ”Clients” or "Loans", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Picture interface of where is editing the client]
(2_3_client_edit.png)

Pic. 2.3 Edit client.

# # # # 2.4 Removing client

**Main scenario:**

* The user, while in the list of clients mode, presses the "Delete" button in the selected client line;
* Application displays confirmation dialog “Please confirm delete client?”;
* The user confirms the removal of the client;
* Record is deleted from database;
* If error occurs, then error message displays;
* If client record is successfully deleted, then list of clients without deleted records is displaying.

![Picture interface of where is deleting the client]
(2_4_client_delete.png)

Pic. 2.4 Delete client dialog .

**Cancel operation scenario:**

* User is in display mode of clients list and press “Delete” button;
* Application displays confirmation dialog “Please confirm delete client?”;
* User press “Cancel” button;
* List of clients without changes is displaying.



# # 3.Loans

# # # # 3.1 Display list of loans

This mode is intended for viewing and editing the loans list

**Main scenario:**

* User selects item “Loans”;
* Application displays list of loans.

![Picture interface of where is viewing the loan list]
(3_1_loans_list_view.png)

Pic. 3.1 View the loans list.

**The list displays the following columns:**

* Loan name - loan's name
* Loan rate (%) - interest rate on a loan
* Nunber of loan applications - loan's number of loan applications.

**Filtering by loan rate :**

* In the loans list view mode, the user sets a loan rate filter and presses the refresh list button (to the right of the loan rate entry field);
* The application will display a form to view the list of loans with updated data.

# # # # 3.2 Add loan

**Main scenario:**

* User clicks the “Add” button in the loans list view mode;
* Application displays form to enter loan data;
* User enters loan data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then record is adding to database;
* If error occurs, then error message is displaying;
* If new loan record is successfully added, then list of loans with added records is displaying.

**Cancel operation scenario:**

* User clicks the “Add” button in the loans list view mode;
* Application displays form to enter loan data;
* User enters loan data and presses “Cancel” button;
* Data don’t save in data base, then list of loans records is displaying to user.
* If the user selects the menu item "Loan applications”, ”Clients” or "Loans", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Picture interface of where is adding the loan]
(3_2_loan_add.png)

Pic. 3.2 Add loan

**When adding a loan, the following details are entered:**

* Loan name - loan's name;
* Loan rate (%) - interest rate on a loan.

**Constraints for data validation:**

* Loan name - maximum length of 30 characters;
* Loan rate (%) - minimal value is one percentage.

# # # # 3.3 Edit loan

**Main scenario:**

* User clicks the “Edit” button in the loans list view mode;
* Application displays form to enter loan data;
* User enters loan data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then edited data is added to database;
* If error occurs, then error message is displaying;
* If loan record is successfully edited, then list of loans with added records is displaying.

**Cancel operation scenario:**

* The user clicks the “Edit” button in the loan list view mode;
* Application displays form to enter loan data;
* User enters loan data and presses “Cancel” button;
* Data don’t save in the database, then the list of loan records is displaying to the user.

If the user selects the menu item "Loan applications”, ”Clients” or "Loans", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Picture interface of where is editing the loan]
(3_3_loan_edit.png)

Pic. 3.3 Edit loan.



# # # # 3.4 Removing the loan

**Main scenario:**

* The user, while in the view list mode of loan applications, presses the "Delete" button in the selected loan line;
* The application displays confirmation dialog “Please confirm delete loan?”;
* The user confirms the removal of the loan;
* Record is deleted from database;
* If error occurs, then error message displays;
* If the loan record is successfully deleted, then the list of loan applications without deleted records is displaying.

Cancel operation scenario:

* A user is in the display mode of a loan application list and presses the “Delete” button;
* The application displays confirmation dialog “Please confirm delete loan?”;
* A user press “Cancel” button;
* The loan applications without changes are displaying.

![Picture interface of where is deleting the loan]
(3_4_loan_delete.png)

Pic. 3.4 Delete loan dialog.


