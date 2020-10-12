package cse2010.homework5;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import static cse2010.homework5.SyntaxTree.buildSyntaxTree;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class SyntaxTreeTest {

    String[] inputs = {
            "10 2 +",
            "1 20 + 31 49 + *",
            "1 2 + 3 4 2 / 5 * + *"
    };

    String[][] expectedTrees = {
            { "10", "+", "2" },
            { "1", "+", "20", "*", "31", "+", "49" },
            { "1", "+", "2", "*", "3", "+", "4", "/", "2", "*", "5" }
    };

    String[] expectedIndents = {
            "+\n"
                    + "  10\n"
                    + "  2\n",

            "*\n"
                    + "  +\n"
                    + "    1\n"
                    + "    20\n"
                    + "  +\n"
                    + "    31\n"
                    + "    49\n",

            "*\n"
                    + "  +\n"
                    + "    1\n"
                    + "    2\n"
                    + "  +\n"
                    + "    3\n"
                    + "    *\n"
                    + "      /\n"
                    + "        4\n"
                    + "        2\n"
                    + "      5\n"
    };

    private <T> void checkIt(List<Node<T>> iterable, List<T> expected) {
        List<T> nodes = new ArrayList<>();
        iterable.forEach(i -> nodes.add(i.getElement()));

        assertEquals(expected, nodes);
    }

    SyntaxTree[] trees = new SyntaxTree[3];

    @BeforeEach
    void setUp() {
        for (int i = 0; i < 3; i++) {
            trees[i] = buildSyntaxTree(inputs[i].split(" "));
        }
    }

    @ParameterizedTest
    @ValueSource(ints = { 0, 1 })
    void should_build_syntax_tree(int index) {
        SyntaxTree tree = buildSyntaxTree(inputs[index].split(" "));
        checkIt(tree.inOrder(), Arrays.stream(expectedTrees[index]).collect(Collectors.toList()));
    }

    @ParameterizedTest
    @CsvSource({
            "(10 + 2), 0",
            "((1 + 20) * (31 + 49)), 1",
            "((1 + 2) * (3 + ((4 / 2) * 5))), 2"
    })
    void should_fully_parenthesize_infix(String expectedInfixes, int index) {
        assertEquals(expectedInfixes, trees[index].parenthesize());
    }

    @ParameterizedTest
    @CsvSource({
            "12.0,      0",
            "1680.0,    1",
            "39.0,      2"
    })
    void should_evaluate_expression(String expectedResult, int index) {
        assertEquals(Double.parseDouble(expectedResult), trees[index].evaluate(), 0.1);
    }

    @ParameterizedTest
    @CsvSource({
            "+ 10 2,                0",
            "* + 1 20 + 31 49,      1",
            "* + 1 2 + 3 * / 4 2 5, 2"
    })
    void should_convert_to_prefix(String expectedPrefix, int index) {
        assertEquals(expectedPrefix, trees[index].toPrefix());
    }

    @ParameterizedTest
    @ValueSource(ints = { 0, 1 })
    void should_print_indented_tree(int index) {
        assertEquals(expectedIndents[index], trees[index].indentSyntaxTree());
    }
}
