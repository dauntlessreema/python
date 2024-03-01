# programme suggests a cat breed based on the seleted personality trait by the user
# purposeful logic error 

# cat breeds list linked to adjective trait
cat_breeds = {
    "energetic": ["Abyssinian", "Bengal", "Siamese"],
    "independent": ["American Shorthair", "Maine Coon", "Norwegian Forest Cat"],
    "affectionate": ["Persian", "Ragdoll"],  
    "gentle": ["Ragdoll", "Scottish Fold", "Birman"],
    "intelligent": ["Sphynx", "Oriental Shorthair", "Russian Blue"]
}

# requesting trait input from user and for loop provides cat breed
user_trait = input("Are you energetic, independent, affectionate, gentle, or intelligent?  ").lower()

for trait, breeds in cat_breeds.items():
    if user_trait in trait.lower():
        print(f"Based on your preference for {trait}, you might like these cat breeds:")
        for breed in breeds:  
            print(f"\t* {breed}")
        break

# logic error below 
if user_trait not in any(trait.lower() for trait in cat_breeds):
    if user_trait.lower() == "independent":  # second check not needed this is if the user has input a trait not listed
        print("\t* Ragdoll")  # only suggesting one incorrect breed
    else:
        print("Hmm, that's interesting!")