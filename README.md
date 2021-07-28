#First, ensure you create a clone of this repo and name it accordingly. 
#Once you clone the rep, open up the file from your Desktop software using the below code in your terminal/command-line:

''' cd ~/Desktop/robo-advisor

#After repo is opened, make the instructions for the service by creating a separate "robo_advisor.py" file in the Desktop app you're using. This will be used to ensure your set-up and environment are correct.

'''
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
'''


#We then need to create a requirements file to ensure all packages are downloaded that we need.

"requests
python-dotenv"

#Note: You can use pandas if you'd like above, but just ensure to enable it in the code above.

#Now, create/set up the environment:

'''
conda create -n stocks-env python=3.8 # (first time only)
conda activate stocks-env
"

#Install your packakes by activating pip install requirements...

#now test the system. If this processes, we're good to continue:
"
python app/robo_advisor.py
"




