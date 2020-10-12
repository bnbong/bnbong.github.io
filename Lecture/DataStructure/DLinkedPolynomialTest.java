package cse2010.homework2;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

class DLinkedPolynomialTest {

    private Polynomial f;

    @BeforeEach
    public void setup() throws Exception {
         f = new DLinkedPolynomial();
    }

    @Test
    void should_generate_empty_polynomial() {
        Polynomial f = new DLinkedPolynomial();

        assertEquals(0, f.termCount());
        assertEquals(0, f.getDegree());
        assertEquals("Empty Polynomial", f.toString());
    }

    @Test
    void should_generate_non_empty_polynomial1() {
        f.addTerm(4.0, 3);
        f.addTerm(3.0, 2);
        f.addTerm(2.0, 1);
        f.addTerm(1.0, 0);


        assertEquals(4, f.termCount());
        assertEquals(3, f.getDegree());
        assertEquals("4.0x^3+3.0x^2+2.0x+1.0", f.toString());
    }

    @Test
    void should_generate_non_empty_polynomial2() {
        f.addTerm(1.0, 3);
        f.addTerm(3.0, 1);
        f.addTerm(2.0, 2);
        f.addTerm(4.0, 0);


        assertEquals(4, f.termCount());
        assertEquals(3, f.getDegree());
        assertEquals("1.0x^3+2.0x^2+3.0x+4.0", f.toString());
    }

    @Test
    void should_merge_terms_with_the_same_exponents() {
        f.addTerm(2.0, 2);
        f.addTerm(1.0, 3);
        f.addTerm(3.0, 1);
        f.addTerm(4.0, 0);
        f.addTerm(2.0, 2);
        f.addTerm(1.0, 3);
        f.addTerm(4.0, 0);
        f.addTerm(3.0, 1);

        assertEquals(4, f.termCount());
        assertEquals(3, f.getDegree());
        assertEquals("2.0x^3+4.0x^2+6.0x+8.0", f.toString());
    }

    @Test
    void add_with_empty_polynomial_should_return_the_same_polynomial() {
        f.addTerm(1.0, 0);
        f.addTerm(2.0, 1);
        f.addTerm(3.0, 3);


        Polynomial g = new DLinkedPolynomial();

        assertEquals("3.0x^3+2.0x+1.0", f.add(g).toString());
    }

    @Test
    void should_add_two_polynomials() {
        f.addTerm(10.0, 8);
        f.addTerm(5.0, 4);
        f.addTerm(3.0, 1);
        f.addTerm(2.0, 3);
        f.addTerm(7.0, 0);

        Polynomial g = new DLinkedPolynomial();

        g.addTerm(1.0, 1);
        g.addTerm(2.0, 2);
        g.addTerm(3.0, 4);
        g.addTerm(4.0, 0);


        Polynomial h = f.add(g);


        assertEquals(6, h.termCount());
        assertEquals(8, h.getDegree());
        assertEquals("10.0x^8+8.0x^4+2.0x^3+2.0x^2+4.0x+11.0", h.toString());
    }

    @Test
    void multiply_with_unit_polynomial_should_return_the_same_polynomial() {
        f.addTerm(1.0, 0);
        f.addTerm(2.0, 1);
        f.addTerm(3.0, 3);

        Polynomial g = new DLinkedPolynomial();
        g.addTerm(1.0, 0);

        assertEquals("3.0x^3+2.0x+1.0", f.mult(g).toString());
    }

    @Test
    void should_multiply_two_polynomials() {
        f.addTerm(10.0, 8);
        f.addTerm(5.0, 4);
        f.addTerm(3.0, 1);
        f.addTerm(2.0, 3);
        f.addTerm(7.0, 0);

        Polynomial g = new DLinkedPolynomial();

        g.addTerm(1.0, 1);
        g.addTerm(2.0, 2);
        g.addTerm(3.0, 4);
        g.addTerm(4.0, 0);

        Polynomial h = f.mult(g);

        assertEquals(12, h.termCount());
        assertEquals(12, h.getDegree());
        assertEquals(
            "30.0x^12+20.0x^10+10.0x^9+55.0x^8+6.0x^7+10.0x^6+18.0x^5+43.0x^4+14.0x^3+17.0x^2+19.0x+28.0",
            h.toString()
        );
    }

    @Test
    void should_not_change_operands_when_added() {
        f.addTerm(2.0, 200);
        f.addTerm(5.0, 1);
        f.addTerm(7.0, 0);

        Polynomial g = new DLinkedPolynomial();

        g.addTerm(3.0, 100);
        g.addTerm(2.0, 2);
        g.addTerm(1.0, 1);

        Polynomial h = f.add(g);

        assertEquals(200, h.getDegree());
        assertEquals(5, h.termCount());
        assertEquals("2.0x^200+3.0x^100+2.0x^2+6.0x+7.0", h.toString());

        assertEquals("2.0x^200+5.0x+7.0", f.toString());
        assertEquals("3.0x^100+2.0x^2+1.0x", g.toString());
    }

    @Test
    void should_not_change_operands_when_multiplied() {
        f.addTerm(2.0, 200);
        f.addTerm(5.0, 1);
        f.addTerm(7.0, 0);

        Polynomial g = new DLinkedPolynomial();

        g.addTerm(3.0, 100);
        g.addTerm(2.0, 2);
        g.addTerm(1.0, 1);

        Polynomial h = f.mult(g);

        assertEquals(300, h.getDegree());
        assertEquals(8, h.termCount());
        assertEquals("6.0x^300+4.0x^202+2.0x^201+15.0x^101+21.0x^100+10.0x^3+19.0x^2+7.0x", h.toString());

        assertEquals("2.0x^200+5.0x+7.0", f.toString());
        assertEquals("3.0x^100+2.0x^2+1.0x", g.toString());
    }

    @Test
    void should_evaluate_at_a_given_point() {
        f.addTerm(3.0, 2);
        f.addTerm(5.0, 1);
        f.addTerm(7.0, 0);

        assertEquals(357.0, f.evaluate(10), 0.1);

        Polynomial g = new DLinkedPolynomial();

        g.addTerm(1.0, 2);
        g.addTerm(2.0, 1);
        g.addTerm(3.0, 0);

        assertEquals(123.0, g.evaluate(10), 0.1);

        assertEquals(480.0, f.add(g).evaluate(10), 0.1);
        assertEquals(43911.0, f.mult(g).evaluate(10), 0.1);
    }

    @Test
    void should_remove_a_term_if_exists() {
        f.addTerm(3.0, 2);
        f.addTerm(5.0, 1);
        f.addTerm(7.0, 0);

        f.removeTerm(1);
        assertEquals(2, f.termCount());
        assertEquals("3.0x^2+7.0", f.toString());
    }

    @Test
    void should_throw_exception_if_try_to_remove_non_existing_term() {
        f.addTerm(3.0, 2);
        f.addTerm(7.0, 0);

        assertThrows(NoSuchTermExistsException.class, () -> f.removeTerm(1));
    }
}