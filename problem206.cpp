/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/*
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // base case
        if(head == nullptr){
            return head;
        }
        ListNode * curr =head; // loop through the linked list
        ListNode * prev = nullptr; // our main answer and start is nullptr

        while(curr != nullptr){
            ListNode * temp = curr -> next; // to save for temporary next addy for curr;
            curr -> next = prev; // will be null for first try; add ne -> 0, 1
            prev = curr; // prev will be the first --> prev will 1 
            curr = temp;  // curr will will next 
        }       
        return prev;
    }
};*/