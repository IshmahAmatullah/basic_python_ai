a = open("D:\\File Ishmah\\[Course]\\basic_python_ai\\ex.txt", "w")
a.write("This is a test. Enjoy it! \n")
a.write("Another thing is to do thing slowly but surely \n")
ListofThingstoSay = ["Be Brave\n", "Brace Yourself\n", "Keep it Simple\n", "Dont waste Your Time\n", "Keep Dreaming\n\n"]
a.writelines(ListofThingstoSay)

z = ["You need at least to: \n", "Eat fried Ice cream\n", "Go to Disney\n", "Travel to the moon\n", "Cook Pineapple Pizza\n", "Dance Salsa\n"]
a.writelines(z)

b = open("D:\\File Ishmah\\[Course]\\basic_python_ai\\ex.txt", "r")
print(b.read())