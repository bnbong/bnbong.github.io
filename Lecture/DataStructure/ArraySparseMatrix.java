package cse2010.homework1;

import javax.lang.model.type.ArrayType;
import java.lang.reflect.Array;
import java.nio.file.FileAlreadyExistsException;

public class ArraySparseMatrix implements SparseMatrix {

    public static final int DEFAULT_CAPACITY = 1024;

    private int rowCount;
    private int columnCount;
    private int elemCount;
    private Entry[] elements = new Entry[0];

    public ArraySparseMatrix(int rowCount, int columnCount, int capacity) {
        elements = new Entry[capacity];
        this.rowCount = rowCount;
        this.columnCount = columnCount;
        this.elemCount = 0;
    }

    public ArraySparseMatrix(int rowCount, int columnCount) {
        this(rowCount, columnCount, DEFAULT_CAPACITY);
    }

    /*
     * This routine simulates reading from files using two-dimensional matrix.
     */
    public static SparseMatrix create(double[][] aMatrix, int rowCount, int columnCount, int elemCount) {
        ArraySparseMatrix matrix = new ArraySparseMatrix(rowCount, columnCount, elemCount);

        int nonZeroCount = 0;
        for (int i = 0; i < aMatrix.length; i++)
            for (int j = 0; j < aMatrix[i].length; j++) {
                if (Double.compare(aMatrix[i][j], 0.0) != 0) {
                    matrix.put(new Entry(i, j, aMatrix[i][j]));
                    nonZeroCount++;
                }
            }

            /*
             * your code goes here
             */ 
            // if (nonZeroCount != elemCount) throw IllegalStateException saying 
            // "Non zero count doesn't match"
        if (nonZeroCount != elemCount) throw new IllegalStateException("Non zero count doesn't match");
        

        return matrix;
    }

    private void put(Entry entry) {
        elements[elemCount++] = entry;
    }

    @Override
    public SparseMatrix transpose() {

        /*
         *   Your code goes here
         */

        ArraySparseMatrix new_arr = new ArraySparseMatrix(this.columnCount, this.rowCount, this.elemCount);

        for(Entry entry : this.elements){ // making empty space for put elements sorted.
            new_arr.put(null);
        }

        for(Entry entry : this.elements){ // putting element
            new_arr.elements[entry.getCol()] = new Entry(entry.getCol(), entry.getRow(), entry.getValue());
        }

        return new_arr;
    }

    @Override
    public SparseMatrix add(SparseMatrix other) {
        if (this.rowCount != other.getRowCount() || this.columnCount != other.getColumnCount())
            throw new IllegalArgumentException("Matrix size doesn't match");

        /*
         *  Your code goes here
         */

        ArraySparseMatrix other_mat = (ArraySparseMatrix)other; // copying & casting other to ArraySparseMatrix
        ArraySparseMatrix output; // return object

        int val_sum = this.getElemCount() + other.getElemCount(); // output's elements count(maximum)

        for (Entry entry_this : this.elements) {
            for (Entry entry_other : other_mat.elements) {
                if (entry_this.getRow() == entry_other.getRow() && entry_this.getCol() == entry_other.getCol()) {
                    val_sum--; // deleting overlapping elements
                }
            }

        }

        output = new ArraySparseMatrix(this.rowCount, this.columnCount, val_sum); // making new A.S.M(=ArraySparseMatrix) space

        Entry[] lists = new Entry[val_sum]; // temporary memorizing about this and other elements

        int list_pointer = 0;

        boolean same = false;

        for(Entry this_ent : this.elements){
            for(Entry other_ent : other_mat.elements){
                if(this_ent.getRow() == other_ent.getRow() && this_ent.getCol() == other_ent.getCol()){
                    same = true;
                    break;
                }
            }
            if(same == true){
                same = false;
                continue;
            }
            else{
                lists[list_pointer++] = this_ent;
            }
        }

        for(Entry other_ent : other_mat.elements){
            for(Entry this_ent : this.elements){
                if(this_ent.getRow() == other_ent.getRow() && this_ent.getCol() == other_ent.getCol()){
                    lists[list_pointer++] = new Entry(other_ent.getRow(), other_ent.getCol(),
                            other_ent.getValue() + this_ent.getValue());
                    same = true;
                    break;
                }
            }
            if(same == true){
                same = false;
                continue;
            }
            else{
                lists[list_pointer++] = other_ent;
            }
        }

        for(int i = 0; i < this.rowCount; i++){
            for(int j = 0; j < this.columnCount; j++){
                for(int k = 0; k < val_sum; k++){
                    if(lists[k].getRow() == i && lists[k].getCol() == j){
                        output.put(lists[k]); // putting elements sorted
                    }
                }
            }
        }

        return output;
    }

    public Entry[] getElements() {
        return elements;
    }


    @Override
    public SparseMatrix multiply(SparseMatrix aMatrix) {
        throw new IllegalStateException("Not implemented");
    }

    @Override
    public int getRowCount() {
        return rowCount;
    }

    @Override
    public int getColumnCount() {
        return columnCount;
    }

    @Override
    public int getElemCount() {
        return elemCount;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof ArraySparseMatrix)) return false;
        ArraySparseMatrix other = (ArraySparseMatrix) obj;

        if (rowCount != other.rowCount || columnCount != other.columnCount || elemCount != other.elemCount)
            return false;

        for (int i = 0; i < elements.length; i++) {
            if (!elements[i].equals(other.elements[i])) return false;
        }
        return true;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append(rowCount + "\t" + columnCount + "\t" + elemCount + "\n");
        for (int i = 0; i < elemCount; i ++)
            builder.append(elements[i] + "\n");

        return builder.toString();
    }
}
