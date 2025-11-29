- An exception is a special type of error that disrupts the normal flow of a
  program. Instead of allowing the program to crash when an error occurs,  
  exceptions allow the program to respond to the error gracefully, either by  
  correcting the problem, logging it for further inspection, or notifying the  
  user in a controlled manner. Without proper exception handling, errors  
  would cause programs to fail unexpectedly, potentially resulting in crashes, data loss, and poor user experiences.  
- Python’s exception handling system uses the `try`, `except`, and `finally` blocks to catch and manage exceptions. Here's a simple example to demonstrate how these blocks work:
	-
	  ```
	  try:
	  	x=10/0
	  except ZeroDivisionError:
	  	print("You cannot divide by zero")
	  finally:
	  	print("This block will always run ")
	  ```
	- The `try` block contains the code that might raise an exception. In this
	  case, we attempt to divide a number by zero, which triggers a `ZeroDivisionError`.  
	- The `except` block catches the exception and handles it. Here, it simply prints a message notifying the user of the error.
	- The `finally` block is used to execute code that must run regardless of whether an exception occurred or not. In this case, it prints a message indicating that it always runs.
	- #### You can also handle multiple exceptions in a single `try` block by adding more `except` clauses.
	-
	  ```
	  try:
	  	number = int(input("Enter a number: "))
	      result = 10/number
	  except ValueError:
	  	print("That is not a valid number")
	  except ZeroDivisionError:
	  	print("You cannot divide by zero")
	  ```
	- It is also possible to catch multiple exceptions in a single block using a tuple:
	-
	  ````
	  try:
	  	#some code that may raise an error
	  except (ValueError, TypeError) as e:
	  	print("An error occured", e)
	  ```
- ### The `finally` Block: Ensuring Code Execution Regardless of Errors
- ### Raising exceptions:
	-
	  ```
	  def validate(age):
	  	if age < 0:
	      	raise ValueError ("Age cannot be negative")
	  	return age
	  ```
- #### Sometimes, you may want to raise your own exceptions in certain conditions, such as when a program's input or state doesn't meet specific requirements. You can raise exceptions using the `raise` keyword.
- #### The `raise` statement allows us to explicitly trigger an exception during program execution. This can be particularly useful when certain conditions are met that require the program to stop or signal an error, even if the error isn't directly related to system failures, but rather to application-specific logic.
- Raising exceptions can be particularly useful in cases where your program’s logic depends on certain conditions. For instance, when dealing with APIs or user input, where invalid data could disrupt the flow of the program, it’s better to raise a specific exception rather than letting Python handle the issue with a generic error.
-
  ```
  class InsufficientBalanceError(exception):
  	def __init__(self, balance, amount):
      	self.balance=balance
          self.amount=amount
          super().__init__(f"Attempt to withraw {amount} with only {balance} available.")
  
  def withdraw(balance, amount):
  	if amount > balance:
      	raise InsufficientBalanceError(balance, amount)
  	return balance - amount
  ```
- #### In this example, we create a custom exception `InsufficientBalanceError` which inherits from `Exception`. The constructor of this exception accepts additional parameters, `balance` and `amount`, which are then used to create a custom error message. The `withdraw` function checks if the requested amount exceeds the available balance and raises the`InsufficientBalanceError` with relevant information.
- ## When to Raise Exceptions =>
	- Raising exceptions manually is not always necessary, but it can be extremely helpful in cases where you need to enforce certain conditions or handle errors in a more controlled way. Some common scenarios for raising exceptions include:
	- Validation Failures: When user input, configuration settings, or API responses don’t meet the expected format, raising an exception can prevent further processing and give clear feedback to the user or developer.
	- Business Logic Violations: If your program has specific rules (e.g., a withdrawal cannot exceed the balance), raising an exception ensures that those rules are followed.
	- Resource Availability: In cases where the program relies on external resources (like files, network connections, or databases), you may raise an exception when resources are unavailable or when certain actions are impossible to perform
	-
