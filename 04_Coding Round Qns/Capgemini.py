"""
Question 1:
    A company is transmitting data to another server. The data is in the form of numbers.
    To secure the data during transmission, they plan to obtain a security key that will be sent along with the data.
    The security key is identified as the count of the unique repeating digits in the data.
    Write an algorithm to find the security key for the data.

Input:
    The input consists of an integer-data, representing the data to be transmitted.

Output:
    Print an integer representing the security key for the given data.

Example:
    Input:          578378923
    Output:         3
    Explanation:    The repeated digits in the data are 7, 8 and 3. So the security key is 3.
"""




"""
Question 2: 
    A company provides network encryption for secure data transfer. The data string is encrypted prior to 
    transmission and gets decrypted at the receiving end. Due to a technical error, the encrypted data got lost and the 
    received string was different from the original string by 1 character. Arnold, a network administrator, 
    is tasked with finding the character that got lost in the network so that the bug does not harm other data that is 
    being transferred through the network.
    Write an algorithm to help Arnold find the character that was missing at the receiving end but present at the sending end.

Input:
    The first line of the input consists of a string - stringSent, representing the string that was sent through the network.
    The next line consists of a string - stringRec, representing the string that was received.

Output:
    Print a character representing the character that was lost in the network during transmission.
    
Note:
    The input strings stringSent and stringRec consist of lowercase and uppercase English alphabets[i.e. a-z, A-Z].

Example:
    Input:
        abcdfjgerj
        abcdfjger
    Output:
        j
    Explanation:
        The character 'j' at the end of the sent string was lost in the network during transmission.  
"""