// From aragorn09 on LeetCode problem 707
struct ListNode1
{
    int val;
    ListNode1 *prev, *next;
    ListNode1() : val(0), prev(nullptr), next(nullptr) {}
    ListNode1(int x) : val(x), prev(nullptr), next(nullptr) {}
    ListNode1(int x, ListNode1 *prev, ListNode1 *next) : val(x), prev(prev), next(next) {}
};

class MyLinkedList {
public:
    ListNode1 *head = nullptr;
    int size;
    /** Initialize your data structure here. */
    MyLinkedList() 
    {
        size = 0;
    }

    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) 
    {
        if(head == nullptr)  {return -1;}
        if(index >= size) {return -1;}
        
        ListNode1* current = head;
        
        while(index != 0)
        {
            if(current != nullptr)
            {
                current = current->next;
            }
            index--;
        }
        
        if(current != nullptr) {return(current->val);}
        else {return;}
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) 
    {
        ListNode1* newNode = new ListNode1;

        newNode->val  = val;
        newNode->next = head;
        newNode->prev = nullptr;

        if(head != nullptr)
        {
            head->prev = newNode;
        }
        head = newNode;
        size++;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) 
    {
        if(head == nullptr) {addAtHead(val);return;}

        ListNode1 *newNode = new ListNode1;
        ListNode1 *current = head;
        newNode->val  = val;
        newNode->next = nullptr;
        
        // Go to end of list
        while(current->next != nullptr)
        {
            current  = current->next;
        }
        
        if(current != nullptr)
        {
            current->next = newNode;
        }
        newNode->prev = current;
        
        size++;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) 
    {
        if(index > size)   {return;}
        if(index == 0)      {addAtHead(val); return; }
        if(index == size)   {addAtTail(val); return; }

        ListNode1 *current = head;
        ListNode1 *newNode = new ListNode1;
        newNode->val = val;

        while(index >= 1)
        {
            current = current->next;
            index--;
        }
        
        current->prev->next = newNode;
        newNode->prev = current->prev;
        newNode->next = current;
        current->prev = newNode;
        
        size++;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) 
    {
        ListNode1 *previous = head;
        ListNode1 *current  = head;
        
        if(head == nullptr) {return;}
        if(index >= size){return;}
        
        if(index == 0)
        {
            if(head->next != nullptr)
            {
                head->next->prev = nullptr;
            }
            ListNode1 *temp = head;
            head = head->next;
            delete temp;
        }
        else if(index == size)
        {
            while(current->next != nullptr)
            {
                previous = current;
                current  = current->next;
            }
            previous->next = nullptr;
            delete current;
        }
        else
        {
            while(index != 0)
            {
                previous = current;
                current  = current->next;
                index--;
            }
            if(current->next != nullptr)
            {
                current->next->prev = previous;
            }
            previous->next = current->next;
            
            delete current;
        }
        size--;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */