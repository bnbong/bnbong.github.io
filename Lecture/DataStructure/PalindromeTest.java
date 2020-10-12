package cse2010.homework4;

import java.util.stream.Stream;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import static org.junit.jupiter.api.Assertions.assertTrue;

class PalindromeTest {

    @ParameterizedTest
    @MethodSource("stringProvider")
    void test(String argument) {

        assertTrue(Palindrome.isPalindrome(argument));
    }

    /* All data below are palindromes */
    static Stream<String> stringProvider() {
        return Stream.of(
                "wow",
                "anna",
                "level",
                "Radar",
                "Step on no pets",
                "Top spot",
                "Don't nod.",
                "No lemon, no melon",
                "Madam I'm Adam",
                "Eva, can I see bees in a cave?",
                "",
                "?",
                "!@#",
                "!aa#",
                "!a#");
    }
}