def pyg_latin():
    user_input = raw_input("Enter a word in English");
    user_input = user_input.strip();
    if ((user_input == '') or (not user_input.isalpha())) :
        print("Enter a valid word with just alphabets. Lets try again.. ");
        pyg_latin();
    else:
        trans = user_input[1:] + user_input[0] + "ay";
        print trans;

pyg_latin();