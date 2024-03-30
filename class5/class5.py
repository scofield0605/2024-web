def rTraverse (head) :
    print("Start right traverse!")
    ptr = head
    while ptr!=None:
        print( 'The color of the car is {}.'.format(ptr.color))
        ptr = ptr.next
    print( 'Finish right traverse!')


# Left traverse the linked listr
def lTraverse (head):
    print("Start left traverse!")
    ptr = head
    while ptr.next!=None:
        ptr = ptr.next
    while ptr!=None:
        print('The color of the car is {}.'.format(ptr.color))
        ptr = ptr.previous
    print( 'Finish left traverse!')

class Car:
    def __init__ (self, color):
        self.color = color
        self.previous = None
        self.next = None
# Initiate the first element of the double linked list.
head = Car("red")
ptr = head
ptr. previous = None
ptr.next = None

# Add next element into linked list.
new = Car("blue") # Create new object.
ptr.next = new # Set the head node next element.
new. previous = ptr # Set the new node previous element.
ptr = new




rTraverse(head)
lTraverse(head)