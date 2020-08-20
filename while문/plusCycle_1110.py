num = int(input())
chk = num
new,tmp,cnt = 0,0,0

while True:
  tmp = num//10 + num%10
  new = (num%10)*10 + tmp%10
  cnt += 1
  num = new
  if new==chk:
    break
print(cnt)   