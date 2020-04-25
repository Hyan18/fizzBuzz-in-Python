def fizzBuzz(n):
    output = ''
    if n % 3 == 0:
        output += 'fizz'
    if n % 5 == 0:
        output += 'buzz'
    if output == '':
        return n
    return output
