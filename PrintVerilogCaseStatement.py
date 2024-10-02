with open("MathCases.txt", "w") as file:
    i = 0
    vari1 = 0
    vari2 = 2
    ans1 = 0
    ans2 = 0
    ans = 0
    file.write("case (que)\n")
    while (i < 72):
        #loop variables 1:1-9 and 2:2-9
        if (vari1 == 9):
            vari1 = 1
            vari2 = vari2 + 1
        else:
            vari1 = vari1 + 1
        #calculate answer
        ans = vari1*vari2
        #one digit is just answer with zero indicator
        if(ans < 10):
            ans1 = ans
            ans2 = -48
        else:
        #two digits get split up
            ans1 = int((ans - ans%10)/10)
            ans2 = ans%10
        file.write(str(i) + ":begin\n")
        file.write("\t//num1:"+ str(vari1) + " num2:"+ str(vari2) + 
                   " ans:" + str(ans) + " a1:" + str(ans1) + 
                   " a2:" + str(ans2) + "\n")
        #make into ascii character values by adding 48
        file.write("\tvari1 <= " + str(vari1 + 48) + ";\n")
        file.write("\tvari2 <= " + str(vari2 + 48) + ";\n")
        file.write("\tans1 <= " + str(ans1 + 48) + ";\n")
        file.write("\tans2 <= " + str(ans2 + 48) + ";\n")
        file.write("\tstate <= 2;\n")
        file.write("end\n")
        i = i + 1
    file.write("default:\n")
    file.write("\tstate <= 40;\n")
    file.write("endcase\n")