package cse2010.homework1;

public class Entry {
    private int row;
    private int col;
    private double value;

    // main constructor
    public Entry(int row, int col, double value) {
        this.row = row;
        this.col = col;
        this.value = value;
    }

    // copy constructor
    public Entry(Entry other) {
        this.row = other.row;
        this.col = other.col;
        this.value = other.value;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Entry)) return false;
        Entry entry = (Entry) o;
        return row == entry.row &&
            col == entry.col &&
            Double.compare(entry.value, value) == 0;
    }

    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }

    public int getCol() {
        return col;
    }

    public void setCol(int col) {
        this.col = col;
    }

    public double getValue() {
        return value;
    }

    public void setValue(double value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return row + "\t" + col + "\t" + value;
    }
}
