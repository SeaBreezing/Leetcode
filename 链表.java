// ListNode类
package leetcode.editor.en;
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    public void add(int newval) {
        ListNode newNode = new ListNode(newval);
        if(this.next == null)
            this.next = newNode;
        else
            this.next.add(newval);
    }
    public void print() {
        System.out.print(this.val);
        if(this.next != null)
        {
            System.out.print("-");
            this.next.print();
            System.out.println("");
        }
    }
}

// 删除链表中指定元素
// https://leetcode.cn/problems/remove-linked-list-elements/
class Solution {
    public ListNode removeElements(ListNode head, int val) {

        ListNode dummy = new ListNode(-1, head);// 虚拟头节点的next是头节点
        ListNode pre = dummy; // 作用是删头结点
        ListNode cur = head;
        while(cur != null){
            if (cur.val == val){ //删掉
                pre.next = cur.next;
            }
            else{
                pre = cur; //pre向前移动一个
            }
            cur = cur.next;//cur向前移动一个
        }
        return dummy.next; //At: 而非head，因为如果head需要被删除，dummy.next就不是head，不能返回head
    }
}
