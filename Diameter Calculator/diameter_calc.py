from fractions import Fraction

print "Do you wish to calculate the Diameter or Radius from a perimeter measurement? Type 'd' or 'r'"
var = raw_input("Please type 'd' or 'r'")


if var == 'd':
	print "Now type the perimeter measurement for the diameter you would like calculate."
	cir = float(raw_input())
	answer = cir/3.1415926535
	print "What accuracy do you want the diameter rounded to. Type 8 for nearest 1/8, 16 for 1/16th etc."
	denominator = int(raw_input())
	rnd = round(answer * denominator)
	frac = Fraction(int(rnd), denominator)
	if rnd < denominator:
		print frac
		print "The diameter of a %s perimeter is" % cir, frac
	else:
		remain = rnd%denominator
		whole_num = int(rnd/denominator)
		print "The diameter of a %s perimeter is" % cir, whole_num, Fraction(int(remain), denominator)
elif var == 'r':
	print "Now type the perimeter measurement for the radius you would like calculate."
	cir = float(raw_input())
	answer = cir/3.1415926535
	print "What accuracy do you want the diameter rounded to. Type 8 for nearest 1/8, 16 for 1/16th etc."
	denominator = int(raw_input())
	rnd = round(answer/2 * denominator)
	frac = Fraction(int(rnd), denominator)
	if rnd < denominator:
		print frac
		print "The radius of a %s perimeter is" % cir, frac
	else:
		remain = rnd%denominator
		whole_num = int(rnd/denominator)
		print "The radius of a %s perimeter is" % cir, whole_num, Fraction(int(remain), denominator)
else:
	print "Error: You did not type 'd' or 'r' Please run again"