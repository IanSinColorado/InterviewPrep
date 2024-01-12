/*
Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
int remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
*/
#include <iostream>
#include <vector>

using namespace std;


class ListNode {
    public:
        int val;
        ListNode* next;

    ListNode(int val) {
        val = val;
        next = nullptr;
    }

};

class LinkedList {
private:
    ListNode* head;
    ListNode* tail;


public:

// LinkedList() will initialize an empty linked list.
    LinkedList() {
    }

// int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
    int get(int index) {
    }

// void insertHead(int val) will insert a node with val at the head of the list.
    void insertHead(int val) {
    }
    
// void insertTail(int val) will insert a node with val at the tail of the list.
    void insertTail(int val) {
    }

// int remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
    bool remove(int index) {
    }

// int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
    vector<int> getValues() {
    }
};
