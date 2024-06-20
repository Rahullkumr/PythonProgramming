# wp to print even index word from a list
# l = ["amazon", "flipkart", "ebay", "insta","twitter", "meta"]
# output
"""
(0, 'amazon')
(2, 'ebay')
(4, 'twitter')
"""
l = ["amazon", "flipkart", "ebay", "insta","twitter", "meta"]

for i,j in enumerate(l):
    if i%2==0:
        print((i,j))