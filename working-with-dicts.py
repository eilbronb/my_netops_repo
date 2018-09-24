my_dictionary = {}
print (type(my_dictionary))


#Assigning a key [Gig0] and a value "link to ISP"
my_dictionary["Gig0"] = "Link to ISP"
print (my_dictionary)

my_dictionary["Gig1"] = "Link to Core Switch"
print (my_dictionary)

print (my_dictionary["Gig1"])

#nested Dictionary
my_list = [3,2,1]
my_other_dictionary = {}
my_other_dictionary["this is a key"] = "This is a Value"
print (my_other_dictionary)

my_other_dictionary["nested list"] = my_list
print (my_other_dictionary)

print (my_other_dictionary["nested list"][1])

my_dictionary["nested list"] = my_list
print (my_dictionary)

my_dictionary["nested dict"] = my_other_dictionary
print (my_dictionary)
print (my_dictionary["nested dict"])
print (my_dictionary["nested dict"]["this is a key"])
