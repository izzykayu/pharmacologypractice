hypokalemia = True
x = 1.5  # x is potassium in mEq/L
if hypokalemia is True:
    if x < 2.5:
        print('may administer insulin', '\t:', 'case is severe')
    elif x <= 3.5:
        print('may administer insulin')
    else:
        print('no drug')
