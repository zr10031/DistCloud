#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mpi.h"
#define NP 10000
int vect1[NP];

int main(int argc, char *argv[])
{
	unsigned long int i, n=(unsigned long int)NP;
	double start, end;
	int rank, size;
	double totsum, locsum = 0.0;
	MPI_Init(&argc,&argv);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	srand(time(NULL)+rank);
	for (i=rank; i<n; i+=size) vect1[i] = (rand() % 100 + 1);
	start = MPI_Wtime();
	for (i=rank; i<n; i+=size)
	{
		locsum += (double) vect1[i];
	}
	MPI_Reduce(&locsum,&totsum,1,MPI_DOUBLE,MPI_SUM,0,MPI_COMM_WORLD);
	end = MPI_Wtime();
	printf("Local Sum on proc#%2d is %f.\n",rank, locsum);
	double t = end-start;
	if(rank == 0)
	{
		printf("Time elapsed is %f secs.\n", t);
		printf("The total sum is %f.\n", totsum);
	}
	MPI_Finalize();
	return 0;
}
