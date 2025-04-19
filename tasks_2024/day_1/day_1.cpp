#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm> // For std::sort
using namespace std;


int main () 
{
	vector< int > first_column;
	vector< int > second_column;
	string line;
	string clmn_1;
	string clmn_2;
	ifstream myfile ("input.txt");
	if (myfile.is_open())
	{

		while(getline(myfile, line)) 
		{
			istringstream iss(line);
            int clmn_1, clmn_2;

            // Extract two integers from the line
            if (iss >> clmn_1 >> clmn_2) 
            {
                first_column.push_back(clmn_1);
                second_column.push_back(clmn_2);
            }
		}
		myfile.close();
	}
	else cout << "Unable to open file"; 

	// Sort the first column in ascending order
	sort(first_column.begin(), first_column.end());
	sort(second_column.begin(), second_column.end());

	int distance = 0;
	int d_helper = 0;

	for(int i = 0; i < first_column.size(); i++)
	{
		d_helper = abs(first_column[i] - second_column[i]);
		distance += d_helper;
	}
	cout << distance << endl;

	int counter = 0;
	int similarity_score = 0;
	int total_similarity_score = 0;

	for (int i = 0; i < first_column.size(); i++)
	{
		for (int j = 0; j < second_column.size(); j++)
		{
			if (first_column[i] == second_column[j])
				counter++;
		}
		similarity_score = first_column[i] * counter;
		counter = 0;
		total_similarity_score += similarity_score;
	}
	cout << "Total similarity score: " << total_similarity_score << endl;



	// //Debug print to verify the vectors
    // cout << "First Column: ";
    // for (int num : first_column) 
	// {
    //     cout << num << " ";
	// 	//cout << typeid(num).name() << " ";
	// }
    // cout << endl;

    // cout << "Second Column: ";
    // for (int num : second_column) 
    //     cout << num << " ";
    // cout << endl;


	return 0;
}