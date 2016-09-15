# Which label for ted leo depending on year.


year = int(input('What year would you like to look?  2001 - Present  '))

if year >= 2001 and year < 2007:
    print('The label was Lookout in {}'.format(year))
elif year >= 2007 and year < 2009:
    print('The label was Touch and Go in {}'.format(year))
elif year > 2009:
    print('The label was Matador in {}'.format(year))
else:
    print("In {} they were not assigned a label".format(year))