#coverting kilometer to miles
def convert(distance_k):
    mile_per_kilometer = 0.6214
    miles = distance_k * mile_per_kilometer
    return miles

#get input
distance_k = float(input("Enter the distance in kilometers:"))
total_miles = convert(distance_k)

#display output
print("Your distance in miles is", total_miles)