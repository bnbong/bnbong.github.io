package cse2010.homework2;

import java.util.Arrays;
import java.util.stream.Collectors;

/*
 * © 2020 CSE2010 HW #2
 *
 * You can freely modify this class except the signatures of the public methods!!
 */
public class DLinkedPolynomial implements Polynomial {

    private DLinkedList<Term> list = null; //double linked list

    public DLinkedPolynomial() {
        list = new DLinkedList<>();
    }

    public int getDegree() { //지수
        /*
            Complete the code here
         */
        Node<Term> term = list.getFirstNode();
        if(term == null){
            return 0;
        }
        else{
            Term compare1 = term.getInfo();
            int degsize = compare1.expo;
            Term compare2 = term.getNext().getInfo();

            for(int i = 0; i < list.size()-1; i++){
                int compare = compare1.compareExponents(compare1, compare2);
                if(compare == 1){ //compare1 is bigger
                    degsize = compare1.expo;
                }
                else if(compare == -1){ //compare2 is bigger
                    degsize = compare2.expo;
                }
                else{
                    continue;
                }
                compare2 = term.getNext().getInfo();
            }
            return degsize;
        }

    }

    @Override
    public double getCoefficient(final int expo) { //계수
        Node<Term> term = list.find(new Term(0.0, expo), Term::compareExponents);

        /*
            Complete the code here
         */
        return term.getInfo().coeff;
    }

    private Term addTerms(Term x, Term y) {
        return new Term(x.coeff + y.coeff, x.expo);
    }

    @Override
    public Polynomial add(final Polynomial p) {
        /*
            Complete the code here
         */

        Polynomial result = new DLinkedPolynomial();
        Node<Term> term = list.getFirstNode();

        if(p.termCount() == 0){
            while(term != null){
                result.addTerm(term.getInfo().coeff, term.getInfo().expo);
                term = list.getNextNode(term);
            }
        }

        else{
            DLinkedPolynomial d = (DLinkedPolynomial)p;
            Node<Term> d_term = d.list.getFirstNode();
            while(d_term != null){
                result.addTerm(d_term.getInfo().coeff, d_term.getInfo().expo);

                d_term = d.list.getNextNode(d_term);
            }
            while(term != null){
                result.addTerm(term.getInfo().coeff, term.getInfo().expo);


                term = list.getNextNode(term);
            }
        }

        return result;
    }

    private Term multTerms(Term x, Term y) {
        return new Term(x.coeff * y.coeff, x.expo + y.expo);
    }

    @Override
    public Polynomial mult(final Polynomial p) {
        /*
            Complete the code here
         */
        Polynomial result = new DLinkedPolynomial();
        Node<Term> term = list.getFirstNode();

        DLinkedPolynomial d = (DLinkedPolynomial)p;
        Node<Term> d_term = d.list.getFirstNode();

        while(term != null){

            d_term = d.list.getFirstNode();
            while(d_term != null){
                result.addTerm(term.getInfo().coeff*d_term.getInfo().coeff, term.getInfo().expo + d_term.getInfo().expo);

                d_term = d.list.getNextNode(d_term);
            }

            term = list.getNextNode(term);
        }
        return result;
    }

    @Override
    public void addTerm(final double coeff, final int expo) {
        /*
            Complete the code here
         */

        if(list.size() == 0) {
            list.addFirst(new Node<>(new Term(coeff, expo)));
        }

        else if(list.size() == 1){
            Node<Term> current = list.getFirstNode();
            if(current.getInfo().expo > expo){
                list.addAfter(current, new Node<>(new Term(coeff, expo)));
            }
            else if(current.getInfo().expo < expo){
                list.addBefore(current, new Node<>(new Term(coeff, expo)));
            }
            else if(current.getInfo().expo == expo){

            }
        }

        else{
            Node<Term> current = list.getFirstNode();

            while(current != null){
                if(current.getInfo().expo == expo){
                    Term merged_coeff = new Term(current.getInfo().coeff + coeff, expo);
                    current.setInfo(merged_coeff);
                    break;
                }
                else if(list.getNextNode(current) != null){
                    if(current.getInfo().expo > expo && list.getNextNode(current).getInfo().expo < expo){
                        list.addAfter(current, new Node<>(new Term(coeff,expo)));
                        break;
                    }
                    else if(current.getInfo().expo < expo){
                        list.addBefore(current, new Node<>(new Term(coeff, expo)));
                        break;
                    }
                }
                else{
                    list.addLast(new Node<>(new Term(coeff, expo)));
                    break;
                }
                current = list.getNextNode(current);
            }
        }
    }

    @Override
    public void removeTerm(final int expo) {
        Node<Term> node = list.find(new Term(0, expo), Term::compareExponents);

        /*
            Complete the code here
         */
        if(node == null){
            throw new NoSuchTermExistsException();
        }

        list.remove(node);
        //NoSuchTermExistsException if no such term exists

    }

    @Override
    public int termCount() {
        return list.size();
    }

    @Override
    public double evaluate(final double val) { //val 을 x 에 대입.
        /*
            Complete the code here
         */

        Node<Term> term = list.getFirstNode();
        Double terms = 0.0;
        Double result = 0.0;

        while(term != null){
            terms = term.getInfo().coeff;
            for(int i = 0; i < term.getInfo().expo; i++){
                terms = terms * val;
            }
            result = result + terms;

            term = list.getNextNode(term);
        }
        return result;
    }

    @Override
    public String toString() {
        if (list.isEmpty())
            return "Empty Polynomial";
        else {
            String[] terms = new String[termCount()];
            int i = 0;
            Node<Term> current = list.getFirstNode();
            do {
                if (current.getInfo().expo == 0) {
                    terms[i++] = String.valueOf(current.getInfo().coeff);
                } else if (current.getInfo().expo == 1) {
                    terms[i++] = current.getInfo().coeff + "x";
                } else {
                    terms[i++] = current.getInfo().coeff + "x^" + current.getInfo().expo;
                }
                current = list.getNextNode(current);
            } while (current != null);
            return String.join("+", terms);
        }
    }

}

