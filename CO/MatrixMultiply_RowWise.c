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

int main() 
{
    int** mat1 = allocateMatrix(N, N);
    int** mat2 = allocateMatrix(N, N);
    int** result = allocateMatrix(N, N);

    // Initialize matrices with random values between 0-100
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            mat1[i][j] = rand() % 10;
            mat2[i][j] = rand() % 10;
        }
    }

    //multiply row wise
    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            result[i][j] = 0;
            for (int k = 0; k < N; k++) 
            {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }

    printf("Multiplication operation completed\n");

    // Free dynamically allocated memory
    freeMatrix(mat1, N);
    freeMatrix(mat2, N);
    freeMatrix(result, N);

    return 0;
}
