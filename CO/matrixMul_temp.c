#include <stdio.h>
#include <stdlib.h>

#define N 1024

// Function to dynamically allocate memory for a matrix
int** allocateMatrix(int rows, int cols) {
    int** matrix = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int*)malloc(cols * sizeof(int));
    }
    return matrix;
}

// Function to free dynamically allocated memory for a matrix
void freeMatrix(int** matrix, int rows) {
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

// Function to multiply matrices using row-wise access
void multiplyRowWise(int** mat1, int** mat2, int** result) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            result[i][j] = 0;
            for (int k = 0; k < N; k++) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}

// Function to multiply matrices using column-wise access
void multiplyColumnWise(int** mat1, int** mat2, int** result) {
    for (int j = 0; j < N; j++) {
        for (int i = 0; i < N; i++) {
            result[i][j] = 0;
            for (int k = 0; k < N; k++) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}

int main() {
    int** mat1 = allocateMatrix(N, N);
    int** mat2 = allocateMatrix(N, N);
    int** result = allocateMatrix(N, N);

    // Initialize matrices with random values between 0-100
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            mat1[i][j] = rand() % 101;
            mat2[i][j] = rand() % 101;
        }
    }

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            printf("%d ",mat1[i][j]);
        }
        printf("\n");
    }

    printf("\n");

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            printf("%d ",mat2[i][j]);
        }
        printf("\n");
    }

    
    // Multiply matrices using row-wise access
    multiplyRowWise(mat1, mat2, result);

    // Print the result for row-wise access
    printf("Result using row-wise access:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    // Multiply matrices using column-wise access
    multiplyColumnWise(mat1, mat2, result);

    // Print the result for column-wise access
    printf("\nResult using column-wise access:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    // Free dynamically allocated memory
    freeMatrix(mat1, N);
    freeMatrix(mat2, N);
    freeMatrix(result, N);

    return 0;
}
