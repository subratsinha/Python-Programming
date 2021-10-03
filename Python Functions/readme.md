### At an airport, a traveler is allowed entry into the ﬂight only if he clears the following checks:
### 1. Baggage Check
### 2. Immigration Check
### 3. Security Check

### The logic for the check methods are given below:

#### check_baggage (baggage_weight)
returns True if baggage_weight is greater than or equal to 0 and less than or equal to 40. Otherwise returns False.

#### check_immigration (expiry_year)
returns True if expiry_year is greater than or equal to 2030 and less than or equal to 2050. Otherwise returns False.

#### check_security(noc_status)
returns True if noc_status is 'valid' or 'VALID', for all other values return False.

#### traveler()
Initialize the traveler Id and traveler name and invoke the functions check_baggage(), check_immigration() and check_security() by passing required arguments.

#### Refer the table below for values of arguments.
If all values of check_baggage(), check_immigration() and check_security() are true, 
display traveler_id and traveler_name
display "Allow Traveler to ﬂy!"

Otherwise,
display traveler_id and traveler_name
display "Detain Traveler for Re-checking!

#### Invoke the traveler() function. Modify the values of diﬀerent variables in traveler() function and observe the output.
