tags = ["found_footage", "science_fiction", "fantasy", "supernatural", "monster", "psychological",
        "zombie", "anthology", "comedy", "body_horror", "slasher", "satire", "romance", "vampire",
        "werewolf", "foreign", "gory", "home_invasion", "thriller", "demon", "possession",
        "disease", "apocalypse", "post-apocalyptic", "action", "cult_classic", "remake", "ghost",
        "alien", "teen", "franchise", "iconic", "surreal", "arthouse", "haunting", "witchcraft",
        "independent"]

movies = {"Paranormal Activity": ["found_footage", "supernatural", "demon", "possession", "franchise", "haunting"],
          "REC": ["found_footage", "zombie", "disease", "foreign"],
          "Quarantine": ["found_footage", "zombie", "disease", "remake"],
          "The Blair Witch Project": ["found_footage", "supernatural", "cult_classic", "franchise", "iconic", "witchcraft"],
          "Candyman (1992)": ["slasher", "thriller", "supernatural", "gory", "cult_classic", "franchise", "iconic"],
          "Candyman (2021)": ["slasher", "supernatural", "gory", "thriller", "franchise", "remake"],
          "Cloverfield": ["found_footage", "monster", "science_fiction", "alien", "franchise"],
          "Creep": ["found_footage", "psychological", "thriller"],
          "Trollhunter": ["found_footage", "fantasy", "monster"],
          "Willow Creek": ["found_footage", "monster"],
          "V/H/S": ["found_footage", "anthology", "monster", "supernatural", "demon", "gory", "franchise"],
          "Shaun of the Dead": ["comedy", "zombie", "romance", "cult_classic", "franchise"],
          "Tremors": ["comedy", "monster", "science_fiction", "cult_classic", "franchise", "action"],
          "Ready or Not": ["comedy", "slasher", "thriller"],
          "Freaky": ["comedy", "slasher", "teen", "satire"],
          "Fright Night (1985)": ["comedy", "monster", "teen", "vampire", "cult_classic", "supernatural", "satire"],
          "Fright Night (2011)": ["comedy", "monster", "teen", "vampire", "remake", "supernatural", "satire"],
          "Tucker & Dale vs Evil": ["comedy", "slasher", "satire", "cult_classic"],
          "Gremlins": ["comedy", "monster", "cult_classic", "franchise", "iconic"],
          "Critters": ["comedy", "alien", "science_fiction", "cult_classic", "franchise", "monster"],
          "Happy Death Day": ["comedy", "slasher", "teen", "satire", "thriller"],
          "Friday the 13th (1980)": ["slasher", "franchise", "cult_classic", "iconic", "gory", "teen"],
          "Halloween (1978)": ["slasher", "thriller", "franchise", "cult_classic", "iconic", "teen"],
          "Halloween (2018)": ["slasher", "thriller", "franchise"],
          "The Texas Chainsaw Massacre (1974)": ["slasher", "thriller", "franchise", "cult_classic", "iconic", "gory"],
          "Child's Play (1988)": ["slasher", "supernatural", "franchise", "cult_classic", "iconic"],
          "The Fly": ["body_horror", "science_fiction", "franchise", "cult_classic", "gory", "monster"],
          "Tusk": ["body_horror", "comedy", "gory", "surreal", "independent"],
          "Eraserhead": ["body_horror", "arthouse", "surreal", "cult_classic", "independent"],
          "The Human Centipede": ["body_horror", "cult_classic", "gory", "science_fiction", "surreal", "franchise", "independent"],
          "The Thing": ["body_horror", "science_fiction", "monster", "cult_classic", "iconic", "alien"],
          "Hellraiser": ["body_horror", "supernatural", "cult_classic", "iconic", "gory"],
          "Slither": ["body_horror", "monster", "science_fiction", "comedy", "gory", "disease"],
          "The Others": ["supernatural", "psychological", "ghost", "haunting"],
          "Insidious": ["supernatural", "franchise", "ghost", "demon", "haunting"],
          "The Conjuring": ["supernatural", "franchise", "demon", "possession", "haunting"],
          "Alien": ["science_fiction", "monster", "iconic", "franchise", "alien", "cult_classic"],
          "Predator": ["science_fiction", "monster", "action", "franchise", "alien", "cult_classic", "gory"],
          "The Blob": ["science_fiction", "monster", "body_horror", "cult_classic", "iconic", "gory"],
          "Dark Skies": ["science_fiction", "monster", "alien"],
          "Apollo 18": ["science_fiction", "monster", "found_footage", "alien"],
          "Phoenix Forgotten": ["science_fiction", "found_footage", "alien", "monster"],
          "Species": ["science_fiction", "monster", "alien", "cult_classic", "gory"],
          "Life": ["science_fiction", "monster", "alien"],
          "Annihilation": ["science_fiction", "monster", "psychological", "alien", "arthouse"],
          "Grave Encounters": ["found_footage", "supernatural", "ghost", "franchise", "satire"],
          "Signs": ["science_fiction", "monster", "alien", "home_invasion", "thriller"],
          "The Cabin in the Woods": ["science_fiction", "supernatural", "comedy", "slasher", "satire", "monster", "gory"],
          "Get Out": ["psychological", "science_fiction", "thriller"],
          "A Nightmare on Elm Street (1984)": ["slasher", "supernatural", "franchise", "cult_classic", "iconic", "gory"],
          "The Witch": ["supernatural", "arthouse", "witchcraft", "gory"],
          "Hereditary": ["supernatural", "psychological", "arthouse", "demon", "possession", "haunting", "ghost", "gory"],
          "128 Days Later": ["zombie", "thriller", "cult_classic", "franchise", "disease", "post-apocalyptic", "gory"],
          "Poltergeist (1982)": ["supernatural", "ghost", "demon", "haunting", "franchise", "cult_classic", "iconic"],
          "The Babadook": ["supernatural", "psychological", "independent", "monster", "cult_classic", "haunting"],
          "The Exorcist": ["supernatural", "demon", "possession", "franchise", "cult_classic", "iconic"],
          "Train to Busan": ["zombie", "disease", "action", "apocalypse", "franchise", "foreign"],
          "Dawn of the Dead (1978)": ["zombie", "post-apocalyptic", "disease", "action", "franchise", "cult_classic", "iconic", "gory"],
          "Psycho": ["slasher", "psychological", "thriller", "cult_classic", "iconic"],
          "Scream (1996)": ["slasher", "satire", "gory", "thriller", "cult_classic", "iconic", "franchise", "teen"],
          "Trick 'r Treat": ["anthology", "supernatural", "slasher", "comedy", "cult_classic", "gory", "monster"],
          "An American Werewolf in London": ["monster", "comedy", "werewolf", "cult_classic", "gory", "franchise"],
          "The Shining": ["supernatural", "psychological", "thriller", "cult_classic",  "franchise", "iconic"],
          "You're Next": ["slasher", "home_invasion", "thriller", "cult_classic"],
          "IT (2017)": ["supernatural", "monster", "slasher", "iconic", "franchise"],
          "The Evil Dead (1981)": ["supernatural", "monster", "demon", "possession", "cult_classic", "gory", "iconic", "franchise"],
          "The Lost Boys": ["monster", "comedy", "vampire", "cult_classic", "franchise", "iconic", "teen", "satire"],
          "Final Destination": ["supernatural", "thriller", "gory", "franchise", "teen"],
          "The Mist": ["science_fiction", "monster", "gory", "apocalypse", "cult_classic"],
          "Saw": ["slasher", "psychological", "thriller", "gory", "iconic", "cult_classic", "franchise"],
          "The Silence of the Lambs": ["psychological", "slasher", "gory", "cult_classic", "iconic", "franchise"],
          "Don't Breathe": ["slasher", "franchise", "thriller"],
          "The Descent": ["monster", "franchise", "thriller"],
          "Ringu": ["supernatural", "psychological", "foreign", "cult_classic", "iconic", "ghost"],
          "The Ring": ["supernatural", "franchise", "iconic", "cult_classic", "remake", "ghost"],
          "Ju-on: The Grudge": ["supernatural", "franchise", "iconic", "cult_classic", "ghost"],
          "The Grudge": ["supernatural", "franchise", "iconic", "cult_classic", "remake", "ghost"],
          "Let the Right One In": ["supernatural", "vampire", "romance", "foreign"],
          "Let Me In": ["monster", "romance", "vampire", "gory", "remake"],
          "Spring": ["monster", "body_horror", "romance", "independent"],
          "The Invisible Man (2020)": ["science_fiction", "thriller", "psychological"],
          "Possessor": ["science_fiction", "psychological", "thriller", "arthouse"],
          "Christine": ["supernatural", "iconic", "cult_classic"],
          "Dog Soldiers": ["monster", "werewolf", "action", "cult_classic", "independent"],
          "Malignant": ["slasher", "body_horror", "science_fiction"],
          "Sleepy Hollow": ["slasher", "supernatural", "fantasy", "witchcraft"],
          "Creepshow": ["anthology", "comedy", "cult_classic", "supernatural"],
          "Tales from the Hood": ["anthology", "comedy", "cult_classic", "supernatural"],
          "Cursed": ["comedy", "teen", "monster", "werewolf"]}