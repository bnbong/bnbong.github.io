package cse2010.homework5;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.OptionalInt;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class LinkedBinaryTreeTest {

    private LinkedBinaryTree<Integer> tree1;
    private LinkedBinaryTree<Integer> tree2;

    @BeforeEach
    void setUp() {
        tree1 = new LinkedBinaryTree<>();
        Node<Integer> root1 = tree1.addRoot(4);

        Node<Integer> l1_1 = tree1.addLeft(root1, 2);
        tree1.addLeft(l1_1, 1);
        tree1.addRight(l1_1, 3);

        Node<Integer> l1_2 = tree1.addRight(root1, 6);
        tree1.addLeft(l1_2, 5);
        tree1.addRight(l1_2, 7);

        tree2 = new LinkedBinaryTree<>();
        Node<Integer> root2 = tree2.addRoot(7);

        Node<Integer> t1_1 = tree2.addLeft(root2, 3);
        tree2.addLeft(t1_1, 1);

        Node<Integer> t1_2 = tree2.addRight(root2, 5);
        tree2.addLeft(t1_2, 2);
    }

    @Test
    void should_add_new_node_to_empty_tree_as_root() {
        LinkedBinaryTree<Integer> tree = new LinkedBinaryTree<>();
        tree.addRoot(7);

        assertEquals(1, tree.size());
        assertEquals(7, tree.root().getElement());
    }

    @Test
    void should_add_left_child_to_a_node_with_no_left_child() {
        LinkedBinaryTree<Integer> tree = new LinkedBinaryTree<>();
        Node<Integer> p = tree.addRoot(5);
        tree.addLeft(p, 1);

        assertEquals(2, tree.size());
        assertEquals(1, tree.root.getLeft().getElement());
    }

    @Test
    void should_add_right_child_to_a_node_with_no_right_child() {
        LinkedBinaryTree<Integer> tree = new LinkedBinaryTree<>();
        Node<Integer> p = tree.addRoot(5);
        tree.addRight(p, 9);

        assertEquals(2, tree.size());
        assertEquals(9, tree.root.getRight().getElement());
    }

    @Test
    void should_traverse_inOrder() {
        assertEquals(7, tree1.size());

        checkIt(tree1.inOrder(), Arrays.asList(1, 2, 3, 4, 5, 6, 7));
    }

    @Test
    void should_traverse_preOrder() {
        checkIt(tree1.preOrder(), Arrays.asList(4, 2, 1, 3, 6, 5, 7));
    }

    @Test
    void should_traverse_postOrder() {
        checkIt(tree1.postOrder(), Arrays.asList(1, 3, 2, 5, 7, 6, 4));
    }

    @Test
    void should_height_be_the_same_as_the_maximum_depth_of_nodes_in_a_tree() {

        int height = tree1.height(tree1.root());
        int depth = getDepth(tree1);

        assertEquals(2, height);
        assertEquals(height, depth);

        int height2 = tree2.height(tree2.root());
        int depth2 = getDepth(tree2);

        assertEquals(2, height2);
        assertEquals(height2, depth2);
    }

    @Test
    void should_attach_two_subtrees_to_external_node() {
        LinkedBinaryTree<Integer> tree = new LinkedBinaryTree<>();
        Node<Integer> root = tree.addRoot(333);

        tree.attach(root, tree1, tree2);

        assertEquals(3, tree.height(tree.root()));
        assertEquals(13, tree.size()); // old tree1.size() + old tree2.size() + 1

        // attached trees can no longer be a standalone tree
        assertEquals(0, tree1.size());
        assertEquals(0, tree2.size());
    }

    private void checkIt(List<Node<Integer>> list, List<Integer> expected) {
        List<Integer> nodes = new ArrayList<>();
        list.forEach(i -> nodes.add(i.getElement()));

        assertEquals(expected, nodes);
    }

    private int getDepth(final LinkedBinaryTree<Integer> tree) {
        final OptionalInt optMax = tree.positions().stream().mapToInt(tree::depth).max();
        return optMax.isPresent() ? optMax.getAsInt() : 0;
    }
}