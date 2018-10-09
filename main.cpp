#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insertionSort(int* original, int tamanho){
	int i, j, atual;
	
	for (i = 1; i < tamanho; i++) {
		atual = original[i];
		for (j = i - 1; (j >= 0) && (atual < original[j]); j--) {
			original[j + 1] = original[j];
        }
		original[j+1] = atual;
	}

}

void selection_sort(int num[], int tam) { 
  int i, j, min, aux;
  
  for (i = 0; i < (tam-1); i++) 
  {
     min = i;
     for (j = (i+1); j < tam; j++) {
       if(num[j] < num[min]) 
         min = j;
     }
     if (num[i] != num[min]) {
       aux = num[i];
       num[i] = num[min];
       num[min] = aux;
     }
  }
   
}

void shellSort(int *vet, int size) {
    int i , j , value;
    int gap = 1;
  
    while(gap < size) {
        gap = 3*gap+1;
    }
    while ( gap > 1) {
        gap /= 3;
        for(i = gap; i < size; i++) {
            value = vet[i];
            j = i;
            while (j >= gap && value < vet[j - gap]) {
                vet[j] = vet [j - gap];
                j = j - gap;
            }
            vet [j] = value;
        }
    }
  
}

void merge(int vetor[], int comeco, int meio, int fim) {
    int com1 = comeco, com2 = meio+1, comAux = 0, tam = fim-comeco+1;
    int *vetAux;
    vetAux = (int*)malloc(tam * sizeof(int));

    while(com1 <= meio && com2 <= fim){
        if(vetor[com1] < vetor[com2]) {
            vetAux[comAux] = vetor[com1];
            com1++;
        } else {
            vetAux[comAux] = vetor[com2];
            com2++;
        }
        comAux++;
    }

    while(com1 <= meio){  //Caso ainda haja elementos na primeira metade
        vetAux[comAux] = vetor[com1];
        comAux++;
        com1++;
    }

    while(com2 <= fim) {   //Caso ainda haja elementos na segunda metade
        vetAux[comAux] = vetor[com2];
        comAux++;
        com2++;
    }

    for(comAux = comeco; comAux <= fim; comAux++){    //Move os elementos de volta para o vetor original
        vetor[comAux] = vetAux[comAux-comeco];
    }
    
    free(vetAux);
   
}

void mergeSort(int vetor[], int comeco, int fim){
    if (comeco < fim) {
        int meio = (fim+comeco)/2;
        
        mergeSort(vetor, comeco, meio);
        mergeSort(vetor, meio+1, fim);
        merge(vetor, comeco, meio, fim);		
 }
    
}

void quick_sort(int *a, int left, int right) {
    int i, j, x, y;
     
    i = left;
    j = right;
    x = a[(left + right) / 2];
  
    while(i <= j) {
        while(a[i] < x && i < right) {
            i++;
        }
        while(a[j] > x && j > left) {
            j--;
        }
        if(i <= j) {
            y = a[i];
            a[i] = a[j];
            a[j] = y;
            i++;
            j--;
        }
    }
     
    if(j > left) {
        quick_sort(a, left, j);
    }
    if(i < right) {
        quick_sort(a, i, right);
    }
    
}

void heapsort(int a[], int n) {
   int i = n / 2, pai, filho, t;
   while(true) {
      if (i > 0) {
          i--;
          t = a[i];
      } else {
          n--;
          if (n == 0) return;
          t = a[n];
          a[n] = a[0];
      }
      pai = i;
      filho = i * 2 + 1;
      while (filho < n) {
          if ((filho + 1 < n)  &&  (a[filho + 1] > a[filho]))
              filho++;
          if (a[filho] > t) {
             a[pai] = a[filho];
             pai = filho;
             filho = pai * 2 + 1;
          } else {
             break;
          }
      }
      a[pai] = t;
   }
}

int metodos(){
 	int menu;
    	printf("\n");
    	printf("\n1 - Selection Sort");
    	printf("\n2 - Insertion Sort");
    	printf("\n3 - Shellsort");
    	printf("\n4 - Mergesort");
    	printf("\n5 - quicksort");
    	printf("\n6 - heapsort");
    	printf("\n7 - Digite 0 Para Sair");
    	scanf("%d",&menu);
    	return menu;
 }

void tela(int *vetor, int tamanho, int menu){
	   clock_t tempo_ord;
	   int contador = 0;
    	switch(menu){
    		case 1:
    			
    			printf("\n");
    			tempo_ord = clock();
    			selection_sort(vetor,tamanho);
    			tempo_ord = clock () - tempo_ord;
    			for(int i=0;i<tamanho;i++){
    				contador = contador + 1;
	                printf("%d ",vetor[i]);	
				}
    			printf("\n numero de instancias = %d",contador);
    			contador = 0;
	            printf("\n %f \n",((float)tempo_ord)/CLOCKS_PER_SEC);
    			break;
    		
    		case 2:
    			printf("\n");
    			tempo_ord = clock();
                insertionSort(vetor,tamanho);
                tempo_ord = clock() - tempo_ord;
                for(int i=0;i<tamanho;i++){
                	contador = contador + 1;
	             	printf("%d ",vetor[i]);
				}
				printf("\n numero de instancias = %d",contador);
				contador = 0;
	            printf("\n %f \n",((float)tempo_ord)/CLOCKS_PER_SEC);
    			break;
    		
    		case 3:
    			printf("\n");
    		    tempo_ord = clock();
    			shellSort(vetor,tamanho);
    			tempo_ord = clock() - tempo_ord;
    			for(int i=0;i<tamanho;i++){
    				contador = contador + 1;
	            	printf("%d ",vetor[i]);	
				}
    			
	            printf("\n numero de instancias = %d",contador);
	            contador = 0;
	            printf("\n %f \n",((float)tempo_ord)/CLOCKS_PER_SEC);
    			break;
    		
    		case 4:
    			int comeco,fim;
    			comeco = 0;
    			fim = tamanho -1;
    			printf("\n");
    				for(int i=0;i<fim+1;i++){
    				contador = contador + 1;
	                printf("%d ",vetor[i]);
				}
                tempo_ord = clock();  		
    			mergeSort(vetor,comeco,fim);
    			tempo_ord = clock() - tempo_ord;
    			for(int i=0;i<fim+1;i++){
    				contador = contador + 1;
	                printf("%d ",vetor[i]);
				}
	            printf("\n numero de instancias = %d",contador);
	            contador = 0;
	            printf("\n %f \n",((float)tempo_ord)/CLOCKS_PER_SEC);
    			break;
    		
    		case 5:
    			printf("\n");
    			int esq,dir;
    			esq = 0;
    			dir = tamanho;
    		    tempo_ord = clock();  
    			quick_sort(vetor,esq,dir);
    			tempo_ord = clock() - tempo_ord;
    			if(tamanho%2 == 1){
    				for(int i=1;i<=tamanho;i++){
    					contador = contador + 1;
	                	printf("%d ",vetor[i]);
					}
 	
				}
				if(tamanho%2 == 0){
					for(int i=1;i<tamanho+1;i++){
					contador = contador + 1;
	                printf("%d ",vetor[i]);
					}
					
				}
				printf("\n numero de instancias = %d",contador);
				contador = 0;
				printf("\n %f \n",((float)tempo_ord)/CLOCKS_PER_SEC);
    			
    			break;
    		
    		case 6:
    		    tempo_ord = clock();  
    			heapsort(vetor,tamanho);
    			tempo_ord = clock() - tempo_ord;
    			printf("\n");
    			if(tamanho%2 == 1){
					for(int i=1;i<tamanho+1;i++){
						contador = contador + 1;
	                    printf("%d ",vetor[i]);	
					}
				
				}
    			if(tamanho%2 == 0){
    				for(int i=1;i<tamanho+1;i++){
    					contador = contador + 1;
	            	printf("%d ",vetor[i]);
			}
				}
				printf("\n numero de instancias = %d",contador);
				contador = 0;
				printf("\n %f \n",((float)tempo_ord)/CLOCKS_PER_SEC); 
    			break;
    		
    		default:
    			break;
		}
    	
}

void gerar_crescente(){
	int*vetor;
	int i,tamanho;
	int pega_menu;
	printf("Entre com o tamanho do vetor ");
    scanf("%d", &tamanho);
    printf("\n");
	vetor=(int *) malloc(tamanho * sizeof (int));
	for(i=0;i<tamanho;i++){
		vetor[i]=i;
		//printf("%d ",vetor[i]);
	}
	pega_menu = metodos();
	tela(vetor,tamanho,pega_menu);
}

void gerar_decrescente(){
    int*vetor;
	int i,tamanho;
	int pega_menu;
	printf("Entre com o tamanho do vetor ");
    scanf("%d", &tamanho);
    printf("\n");
	vetor=(int *) malloc(tamanho * sizeof (int));
	for(i=tamanho-1;i>=0;i--){
		vetor[i]=i;
	//	printf("%d ",vetor[i]);
	}
	pega_menu = metodos();
	tela(vetor,tamanho,pega_menu);
}


void gerar_aleatorio(){
	
 srand(time(NULL));
 int* vetor;
 int i,tamanho;
 int pega_menu;

 printf("Entre com o tamanho do vetor ");
 scanf("%d", &tamanho);
 printf("\n");
 vetor=(int *) malloc(tamanho * sizeof (int));
 for(i=0;i<tamanho;i++){ 
	vetor[i]=rand()%100000; //inserção dos valores no vetor.
	//printf("%d ",vetor[i]); //impressao dos valores contidos no vetor
 }
 pega_menu = metodos();  
 tela(vetor,tamanho,pega_menu);
}



int main(void){
int op;
do{
	printf("\n");
	printf("\n1 - Gerar numeros aleatorios");
	printf("\n2 - Gerar numeros em ordem crescente");
	printf("\n3 - Gerar numeros em ordem decrescente");
	printf("\n0 - Para sair ");
	scanf("\n%d", &op);
	printf("\n");
	switch(op){
		case 1:
			gerar_aleatorio();
			break;
		case 2:
			gerar_crescente();
			break;
		case 3:
			gerar_decrescente();
			break;
		default:
		    break;
	}
	
}while(op != 0);
return 0;
}
