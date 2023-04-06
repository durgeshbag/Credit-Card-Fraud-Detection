We have created a "Matching algorithm" that helps in credit card fraud detection. It uses the
hunts algorithm to form decision trees.

This algorithm has been divided into two parts
	1. Online Credit card fraud detection
	2. Offline Credit card fraud detection

Online Credit card fraud detection
This type of fraud includes online transactions to make purchases, shopping , etc
Parameters for fraud detection
	*Credit card details
	*IP address
	*Email
	*Purchase cost
	*Frequency of purchase
	*Location-(shipping,billing address)

Offline Credit card fraud detection
This type of frauds include misuse of physical credit cards as a result of stolen cards,
forged cards, lost cards etc.
Parameters for fraud detection
	*Transaction type
		Swipe and pay
		Touch and pay
	*IP address - device used to pay
	*Purchase cost
	*Frequency of purchase
	*Pin entry

App setup
1. Training data set:
	It contains Legal and fraud transactions of credit card this training data set is
	fed to hunt's algorithm
2. Hunt's algorithm:
	This algorithm uses a training data set to form a decision tree of parameters
	which is to be analysed for fraud detection.
3. Matching algorithm:
	a) The matching algorithm detects to which pattern the incoming transaction
	matches more
	b) A sample of current transaction and recent transaction from the past is
	fed to algorithm
	c) If the incoming transaction is matching more with legal pattern of the
	particular customer, then the algorithm returns  "legal transaction"
	d) If the incoming transaction is matching more with fraud pattern of that
	customer, then the algorithm returns  "fraud transaction"

Note: Due to unavailability of training data-set. This code assumes that the input values for card_no, cvv, ip_address, email_id, location, amount, and frequency will be strings representing either "valid" or "invalid".
