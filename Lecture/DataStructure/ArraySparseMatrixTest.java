package cse2010.homework1;

import org.junit.jupiter.api.Test;
import org.junit.platform.engine.support.descriptor.FileSystemSource;

import static org.junit.jupiter.api.Assertions.*;

class ArraySparseMatrixTest {

    @Test
    void should_create_sparseMatrix_from_2DArray() {
        // Arrange (Given)
        double[][] input = {
            {0, 0, 1.0, 0},
            {1.0, 2.0, 0, 0},
            {0, 0, 0, 3.0}
        };

        Entry[] sparseMatrix = {
            new Entry(0, 2, 1.0),
            new Entry(1, 0, 1.0),
            new Entry(1, 1, 2.0),
            new Entry(2, 3, 3.0)
        };

        // Act (When)
        SparseMatrix result = ArraySparseMatrix.create(input, 3, 4, 4);

        // Assert (Then)
        assertAll("Check sparse matrix creation",
            () -> assertEquals(4, result.getElemCount()),
            () -> assertEquals(3, result.getRowCount()),
            () -> assertEquals(4, result.getColumnCount()),
            () -> assertArrayEquals(sparseMatrix, ((ArraySparseMatrix) result).getElements(), "Sparse matrix construction fail")
        );
    }

    @Test
    void should_transpose_matrix() {
        // Given
        double[][] input = {
            {0, 0, 1.0, 0},
            {1.0, 2.0, 0, 0},
            {0, 0, 0, 3.0}
        };

        double[][] output = {
            {0, 1.0, 0},
            {0, 2.0, 0},
            {1.0, 0, 0},
            {0, 0, 3.0}
        };
        SparseMatrix inputMatrix = ArraySparseMatrix.create(input, 3, 4, 4);
        SparseMatrix expectedMatrix = ArraySparseMatrix.create(output, 4, 3, 4);

        // When
        final SparseMatrix actualMatrix = inputMatrix.transpose();

        assertEquals(expectedMatrix, actualMatrix, "Transpose failed");
    }

    @Test
    void should_add_matrices() {
        //Given
        double[][] m1 = {
            {0, 0, 1.0, 0},
            {1.0, 2.0, 0, 0},
            {0, 0, 0, 3.0}
        };

        double[][] m2 = {
            {1.0, 0, 0, 2.0},
            {0, 3.0, 0, 0},
            {4.0, 0, 5.0, 0}
        };

        double[][] output = {
            {1.0, 0, 1.0, 2.0},
            {1.0, 5.0, 0, 0},
            {4.0, 0, 5.0, 3.0}
        };

        SparseMatrix expectedMatrix = ArraySparseMatrix.create(output, 3, 4, 8);
        SparseMatrix sm1 = ArraySparseMatrix.create(m1, 3, 4, 4);
        SparseMatrix sm2 = ArraySparseMatrix.create(m2, 3, 4, 5);

        // When
        SparseMatrix result = sm1.add(sm2);

        // Then
        assertEquals(expectedMatrix, result, "Addition failed");
        assertEquals(expectedMatrix, sm2.add(sm1), "Addition failed");
    }

    @Test
    void should_throw_exception_if_array_dimensions_differ() {
        // Given
        double[][] m1 = {
            {0, 0, 1.0, 0},
            {1.0, 2.0, 0, 0},
            {0, 0, 0, 3.0}
        };

        double[][] m2 = {
            {1.0, 0, 0, 2.0},
            {0, 3.0, 0, 0},
        };

        SparseMatrix sm1 = ArraySparseMatrix.create(m1, 3, 4, 4);
        SparseMatrix sm2 = ArraySparseMatrix.create(m2, 2, 4, 3);

        // When
        IllegalArgumentException exception =
            assertThrows(IllegalArgumentException.class, () -> sm1.add(sm2));

        // Then
        assertEquals("Matrix size doesn't match", exception.getMessage());
    }

    @Test
    void should_throw_exception_if_input_is_malformed() {
        // Arrange (Given)
        double[][] m1 = {
            {0, 0, 1.0, 0},
            {1.0, 2.0, 0, 0},
            {0, 0, 0, 3.0}
        };

        // Act (When)
        IllegalStateException exception =
            assertThrows(IllegalStateException.class, () -> ArraySparseMatrix.create(m1, 3, 4, 5)
        );

        // Assert (Then)
        assertEquals("Non zero count doesn't match", exception.getMessage());
    }
}