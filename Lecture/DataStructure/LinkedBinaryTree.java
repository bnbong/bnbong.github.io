package cse2010.homework5;

public class LinkedBinaryTree<E> implements BinaryTree<E> {

    /**
     * Factory function to create a new node storing element e.
     */
    protected Node<E> createNode(E e, Node<E> parent, Node<E> left, Node<E> right) {
        return new Node<>(e, parent, left, right);
    }

    // LinkedBinaryTree instance variables
    protected Node<E> root = null;
    protected int size = 0;

    /**
     * Returns the number of nodes in the tree.
     */
    @Override public int size() {
        return size;
    }

    /**
     * Returns the root node of the tree (or null if tree is empty).
     */
    @Override public Node<E> root() {
        return root;
    }

    /**
     * Returns the node of p's parent (or null if p is root).
     */
    @Override public Node<E> parent(final Node<E> p) {
        return p.getParent();
    }

    /**
     * Returns the node of p's left child (or null if no child exists).
     */
    public Node<E> left(Node<E> p) {
        return p.getLeft();
    }

    /**
     * Returns the node of p's right child (or null if no child exists).
     */
    public Node<E> right(Node<E> p) {
        return p.getRight();
    }

    /**
     * Check whether the node of p is the left child.
     * @return true if left child, false otherwise
     */
    public boolean isLeftChild(Node<E> p) {
        Node<E> parent = parent(p);
        return parent != null && parent.getLeft() == p;
    }

    /**
     * Check whether the node of p is the right child.
     * @return true if right child, false otherwise
     */
    public boolean isRightChild(Node<E> p) {
        Node<E> parent = parent(p);
        return parent != null && parent.getRight() == p;
    }

    /**
     * Places element at the root of an empty tree and returns the root.
     */
    public Node<E> addRoot(E e) {
        if (!isEmpty())
            throw new IllegalStateException("Tree is not empty");
        root = createNode(e, null, null, null);
        size = 1;
        return root;
    }

    /**
     * Creates a new left child of node p storing element e; returns it.
     */
    public Node<E> addLeft(Node<E> p, E e) {
        if (p.getLeft() != null)
            throw new IllegalArgumentException("p already has a left child");
        Node<E> child = createNode(e, p, null, null);
        p.setLeft(child);
        size++;
        return child;
    }

    /**
     * Creates a new right child of node p storing element e; returns it.
     */
    public Node<E> addRight(Node<E> p, E e) {
        if (p.getRight() != null)
            throw new IllegalArgumentException("p already has a right child");
        Node<E> child = createNode(e, p, null, null);
        p.setRight(child);
        size++;
        return child;
    }

    /**
     * Replaces the element at node p with e and returns the replaced element.
     */
    public E set(Node<E> p, E e) {
        E temp = p.getElement();
        p.setElement(e);
        return temp;
    }

    /**
     * Attaches trees t1 and t2 as left and right subtrees of external p.
     */
    public void attach(Node<E> p, LinkedBinaryTree<E> t1, LinkedBinaryTree<E> t2) {
        if (isInternal(p))
            throw new IllegalArgumentException("p must be a leaf");

        size += t1.size() + t2.size();
        if (!t1.isEmpty()) {
            t1.root.setParent(p);
            p.setLeft(t1.root);
            t1.root = null;
            t1.size = 0;
        }
        if (!t2.isEmpty()) {
            t2.root.setParent(p);
            p.setRight(t2.root);
            t2.root = null;
            t2.size = 0;
        }
    }

    /**
     * Removes the node p and replaces it with its child, if any, and returns element in p.
     */
    public E remove(Node<E> p) {
        if (numChildren(p) == 2)
            throw new IllegalArgumentException("p has two children");

        Node<E> child = (p.getLeft() != null ? p.getLeft() : p.getRight());
        if (child != null)
            child.setParent(p.getParent()); // child’s grandparent becomes its parent
        if (p == root)
            root = child;
        else {
            Node<E> parent = p.getParent();
            if (p == parent.getLeft())
                parent.setLeft(child);
            else
                parent.setRight(child);
        }
        size--;
        E temp = p.getElement();
        p.setElement(null);
        p.setLeft(null);
        p.setRight(null);
        p.setParent(p);
        return temp;
    }
}
