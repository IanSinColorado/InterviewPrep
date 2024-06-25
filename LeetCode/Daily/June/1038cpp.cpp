struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int globalSum;
    TreeNode* postExtremeLeftFunc(TreeNode* node) {
        TreeNode* post = node->right;
        while(post->left != nullptr && post->left != node)
            post = post->left;
        return post;
    }
    TreeNode* bstToGst(TreeNode* root) {
        globalSum = 0;
        TreeNode* node = root;

        while(node != nullptr){
            TreeNode* post = node->right;
            if(post == nullptr){
                globalSum += node->val;
                node->val = globalSum;
                node = node->left;
            } else {
                TreeNode* postExtremeLeft = postExtremeLeftFunc(node);
                if(postExtremeLeft->left == nullptr) {
                    postExtremeLeft->left = node;
                    node = node->right;
                } else {
                    postExtremeLeft->left = nullptr;
                    globalSum += node->val;
                    node->val = globalSum;
                    node = node->left;
                }
            }
        }
        return root;
    }
};