nums = [175, 90, 131, 73, 51, 157, 175, 182, 94, 184]

oddCount = 0
evenCount = 0

for x in nums:
  if (x % 2) == 0:
    evenCount += 1
  else:
    oddCount += 1

diff = abs(oddCount - evenCount)

print(diff)
