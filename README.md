# Xmas_Drawings
 A script that randomizes my family's christmas gift exchange according to several rules

# Required Packages
 - Python v3.9.15
 - Pandas v1.5.1

# Rules

1. Our parents are excluded because we all give them gifts
2. An individual will give 1 gift to 1 recipient
3. Partners are not allowed to give to each other (they'll give each other their own gifts)
4. There are no duos allowed
   - This means that if Person_A gives to Person_B, Person_B is not allowed to give to Person_A
5. There are no trios allowed
   - I.e., Person_A -> Person B, Person_B -> Person_C, Person_C -> Person_A is not allowed
