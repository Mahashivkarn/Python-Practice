prod={"Macbook":700,
            "Asus":650,
            "Lenevo":675,
            "Dell":720,
            }

most_expensive=max(prod,key=prod.get)

print(most_expensive)

print(prod[most_expensive])

 