def bmi_calculate(weight, height):
    bmi = 703 * weight/ (height * height)

    if bmi <= 18.5:
        print("your bmi is {:1f}. You are underweight.".format(bmi))
    elif 18.5 > bmi <= 25:
        print("your bmi is {:1f}. You are normal weight.".format(bmi))
    elif 25 < bmi < 30:
        print("your bmi is {:1f}. You are overweight.".format(bmi))
    else:
        print("your bmi is {:1f}. You are obese.".format(bmi))