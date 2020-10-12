package cse2010.homework1;

public interface SparseMatrix {
    SparseMatrix transpose();
    SparseMatrix add(SparseMatrix aMatrix);

    // You don't have to implement multiply.
    SparseMatrix multiply(SparseMatrix aMatrix);

    int getRowCount();
    int getColumnCount();
    int getElemCount();
}
