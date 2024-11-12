def bubble_sort(arr):
   n = len(arr)
   i=0
   swap = 0
   for i in range(0,n):
      for j in range(0, n-i-1):
         if arr[j] > arr[j+1]:
            swap = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = swap
   return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)
