def mainfunction(number):
    dev={100:"hundred",1000:"thousand",100000:"lakh",10000000:"crore",1000000000:"billion"}
    if number is 0:
        return "Zero"
    if number<100:
        result=handel_upto_99(number)

    else:
        result=""
        while number>=100:
            devideby=1
            length=len(str(number))
            for i in range(length-1):
                devideby*=10
            if number%devideby==0:
                if devideby in dev:
                    return handel_upto_99(number/devideby)+" "+ dev[devideby]
                else:
                    return handel_upto_99(number/(devideby/10))+" "+ dev[devideby/10]
            res=return_bigdigit(number,devideby)
            result=result+' '+res
            if devideby not in dev:
                number=number-((devideby/10)*(number/(devideby/10)))
            number=number-devideby*(number/devideby)

        if number <100:
            result = result + ' '+ handel_upto_99(number)
    return result

mainfunction(number=12)
