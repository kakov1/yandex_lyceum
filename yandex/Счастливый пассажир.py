def lucky(ticket):
    global lastTicket
    if sum(map(int, list(str(lastTicket))[:3])) == \
            sum(map(int, list(str(lastTicket))[3:])) and \
            sum(map(int, list(str(ticket).rjust(6, '0'))[:3])) == \
            sum(map(int, list(str(ticket).rjust(6, '0'))[3:])):
        return 'Счастливый'
    else:
        return 'Несчастливый'
