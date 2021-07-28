#First, ensure you create a clone of this repo and name it accordingly. 
#Once you clone the rep, open up the file from your Desktop software using the below code in your terminal/command-line:

''' cd ~/Desktop/robo-advisor

#After repo is opened, make the instructions for the service by creating a separate "robo_advisor.py" file in the Desktop app you're using. This will be used to ensure your set-up and environment are correct.

'''sh
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

'''sh
conda create -n stocks-env python=3.8 # (first time only)
conda activate stocks-env
"

#Install your packakes by activating pip install requirements...

#now test the system. If this processes, we're good to continue:
''' sh
python app/robo_advisor.py
"'

#After we've tested the inputs, it's time to incorporate the data

#Create a dotenv file with the APIKey you've generated from AlphaVantage's website and code it into the file

#Prep the input for the stock symbol. We need to prompt user to input a format that matches what AlphaVantage accepts

'''sh
print("-------------------------")
x = input("Select your symbol:")
print("Stock symbol selected:", x)
print("Let me look that up for you...")
'''

#Here is where we need to tell the system what to import. Ensure you include code to track and incorporate the important values to you such as Closing Price, High Price, etc. based on the instructions of the assignment and what you want incorporated.


#Upon retrieval of the information, ensure you code the data into a csv and save it into your VS Code and Github Desktop for a committ

#Lastly, you'll need to build your recommendation formula. In my case, I chose to use an evaluator of closing price against the average of the high prices in the dataset. Programmed a buy or sell based on if the figure was above or below the mean. 

#Ensure your code is complete and that your roboadvisor functions properly and push to Github. Happy investing!



