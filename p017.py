def numtotext(n):

	nums = {
		0: '',
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine',

		10: 'ten',
		11: 'eleven',
		12: 'twelve',
		13: 'thirteen',
		14: 'fourteen',
		15: 'fifteen',
		16: 'sixteen',
		17: 'seventeen',
		18: 'eighteen',
		19: 'nineteen',

		20: 'twenty',
		30: 'thirty',
		40: 'forty',
		50: 'fifty',
		60: 'sixty',
		70: 'seventy',
		80: 'eighty',
		90: 'ninety',
		100: 'hundred',
		1000: 'thousand'
		}
	
	string = ''

	if len(str(n)) > 1:
		if len(str(n)) > 3:
			return nums[1] + ' ' + nums[1000]
		elif len(str(n)) > 2:
			if int(str(n)[1:]) < 20:
				tmp = nums[int(str(n)[1:])]
			else:
				tmp = nums[int(str(n)[1]+'0')] + '-' + nums[int(str(n)[2])]
			return nums[int(str(n)[0])] + ' ' + nums[100] + ' and ' + tmp
		if n < 20:
			return nums[n]
		else:
			return nums[int(str(n)[0]+'0')] + '-' + nums[int(str(n)[1])]
	else:
		return nums[n]

count = 0
for i in range(1, 1001, 1):
	print(count, '+', len(numtotext(i).replace('-', '').replace(' ','')), '#', i, numtotext(i))
	count += len(numtotext(i).replace('-', '').replace(' ',''))
print('\nFinal count: %s' % count)
print('Does not count spaces and hyphens.')