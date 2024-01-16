class MyListNode {
    public:
        int val;
        MyListNode* next;
        MyListNode* back;

    MyListNode(int val) {
        val = val;
        next = nullptr;
        back = nullptr;
    }

};

class MyLinkedList {
private:
    MyListNode* head;
    MyListNode* tail;
    int size;

public:
// MyLinkedList() Initializes the MyLinkedList object.
    MyLinkedList() {
        head = nullptr;
        tail = head;
        size = 0;
    }
    
// int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    int get(int index) {
        if(head == nullptr) { return -1; }
        if(index >= size) { return -1; }

        MyListNode* curr = head->next;
        int i = 0;

        while(curr != nullptr) {
            if (i == index) {
                return curr->val;
            }

            i++;
            curr = curr->next;
        }

        return -1;
    }
    
// void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    void addAtHead(int val) {
        MyListNode* newNode = new MyListNode(val);

        if (head == nullptr) {
            // then this is the first node of the linked list
            head = newNode;
            tail = head;
            size++;
            return;
        }

        newNode->next = head;
        head->back = newNode;
        head = newNode;
        size++;
    }
    
// void addAtTail(int val) Append a node of value val as the last element of the linked list.
    void addAtTail(int val) {
        MyListNode* newNode = new MyListNode(val);

        if (tail == nullptr) {
            // then this is the first node of the linked list
            tail = newNode;
            head = tail;
            size++;
            return;
        }

        newNode->back = tail;
        tail->next = newNode;
        tail = newNode;
        size++;
    }
    
// void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    void addAtIndex(int index, int val) {
        if ((index > size) || (index < 0)) { return; }
        
        MyListNode* newNode = new MyListNode(val);

        // add to the beginning of the list
        if (index == 0) {
            newNode->next = head;
            head->back = newNode;
            head = newNode;

            // check for case where this is the first index
            if (tail == nullptr) { tail = head; }
            size++;
            return;
        }

        // add to the end of the list
        if (index == (size - 1)) {
            newNode->back = tail;
            tail->next = newNode;
            tail = newNode;

            // check for case wehre this is the first node
            if (head == nullptr) { head = tail; }
            size++;
            return;
        }

        // otherwise in the middle of the list
        MyListNode* curr = head->next;
        int i = 0;

        while (i != index) {
            curr = curr->next;
            i++;
        }

        // constructive actions
        newNode->next = curr;
        newNode->back = curr->back;

        // destructive actions
        curr->back->next = newNode;
        curr->back = newNode;
        size++;
    }
    
// void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
    void deleteAtIndex(int index) {
        if((index >= size) || (index < 0)) { return; }
        
        if (index == 0) {
            MyListNode* del = head;
            head = head->next;
            head->back = nullptr;
            delete del;
            size--;
            return;
        }

        if (index == (size - 1)) {
            MyListNode* del = tail;
            tail = tail->back;
            tail->next = nullptr;
            size--;
            delete del;
        }

        MyListNode* curr = head->next;
        int i = 0;

        while (curr != nullptr) {
            if (i == index) {
                MyListNode* del = curr;

                curr->back->next = del->next;
                curr->next = del->back;
                size--;

                delete del;
            }

            curr = curr->next;
            i++;
        }
        
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