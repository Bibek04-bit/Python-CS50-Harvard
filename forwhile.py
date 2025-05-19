# while True:
#   n = int(input("What's n? "))
#   if n>0:
#     break
  
# for _ in range(n):
#   print("Bibek")

def main():
  i = int(input("Enter a num: "))
  hello(i)
  
  
def hello(n):
  for i in range(n):
    print("hello")
    
main()