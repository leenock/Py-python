# The format() method allows you to format selected parts of a string.
#
# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
#
# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

price = 49
#txt = "The price is {} dollars"
txt = "The price is {:.2f} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#Index Numbers

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))