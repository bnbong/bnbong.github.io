package cse2010.homework2;

/*
 * © 2020 CSE2010 HW #2
 *
 * DO NOT MODIFY THIS CLASS!
 */
public class Term {
    /*
     * Public field is a bad idea. But, for the sake of simplicity .....
     */
    public double 	coeff;	// coefficient
    public int 		expo;	// exponent

    public Term(double coeff, int expo) {
        this.coeff = coeff;
        this.expo = expo;
    }

    public static int compareExponents(Term t1, Term t2) {
        if (t1.expo > t2.expo)
            return 1;
        if (t1.expo < t2.expo)
            return -1;
        return 0;
    }

    public static int compareCoefficients(Term t1, Term t2) {
        if (t1.coeff > t2.coeff)
            return 1;
        if (t1.coeff < t2.coeff)
            return -1;
        return 0;
    }

    public static int compare(Term t1, Term t2) {
        if (t1.expo > t2.expo)
            return 1;
        if (t1.expo < t2.expo)
            return -1;
        if (t1.coeff > t2.coeff)
            return 1;
        if (t1.coeff < t2.coeff)
            return -1;
        return 0;
    }

    @Override public boolean equals(final Object o) {
        if (this == o)
            return true;
        if (!(o instanceof Term))
            return false;
        final Term term = (Term) o;
        return Double.compare(term.coeff, coeff) == 0 &&
                expo == term.expo;
    }

    @Override public String toString() {
        return "Term{" +
                "coeff=" + coeff +
                ", expo=" + expo +
                '}';
    }
}
