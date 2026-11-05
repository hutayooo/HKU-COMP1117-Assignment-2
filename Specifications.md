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

- **When a ride is refused:**: According to the brief, there are 2 conditions that has to be met when a ride is accepted. So, using that, we can work out that a ride is refused if either: 
- the balance before the ride is 0 or less. a pre-ride balance of exactly 0 is refused. A value like 0.50 or 1 is accepted
- or the balance after the transaction/after paying would be less than -35. if the post-ride balance is exactly -35, it is accepted. anything below that like -35.5 is refused

- **When a top-up is refused:**: Once again, according to the brief, there are 3 conditions that has to be met when a top-up is accepted. So, we can work out that a top-up is refused if: 
- the topup amount is not between 50-1000 inclusive. a value between 50-1000 is accepted, while values like 49 or 1050 is refused
- the top-up amount is not a multiple of 50. an amount like 75 or 125 fails this check and is refused, even though it falls within the 50 to 1000 range
-or the balance after the top-up is more than 3000. if a card has a balance of 2500 and receives a top-up of 500, the resulting balance is exactly 3000, which is accepted. if the balance after a topup is more than 3000 (e.g. 3050), the topup is refused

- **What a refused transaction changes, and what it does not:**
- What it changes: It changes the refused count, where it adds 1 to the total count of refused transactions. To accomodate for the history transaction section, it still receives a transaction number in sequential (ascending) order. A refused transaction will also change the status of the interchange discount flag (follows_ride) to false. The next ride will not receive the interchnage discount
- What is doesn't change: The balance of the card does not change since the transaction was refused, regadless if it is a refused top-up or ride. No fares will also be charged or added to the cumulative total of fees paid. It also does not increase the successful transaction counts. This is specifically for the number of successful rides taken of top-ups made. It is also still recorded in the transactions list as a tuple to be printed in the history output, but its status is now 'refused' instead of 'accepted'

- **The lowest balance:**: It'll start with the starting balance as its baseline. It is then updated when a successful transaction causes the balance to drop below the previously recorded lowest balance. Refused rides will not affect the current balance, and thus the lowest balance. We will check if the current balance constitutes as the lowest balance after every successful transaction. 

- **The transaction history:** which transactions appear, their order and numbering, and what each line shows. How is this different from your chat history? 
The transaction history records every attempted transaction throughout the day and formats the final printed output after the summary lines. The data structure is a list, possibly with the name 'transactions', where it stores tuples:
- kind: integer 1 for a ride or 2 for a top-up
- status: bool, true if accepted, false if rejected
- balance_after: float, the resulting balance if it is approved, or the prior balance if it is refused
It then prints each record sequentially in input order, and is numbered starting from 1. It does not perform calculations of any sort, and the list should be untouched (function does not return, only print). The format of the output is stated and is in the brief <number>: <Ride|Top-up> <accepted|refused>. Balance: <0.00>, and is printed after the 7 lines summary. The raw data tuple from transactions is converted into human-readable text via the transaction_history function

## Edge cases

The inputs where something special happens, and what the program must do in
each. For example: a ride straight after a refused ride, or a top-up that
lands exactly on 3000.

1. Ride immediately following a refused ride
- A user attempts a ride, it gets refused, and they attempt a ride directly after
- The first refused transaction resets follows_ride to False. As such, the next ride after, even if its accepted, gets no interchange discount

2. Top-up landing on the balance cap (3000)
- A card with a balance of $2500 receives a $500 top up, bringing the resulting balance to exactly 3000. Or any other combination of valid top-ups that result in a balance of 3000
- The top-up is accepted because the rule specifies a maximum balance of <= 3000. If the balance goes to 3001 or above, the top-up is denied

3. Ride dropping balance to exactly the negative balance limit (-35)
- A ride fare reduces the card's post-ride balance to exactly -35
- The ride is accepted because the post-ride rule permits balances >= -35. If the post ride balance is -35.5 or below instead, the ride is refused

4. Pre-Ride balance of exactly 0
- A card has a balance of 0 when attempting a ride
- The ride is refused because the pre-ride balance must be strictly greater than 0

5. Top-up amounts at the extremes
- A user top-ups exactly 50 or exactly 1000
- If the balance after the top-up would be 3000 or less, they will be accepted. Also, they are accepted since 50 and 1000 are both multiples of 50. A topup value like 49 or 1001 would be rejected as it is outside of the 50-1000 acceptable range

6. Top-up amount within the range but not a multiple of 50
- A user attempts to top-up 75  
- Although within the range, the top-up is denied because it is not a multiple of 50

7. Interchange discount brings fare to 0
- The original fare is 0.5, and an interchange discount is applied
- The fare becomes 0, not -0.5 as the fare after the discount is capped at 0

8. Elder fare boundary at 2
- An elder has a fre of 3, and another at 1
- Anything above 2 gets capped to 2, so a fare of 3 would be set to 2. However, a fare of 1 will still be 1 as it is below the cap

9. Zero transactions
- User inputs zero transactions
- Only outputs the 7 summary lines

10. First transaction is a top-up
- The follows_ride flag will be set to false, meaning the next ride (if any) will get no discount
