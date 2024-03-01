#the following creates a blank string then adds 1 star per run of the for loop once the number of stars is reached the star pattern will reduce

#defined variable

star_number = ""
stars = 5

#the loop to present the desired pattern 

for star_number in range(1, 2 * stars):
  if star_number <= stars:
    print('*' * star_number)
  else:
    print('*' * (2 * stars - star_number)) 
