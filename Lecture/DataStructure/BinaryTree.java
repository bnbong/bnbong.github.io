package cse2010.homework5;

import java.util.ArrayList;
import java.util.List;

public interface BinaryTree<E> {

    enum TraverseOrder { PreOrder, PostOrder, InOrder }

    /**
     * Returns the root node of the tree (or null if tree is empty).
     * @return root node of the tree (or null if tree is empty)
     */
    Node<E> root();

    /**
     * Returns true if node p represents the root of the tree.
     *
     * @param p    A valid node within the tree
     * @return true if p is the root of the tree, false otherwise
     */
    default boolean isRoot(Node<E> p) {
        return root() == p;
    }

    /** Returns the node of p's left child (or null if no child exists). */
    Node<E> left(Node<E> p);

    /** Returns the node of p's right child (or null if no child exists). */
    Node<E> right(Node<E> p);

    /** Returns the node of p's sibling (or null if no sibling exists). */
    default Node<E> sibling(Node<E> p) {
        Node<E> parent = parent(p);
        if (parent == null) return null;
        if (p == left(parent))
            return right(parent);
        else
            return left(parent);
    }

    /**
     * Returns the number of children of node p.
     *
     * @param p    A valid node within the tree
     * @return number of children of node p
     */
    default int numChildren(Node<E> p) {
        int count=0;
        if (left(p) != null)
            count++;
        if (right(p) != null)
            count++;
        return count;
    }

    /**
     * Returns a list of the nodes representing p's children.
     *
     * @param p    A valid node within the tree
     * @return list of the nodes of p's children
     */
    default List<Node<E>> children(Node<E> p) {
        List<Node<E>> snapshot = new ArrayList<>(2);
        if (left(p) != null)
            snapshot.add(left(p));
        if (right(p) != null)
            snapshot.add(right(p));
        return snapshot;
    }

    /**
     * Check whether the node p is the left child.
     * @return true if left child, false otherwise
     */
    boolean isLeftChild(Node<E> p);

    /**
     * Check whether the node p is the right child.
     * @return true if the right child, false otherwise
     */
    boolean isRightChild(Node<E> p);

    /**
     * Returns the height of the subtree rooted at node p.
     *
     * @param p A valid node within the tree
     */
    default int height(Node<E> p) {
        int h = 0;
        for (Node<E> c : children(p))
            h = Math.max(h, 1 + height(c));
        return h;
    }

    /**
     * Returns the number of nodes in the tree.
     * @return number of nodes in the tree
     */
    int size();

    /**
     * Tests whether the tree is empty.
     * @return true if the tree is empty, false otherwise
     */
    default boolean isEmpty() {
        return size() == 0;
    }

    /**
     *  Returns the depth of node p from the root.
     *
     * @param p A valid node within the tree
     */
    default int depth(Node<E> p) {
        if (isRoot(p))
            return 0;
        else
            return 1 + depth(parent(p));
    }

    /**
     * Returns the node of p's parent (or null if p is root).
     *
     * @param p    A valid node within the tree
     * @return node of p's parent (or null if p is root)
     */
    Node<E> parent(Node<E> p);

    /**
     * Returns true if node p has one or more children.
     *
     * @param p    A valid node within the tree
     * @return true if p has at least one child, false otherwise
     */
    default boolean isInternal(Node<E> p) {
        return numChildren(p) > 0;
    }

    /**
     * Returns true if node p does not have any children.
     *
     * @param p    A valid node within the tree
     * @return true if p has zero children, false otherwise
     */
    default boolean isExternal(Node<E> p) {
        return numChildren(p) == 0;
    }

    /**
     * Returns the list of all the nodes of in the tree.
     * @return list of the tree's nodes
     */
    default List<Node<E>> positions() {
        return preOrder();
    }

    //---------- support for various traversals of a tree ----------
    /**
     * Adds nodes of the subtree rooted at node p to the given
     * snapshot using a preorder traversal
     * @param p       node serving as the root of a subtree
     * @param snapshot  a list to which results are appended
     */
    private void preorderSubtree(Node<E> p, List<Node<E>> snapshot) {
        snapshot.add(p); // for preOrder, we add node p before exploring subtrees
        for (Node<E> c : children(p))
            preorderSubtree(c, snapshot);
    }

    /**
     * Returns the list of nodes of the tree, reported in preorder.
     * @return list of the tree's nodes in preorder
     */
    default List<Node<E>> preOrder() {
        List<Node<E>> snapshot = new ArrayList<>();
        if (!isEmpty())
            preorderSubtree(root(), snapshot); // fill the snapshot recursively
        return snapshot;
    }

    /**
     * Adds nodes of the subtree rooted at node p to the given
     * snapshot using a postorder traversal
     * @param p       Node serving as the root of a subtree
     * @param snapshot  a list to which results are appended
     */
    private void postorderSubtree(Node<E> p, List<Node<E>> snapshot) {
        for (Node<E> c : children(p))
            postorderSubtree(c, snapshot);
        snapshot.add(p); // for postOrder, we add position p after exploring subtrees
    }

    /**
     * Returns the list of nodes of the tree, reported in postorder.
     * @return list of the tree's nodes in postorder
     */
    default List<Node<E>> postOrder() {
        List<Node<E>> snapshot = new ArrayList<>();
        if (!isEmpty())
            postorderSubtree(root(), snapshot); // fill the snapshot recursively
        return snapshot;
    }

    /**
     * Adds positions of the subtree rooted at node p to the given snapshot.
     */
    private void inorderSubtree(Node<E> p, List<Node<E>> snapshot) {
        if (left(p) != null)
            inorderSubtree(left(p), snapshot);
        snapshot.add(p);
        if (right(p) != null)
            inorderSubtree(right(p), snapshot);
    }

    /**
     * Returns an iterable collection of positions of a tree, reported in inOrder
     */
    default List<Node<E>> inOrder() {
        List<Node<E>> snapshot = new ArrayList<>();
        if (!isEmpty())
            inorderSubtree(root(), snapshot); // fill the snapshot recursively
        return snapshot;
    }
}
