from pandas import DataFrame


def generate_table(num_propositions):
    data_3 = {
        'p': [True, True, True, True, False, False, False, False],
        'q': [True, True, False, False, True, True, False, False],
        'r': [True, False, True, False, True, False, True, False]
    }
    data_2 = {
        'p': [True, True, False, False],
        'q': [True, False, True, False]
    }
    if num_propositions == 2:
        return DataFrame(data_2)
    else:
        return DataFrame(data_3)


def evaluate_logical_expression(expression, values):
    """Evaluate a logical expression using given truth values."""
    # Replace logical operators
    expression = expression.replace('AND', '&')
    expression = expression.replace('OR', '|')
    expression = expression.replace('->', '>=')
    expression = expression.replace('!', 'not ')

    # Evaluate the expression using the given values
    try:
        # Use eval to evaluate the expression with the provided values
        # print(f"Evaluating expression: {expression}")
        result = eval(expression, {}, values)
        # print(f"Evaluated result: {result}")

        # If the expression contains an implication (->), handle it separately
        if '>=' in expression:
            parts = expression.split('>=')
            premise = parts[0].strip()
            conclusion = parts[1].strip()
            # Evaluate the premise and the conclusion separately
            premise_value = evaluate_logical_expression(premise, values)
            conclusion_value = evaluate_logical_expression(conclusion, values)
            # Check if the implication holds true
            if premise_value and not conclusion_value:
                return False
            else:
                return True

        # Otherwise, return the boolean result of the expression
        return bool(result)

    except Exception as e:
        print(f"Error evaluating expression '{expression}': {e}")
        return None


def identify_critical_rows(df):
    """Identify critical rows where all premises are True."""
    premises_columns = df.columns[3:-1]  # Assuming columns from index 3 to second-to-last are premises
    return df[df[premises_columns].all(axis=1)]


def check_argument_validity(df, conclusion_column, num_propositions):
    """Check the validity of the argument based on identified critical rows."""
    critical_rows = identify_critical_rows(df)

    if critical_rows.empty:
        print("No critical rows found. Argument cannot be validated.")
        return False

    # Check if the conclusion is True in all critical rows
    conclusion_valid = critical_rows[conclusion_column].all()
    if num_propositions == 2:
        selected_columns = critical_rows.iloc[:, 2:]
    else:
        selected_columns = critical_rows.iloc[:, 3:]

    if conclusion_valid:
        print(selected_columns)
        print(f"The argument is valid. '{conclusion_column}' is True in all critical rows.")
    else:
        print(selected_columns)
        print(f"The argument is invalid. '{conclusion_column}' is False in some critical rows.")

    return conclusion_valid


def main():

    print('Welcome to truth table generator')
    print('-----------------------------------------------')
    print('Enter the number of propositions (2 or 3): ')
    num_propositions = int(input())

    while True:
        if num_propositions in [2, 3]:
            break
        else:
            print('Numer of propositions must be 2 or 3.\n')
            print('Choose the number of propositions (2 o 3):')
            num_propositions = int(input())

    df = generate_table(num_propositions)
    print(df)

    print('-----------------------------------------------')

    print('Now we are going to build the premises.')
    premises = []
    print('Use the following format for premises: (p AND q), (p AND q) -> p')
    print('''
        If there's a negation in the premise 
        eg.  p -> (q OR !r)
        close the negation with parenthesis
        p -> (q OR (!r))
            ''')

    while True:
        print('Enter the number of premises (or 0 to end):')
        num_premises = int(input())
        if num_premises == 0:
            break
        # if num_premises > 2:
        #     print('Only 2 premises are allowed')
        #     continue
        else:
            for i in range(num_premises):
                premise_str = input(f'Enter premise {i+1}: ').strip()
                premises.append(premise_str)

    # print(premises)
    print(premises)
    # Evaluate and add premises to the dataframe
    for idx, premise in enumerate(premises):
        col_name = premises[idx]
        df[col_name] = df.apply(lambda row: evaluate_logical_expression(premise, row.to_dict()), axis=1)
        # Convert the resulting column to boolean values (True/False)
        df[col_name] = df[col_name].astype(bool)

    print(df)

    print('-----------------------------------------------')
    print('Enter the conclusion:')
    conclusion = input().strip()
    conclusion_column = f'∴ {conclusion}'
    df[conclusion_column] = df.apply(lambda row: evaluate_logical_expression(conclusion, row.to_dict()), axis=1)
    df[conclusion_column] = df[conclusion_column].astype(bool)

    print(df)
    # Check the validity of the argument
    print('--------------------------------------------------------------------')
    print("Now let's check if the argument is valid.")
    validity = check_argument_validity(df, conclusion_column, num_propositions)

    if validity:
        print(f"{conclusion_column} is True in all critical rows.")
    else:
        print(f"{conclusion_column} is False in some critical rows.")


if __name__ == "__main__":
    main()
