#THis will have the backend of the app/website
Number=[4,5]
colour_codes={"Black":[0,1,20], "Brown":[1,10,1], "Red":[2,100,2], "Orange":[3,1000,3], "Yellow":[4, 10000, 100], "Green":[5,100000,0.5], "Blue":[6,1000000,0.25], "Violet":[7,10000000,0.1], "Gray":[8,100000000,0.05], "Gold":[0,0.1,5], "Silver":[0,0.01,10]}
def resistance_4(band1, band2, mult, tol):
    Res=(colour_codes[band1][0]*10 + colour_codes[band2][0])*colour_codes[mult][1]
    string= str(Res) +" ohm" + "  ±" + str(colour_codes[tol][2])+"%"
    return string
def resistance_5(band1, band2, band3, mult, tol):
    Res=(colour_codes[band1][0]*100 + colour_codes[band2][0]*10 + colour_codes[band3][0])*colour_codes[mult][1]
    string= str(Res) +" ohm" + "  ±" + str(colour_codes[tol][2])+"%"
    return string
