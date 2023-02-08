#include <iostream>
#include <numeric>


	
int func_calc_score (int rad_score , int comptr_score) ;
int main() {
	
	/* 
	2023-02-06 17:30 
	ultra simple program to calculates the catch up games that I need to play on Chess.com 
	in order to  maintain or surpass my competitors.
	*/
	
	int my_score = 667; 
	int competitor_score = 1000 ;
	func_calc_score (my_score , competitor_score) ;  
		
	
	
	
	return 0;
}


int func_calc_score(int rad_score , int comptr_score) {
	
	int diff =  (comptr_score - rad_score) ;
	int arr_trophies_cat [] = {15 , 9 , 3} ;
	int n = 3 , sum =0  ;
	
	
	
	
	int avg_trophy_count = ((15 + 9 +3) /3) ;
	
	sum = std::accumulate(arr_trophies_cat , arr_trophies_cat+n , sum) ;
	std::cout <<"The differenceI need to catch on is :" << diff << std::endl; 
	//std::cout <<"\n" << std::endl ; 
	std::cout << "the trophy_array is: " << sum << std::endl;
	std::cout <<"Therefore throughput rate is: "<< (diff/ (sum/3)) << std::endl;
	
	
	return 0;
}