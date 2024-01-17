class MyListNode {
    public:
        int val;
        MyListNode* next;
        MyListNode* back;

    MyListNode(int value) {
        val = value;
        next = nullptr;
        back = nullptr;
    }

};

class MyLinkedList {
private:
    MyListNode* head;
    int size;

public:
// MyLinkedList() Initializes the MyLinkedList object.
    MyLinkedList() {
        head = nullptr;
        size = 0;
    }
    
// int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    int get(int index) {
        if(head == nullptr) { return -1; }
        if(index >= size) { return -1; }

        MyListNode* curr = head;
        int i = 0;

        while(i != index) {
            if (curr != nullptr) {
                curr = curr->next;
            }
            i++;
        }

        if(curr != nullptr) {return (curr->val);}

        return -1;
    }
    
// void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    void addAtHead(int val) {
        MyListNode* newNode = new MyListNode(val);
        newNode->next = head;

        // check to see if there are nodes in the list
        // if so, set the back link
        if(head != nullptr) {
            head->back = newNode;
        }

        head = newNode;
        size++;
    }
    
// void addAtTail(int val) Append a node of value val as the last element of the linked list.
    void addAtTail(int val) {
        if(head == nullptr) { addAtHead(val); return; }
        MyListNode* newNode = new MyListNode(val);
        MyListNode* current = head;

        // get to the end of the list
        while(current->next != nullptr) {
            current = current->next;
        }

        if(current != nullptr) {
            current->next = newNode;
        }

        newNode->back = current;
        size++;
    }
    
// void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    void addAtIndex(int index, int val) {
        if ((index > size) || (index < 0)) { return; }

        // check if its adding at the beginning of the list
        if (index == 0) { addAtHead(val); return; }

        // check if its addding at the end of the list
        if (index == size) { addAtTail(val); return; }
        
        // otherwise, index is somewhere in the current list
        MyListNode* newNode = new MyListNode(val);
        MyListNode* current = head;

        // index counter to stop in the right place
        int i = 0;

        while(i != index) {
            current = current->next;
            i++;
        }

        current->back->next = newNode;
        newNode->back = current->back;
        newNode->next = current;
        current->back = newNode;
        size++;
    }
    
// void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
    void deleteAtIndex(int index) {
        if(head == nullptr) { return; }
        if((index > size) || (index < 0)) { return; }

        MyListNode* previous = head;
        MyListNode* current = head;
        
        // delete at the beginning of the list
        if (index == 0) {
            if(head->next != nullptr) {
                head->next->back = nullptr;
            }
            current = head;
            head = head->next;
            // head->back = nullptr;
            delete current;
        }
        // delete at the end of the list
        else if(index == size) {
            while(current->next != nullptr) {
                previous = current;
                current = current->next;
            }

            previous->next = nullptr;
            delete current;
        } 
        // delete in the middle of the list
        else {
            int i = 0;
            while(i != index) {
                previous = current;
                current = current->next;
                i++;
            }
            if(current->next != nullptr) {
                current->next->back = previous;
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
int index = 0;
int val = 1;

MyLinkedList* obj = new MyLinkedList();
int param_1 = obj->get(index);
obj->addAtHead(val);
obj->addAtTail(val);
obj->addAtIndex(index,val);
obj->deleteAtIndex(index);