PLACEHOLDER="[name]"
with open("./Input/Names/invited_names.txt", mode="r") as  names_file:
    names=names_file.readlines()
    print(names)
with open("./Input/Letters/starting_letter.txt",) as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        new_letter=new_letter.replace("Angela","Kaustubh")
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx",mode="w") as invite_file:
            invite_file.write(new_letter)

