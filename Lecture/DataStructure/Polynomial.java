package cse2010.homework2;

/*
 * © 2020 CSE2010 HW #2
 *
 * DO NOT MODIFY THIS CLASS!
 */
public interface Polynomial {
    /**
     * Returns the degree of the polynomial.
     * @return degree
     */
	public int getDegree();

    /**
     * Returns the coefficient of the term with exponent "exp".
     * @param exp exponent of the term
     * @return the coefficient
     */
	public double getCoefficient(final int exp);
	
    /**
     * Add this polynomial object with the polynomial "p" and returns the
     * resulting polynomial (c = a + b)
     * This object should "NOT" be changed as a result of this operation.
     * @param p polynomial to be added
     * @return a polynomial
     */
	public Polynomial add(final Polynomial p);
	
    /**
     * Multiply this polynomial object with the polynomial "p" and returns
     * the resulting polynomial (c = a * b)
     * This object should "NOT" be changed as a result of this operation.
     * @param p polynomial to be multiplied
     * @return a polynomial
     */
	Polynomial mult(final Polynomial p);

    /**
     * Insert a new term to this polynomial object.
     * Merge terms if a term with the same exponent already exists.
     * @param coeff coefficient of the term
     * @param expo exponent of the term
     */
	public void addTerm(final double coeff, int expo);

    /**
     * Removes a term with exponent "expo".
     * @param expo exponent of the term to be removed
     * @throws NoSuchTermExistsException if no such term exists
     */
	public void removeTerm(final int expo);

    /**
     * Returns the result of the polynomial evaluation for a given input "x".
     * @param x the value to be evaluated by this polynomial
     * @return an evaluated value at point "x"
     */
	public double evaluate(final double x);

    /**
     * Returns the number of non-zero terms in this polynomial
     * @return the number of non-zero terms
     */
	public int termCount();
}