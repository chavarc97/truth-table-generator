# Truth Table Generator and Argument Evaluator

This Python script allows you to generate truth tables based on 2 or 3 propositions and evaluate logical arguments using those truth values. It includes functionality to define premises and conclusions and check the validity of logical arguments based on truth table analysis.

## Prerequisites

- Python 3.x
- pandas library

## Getting Started

1. **Clone the Repository**

   ```bash
   
   git clone https://github.com/chavarc97/truth-table-generator.git
   cd truth-table-generator

2. **Install dependencies**
	```bash
	pip install pandas
	
## Usage
1.  **Generate a Truth Table**
    
    -   Enter the number of propositions (2 or 3) when prompted.
    -   The script will generate a truth table for the specified number of propositions.
2.  **Define Premises**
    
    -   Enter the number of premises you want to define.
    -   Use the format `(p AND q)`, `(p OR q)`, `(p -> q)` to define each premise.
    -   Premises will be evaluated and added to the truth table.
3.  **Define Conclusion**
    
    -   Enter the conclusion you want to evaluate.
    -   The script will evaluate the conclusion based on the truth table and premises.
4.  **Check Argument Validity**
    
    -   The script will determine whether the argument is valid based on the defined premises and conclusion.

## Example

Suppose we want to evaluate the argument:

Premises:

-   `(p AND q)`
-   `(p OR q) -> p`

Conclusion:

-   `∴ p`

The script will generate a truth table, evaluate the premises, and check if the conclusion holds true in all valid cases.

## Note

-   Ensure to use the correct logical operators (`AND`, `OR`, `->`) when defining premises.
-   Invalid expressions or logical errors may cause the script to throw an error or produce unexpected results.

Feel free to explore and modify the script to suit your needs!