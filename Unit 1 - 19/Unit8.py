# Dictionaries

    # Dictionaries are UNORDERED MAPPINGS for storing objects.
        # Previously we saw how lists store objects in an ordered sequence, dictionaries use a KEY-VALUE pairing instead.

    # This Key-Value pair allows users to quickly grab objects without needing to know an index location.

    # Dictionaries use curly braces and colons to signify the keys and their associated values.
        #   {"key1":"value1","key2":"value2"}

    # So when to choose a list and when to choose a dictionary?
        # Dictionaries:
            # + objects retrieved by key aname.
            # Unordered and can not be stored.
        # List: 
            # + objects retrieved by location.
            # Ordered sequence can be indexed or sliced.

    # Ex 1 
my_dict = {"key1":"value1","key2":"value2"}
my_dict
my_dict['key1']

    # Ex 2
price_lookup = {"apple":2.99,"orange":1.99,"milk": 5.80}
price_lookup['apple']

    # Ex 3 
        # get the value from each key.
d = {'k1':123,'k2':[0,1,2],'k3':{'insedekey':100}}
d['k1']
d['k2']
d['k2'][2]
d['k3']
d['k3']['insedekey']

    # Ex 4 
        # grab the key.
        # made into list.
        # indexing of the list to grab the letter.
        # upper case the letter.
d = {'key1':['a','b','c']}
mylist = d['key1']
mylist
letter = mylist[2]
letter
letter.upper()
        # shorter cut to upper case the letter. 
d['key1'][2].upper()

    # Ex 5 
        # Adding in dictionary.
d = {'k1': 100, 'k2':200}
d['k3'] = 300
d
        # Overwrite an existing key value pair.
d['k1'] = 'New Value'
d
        # See all of the KEY in dictionary.
d = {'k1': 'New Value', 'k2': 200, 'k3': 300}
d.key()
        # See all of the VALUE in dictionary.
d.values()
        # See all of the KEY and VALUE in dictionary.
d.items()