import random
import time

name = input("Hello! Who do I have the pleasure of speaking too? ")

skin = input("Hello "  +   name   +  " let's get you a skincare routine! Would you say you have dry or oily skin? ")

oily=["First Aid Beauty Pure Skin Deep Cleanser With Red Clay is a good choice! it is a middle range price as well",
    "Tatcha The Deep Cleasne is slightly exfoaliating to help ban shine",
    "La Roche Posey Toleriane Purifying Foaming Facial Cleanser is a great budget pick"]

dry=["Vanicream Facial Cleanser is fragrance, dye,and paraben free and a budget option",
   "Kiehls Ultra Facial Cleanser is a more extravaant option but has good reivews"
    ,"Fresh Soy Face Cleanser is also pricey but proven reviews"]
    
moisturizing=["Yves Saint Laurent Pure Shots Hydra Bounce Essence-In-Lotion is a very boougie pick but you are worth it! ","Paula's Choice Advanced Replenishing Toner with Hyaluronic Acid is a middle ground budget pick but a cult favorite","a very good budget pick is Thayer's Alcohol-Free Unscented Witch Hazel Facial Toner with Aloe Vera Formula and avalible most anywhere!"]

pores=["Neutrogena Pore Refining Toner with AHAs will help clear out pores and exfoliate","The Body Shop Tea Tree Skin Clearing Mattifying Toner does a great job","Pixi Glow Tonic also has acid to help clear out pores"]

if skin == "dry":
    print(random.choice(dry))
elif skin == "oily":
    print(random.choice(oily))
    
time.sleep(2)

toner=input("""Now let's get you a toner. Are you looking for something moisturizing or some to deep clean your pores? """)

if toner == "moisturizing":
    print(random.choice(moisturizing))
elif toner == "deep clean":
    print(random.choice(pores))
    
time.sleep(2)

light=["""Stratia Liquid Gold is an indie brand with an amazing ceramide and sea. buckthorn complex""","""Neutrogena Hydro Boost Water Gel is a budget pick""","""Caudalie Resveratrol Lift Lightweight Firming Cashmere Moisturizer is a high end pick but a very good brand"""]

heavy=["""CeraVe Moisturizing Cream aka 'CeraVe in the tub' is a staple.""","""Weleda Skin Food is nourshing and full of fatty acids""","""Tatcha The Dewy Skin Cream is a high end cream with anthocyanin, an antioxidant"""]

face=input("""Let's not forget to moisturise! Do you want a lightweight or a heavy moisturiser? """ )

if face == "lightweight":
     print(random.choice(light))
elif face == "heavy":
    print(random.choice(heavy))
    
    time.sleep(2)
    
print("""Don't forget sunscreen!""")
    
    
