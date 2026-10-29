# A2 Harbour Card: My Specifications

**Finish this file first, before any code is written.** You supply the
reasoning and fill in this worksheet in your own words, with the AI
assistant's help. It describes the problem only, not how your program will solve
it.

## Input and output types

What the program reads and what it prints, with the type of each value:
int, float, str, bool. Say why.

- **Inputs:** what values does the program read, in what order, and what
  type is each?
  1. Card Type: An integer from 1-3, since there are no decimals. 1 is an adult, 2 is a student, 3 is an elder
  2. Starting Balance: Also an integer from -35 to 3000. The brief explicitly states that it is a whole number, which translates to the int data type

  For the next inputs, they will be looping until the user exits the loop manually
  3. Transaction kind: Another integer for the same reason, ranging from 0-2. 1 is a ride, 2 is a top-up, 0 is to exit, thus breaking the loops
  4. Transaction amounts: Once again, from the brief, the amount if a whole number, regardless if it is a top-up or a ride. So, the data type for this is int. However, it is important to note that the min/max values differ between a top-up and a ride

- **Outputs:** what does the program print, what type is each value, and
  how are the money values printed?
  1. Card type: String, as the output is either 'student', 'adult', or 'elder' which corresponds to the string data type  
  2. Rides taken: Integer, as it outputs the number of rides the user takes. It is impossible to have a decimal number of rides, so this data type is an integer
  3. Top-ups: Also integer, for the same reason that it is impossible to have a decimal number of top-ups
  4. Fares paid: Float, since the fare paid, as stated in the brief "every fare and every balance in this assignment is a whole number or ends in .5", we need to be prepared for the .5 case (due to student discount to a odd-numbered fare). As such, a float is used instead of int, to handle the decimal
  5. Lowest Balance: Float, since the balance is a whole number or ends in 5. For the same reason as fares paid, lowest balance also needs to be a float to handle the decimal
  6. Final Balance: FLoat, for the same reasons
  7. Refused: Integer, as it outputs the number of times a transaction was refused, which again has to be a whole number and cannot be a decimal
  
  After that, there is a transaction history. Each line represents a single transaction with each line consisting:
  1. Transaction number: Integer. Once again, the transaction number cannot be a decimal, and will print whole numbers in ascending order starting from 1 in the 1st line
  2. Category: String, shows if the transaction is a topup or ride
  3. Status: String. This is the verdict of the transaction: (top-up/ride + accepted/rejected). This requires the string data type to represent
  4. Transaction Balance: Float, for the same reasons that the balance can be a whole number or decimal ending with .5. However, not to be confused with the other balances, transaction balance records the balance directly after that transaction has been completed

## The rules in my own words

State each rule in your own words, not the assignment's wording pasted back.
For every boundary, write **both sides**: what happens exactly on it, and
what happens just past it.

- **What a ride costs:**: An adult pays the full cost, while a student card only pays half. An elder pays $2 or the full fare if the fare is less than $2. In other words, min(2, fare). An interchange discount of $1 is applied to the value we just worked out above. However, the final value cannot drop below 0. Meaning the value cap after the discount is $0. In other words, max(0, fare-1). If the previous transaction is a topup (regardless of status), a refused ride, or if it is the first ride of the day, no discount is applied. main() tracks this using a variable follows_ride, where True means the previous transaction was an accepted ride (apply interchange discount), and a False means the previous transaction is not an accepted ride

- **When a ride is refused:**: According to the brief, there are 2 conditions that has to be met when a ride is accepted. So, using that, we can work out that a ride is refused if either the balance before the ride is 0 or less, or the balance after the transaction/after paying would be less than -35. 
- **When a top-up is refused:**
- **What a refused transaction changes, and what it does not:**
- **The lowest balance:**
- **The transaction history:** which transactions appear, their order and numbering, and what each line shows. How is this different from your chat history?

## Edge cases

The inputs where something special happens, and what the program must do in
each. For example: a ride straight after a refused ride, or a top-up that
lands exactly on 3000.

-
