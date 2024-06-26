# Sum List - Q4

from LinkedList import LinkedList

def sumList(lla,llb):
    n1 = lla.head
    n2 = llb.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    
    return ll

lla = LinkedList()
lla.add(7)
lla.add(1)
lla.add(6)

llb = LinkedList()
llb.add(5)
llb.add(9)
llb.add(2)
print(lla)
print(llb)
print(sumList(lla,llb))

# Time complexity is O(n)
# Space complexity is O(n)