package cse2010.homework4;

/*
 * CSE2010 Homework #4: Location.java
 * 
 * DO NOT MODIFY THIS FILE!
 * 
 */
public class Location {
	public int row;
	public int col;
	
	public Location(int row, int col) {
		this.row = row;
		this.col = col;
	}
	
	public String toString() {
		return "[" + String.valueOf(row) + "," + String.valueOf(col) + "]";
	}
}