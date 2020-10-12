package cse2010.homework4;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class MazeTest {

    // System Under Test
    private Maze maze;

    private int[][] testMaze = new int[][] {
            { 0, 1, 0, 1, 0 },
            { 0, 0, 0, 0, 0 },
            { 0, 1, 0, 0, 1 },
            { 1, 0, 1, 0, 0 },
            { 0, 1, 1, 1, 0 }
    };

    @Test
    void testMaze1_1() {
        maze = new Maze(testMaze, new Location(0, 0), new Location(4, 4));

        maze.printMaze();

        assertTrue(maze.findPath());

    }

    @Test
    void testMaze1_2() {
        maze = new Maze(testMaze, new Location(4, 4), new Location(0, 0));

        maze.printMaze();

        assertTrue(maze.findPath());
    }

    @Test
    void testMaze1_3() {
        maze = new Maze(testMaze, new Location(2, 0), new Location(4, 4));

        maze.printMaze();

        assertTrue(maze.findPath());
    }

    @Test
    void testMaze1_4() {
        maze = new Maze(testMaze, new Location(0, 4), new Location(4, 4));

        maze.printMaze();

        assertTrue(maze.findPath());
    }

    @Test
    void testMaze1_5() {
        maze = new Maze(testMaze, new Location(0, 4), new Location(4, 0));

        maze.printMaze();

        assertFalse(maze.findPath());
    }
}