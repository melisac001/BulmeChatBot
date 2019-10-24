from bulme import Eliza
import script


print("""

BBBBB   UU   UU   LL      MM     MM   EEEEEE
BB   B  UU   UU   LL      MM M M MM   EE
BBBBB   UU   UU   LL      MM  M  MM   EEEE
BB   B  UU   UU   LL      MM     MM   EE
BBBBB     UUU     LLLLLL  MM     MM   EEEEEE
 

""")


bulme = Eliza(script)

print(bulme.welcome())

while True:
    user_input = input(">")
    
    if user_input == "q":
        break
    
    answer = bulme.answer(user_input)
    print(answer)
    
print(bulme.goodbye())
