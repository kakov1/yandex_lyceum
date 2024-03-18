def quarter(xcoord, ycoord):
    if xcoord > 0:
        print('I четверть' if ycoord > 0 else 'IV четверть')
    else:
        print('II четверть' if ycoord > 0 else 'III четверть')
