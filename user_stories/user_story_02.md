# User story mark book as borrowed.

Mark a book that was previously unborrowed as now borrowed.

## Actors

* Person (Role: Admin)

## Input

Button next to the book in the list

## Internal state change

The column "status" in the "Books" table is switched from "not borrowed" to "borrowed".

## Output 

The book in the list is now marked as "borrowed".

## Errors

* There is no real possibility for an error.

## Expected Errors

* There are no expected errors.
