print('DSM-5 Criteria for Anorexia Nervosa')
print('Patient presents with restricting type and is in partial remission')
anorexia_nervosa = True   # DSM-5 Criteria for Anorexia Nervosa
_BMI = 15    # kg/m^2
if anorexia_nervosa is True:
    if _BMI >= 17:
        print('Mild')
    elif 16 <= _BMI < 17:
        print('Moderate')
    elif 15 <= _BMI < 16:
        print('Severe')
    elif _BMI < 15:
        print('Extreme')