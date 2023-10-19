# In a file called adieu.py, implement a program that prompts the user for names,
# one per line, until the user inputs control-d.
# Assume that the user will input at least one name. Then bid adieu to those names,
# separating two names with one 'and', three names with two commas and one 'and',
# and "n" names with "n-1" commas and one 'and', as in the below:

# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

# Hints
# NOTE: that the inflect module comes with quite a few methods, per pypi.org/project/inflect.
# You can install it with:
# pip install inflect



import inflect

p = inflect.engine()
name_list = []

while True:
    try:
        name = input("Name: ").strip().title()
        name_list.append(name)
    except EOFError:
        print()
        print("Adieu, adieu, to", p.join(name_list))
        break
