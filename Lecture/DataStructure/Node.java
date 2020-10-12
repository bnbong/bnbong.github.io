package cse2010.homework5;

public class Node<E> {
    private E element;
    private Node<E> parent;
    private Node<E> left;
    private Node<E> right;

    /**
     * Constructs a node with the given element and neighbors.
     */
    public Node(E element, Node<E> parent, Node<E> left, Node<E> right) {
        this.element = element;
        this.parent = parent;
        this.left = left;
        this.right = right;
    }

    // accessor methods
    public E getElement() {
        return element;
    }

    public Node<E> getParent() {
        return parent;
    }

    public Node<E> getLeft() {
        return left;
    }

    public Node<E> getRight() {
        return right;
    }

    // update methods
    public void setElement(E e) {
        element = e;
    }

    public void setParent(Node<E> parentNode) {
        parent = parentNode;
    }

    public void setLeft(Node<E> leftChild) {
        left = leftChild;
    }

    public void setRight(Node<E> rightChild) {
        right = rightChild;
    }

    @Override public String toString() {
        return "Node{" +
                "element=" + element +
                ", parent=" + (parent != null ? parent.getElement() : "null") +
                ", left=" + (left != null ? left.getElement() : "null") +
                ", right=" + (right != null ? right.getElement() : "null");
    }

}
