def ride_fare(card_type, full_fare, follows_ride):
    # Returns the fare for this ride, after the card type and the interchange discount.
    if card_type == 1: # adult, full fare
        fare = full_fare
    elif card_type == 2: #student, divided in half, 2.00 to support float number
        fare = full_fare/2.00
    elif card_type == 3:
        if full_fare >= 2.00: #elder discount is capped at 2. otherwise, the fare is a full fare
            fare = 2.00
        else:
            fare = full_fare
    
    if follows_ride:
        fare -= 1.00 #apply interchange discount if follows_ride is true
        if fare < 0.00:
            fare = 0.00 #ensures fare after the discount isnt negative
    return fare

def can_ride(balance, fare):
    # Returns True if the card accepts a ride costing fare, otherwise False.
    return balance > 0 and (balance-fare) >= -35 #ride is accepted only if the balance before the ride is more than 0 and the balance after is more than or equal to -35

def can_top_up(balance, amount):
    # Returns True if the card accepts this top-up, otherwise False.
    return (50 <= amount <= 1000) and (amount % 50 == 0) and (balance + amount <= 3000) # a top-up will only be accepted only if the amount is between 50 and 1000 inclusive, amount is a multiple of 50, and the balance after is less than or equal to 3000
    pass  # your code here

def transaction_history(transactions):
    # Prints each recorded transaction in order. Returns nothing.
    for i in range(len(transactions)): #loops through every element in the transaction
        index = i+1 #i+1 as i starts from 0, while numbering starts from 1
        kind, status, balance_after = transactions[i] #unpacks the tupple and assigns them to these variables
        if kind == 1:
            kindstr = "Ride"
        else:
            kindstr = "Top-up"
        
        if status:
            statusstr = "accepted"
        else:
            statusstr = "refused"
        
        print(str(index) + ": " + kindstr + " " + statusstr + ". Balance: " + "{:.2f}".format(balance_after))

def main():
    # main() is yours to write, by working it out with the AI assistant.
    # Some things it will need to do:
    #   - keep track of the balance, whether the last transaction was an
    #     accepted ride, and the transaction history
    #   - read transactions until the input ends
    #   - for each transaction, decide what to do, using your first three functions
    #   - print the summary and call transaction_history at the end
    card_type = int(input("Card type (1 adult, 2 student, 3 elder): "))
    if card_type == 1:
        cardstr = "adult"
    elif card_type == 2:
        cardstr = "student"
    else:
        cardstr = "elder"
    balance = float(input("Starting balance: "))
    lowest_bal = balance
    follows_ride = False
    transactions = []
    
    rides = 0
    topups = 0
    fares_paid = 0.00
    refused = 0
    
    while True:
        type = int(input("Transaction (1 ride, 2 top-up, 0 stop): "))
        if type == 0:
            break #0 = stop, breaks the loop

        elif type == 1: #ride
            amount = float(input("Amount: "))
            fare = ride_fare(card_type, amount, follows_ride) #calculates fare
            
            if can_ride(balance, fare):
                balance -= fare
                follows_ride = True
                rides += 1
                fares_paid += fare
                accepted = True
            else: #balance doesnt change
                follows_ride = False
                refused += 1
                accepted = False

            if balance < lowest_bal: #updates lowest balance if the current balance is lower than the previous lowest balance
                lowest_bal = balance
            
            transactions.append((1, accepted, balance))
            
        elif type == 2: #top-up
            amount = float(input("Amount: "))
            
            if can_top_up(balance, amount):
                balance += amount
                topups += 1
                accepted = True
            else: #balance doesnt change
                refused += 1
                accepted = False
            
            follows_ride = False #top-up resets follows_ride to false
            
            if (balance < lowest_bal): #updates lowest balance if the current balance is lower than the previous lowest balance
                lowest_bal = balance #technically this shouldnt happen ever as a topup will increase balance, yet a rejected one wont change it. but just in case
                
            transactions.append((2, accepted, balance))
    
    #print summary
    print("Card type:", cardstr)
    print("Rides taken:", rides)
    print("Top-ups:", topups)
    print("Fares paid:", "{:.2f}".format(fares_paid))
    print("Lowest balance:", "{:.2f}".format(lowest_bal))
    print("Final balance:", "{:.2f}".format(balance))
    print("Refused:", refused)
    
    transaction_history(transactions)


main()  # Don't change this
