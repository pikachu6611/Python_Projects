These are the programs using Python Asyncio module which runs commands asynchronously to avoid await times in between execution process.

- With synchronous code execution, one thing happens after another.
- With asynchronous code execution, many things happen at same time.  Asynchronous does not automatically mean faster. It just means that program can do other useful work instead of idly while waiting for things like network request or database query.
- AsyncIO excels at IO bound tasks (which is anytime your program is waiting for something external)
- AsyncIO is single threaded and runs on a single process.
- It uses 'cooperative multitasking' where tasks voluntarily give up control.
- CPU bound tasks that need heavy computation, use processes instead.

  - Asyncio.run creates an event loop that runs and manages asynchronous functions. Asyncio.run keeps track of all tasks and when a task is suspended because it is waiting for something else, control returns to the event loop which then finds another task to start or resume.
-
- Asyncio.run works by:
  background-color:: red
	- => getting the event loop
	- => running tasks until they are marked complete
	- => closing the event loop whenever its done.
-
- AWAIT should always be used in an async function. When you AWAIT something, you are telling the event loop to pause the execution of  the current function and yield control back to the event loop which can then run another task.

- In python's AsyncIO there are 3 main types of awaitable objects:
-
- ### => Coroutines which are created when you call an async function
	- Coroutines are functions defined with the ASYNC DEF keywords
		- async def main(): --> so main is a coroutine here
		  background-color:: yellow
	- Coroutines are functions whose execution we can pause.
	- Coroutine Function => which we defined using async def keywords
	  background-color:: blue
	- Coroutine object => it is the awaitable  that gets returned when we call the function
	  background-color:: blue
		-
- ### => Tasks, they are wrappers around coroutines that are scheduled on the event loop
	- Tasks are wrapped coroutines that can be executed independently
	- when we wrap a coroutine in a task using asyncio.create_task, it is handed to the event loop and scheduled to run whenever it  gets a chance
	- Task will keep track of whether coroutine finished successfully, raised an error, or got canceled just like FUTURE.
	- In fact, TASKS are FUTURE under the hood but with extra logic to run the coroutine.
	- So TASKS are more used than FUTURE.

 - ### => Futures. They are low level objects representing eventual results (they are a promise of a result that will be available later)
 - - The futures job is to hold a certain state and result.  The state can be->
	- ==> pending, meaning the future does not have any result or exception yet.
	- ==>canceled, if it was canceled using future.cancel()
	- ==> finished, by a result being set by future.set_result()
	- ==> exception with future.set_exception()
 
