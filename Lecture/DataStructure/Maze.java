package cse2010.homework4;
/*
 * CSE2010 Homework #4:
 * Problem 3: Maze
 *
 * Complete the code below.
 */

import java.util.Arrays;

//import cse2010.homework4.solution.Location;

public class Maze {
    private int numRows;
    private int numCols;

    private int[][] maze;
    private boolean[][] visited = null;

    private Location entry; // Entry Location
    private Location exit;  // Exit Location


    public Maze(int[][] maze, Location entry, Location exit) {

        this.maze = maze;
        numRows = maze.length;
        numCols = maze[0].length;
        visited = new boolean[numRows][numCols]; // initialized to false

        this.entry = entry;
        this.exit = exit;
    }

    public void printMaze() {

        System.out.println("Maze[" + numRows + "][" + numCols + "]");
        System.out.println("Entry index = (" + entry.row + ", " + entry.col + ")");
        System.out.println("Exit index = (" + exit.row + ", " + exit.col + ")" + "\n");

        for (int i = 0; i < numRows; i++) {
            System.out.println(Arrays.toString(maze[i]));
        }
        System.out.println();
    }

    public boolean findPath() {

        return moveTo(entry.row, entry.col);
    }

    private boolean moveTo(int row, int col) {

        /*
              Your code goes here ...
         */

        if(row < 0 || col < 0 || row >= numRows || col >= numCols){
            return false;
        }
        else if(maze[row][col] == 1 || visited[row][col]){
            return false;
        }
        else if(row == exit.row && col == exit.col){
            visited[row][col] = true;
            return true;
        }
        else if(true){
            this.visited[row][col] = true;
            if(moveTo(row-1,col) || moveTo(row,col+1) || moveTo(row+1,col) || moveTo(row,col-1)){
                return true;
            }
            this.visited[row][col] = false;
            this.maze[row][col] = 1; //replace blocked section to number '1'
            return false;
        }

        if(visited[exit.row][exit.col] == true){
            return true;
        }

        return false;
    }


}