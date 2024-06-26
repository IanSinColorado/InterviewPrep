# include <vector>

using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// Turn the binary search tree into a sorted array
// Then simply use binary search to find the midpoint, then make anything left
// the left subtree and anything to the right the right subtree; do this recursively
// until the entire tree is made
// It will guaranteed be balanced
//    [1, 2, 3, 4, 5]
//     /           \
// [1, 2]         [4, 5]
// ..               ...
class Solution {
public:
    void inorderTraversal(TreeNode* node, vector<TreeNode*>& inorderNodes) {
        if(node == nullptr) return;
        inorderTraversal(node->left, inorderNodes);
        inorderNodes.push_back(node);
        inorderTraversal(node->right, inorderNodes);
    }

    TreeNode* buildBalancedBST(vector<TreeNode*>& inorderNodes, int l, int r){
        if (l > r) return nullptr;
        int mid = (l+r)/2;
        TreeNode* node = inorderNodes[mid];
        node->left = buildBalancedBST(inorderNodes, l, mid-1);
        node->right = buildBalancedBST(inorderNodes, mid+1, r);
        return node;
    }

    TreeNode* balanceBST(TreeNode* root) {
        vector<TreeNode*> inorderNodes;
        inorderTraversal(root, inorderNodes);

        TreeNode* newRoot = buildBalancedBST(inorderNodes, 0, inorderNodes.size()-1);
        return newRoot;
    }
};






class Solution {
public:
    void rightRotate(TreeNode* parent, TreeNode* node) {
        TreeNode* tmp = node->left;
        node->left = tmp->right;
        tmp->right = node;
        parent->right = tmp;
    }

    void leftRotate(TreeNode* parent, TreeNode* node) {
        TreeNode* tmp = node->right;
        node->right = tmp->left;
        tmp->left = node;
        parent->right = tmp;
    }

    void makeRotations(TreeNode* vineHead, int count) {
        TreeNode* current = vineHead;
        for (int i = 0; i < count; ++i) {
            TreeNode* tmp = current->right;
            leftRotate(current, tmp);
            current = current->right;
        }
    }

    TreeNode* balanceBST(TreeNode* root) {
        TreeNode* vineHead = new TreeNode(0);
        vineHead->right = root;
        TreeNode* current = vineHead;

        // convert to vine or just one line of values
        while(current->right){
            if(current->right->left) {
                rightRotate(vineHead, vineHead->right);
            } else {
                current = current->right;
            }
        }

        // count the number of nodes
        int nodeCount = 0;
        current = vineHead->right;
        while(current) {
            ++nodeCount;
            current = current->right;
        }

        // Convert vine to balanced BST
        int m = pow(2, floor(log2(nodeCount + 1))) - 1;
        makeRotations(vineHead, nodeCount - m);
        while(m > 1) {
            m /= 2;
            makeRotations(vineHead, m);
        }

        TreeNode* balancedRoot = vineHead->right;

        delete vineHead;
        return balancedRoot;
    }
};