
# 1. The volume of a sphere with radius r is 4/3*(pi)r^3 . What is the volume
# of a sphere with radius 5?

radius = 5
pi = 3.1415926535897931

print('The volume of a sphere with radius 5 is {:.5f}.'.format(4.0/3.0*pi*radius**3))

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
#  Shipping costs $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?

book_discount = 24.95 * .40
book_cost = (24.95 - book_discount) * 60 
shipping = 3 + (.75 * 59)

print('The total wholesale cost for 60 copies is {:.0f}.'.format(book_cost + shipping))

#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

start_time = (6*60 + 52)*60
easy_time = (8*60 + 15)*2
tempo_time = (7*60 + 12)*3

bf_hour = (start_time + easy_time + tempo_time)/(60*60)
bf_int_hour = int(bf_hour)

bf_minute  = (bf_hour - bf_int_hour)*60
bf_int_minute = int(bf_minute)

print('Breakfast is at {}:{}'.format(bf_int_hour,bf_int_minute))

#4.
#If my average grade rises from 82 to 89. What is the percentage of the increase?
#Format the result as 'xx.x%'. Keep one figure after decimal point.

initial_grade = 82
final_grade = 89
percent_change = ((final_grade-initial_grade)/(initial_grade)) * (100)

print('The percentage of the increase is {:.1f}%'.format(percent_change))