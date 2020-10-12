package cse2010.homework2;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

class DLinkedListTest {

    private DLinkedList<Term> list;

    @BeforeEach
    void setUp() {
        list = new DLinkedList<>();
    }

    @Test
    void should_create_a_new_node() {
        Node<Term> node = new Node<>(new Term(1.0, 2));

        assertEquals(new Term(1.0, 2), node.getInfo());
        assertEquals(1.0, node.getInfo().coeff);
        assertEquals(2, node.getInfo().expo);
        assertNull(node.getNext());
        assertNull(node.getPrev());
    }

    @Test
    void should_create_an_empty_list() {

        assertTrue(list.isEmpty());
        assertEquals(0, list.size());
    }

    @Test
    void should_increment_size_if_new_node_added_at_front() {

        list.addFirst(new Node<>(new Term(2.0, 2)));
        assertEquals(new Term(2.0, 2), list.getFirstNode().getInfo());
        assertEquals(1, list.size());

        list.addFirst(new Node<>(new Term(1.0, 1)));
        assertEquals(new Term(1.0, 1), list.getFirstNode().getInfo());
        assertEquals(2, list.size());
    }

    @Test
    void should_increment_size_if_new_node_added_at_rear() {
        list.addLast(new Node<>(new Term(2.0, 2)));
        assertEquals(new Term(2.0, 2), list.getLastNode().getInfo());
        assertEquals(1, list.size());

        list.addLast(new Node<>(new Term(1.0, 1)));
        assertEquals(new Term(1.0, 1), list.getLastNode().getInfo());
        assertEquals(2, list.size());
    }

    @Test
    void should_return_the_node_with_matching_term() {
        list.addFirst(new Node<>(new Term(100.0, 100)));
        list.addFirst(new Node<>(new Term(50.0, 50)));
        list.addFirst(new Node<>(new Term(1.0, 1)));

        Node<Term> node = list.find(new Term(50.0, 50), Term::compare);
        assertEquals(new Term(50.0, 50), node.getInfo());
    }

    @Test
    void should_return_null_if_no_node_with_matching_term_exists() {
        list.addFirst(new Node<>(new Term(100.0, 100)));
        list.addFirst(new Node<>(new Term(50.0, 50)));
        list.addFirst(new Node<>(new Term(1.0, 1)));

        Node<Term> node = list.find(new Term(30.0, 50), Term::compare);
        assertNull(node);
    }

    @Test
    void should_return_the_node_with_matching_exponent() {
        list.addFirst(new Node<>(new Term(100.0, 100)));
        list.addFirst(new Node<>(new Term(50.0, 50)));
        list.addFirst(new Node<>(new Term(1.0, 1)));

        // the coefficient is arbitrary in this case
        Node<Term> node = list.find(new Term(0, 50), Term::compareExponents);
        assertEquals(new Term(50.0, 50), node.getInfo());
    }

    @Test
    void should_add_new_node_in_the_middle_of_the_list_case1() {
        list.addFirst(new Node<>(new Term(1.0, 1)));
        list.addFirst(new Node<>(new Term(50.0, 50)));
        list.addFirst(new Node<>(new Term(100.0, 100)));

        // the coefficient is arbitrary in this case
        Node<Term> current = list.find(new Term(0, 50), Term::compareExponents);

        list.addBefore(current, new Node<>(new Term(15.0, 15)));

        assertEquals(4, list.size());
        assertEquals(new Term(15.0, 15), list.getPrevNode(current).getInfo());
    }

    @Test
    void should_add_new_node_in_the_middle_of_the_list_case2() {
        list.addFirst(new Node<>(new Term(1.0, 1)));
        list.addFirst(new Node<>(new Term(50.0, 50)));
        list.addFirst(new Node<>(new Term(100.0, 100)));

        // the coefficient is arbitrary in this case
        Node<Term> current = list.find(new Term(0, 50), Term::compareExponents);

        list.addAfter(current, new Node<>(new Term(15.0, 15)));

        assertEquals(4, list.size());
        assertEquals(new Term(15.0, 15), list.getNextNode(current).getInfo());
    }

    @Test
    void should_decrement_size_if_a_node_is_removed() {
        list.addFirst(new Node<>(new Term(1.0, 1)));
        list.addLast(new Node<>(new Term(50.0, 50)));
        list.addFirst(new Node<>(new Term(100.0, 100)));
        list.addLast(new Node<>(new Term(75.0, 75)));

        assertEquals(4, list.size());

        Node<Term> current = list.find(new Term(0, 50), Term::compareExponents);
        list.remove(current);

        assertEquals(3, list.size());
    }
}