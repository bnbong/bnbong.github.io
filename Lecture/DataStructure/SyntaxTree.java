package cse2010.homework5;

import java.util.*;

public class SyntaxTree extends LinkedBinaryTree<String> {

    public static SyntaxTree buildSyntaxTree(String[] expr) {

        // construct an expression syntax tree ...
        SyntaxTree myTree = new SyntaxTree();
        Stack<SyntaxTree> myStack = new Stack<>();
        Stack<String> myStringStack = new Stack<>();

        for(int i = 0; i < expr.length; i++){


            if(expr[i].compareTo("+") != 0 && expr[i].compareTo("-") != 0 && expr[i].compareTo("*") != 0 && expr[i].compareTo("/") != 0){


                myStringStack.push(expr[i]);

            }
            else{
                SyntaxTree tree = new SyntaxTree();

                Node<String> p = tree.addRoot(expr[i]);

                //uses two stack, push String "t" in myStringStack when new little tree has made.
                //"t" will pointing the top element of myStack.

                //determine top of myStringStack is t here
                if(myStringStack.peek() == "t"){

                    myStringStack.pop();
                    if(myStringStack.peek() == "t"){ //will be left left tree
                        //case : two "t" in myStringStack -> pop two trees in myStringStack and
                        //      push "t" in myStringStack and push a tree in myStack.
                        myStringStack.pop();
                        SyntaxTree rightelem = myStack.pop();
                        SyntaxTree leftelem = myStack.pop();

                        tree.attach(p, leftelem, rightelem);
                    }
                    else{
                        //case : one number and "t" in myStringStack -> pop two elements in myStringStack and
                        //      push "t" in myStringStack and push a tree in myStack
                        SyntaxTree rightelem = myStack.pop(); //will be right leaf tree

                        tree.addLeft(p, myStringStack.pop()); //will be left element
                        p.setRight(rightelem.root);
                        rightelem.root.setParent(p);
                        //tree.attach(p, null, rightelem);
                    }

                }
                else{
                    tree.addRight(p, myStringStack.pop()); //right number has determined.
                    if(myStringStack.peek() == "t"){
                        myStringStack.pop();
                        //case : one number and "t" in myStringStack -> pop two elements in myStringStack and
                        //      push "t" in myStringStack and push a tree in myStack
                        SyntaxTree leftelem = myStack.pop();

                        p.setLeft(leftelem.root);
                        leftelem.root.setParent(p);
                        //tree.attach(p, leftelem, null);
                    }
                    else{
                        tree.addLeft(p, myStringStack.pop());
                    }
                }


                myStack.push(tree);
                myStringStack.push("t");
            }

        }


        myTree = myStack.pop();
        return myTree;
    }

    public String parenthesize() {
        // you may define helper recursive method and use it here...
        String parenthesized_tree = helper_parenthesize_root(this.root.getLeft(), this.root, this.root.getRight());

        return parenthesized_tree;
    }

    public String helper_parenthesize_root(Node left, Node root, Node right){

        if(!left.getElement().equals("+") && !left.getElement().equals("-")
                && !left.getElement().equals("*") && !left.getElement().equals("/")){

            // left and right element are number
            if(!right.getElement().equals("+") && !right.getElement().equals("-")
                    && !right.getElement().equals("*") && !right.getElement().equals("/")){
                return "(" + left.getElement() + " " +
                        root.getElement() + " " + right.getElement() + ")";
            }
            // left element is number, right element is another tree
            return "(" + left.getElement() + " " + root.getElement() + " " +
                    helper_parenthesize_root(right.getLeft(), right, right.getRight()) + ")";
        }
        // left element is another tree, right element is number
        else if(!right.getElement().equals("+") && !right.getElement().equals("-")
                && !right.getElement().equals("*") && !right.getElement().equals("/")){
            return "(" + helper_parenthesize_root(left.getLeft(), left, left.getRight()) + " " +
                    root.getElement() + " " + right.getElement() + ")";
        }
        // left and right element are another tree
        else{
            return "(" + helper_parenthesize_root(left.getLeft(), left, left.getRight()) + " " + root.getElement() +
                    " " + helper_parenthesize_root(right.getLeft(), right, right.getRight()) + ")";
        }
    }

    public double evaluate() {
        // you may define helper recursive method and use it here...
        return helper_evaluate(this.root.getLeft(), this.root, this.root.getRight());
    }

    public double helper_evaluate(Node left, Node root, Node right){
        if(!left.getElement().equals("+") && !left.getElement().equals("-")
                && !left.getElement().equals("*") && !left.getElement().equals("/")){

            // left and right element are number
            if(!right.getElement().equals("+") && !right.getElement().equals("-")
                    && !right.getElement().equals("*") && !right.getElement().equals("/")){
                double left_double = Double.parseDouble((String)left.getElement());
                double right_double = Double.parseDouble((String)right.getElement());
                if(root.getElement().equals("+")){
                    return left_double + right_double;
                }
                else if(root.getElement().equals("-")){
                    return left_double - right_double;
                }
                else if(root.getElement().equals("*")){
                    return left_double * right_double;
                }
                else {
                    return left_double / right_double;
                }
            }
            // left element is number, right element is another tree
            double left_double = Double.parseDouble((String)left.getElement());
            if(root.getElement().equals("+")){
                return left_double + helper_evaluate(right.getLeft(), right, right.getRight());
            }
            else if(root.getElement().equals("-")){
                return left_double - helper_evaluate(right.getLeft(), right, right.getRight());
            }
            else if(root.getElement().equals("*")){
                return left_double * helper_evaluate(right.getLeft(), right, right.getRight());
            }
            else {
                return left_double / helper_evaluate(right.getLeft(), right, right.getRight());
            }
        }
        // left element is another tree, right element is number
        else if(!right.getElement().equals("+") && !right.getElement().equals("-")
                && !right.getElement().equals("*") && !right.getElement().equals("/")){
            double right_double = Double.parseDouble((String)right.getElement());
            if(root.getElement().equals("+")){
                return helper_evaluate(left.getLeft(), left, left.getRight()) + right_double;
            }
            else if(root.getElement().equals("-")){
                return helper_evaluate(left.getLeft(), left, left.getRight()) - right_double;
            }
            else if(root.getElement().equals("*")){
                return helper_evaluate(left.getLeft(), left, left.getRight()) * right_double;
            }
            else {
                return helper_evaluate(left.getLeft(), left, left.getRight()) / right_double;
            }
        }
        // left and right element are another tree
        else{
            if(root.getElement().equals("+")){
                return helper_evaluate(left.getLeft(), left, left.getRight())
                        + helper_evaluate(right.getLeft(), right, right.getRight());
            }
            else if(root.getElement().equals("-")){
                return helper_evaluate(left.getLeft(), left, left.getRight())
                        - helper_evaluate(right.getLeft(), right, right.getRight());
            }
            else if(root.getElement().equals("*")){
                return helper_evaluate(left.getLeft(), left, left.getRight())
                        * helper_evaluate(right.getLeft(), right, right.getRight());
            }
            else {
                return helper_evaluate(left.getLeft(), left, left.getRight())
                        / helper_evaluate(right.getLeft(), right, right.getRight());
            }
        }
    }

    public String toPrefix() {
        // you may define helper recursive method and use it here...
        return helper_toPrefix(this.root.getLeft(), this.root, this.root.getRight());
    }

    public String helper_toPrefix(Node left, Node root, Node right){
        //if left is digit
            //if right is digit = return root + left + right
            //if right is not digit = return root + left + recurse
        //if right is digit
            //if left is digit = return root + left + right
            //if left is not digit = return root + recurse + right
        //else return root and recurse
        if(!left.getElement().equals("+") && !left.getElement().equals("-")
                && !left.getElement().equals("*") && !left.getElement().equals("/")){

            // left and right element are number
            if(!right.getElement().equals("+") && !right.getElement().equals("-")
                    && !right.getElement().equals("*") && !right.getElement().equals("/")){
                return root.getElement() + " " + left.getElement() + " " + right.getElement();
            }
            // left element is number, right element is another tree
            return root.getElement() + " " + left.getElement() + " " +
                    helper_toPrefix(right.getLeft(), right, right.getRight());
        }
        // left element is another tree, right element is number
        else if(!right.getElement().equals("+") && !right.getElement().equals("-")
                && !right.getElement().equals("*") && !right.getElement().equals("/")){
            return root.getElement() + " " +
                    helper_toPrefix(left.getLeft(), left, left.getRight()) + " " + right.getElement();
        }
        // left and right element are another tree
        else{
            return root.getElement() + " " + helper_toPrefix(left.getLeft(), left, left.getRight()) +
                    " " + helper_toPrefix(right.getLeft(), right, right.getRight());
        }
    }

    public String indentSyntaxTree() {
        // you may define helper recursive method and use it here...
        return helper_indentSyntaxTree(this.root.getLeft(), this.root, this.root.getRight(), 0) + "\n";
    }

    public String helper_indentSyntaxTree(Node left, Node root, Node right, int level){
        if(!left.getElement().equals("+") && !left.getElement().equals("-")
                && !left.getElement().equals("*") && !left.getElement().equals("/")){

            // left and right element are number
            if(!right.getElement().equals("+") && !right.getElement().equals("-")
                    && !right.getElement().equals("*") && !right.getElement().equals("/")){
                String space = "  ";
                for(int i = 0; i < level; i++){
                    space = space + space;
                }
                return root.getElement() + "\n" +
                        space + left.getElement() + "\n" +
                        space + right.getElement();
            }
            // left element is number, right element is another tree
            String space = "  ";
            for(int i = 0; i < level; i++){
                space = space + space;
            }
            return root.getElement() + "\n" +
                    space +  left.getElement() + "\n" +
                    space +  helper_indentSyntaxTree(right.getLeft(), right, right.getRight(), level+1);
        }
        // left element is another tree, right element is number
        else if(!right.getElement().equals("+") && !right.getElement().equals("-")
                && !right.getElement().equals("*") && !right.getElement().equals("/")){
            String space = "  ";
            for(int i = 0; i < level; i++){
                space = space + space;
            }
            return root.getElement() + "\n" +
                    space + helper_indentSyntaxTree(left.getLeft(), left, left.getRight(), level+1) + "\n" +
                    space + right.getElement();
        }
        // left and right element are another tree
        else{
            String space = "  ";
            for(int i = 0; i < level; i++){
                space = space + space;
            }
            return root.getElement() + "\n" +
                    space + helper_indentSyntaxTree(left.getLeft(), left, left.getRight(), level+1) + "\n" +
                    space + helper_indentSyntaxTree(right.getLeft(), right, right.getRight(), level+1);
        }
    }

    public static void main(String... args) {

        System.out.println("Homework 5");
    }
}


