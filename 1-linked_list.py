class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Функція реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  
            current.next = prev  
            prev = current 
            current = next_node  
        self.head = prev

#Сортування однозв'язного списку (сортування вставками)
    def sort(self):
        if not self.head or not self.head.next:
            return

        sorted_list = None 
        current = self.head

        while current:
            next_node = current.next  
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        if not sorted_list or new_node.data < sorted_list.data:
            new_node.next = sorted_list
            return new_node

        current = sorted_list
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_list
    

#Об'єднання двох відсортованих списків
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node(0)  
        tail = dummy

        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next


        tail.next = list1 if list1 else list2
        return dummy.next


if __name__ == "__main__":
    # Створення першого списку
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print("Original list:")
    ll.print_list()

    # Реверсування списку
    ll.reverse()
    print("Reversed list:")
    ll.print_list()

    # Сортування списку
    ll.sort()
    print("Sorted list:")
    ll.print_list()

    # Створення другого списку
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(6)
    ll2.append(0)
    ll2.sort()

    print("Second sorted list:")
    ll2.print_list()

    # Об'єднання двох списків
    merged_head = LinkedList.merge_sorted_lists(ll.head, ll2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head

    print("Merged sorted list:")
    merged_list.print_list()

